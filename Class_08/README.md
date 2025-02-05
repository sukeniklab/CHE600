# CHE600 Class 8 – First program and numpy

Today we will write our first scientific "simulation" and learn about the numpy library. 
Topics include:	
1. [Python Overview](#python-overview)
2. [Running python](#running-python)


# Scientific simulation: Does a random walker ever get back home?

A [random walk](https://en.wikipedia.org/wiki/Random_walk) describes a process that progresses through a series of steps, where each step is decided randomly. It is used to model a vast range of systems, from [financial markets](https://en.wikipedia.org/wiki/Random_walk_hypothesis) to [polymer structure](https://en.wikipedia.org/wiki/Ideal_chain) to [bacterial motion](https://en.wikipedia.org/wiki/Chemotaxis). The beauty of this system the vast complexity that arises from a very simple set of rules.

## I. 1D random walker
1. Consider a 1-dimensional random walker that starts out at position 0 (aka _home_) and randomly takes steps forward (+1) or backward (-1).  What is the probability that the random walk gets back An interesting question is what fraction of such random walkers ever get back home (position 0) in 1 step? In 2 steps? In 3 steps? In 10,000 steps? Let's write some code to simulate this.
 
2. Start a [new Jupyter notebook](../Class_07-Python_intro/README.md/#iii-jupyter-notebooks) on VSCode. Save it in your class_08 directory as "random_walkers.ipynb". In the first cell, insert the following code:

```python
from random import choice

# how many 1D random walkers to send out
trials=1

# how many steps each walker takes
steps=50

# a variable to check if the walker got home.
gothome=0

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

3. Run this program. What is your result? 

4. Change the number of trials from 10 to 100, and then to 1,000, and re-run every time (no need to start a new cell). Did the fraction that got home change?

5. Change the number of steps to 10,000 and re-run with 1,000 trials. Did the fraction that got home change?

## II. 2D random walker

1. The problem gets more interesting and complicated as we increase the number of dimensions the random walker is moving around in. **Extend the script above to make the walker move in two dimensions instead of just one.**
    1. To do this start a new cell, and copy and paste the 1D walker as a starting point for the 2D walker.
    2. You will need to add another variable similar to point in the 1D walker (but with a different name so point does not overwrite) and assign it a random value. 
    3. Note that if we randomly change both x & y coordinates by -1 or +1, the walker moves diagonally like a checkers piece. How can you make some of the steps move straight instead of diagonally?
    4. There is some nuance in how you write the code. For example, do you consider movements in both dimensions at once? Do you pick a dimension randomly then move only on that dimension? Does this affect the outcome? 
    5. Either way you picked, write down the fraction of runs that returned to (0,0).

2. Finally, in a new cell extend your script to 3 dimensions. Calculate the fraction of runs that returned home. This will need to be submitted. For submission, upload your notebook ```random_walkers.ipynb``` to the "random walkers" submission link on blackboard. In the textbox, please write what fraction of walkers returned home for each dimensionality.

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
data5 = np.random.rand(100,3) # a 100x3 matrix of random numbers between 0 and 1
list6=[1,2,3,4,5,6]
data6=np.array(list6)
```

## III. Slicing and dicing numpy arrays

Similar to lists, we call the array with an index in square brackets to call the contents of that range. More ways to slice arrays in Table 2-4 below:

data5[0]   # returns an array from 1st row of the data5 array.
data5[0,:] # same as above
data5[0,0] # returns a scalar from first row and column
data5[0:20,0] # returns the first 20 rows from the first column

K.	Numpy arithmetic works the same way as scalars element-by-element:

X = np.arange(10) # create a vector with integers 0 to 9
X + X # element-wise addition of X
X * 2 # should give same result
X / 2 # note this will change the dtype of the vector!

J. Notice this CANNOT be done with python lists that we studied last week! Try:

alist = [1,2,3,4,5]
alist * 2
alist + alist

What happens? How would you multiply each member of the list by 2? 
Now create an array from the list, and try again:

nplist = np.array(alist)
nplist * 2
nplist + nplist
 
L.	Numpy has many functions that can reshape, copy, or add onto arrays. More function in Table 2-5 in Numerical Python. Check the shape of each of these to try and understand what they do:

data6 = np.random.rand(100,3)
data7 = np.reshape(data6,[60,5])
data8 = np.mean(data6,axis=0)
data9 = np.mean(data6,axis=1)
data10 = np.mean(data6)




  
 



II. Numpy file I/O (input/output)

A.	Numpy has very powerful commands to import and export numeric data. The main command is called loadtext and savetxt. Let’s try it out. Download CONTACTMAP.dat from the week 5 module on CatCourses. Save it to your working directory. What is your working directory? It will appear here:


 

B.	 Import the file into spyder:

data_load = np.loadtxt('CONTACTMAP.dat', skiprows=1)
data_load.shape
data_load.dtype
data_load[1,:]
C.	loadtxt() is a numpy function with lots of options. It requires one parameter: the name of the file (a string or a string variable). We pass it another, optional string, skiprows, which tells it how many rows to skip (for example if they contain a header). Type np.loadtxt in the help search box to see all of them. 

 

D.	The np.savetxt command saves a text file. also has lots of flags to help you write the output you want. Let’s try it out:

data = np.random.randn(100,3)
np.savetxt('data.csv', data, delimiter=',', header='x,y,z',comments = '\"# random x, y, z coordinates\"\n')

You can now use excel or a text editor to open the file and look at its contents.

III. Independent work

A.	Write a script called board.py. The script generates a square matrix of size NxN, where M elements will have the value 1 and the rest will have the number 0. N and M should be variables that are defined in the beginning of the script. Hint: use np.random.choice to pick M specific matrix indices.

B.	Use the sum function of the array to verify you have the correct number of ones in your array. Print out the array and the number of ones.

C.	Upload board.py to CatCourses, as well as a screenshot of 5 5x5 arrays with 8 1’s in each. 


