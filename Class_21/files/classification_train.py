# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 13:28:56 2022

@author: ssukenik
"""
import os

import torch

from parrot import process_input_data as pid
from parrot import brnn_architecture
from parrot import train_network
from parrot import brnn_plot
from parrot.tools import validate_args
from parrot.tools import dataset_warnings


#%% Set parameters

# Hyper-parameters
hidden_size = 10
num_layers = 1
learning_rate = 0.001
batch_size = 32
num_epochs = 100

# Data format
dtype = 'sequence'
num_classes = 3

# Other flags
stop_cond = 'iter'
encode = 'onehot'
verbose = True
silent = False
setFractions = [0.7, 0.15, 0.15]
excludeSeqID = False
probabilistic_classification = False
include_figs = True
ignore_warnings = False
ignore_metrics = False
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# file I/O
data_file = 'seq_class_dataset.tsv'
network_file = 'seq_class_network.pt'
filename_prefix = network_file.split('.')[0]
output_dir = os.getcwd()

#%% initialize network objects

# Set encoding scheme and/or validate user scheme
encoding_scheme, encoder, input_size = validate_args.set_encoding_scheme(encode)

# Initialize network as classifier or regressor
problem_type, collate_function = validate_args.set_ml_task(num_classes, dtype)

# Initialize network architecture
brnn_network = brnn_architecture.BRNN_MtO(input_size, hidden_size,
                                              num_layers, num_classes, device).to(device)
#%% Prepare training, validation, and test datasets

# Split data
train, val, test = pid.split_data(data_file, datatype=dtype, problem_type=problem_type,
                                  num_classes=num_classes, excludeSeqID=excludeSeqID, 
                                  encoding_scheme=encoding_scheme, 
                                  encoder=encoder, percent_val=setFractions[1], 
                                  percent_test=setFractions[2], ignoreWarnings=ignore_warnings)

# Check if batch size is appropriate for training dataset size
dataset_warnings.eval_batch_size(batch_size, len(train))

# load train, validation, and test datasets
train_loader = torch.utils.data.DataLoader(dataset=train,
                                           batch_size=batch_size,
                                           collate_fn=collate_function,
                                           shuffle=True)
val_loader = torch.utils.data.DataLoader(dataset=val,
                                         batch_size=batch_size,
                                         collate_fn=collate_function,
                                         shuffle=False)
test_loader = torch.utils.data.DataLoader(dataset=test,
                                          batch_size=1,		# Set test batch size to 1
                                          collate_fn=collate_function,
                                          shuffle=False)
#%% output 

if silent is False:
    print()
    print("PARROT with user-specified parameters")
    print("-------------------------------------")
    print('Train on:\t%s' % device)
    print("Datatype:\t%s" % dtype)
    print("ML Task:\t%s" % problem_type)
    print("Learning rate:\t%f" % learning_rate)
    print("Number of layers:\t%d" % num_layers)
    print("Hidden vector size:\t%d" % hidden_size)
    print("Batch size:\t%d\n" % batch_size)
    print("Validation set loss per epoch:")

#%% Train network
train_loss, val_loss = train_network.train(brnn_network, train_loader, val_loader, datatype=dtype,
                                           problem_type=problem_type, weights_file=network_file, 
                                           stop_condition=stop_cond, device=device, 
                                           learn_rate=learning_rate, n_epochs=num_epochs, 
                                           verbose=verbose, silent=silent)

# Plot training & validation loss per epoch
brnn_plot.training_loss(train_loss, val_loss, output_file_prefix=filename_prefix)

# Test network
test_loss, test_set_predictions = train_network.test_labeled_data(brnn_network, test_loader,
                                                datatype=dtype, problem_type=problem_type,
                                                weights_file=network_file, num_classes=num_classes,
                                                probabilistic_classification=probabilistic_classification,
                                                include_figs=include_figs, device=device,
                                                output_file_prefix=filename_prefix)

if silent is False:
    print('\nTest Loss: %.4f' % test_loss)

# Output performance metrics
brnn_plot.write_performance_metrics(test_set_predictions, dtype, problem_type,
                                      probabilistic_classification, filename_prefix)

# Output the test set predictions to a text file
brnn_plot.output_predictions_to_file(test_set_predictions, excludeSeqID, encoding_scheme,
                                probabilistic_classification, encoder, output_file_prefix=filename_prefix)

