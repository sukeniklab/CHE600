# CHE600 Class 8 – First program and numpy

Today we will write our first scientific "simulation" and learn about the numpy library. 
Topics include:	
1. [Random walker](#scientific-simulation-does-a-random-walker-ever-get-back-home)
2. [Intro to numpy](#adding-functionality-to-python-numpy)
3. [Independent work: generating a board](#independent-work)

# Scientific simulation: Does a random walker ever get back home?

A [random walk](https://en.wikipedia.org/wiki/Random_walk) describes a process that progresses through a series of steps, where each step is decided randomly. It is used to model a vast range of systems, from [financial markets](https://en.wikipedia.org/wiki/Random_walk_hypothesis) to [polymer structure](https://en.wikipedia.org/wiki/Ideal_chain) to [bacterial motion](https://en.wikipedia.org/wiki/Chemotaxis). The beauty of this system the vast complexity that arises from a very simple set of rules.

## I. 1D random walker
1. Consider a 1-dimensional random walker that starts out at position 0 (aka _home_) and randomly takes steps forward (+1) or backward (-1).  What is the probability that the random walk gets back An interesting question is what fraction of such random walkers ever get back home (position 0) in 1 step? In 2 steps? In 3 steps? In 10,000 steps? Let's write some code to simulate this.
 
2. Start a [new Jupyter notebook](../Class_07-Python_intro/README.md/#iii-jupyter-notebooks) on VSCode. Save it in your class_08 directory as "random_walkers.ipynb". In the first cell, insert the following code and run it.

```python
from random import choice
# how many 1D random walkers to send out
trials=1
# how many steps each walker takes
steps=50
# a variable to check if the walker got home.
gothome=0
```

3. That takes care of our imports and variables. Next, in a new cell, put the main part of the code:

```python
#loop over trials
for i in range(trials):
    position=0
    # loop over steps
    for step in range(steps):
        position+=choice((-1,1))
        # if the walker got home, break out of the steps loop and move to next trial
        if position==0:
            gothome+=1
            break
print("For %i trials, fraction that got home=%f" % (trials, gothome/trials))
```

4. Run this program. What is your result? 

4. Change the number of trials from 10 to 100, and then to 1,000, and re-run every time (don't forget to run both the top and the bottom cells!). Did the fraction that got home change?

5. Change the number of steps to 10,000 and re-run with 1,000 trials. Did the fraction that got home change?

## II. 2D random walker

1. The problem gets more interesting and complicated as we increase the number of dimensions the random walker is moving around in. **Extend the script above to make the walker move in two dimensions instead of just one.**
    1. To do this start a new cell, and copy and paste the 1D walker as a starting point for the 2D walker.
    2. You will need to add another variable similar to point in the 1D walker (but with a different name so point does not overwrite) and assign it a random value. 
    3. Note that if we randomly change both x & y coordinates by -1 or +1, the walker moves diagonally like a checkers piece. How can you make some of the steps move straight instead of diagonally?
    4. There is some nuance in how you write the code. For example, do you consider movements in both dimensions at once? Do you pick a dimension randomly then move only on that dimension? Does this affect the outcome? 
    5. Either way you picked, write down the fraction of runs that returned to (0,0).

2. Finally, in a new cell extend your script to 3 dimensions. Calculate the fraction of runs that returned home. 

3. This exercise will need to be submitted. For submission, upload your notebook ```random_walkers.ipynb``` to the "class 8 - random walkers" submission link on blackboard. In the textbox, please write what fraction of walkers returned home for each dimensionality.

## III. Optional independent work – N dimensions random walker

Mathematicians have solved (complicated) equations to predict what fraction of random walkers get home in an infinite number of steps for different dimensions.  (Data from: http://mathworld.wolfram.com/PolyasRandomWalkConstants.html)

1. Let’s create random walker simulations in N-dimensions. Your task is to write a general script that will have the number of dimensions as a variable, use this to generate the walkers and print out the fraction of walkers who returned home. Save this script as rwalknd.py

2. To do this, store the location as a list with N integers, where N is the number of dimensions. For every step of the walker, change each member of this list by ± 1 at random using the choice function.

3. Feel free to play around with steps/trials, but 10000/100 is a good estimate. How do you think accuracy will be affected by this? How do you expect the number of walkers that returned home to change as the number of dimensions increases?

4. Make a .csv file (manually, for now) with the header “N_dimensions,fraction_returned” that contains all the fractions your script has calculated, and save it as returned_home.csv. Upload this as well as your script to canvas using the upload link.

5. If you’ve completed this, please submit to the week5 module as well.

# Adding functionality to python: Numpy
I. Intro to Numpy

Numpy is a library that includes many new functions related to numerical operations, but most importantly numpy introduces a new data type, the numpy array, which lets us work with vectorized variables. Vectorized variables are similar to lists, but they can only contain a single type of numeric variable (int, float), and can contain any number of dimensions (1D - vector, 2D - matrix, nD - n-dimensional matrix).

Like most other python libraries, Numpy is an open source library that is developed by volunteers. You can find more information about the numpy project [here](https://numpy.org/). A free textbook, Numerical Python, is available [here](https://jrjohansson.github.io/numericalpython.html). We will reference this book on occasion. It is an excellent reference for a few popular libraries, including Numpy

## I. The numpy array

Arrays are numerical matrices that have a host of operations that you can perform on them. Let’s create a numpy array. 

1. Start a new jupyter notebook in VSCode. Call it "numpy.ipynb". Input the following commands into the first cell:

```python
import numpy as np
arr = np.array([1,2,3,4,5])
arr
print(arr)
```

2. Arrays do not behave like python lists. Try this example in a new cell:

```python
lis = [1,2,3,4,5]
print(type(lis))
print(type(arr))
print(lis*4)
print(arr*4)
```

3. Numpy arrays contain numerous _properties_ that report on dimensions, shape, and other parameters. These are **not** functions - they do not require any arguments or parameters (hence they do not have ```()``` following the call). Here are a few to try out, in a new cell type:

```python
print(arr.ndim) #numer of dimensions
print(arr.shape) #shape of the array
print(arr.size) #number of elements in the array
print(arr.dtype) # data type of the elements in the array
```

4. arr is a one dimensional array (aka vector). How can we define an array with 2 dimensions (aka matrix)?

```python
data = np.array([[1,2],[3,4],[5,6]])
data
print(data)
type(data)
data.ndim  
data.shape # no. of rows and columns (in that order) of the array
data.size  # how many elements in the array
data.dtype # type of data in the array (int/float)
```

## II. Creating Numpy arrays

1. There are many ways to create NumPy arrays below. Many more ways in Table 2-3 below.

```python
data3 = np.zeros([100,3]) # a 100x3 matrix of zeros
data4 = np.ones([100,3])  # a 100x3 matrix on ones
data5 = np.random.rand(20,5) # a 20x5 matrix of random numbers between 0 and 1
data6 = np.linspace(0,1,50) # a 50-element array of numbers between 0 and 1 with a fixed increment
data7 = np.arange(500) # an array of integers from 0 to 499 (similar to range)
```

2. We can create empty arrays:

```python
empty=np.array()
```

3. Note that arrays are not lists, but we can create an array FROM a list:

```python
myList=[1,2,3,4,5,6]
print(type(list6))
myArr=np.array(myList)
print(type(myArr))
```

## III. Slicing and dicing numpy arrays

Like lists, arrays have indices that can be used to call slices or set values in specific positions of arrays. But numpy arrays contains a huge number of new and powerful functions. Some of these are described below. Others can be found in [Numerical Python](https://nbviewer.org/github/jrjohansson/numerical-python-book-code/blob/master/ch02-code-listing.ipynb)

1. Like lists, we call the array with an index in square brackets to call the contents of that range. Remember that all indexing in python starts from 0! Because arrays are not one dimensional, we can provide an index in each dimensions using comma. Try the following:

```python
print(data5)
print(data5[0,:])   # returns the entire 1st row of the data5 array.
```
```python
print(data5[0]) # same as above
```
```python
print(data5[0,0]) # returns a scalar from first row and column
```
```python
print(data5[0:10,0:1]) # returns the first 10 rows of the 2 right-hand side columns
```

2. We can work in multiple dimensions. Here is a 3D example, but this can be extended to any number of dimensions:

```python
# Create a 5x5x5 array of random numbers
randomCube = np.random.rand(5,5,5)
print(randomCube[:,:,-1]) # prints all rows and columns of the last "slice" of the cube
```

3. We can search arrays for specific conditions:

```python
# the where function accepts a conditional. 
# In this case, the conditional looks for values in randomCube larger than 0.5
print(np.where(randomCube>0.5))
```

4. Numpy has many functions that can reshape arrays. For example, we can turn our 3D cube into a 2D matrix:

```python
# we can reshape the cube to a 2D matrix, eliminating one of the dimensions
print(randomCube.shape)
myArr = np.reshape(randomCube,[25,5])
print(myArr.shape)
```
```python
# we can reshape a vector to a 2D matrix
vec = np.random.randn(49)
print(vec)
vec = np.reshape(vec,[7,7])
print(vec)
```

5. We can get the sum, mean, median, standard deviation, or other calculatable constants from our arrays quickly:

```python
# the sum function
print(np.sum(randomCube))
```
```python
# the sum function on a slice
print(np.sum(randomCube[:,:,2]))
```
```python
# mean, median, and standard deviation
print(np.mean(randomCube))
print(np.median(randomCube))
print(np.std(randomCube))
```

## IV. Numerical calculations with arrays 

The main power of arrays is that we can perform mathematical operations on each element of the array in one quick line. 

1. To understand the power of arrays, let's try performing mathematical operations on a list:

```python
alist = list(range(50))
# addition or multiplication will not work:
print(alist * 2)
print(alist + alist)
```

If we want to do operations, we actually need a for loop. This is annoying, reduces readability of our code, and increases the computational cost of our script:

```python
newlist=[]
for i in range(len(list)):
    newlist.append(alist[i]*2)
print(newlist)
```

2. Numpy arithmetic works the same way as scalars element-by-element. It is very easy to write, and very computationally efficient:

```python
aarray = np.arange(50) # create a vector with integers 0 to 9
print(aarray+aarray) # element-wise addition of X
print(aarray * 2) # should give same result
```

## V. Numpy functions


```python
# we can calculate averages along for the entire array
print(np.mean(data6,axis=0))
```
data9 = np.mean(data6,axis=1)
data10 = np.mean(data6)

## VI. Numpy file I/O (input/output)

Numpy has very powerful commands to import and export numeric data. The main commands are loadtext and savetxt. Let’s try it out. 

1. Download CONTACTMAP.dat from this week's module on blackboard. Save it to your ```class_08``` working directory. What is your working directory? It will appear in the explorer tab on the left hand side of the VSCode window.

1. Start a new script called "import.ipynb". Make sure it's in the same directory as the CONTACTMAP.dat file. In the first cell place the import code ```import numpy as np``` and in the next cell write the following:

```python
data_load = np.loadtxt('CONTACTMAP.dat', skiprows=1)
print(data_load.shape)
print(data_load.dtype)
print(data_load[1,:])
```

2. ```loadtxt()``` is a numpy function with lots of options. It requires one parameter: the name of the file (a string or a string variable). We pass it another, optional parameter, skiprows, which tells it how many rows from the top it should skip for the import (for example if they contain a text header - remember that arrays can only contain one type of variable!). The help for [np.loadtxt](https://numpy.org/doc/2.1/reference/generated/numpy.loadtxt.html) contains all the parameters, their meaning, and their default values.

 3. The ```np.savetxt``` command saves a text file. also has lots of optional [parameters](https://numpy.org/doc/2.1/reference/generated/numpy.savetxt.html) to help you format the output you want. Let’s try it out:

```python
data = np.random.randn(100,3)
np.savetxt('data.csv', data, delimiter=',', header='x,y,z',comments = '\"# random x, y, z coordinates\"\n')
```

4. Remember that if the filename does not contain a directory path it will be written in your current working directory, which is highlighted in orange in the VSCode explorer. You can now use excel or a text editor to open the file and look at its contents.

# Independent work

1. Start a new python notebook called board.ipynb. The script should generate a numpy array called ```board``` which will be a 2D (square) matrix of size NxN, where M positions on the matrix, randomly selected, will have the value 1 and the rest will have the value 0. N and M should be variables that are defined in the beginning of the script. 

2. **Note:** There are many ways to do this simple task. I suggest you try tackling it yourself, and not assigning it to an LLM - remember right now you are trying to learn how to think like a programmer! You should always start with small N's and M's, and print out your output to help debug your script.

3. See hints below if you are stuck.

<details>
<summary><b>Different options to solve this problem</b></summary>
* use a for loop to assign 1's (simplest but most expensive computationally) 
* use np.random.choice() to pick M matrix indices and set their value to 1
* create a vector of zeros of size N^2, set the first M positions as 1, then shuffle and reshape into an NxN matrix
</details>

4. With the script to prepare the ```board``` array completed, use the sum function of the array (```board.sum()```) to verify you have exactly M ones. Print out the array itself and the number of ones.

5. Upload board.ipynb to the blackboard "class 8 - board" submission link, as well as screenshots of 5 5x5 arrays with 8 1’s in each. 


