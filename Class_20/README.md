# CHE600 - class 20

Topics:

[Homework III - working with databases]

# Homework III

Your assignment involves testing some hypotheses using publication data and online databases. The work should be done independently.

## I. Overview

Protein copy numbers are a critical aspect of their function. For example, enzymatic function is determined by an enzymes turnover rate and efficiency - but even the most efficient enzymes will not be effective if they exist in a single copy in the cell! Copy numbers are of course regulated by the rate of synthesis of the protein. However, an unappreciated component of copy numbers is the rate of protein degredation. 

1. Your task is to compile a database of protein degredation rates, and try to find correlates with different protein features. Protein degredation rates are measured by protein half life - the rate (in minutes) at which a protein population is reduced by half.

2. A recent paper, from [Christiano et al 2014](https://doi.org/10.1016/j.celrep.2014.10.065), quantified the halflife of over 4000 yeast proteins.

3. The datasets, in CSV format, is available [here](./files/Christiano_etal_halflife.csv)


## II. Getting started

1. Start a new notebook called ```homework3.ipynb```. The entire exercise can be completed in a single notebook

2. Import pandas, matplotlib, numpy, and other libraries you may need in the first cell.

3. Import the dataset to a pandas dataframe

4. Plot the distribution of the _log10_ of the halflife using the ```hist()``` function of your [dataframe](https://pandas.pydata.org/docs/reference/api/pandas.Series.hist.html)

5. What is the average, std, and median of the halflives?

## IV. Pulling information from uniprot

1. The identifier of each protein in the dataset is a UniProt accession code. Open one of the files, and look up the uniprot ID on the [website](https://uniprot.org). Familiarize yourself with the database and the different categories of information this database provides.

2. A good overview tutorial on how to explore a uniprot entry is available [here](https://www.youtube.com/watch?v=BHu88Sv--mc)

3. We want to pull information from uniprot for every single entry. Specifically, we will want to pull the _sequence_ of each entry.

2. You can do this in several ways:
    1. a [REST API](https://www.uniprot.org/help/api_queries) for uniprot 
    2. [recommended] - a [python library](https://david-araripe.github.io/UniProtMapper/stable/index.html) that will pull entries for you.

3. You are on your own! Figuring out the best way to do things is part of the challenge! Remember you will need to install libraries using ```!pip install <library name>``` if you have not installed them previously!

## V. Sequence analysis

Now that we have the full length sequence for each protein, let's perform some further analyses. 

1. The question we are interested in is whether or not the degree of disorder in a sequence is correlated with the halflife of a protein. In other words - does increased protein disorder coincide with higher rates of degredation?

2. To do this, we will need to predict the disorder of each sequence. One way to do this is through a library called [metapredict](https://metapredict.readthedocs.io/en/latest/getting_started.html)

3. Install the library on your computer, and read the documentation. Using a for loop, predict the disorder of each sequence in your dataset, and add the disorder as a column to your main DataFrame.

4. Plot the disorder score _vs_ the halftime. 

5. Using [scipy.stats.pearsonr()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html) calculate the [spearman rank coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) between the disorder score and the halftime, and describe the results: is there a correlation?

6. Upload the full notebook, and answers written as comments or _markdown cells_ to blackboard by 4/18, 11:59 PM.

## Good luck!

