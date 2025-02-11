# CHE600 class 9 - numpy (cont.)

Today we will continue our exploration of numpy arrays, and then use them to write a script which we will use later in class. 

Topics include:	
1. [Numpy array slicing and dicing](#iv-slicing-and-dicing-numpy-arrays-cont)
2. [Independent work: generating a board](#independent-work)
3. [Visualizing with matplotlib](#visualizing-data-with-matplotlib)

## IV. Slicing and dicing numpy arrays (Cont.)

(we are picking up from [here](../Class_08/README.md#iv-slicing-and-dicing-numpy-arrays)). Start a new jupyter notebook in a class09 directory. In the first cell make sure you have ```import numpy as np```.

3. We can search arrays for specific conditions using the ```np.where()``` function. This function accepts conditionals, and returns a list arrays - each array is the indices where the condition is met in a single dimension. In this case, the where command will return two lists of indices where our random 2D matrix has values higher than 0.8:

```python
# Generate a 10X10 matrix of random numbers
random2D = np.random.rand(10,10)
# feed the result of the np.where() function into two variables: x and y
# The conditional is that the value of random2D must be larger than 0.8
[x_idx,y_idx]=np.where(random2D>0.8)
# Loop over each index in x, then look up the value of that index in the matrix
for i in range(len(x_idx)):
    print('(%i, %i) value is %f' % (x_idx[i],y_idx[i],random2D[x_idx[i],y_idx[i]]))
```

4. Numpy has many functions that can reshape arrays. For example, we can turn our 3D cube into a 2D matrix:

```python
# we can reshape the cube to a 2D matrix, eliminating one of the dimensions
randomCube = np.random.rand(5,5,5)
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
# the sum function be default summs all elements
print(np.sum(randomCube))
# we can also provide the axis to work on as a parameter. Here we're summing over columns
# but since this is a 3D matrix it will return a 2D matrix
print(np.sum(randomCube,axis=1))
# We can carry another sum operation to return a vector
print(np.sum(np.sum(randomCube,axis=1),axis=0))
```
```python
# the sum function on a slice
print(np.sum(randomCube[:,:,2]))
```
```python
# mean, median, and standard deviation all have specific functions
# notive that we can run them on a full array, but also on sliced (same as the np.sum() function)
mean = np.mean(randomCube)
median = np.median(randomCube)
std = np.std(randomCube)
print('random cube mean: %f, median: %f, std: %f'%(mean,median,std))
```

## V. Numerical calculations with arrays 

The main power of arrays is that we can perform mathematical operations on each element of the array in one quick line. 

1. To remind us of the power of arrays, let's try performing mathematical operations on a list (We've already seen this, but just so we're keeping track!)

```python
alist = list(range(10))
# addition or multiplication will not work:
print(alist)
print(alist * 2)
print(alist + alist)
```

Mathematical operations on a list require for loop. This is annoying, reduces readability of our code, and most importantly increases the computational cost of our script:

```python
newlist=[]
for i in range(len(alist)):
    newlist.append(alist[i]*2)
print(newlist)
```

2. Numpy arithmetic works the same way as scalars element-by-element. It is very easy to write, and very computationally efficient:

```python
aarray = np.arange(10) # create a vector with integers 0 to 9
print(aarray)
print(aarray+aarray) # element-wise addition of X
print(aarray * 2) # should give same result
```

## VI. Numpy file I/O (input/output)

Numpy has very powerful commands to import and export numeric data. The main commands are loadtext and savetxt. Let’s try it out. 

1. Download [CONTACTMAP.dat](./files/CONTACTMAP.dat) from the link or from this week's module on blackboard. Save it to your ```class_09``` working directory. **What is your working directory?** It will appear in the explorer tab on the left hand side of the VSCode window, or you can type ```pwd``` in a cell to find out!

2.  In a new cell place the import code write the following:

```python
data_load = np.loadtxt('CONTACTMAP.dat', skiprows=1)
print(data_load.shape)
print(data_load.dtype)
print(data_load[35,:])
```

3. ```loadtxt()``` is a numpy function with lots of options. It requires one parameter: the name of the file (a string or a string variable). We pass it another, optional parameter, skiprows, which tells it how many rows from the top it should skip for the import (for example if they contain a text header - remember that arrays can only contain one type of variable!). The help for [np.loadtxt](https://numpy.org/doc/2.1/reference/generated/numpy.loadtxt.html) contains all the parameters, their meaning, and their default values.

 3. The ```np.savetxt``` command saves a text file. also has lots of optional [parameters](https://numpy.org/doc/2.1/reference/generated/numpy.savetxt.html) to help you format the output you want. Let’s try it out:

```python
data = np.random.randn(100,3)
np.savetxt('data.csv', data, delimiter=',', header='x,y,z',comments = '# random x, y, z coordinates\n')
```

4. Remember that if the filename does not contain a directory path it will be written in your current working directory, which is highlighted in orange in the VSCode explorer. You can now use excel or VSCode directly to open the file and look at its contents.

# Independent work

1. Start a new jupyter notebook called board.ipynb. 

2. Your tasp is to generate a numpy array called ```board``` which will be a 2D (square) matrix of size NxN, where M positions on the matrix, randomly selected, will have the value 1 and the rest will have the value 0. N and M should be variables that are defined in the beginning of the script. 

2. **Note:** There are many ways to do this simple task. I suggest you try tackling it yourself, and not assigning it to an LLM - remember right now you are trying to learn how to think like a programmer! You should always start with small N's and M's, and print out your output to help debug your script.

3. See hints below if you are stuck.

<details>
<summary><b>Different options to solve this problem</b></summary>
<li> use a for loop to assign 1's (simplest but most expensive computationally, also might pick the same position twice)
<li> use <a target="_blank" href="https://numpy.org/doc/2.1/reference/random/generated/numpy.random.choice.html#numpy.random.choice">np.random.choice()</a> function with the ```replace=False``` parameter to pick M unique matrix indices and set their value to 1
<li> create a vector of zeros of size N^2, set the first M positions as 1, then <a target="_blank" href="https://numpy.org/doc/2.1/reference/random/generated/numpy.random.shuffle.html">shuffle</a> and <a target="_blank" href="https://numpy.org/doc/2.1/reference/generated/numpy.reshape.html#numpy-reshape">reshape</a> into an NxN matrix
</details>

4. With the script to prepare the ```board``` array completed, use the sum function of the array (```board.sum()```) to verify you have exactly M ones. Print out the array itself and the number of ones.

5. Upload ```board.ipynb``` to the blackboard "class 9 - board" submission link, as well as screenshots of 5 5x5 arrays with 8 1’s in each. 

# Visualizing data with matplotlib

To visualize numerical data, we will use the [Matplotlib](https://matplotlib.org/) package. This is another one of the most popular python libraries, with very extensive [support](https://matplotlib.org/stable/users/index),[tutorials](https://matplotlib.org/stable/tutorials/index) and a massive [gallery](https://matplotlib.org/stable/gallery/index.html) of visualization examples, complete with code. Because it's so heavily used, LLMs tend to be very good at generating matplotlib visualizations, and you are encouraged to try it. Our end goal today is to is to visualize the "boards" of 0's and 1's we've created. 

## I. Matplotlib intro

1. Start a new notebook in your class 9 directory called ```visuals.ipynb```. Let's start by making sure matplotlib is installed. To do this, run ```pip``` using a system command (```!```) iun the same way we've done for numpy. Notice you will only need to do this once, not every time you want to use matplotlib!

```python
!pip install matplotlib
```

2. Next, let's import matplotlib into our iPython console. Note that the actual "visualization engine" of matplotlib is coded in a sub-library called pyplot, for which the standard import is as ```plt```. Let’s also import Numpy because we will be using it to generate and process data:

```python
import matplotlib.pyplot as plt
import numpy as np
```

3. Now, let’s use numpy to generate some data:

```python
# generate 100 linearly spaced x-values between -5 and 2
x = np.linspace(-5,2,100)
# use a polynomial to generate 100 y-values based on x
y = x**3 - 2*x**2 -5
# add normally distributed random numbers to y values 
# using the randn() function to simulate experimental noise.
y += np.random.randn(100)
```

4. We've generated an (x,y) dataset. Let's try some visualizations!

```python
plt.plot(x,y)
```
```python
plt.scatter(x,y)
```
```python
plt.plot(x,y)
plt.scatter(x,y)
```

5. Notice that this appears "in-line" in your notebook. This is very useful to display the result of a calculation and/or visualization. However, sometimes we'd want our images to open up in a separate window. We can change this behavior to show up in its own window by typing the magic command %matplotlib. 

```python
# set figure to pop up in a new window
%matplotlib qt 
plt.plot(x,y)
plt.scatter(x,y)
```
```python
# back to normal ("in-line") behavior.
%matplotlib inline
plt.plot(x,y)
plt.scatter(x,y)
```

6. Let’s play around with some more options. We’ll plot several plots on the same axes. In a new cell, add the following lines: 

```python
# Generate first and second derivatives of y
y2 = 3*x**2 + 4*x
y3 = 6*x + 4

# Generate a plt figure object called fig and a plt axis object called ax
# using the plt.subplots() function. This allows you to modify the plotting area.
# Here we pass the figure size we want into this function
fig,ax = plt.subplots(figsize=[5,5])
print(type(ax))
print(type(fig))

# Now call the plot() function through the ax object. 
# Note this has to be done in the same cell!
ax.plot(x,y,color = 'red', label='y')
ax.plot(x,y2,color = 'blue', label='y\'')
ax.plot(x,y3,color = 'green', label='y\'\'')
ax.legend(title='lines')
```

7. Let’s try to plot a few figures side by side. In a new cell:

```python
fig,ax = plt.subplots(1,3,figsize=(12,4))
ax[0].plot(x,y,color = "red", label="y")
ax[1].plot(x,y2,color = "blue", label="y'")
ax[2].plot(x,y3,color = "green", label="y''")
for i in range(3):
    ax[i].set_xlabel("x")
    ax[i].legend()
    ax[0].set_ylabel("y")
```

## II. Visualizing boards

Our next goal is to generate a board using the code we've written [before](#independent-work). If you don’t have this code ready, now is the time to complete it! 

1. Let’s load our board.py script from last class into a new cell and run it to generate a variable called ```board```. Let's use N=5 and M=8 for this initial visualization. 

2. We want to visualize this board. A good way to do that would be to use scatter, which draws markers (as opposed to lines) on a 2D axis. To do that, we would need the (x,y) coordinates (i.e. the row and column number) of all the ones in the matrix. We can do this easily with Numpy’s np.where command:

```python
fig,ax = plt.subplots(figsize=[5,5])
[x,y] = np.where(board==1)
ax.scatter(x,y,marker="s",c='red',s=500)
[x,y] = np.where(board==0)
ax.scatter(x,y,marker="s",c='grey',s=500)
```

3. There are other ways to visualize this type of map – for example ```plt.imshow()``` and ```plt.pcolor()``` are two other options that can visualize the board directly (ie, will not need the np.where() function). Try them both - there is no one correct answer!

## III. Saving visualizations


1. Once a figure is generated, there's no need to keep it only in the notebook! We can copy it from VSCode and paste it directly any where we'd like. 

2. More importantly, we can also export our figures in different formats. To do this we call the savefig() function through the ```fig``` object we created with the ```plt.subplots()``` command. Note that like every other function we learned today, there are many options to savefig, and you can export in different formats/resolutions/etc. 

```python
fig.savefig('board.png')
fig.savefig('board.svg')
```

3. Upload ```board.png``` and ```visuals.ipynb``` to the class 9 "Board" submission link on blackboard

3. Note that matplotlib automatically detects the format of the figure based on the suffix. A file name ending with ```.png``` will generate a raster image (composed of pixels) that is good for emailing or displaying on a webpage. A ```.svg``` creates a scaleable vector graphics that has unlimited resolution (i.e. you can size it as small or large as you want without suffering pixelation). This is the prefered format for scientific publications, and can be opened with Adobe Illustrator or [Inkscape](https://inkscape.org/) (free and recommended!).
