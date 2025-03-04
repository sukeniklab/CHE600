# CHE600 - Class 12

Topics today:
1. [Pandas – a python based Excel](#pandas--a-python-based-excel)
2. [Class assignment - generating many plots](#class-exercise-plotting-large-datasets)
3. [Visualizations with Seaborn](#seaborn--a-package-for-statistical-data-visualization)

# Pandas – a python based Excel

Today’s class will introduce you to [Pandas](https://pandas.org) – a very popular python library that allows you to work with data like you would with excel: unlike numpy, pandas doesn’t care if your data is numerical, textual, or even more complicated data types like lists, dictionaries or arrays. 

1. Pandas is very powerful and extremely useful – it is how my lab imports and processes experimental (and simulation) data to process, analyze, and visualize. Let's start by using ```pip``` to install it. Start a new jupyter notebook called ```class12.ipynb```. In the first cell, type the followin (**you will only need to do this once!**)

```python
!pip install pandas
```

2. Pandas contains contains two main data types: the Series and the DataFrame which is essentially a collection of Series. A Series is 1 dimensional (similar to a 1D numpy array) and a DataFrame is multidimensional. The main difference is that Series and DataFrames include indexing - you can name the indices and columns (whereas in numpy you can only call their number). This makes for increased readability. In addition, both Series and DataFrames accept any data type – not just numerical data!

## I. the pandas Series

1. Let’s create a pandas series in your notebook:

```python
import pandas as pd
s = pd.Series([100,200,300,400,500,500,200])
print(s)
type(s) 
```

2. Notice the printout contains the values, but also a numerical index for these values (like row number in excel). The Series object, like other data objects we’ve seen, contains a bunch of functions and properties. Try some examples:

```python
s.index # displays only the indices of the Series
```
```python
s.values # returns only the values of the Series
```
```python
s.unique() # displays only unique values in the Series
```
```python
s.sort_values() # sorts the Series based on values
```
```python
s.sort_index() # sorts the Series based on index
```

3. Notice that index and values are properties while unique()and sort_values() are functions. We know this because unique requires an argument (even if it’s empty!). If you do not add these parenthesis in you will not call the function at all! Properties on the other hand return their value, and if you do add parenthesis will throw an error (saying the property is not a function).

4. We can get statistics on a series through statistical functions:

```python
s.mean()   # mean of the Series
```
```python
s.median() # median of the Series 
```
```python
s.std() # standard deviation of the Series
```
```python
s.describe() # an overview of the series, including mean, standard deviation, and quantiles
```

5. We can change our Series name and indices:

```python
# set the index using a list. Note that this needs to of the same length as the Series!
s.index = ["S","M","T","W","R","F","sat"]
# set the name of the series
s.name = "payment"
print(s)
```

6. We can slice our Series, meaning keep only a subset of the list. Note that you must assign the slice to a variable (or a function) – otherwise it will only be sent to standard output and not saved:

```python
s["S"] # index "S" of the series
```
```python
# indices "S" and "R" of the series
s[["S","R"]]
```
```python
# iloc (index location) selects the first through third row
s.iloc[0:3]
```
```python
# iloc selects the 3 through the row before last
s.iloc[2:-1]
```
```python
# The average of the above selection 
s.iloc[2:-1].mean()
```

7. Notice that because a slice from a Series is also a Series it retains all Series functions and properties! If we want to generate a different type of variable we can use one of the follow:

```python
# generates a list variable
s_list = s.to_list() 
print(s_list)
print(type(s_list))
```
```python
# generates a numpy array from s
s_np = s.to_numpy() 
print(s_np)
print(type(s_np))
```

## II. The pandas DataFrame

Now let’s create a DataFrame - a dataframe is composed of multiple Series, all having the same index. The series then become columns in our DataFrame.

1. One way to creat a DataFrame is by combining two series. Let's create another series, and concatenate it with the first series using the ```pd.concat()``` function to create a dataframe.

```python
# generate a new Series called m from Series s
m = s*0.1
# give it the same index but a different name
m.index = s.index
m.name = 'tax'
print(m)
```
```python
# use pd.concat() to join the two series. The axis=1 column means they are joined on columns (as opposed to rows)
df = pd.concat([s,m],axis=1) 
print(df)
print(type(df))
```

2. Notice that we now created a DataFrame. The indices are the same as the indices of the individual Series (they are the same by design since we set ```m.index = s.index```), but the column headers are now set by the name of each Series.

## III. Importing data to create a DataFrame

Another way to create a DataFrame is to import a file. Pandas has even more powerful import options than numpy: you can import csv’s and text-based data of course, but you can also import excel workbooks (including ones with multiple sheets!) and other complex data structures like HDF, XML, and JSON. We will only use the csv import option today.

1. Download [fret_data.csv](./files/fret_data.csv) and place it in the same folder as your current notebook. This dataset contains the results of ~4700 experiments done in the lab. Put it in a dedicated directory where you will write today’s script, and import the data:

```python
# read in the contents of a comma seperate values file
# by default, the function creates a range of numbers for the index and assigns the first row as the column headers
df = pd.read_csv("fret_data.csv")
print(df)
```
```python
df.describe() # display stat summary on each column
```
```python
df.index # display the row indices
```
```python
df.columns # displays the column headers
```
```python
df.values # displays the values as a numpy array
```
```python
df.shape # shape of dataframe
```
```python
df.head(5) # displays first 5 lines of DataFrame
```
```python
df.info() # displays the type of each column 
```

2. pd.read_csv() is only one import function. Importantly, pandas can easily import a wide range of spreadsheets, including tab separated (```pd.read_table()```) and excel files (```pd.read_excel()```). Notice that now we have both indices and columns names! (both are properties, not functions!). 

## IV. Slicing and dicing DataFrames

Like lists and arrays, we need to be able to select a subset of a dataframe.

1. We can select only a single column in a dataframe. If we do this, we will get a Series object back. If we select more than two columns, we'll get a DataFrame back:

```python
s2 = df["protein_name"]
print(s2)
print(type(s2))
```
```python
df2 = df[['protein_name','E_f']]
print(df2)
print(type(df2))
```

2. We can use conditionals to slice the DataFrame in any way we want. A conditional on a dataframe or a slice will return a pandas Series of Booleans (true/false values) according to where the condition is met. 

```python
idx = df["protein_name"]=="GS0" 
print(idx)
```

3. Note that a the resulting list (```idx```) can then be used as an index:

```python
print('before slicing:')
print(df.shape)
print(df['protein_name'].unique())
print('after slicing:')
# applying the boolean series as an index removes all rows where "protein_name" is not "GS"
print(df[idx].shape)
print(df[idx]['protein_name'].unique())
```

4. In general we can just put the conditionals directly into the indexing. In the example below, we use this approach to make even more complex conditionals. What will this line do?

```python
sliced2 = df[(df["protein_name"]=="GS0")&(df["repeat"]>1)]
print(sliced2[['protein_name','repeat']])
```

## V. Operations with Series and DataFrames

1. We can perform operations between different columns of a DataFrame (so long as they are numerical!). This will return a series:

```python
ratio = df['E_f']/df['E_f_GS']
print(ratio)
```

2. We can assign new columns to the DataFrame:

```python
df["ratio"]=ratio
df["constant"]=3
df["calc"]=df["E_f"]-df["E_f_GS"]
print(df.iloc[:,-4:])
```

3. We can combine between two dataframes based on the values in a specific column. Download the excel sheet [prot_data.csv](./files/prot_data.csv) from this week’s module to your working directory. Import it into pandas with:

```python
# here we set the index column to be the first column
prots_df = pd.read_csv('prot_data.csv',index_col=0)
prots_df.head(10)
```

4. notice that the protein names are the same as ```df```, but other columns are different. We will want to merge ```prots_df``` with ```df```. To do this, we will use the ```pd.merge()``` function. The left dataframe is the main one, and the merge will be based on data existing there.

```python
# provide the left and right dataframe, and the column names on which to merge
merged_df = pd.merge(df,prots_df,left_on='protein_name',right_on='prot')
print(merged_df.shape)
print('columns in df:')
print(df.columns)
print('columns in prots_df:')
print(prots_df.columns)
print('columns in merged_df:')
print(merged_df.columns)
print(merged_df['protein_name'].unique())
```

5. DataFrames have many more [attributes and functions](https://pandas.pydata.org/docs/reference/frame.html). For example, you can have multiple levels of column or index names (aka [MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html) which allows you to have multi-dimensional DataFrames. When you type out the index or column of these DataFrames instead of a list of values you will get back an object called MultiIndex – we will not cover this in this class. I encourage you to look through the pandas documentation online and play around with more options.

6. **A word of warning on imports** – the csv file you’ve imported is already optimized for pandas. Often, this will not be the case. The read_csv function contains many options that allow you to ignore rows/columns, use specific rows/columns as indices or column names, etc. Often though, the best idea is to think carefully about how you arrange your data – when my students collect data we spend some time thinking about how to arrange it and what properties of the experiment to record (eg time, temp, repeat, etc.) so that in the end we can import, manipulate, and plot it easily and efficiently.

# Class exercise: Plotting large datasets

1. Last week we’ve seen some very basic plotting functions. We’re now going to try and make some fancier plots to give you some idea of the power you have with matplotlib and pandas. Start a new notebook called ```plotChi.ipynb```. Make sure it is in the same directory as ```fret_data.csv```. 

2. fret_data.csv contains the structural data of different proteins in different solution conditions obtained from FRET experiments. Each row has (among other things) the protein name (_protein_name_), the solute name (_solute_), the concentration of that solute (_conc_), and the dimensions of the protein in those conditions _chi_, where chi > 0 is expanded, chi < 0 is compacted). We are going to want to plot chi vs solute concentration for each protein and each solute type.

3. The script should do the following:
    1. Import pyplot and pandas
    2. import ```fret_data.csv``` into a pandas DataFrame
    3. Loop over all protein names (use the unique() function to create your iteration list!)
    4. Loop over all ‘solute’ types
    5. Within each iteration of these two loops, slice the DataFrame such that the resulting dataset will contain only a single protein and solute type. 
    6. Still within each iteration, using matplotlib, generate a fig and ax object using ```plt.subplots()```. Use the ```ax.scatter()``` function to create a scatter plot where the x value is the concentration of the solute (the ```conc``` column) and the y value is the structural dimensions of the protein (the ```chi``` column)

4. The end result will be a large number of scatter plots. Make sure you include the solute type and the protein type as text on your plot (you can use ```ax.set_xlabel()``` or ```ax.text()``` functions to display text from the iterable variable (google how these commands work if needed).

5. Upload 5 of these plots as png files to the class 12 assignment on blackboard, as well as the script.

# Seaborn – a package for statistical data visualization

Often we will need to work with large datasets that have many dimensions or representations. Turning these into a single bar graph not only loses much of your data, it also hides away information that could be crucial to understanding or interpreting the data. For example:

<img src="./images/superPlots.png" width = 450 align="center">

1. The Seaborn python library offers many options to visualize data in an inclusive way, with lots of bells and whistles. This is a great library for publication-level graph preparation. 

2. Lets try plotting a swarm plot of some data. First, start a new notebook in your class12 directory. Download the [dataset](./files/cells.csv) file and import it using pandas ```pd.read_csv()```. 

```python
cells = pd.read_csv('cells.csv',index_col=0)
```

3. Have a look at the data. Each row contains information about a single cell measured under the microscope. Each cell has a specific labeled protein expressed inside it, denoted in the ‘prot’ column.

4. We want to understand how the identity of the protein affects different parameters for this dataset. To do this with matplotlib requires some extensive slicing. Seaborn lets us do this very easily. First, let's install seaborn. Remember that you need to run this line ONLY ONCE, so you can erase the cell after it has run.

```python
!pip install seaborn
```

5. In the first cell, now add an import for seaborn in your script:

```python
import seaborn as sns
```

6. Next, let’s visualize the data using a box chart:

```python
sns.boxplot(x='prot', y='area', data=cells, showfliers=False)
```

7. here we use the categorical protein name as the x axis and the cell area in μm2 as the y-axis. Is there a correlation?

8. Now let’s move sequentially over each column in our dataset and see where the protein identity determines the parameter. Write a simple code to do this - you can use ```cells.columns``` do get a list of all parameters.

9. Box charts are nice, but they do not show if the data is uniformly distributed or has multiple modalities. A violin plot shows the full distribution of the curve. Let’s try doing that! 

```python
sns.violinplot(x='prot',y='area',data=cells)
```

10. In the case we have an x-axis that is not categorical, we can use scatterplots to plot the data. For example, let’s look at how the cell area correlates with the directA_before parameter, which is a proxy for protein concentration.

```python
sns.scatterplot(x='area',y='directA_before',data=cells,alpha=0.2)
```

11. We can color this scatterplot using a categorical columns, like the protein identity ‘prot’ or the data the cell was measured ‘date’:

```python
sns.scatterplot(x='area',y='directA_before',
data=cells,alpha=0.2,hue='prot')
```

12. The plotreg command lets us look at correlations. Coupled to database slicing this becomes very powerful. Start a new script, and write in the following:

```python

axIdx = 0 # set a counter
fig,ax = plt.subplots(1,4,figsize=[12,4],sharex=True,sharey=True) # create axis subplots
color = sns.color_palette() # generate colormap

# loop over all protein names
for prot in cells['prot'].unique():
    # slice the dataFrame
    sliced = cells[cells['prot']==prot]
    # plot
    sns.regplot(x='directA_before',y='D/A_before', color=color[axIdx], scatter_kws={'alpha':0.2,'s':1}, data=sliced, ax=ax[axIdx], order=1)
    axIdx+=1
```

13. You can notice that the scattered points often overlap. We may want to display this as a density map instead, such that regions on the plot where there are many points show up as a high density. This lets us better observe the features on the plot. Add the following lines to in a new cell:

```python
axIdx = 0 # set a counter
color = sns.color_palette()  # generate colormap

# loop over all protein names
for prot in cells['prot'].unique():
    # slice the dataFrame
    sliced = cells[cells['prot']==prot]
    # plot
    sns.jointplot(x='directA_before',y='D/A_before', color=color[axIdx],data=sliced,kind='hex')
    # set graph limits
    plt.xlim(0,20000)
    plt.ylim(0.1,0.7)
    plt.text(300,0.68,prot,fontsize=20)
    axIdx+=1

```

14. You can view many more (working!) examples in the [seaborn gallery](https://seaborn.pydata.org/examples/index.html)