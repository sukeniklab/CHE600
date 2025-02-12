# CHE600 - Class 10 - defining functions

Today we'll learn how to define functions in scripts. We've mentioned in the beginning that python can be run "sequentially" (i.e. line-by-line) which is what we've done so far. Today we'll learn how to create our own functions that will accept parameters and return specific results.

# defining functions

## I. The def keyword

Python allows you to define functions in scripts. In this way, you can call the function from anywhere in your script, any number of times. The function, like others we’ve used can accept any inputs you define, and return anything that has been created during its executation as output.

1. Let’s start by writing a function called genBoard that accepts two variables, N and M, and generates an NxN 2D matrix with zeros and M ones. Start a new jupyter notebook in class10 directory called make_board.ipynb. 

2. Import numpy and matplotlib.pyplot into it in the first cell. 

3. In a new cell, define a new function using the ```def``` keyword. Note that when you run this cell nothing will happen. This is because we only DEFINE the function, but do not actuall call it!

```python
def myFunc(x):
	# print a line every time the function runs
	print('myFunc is now running!')
	# return two variables: N-2 and M+2
	y=x*x
	return(x+2,y)
```

4. This function is called by calling myFunc(), and accepts a single input variable. It returns two variables: the input variable x incremented by 2, and y which is the square of x. Notice the format here is like a for loop or conditional – everything following ```def``` with an indent will be a part of this function! Let's now call the function and observe the output. In a new cell, type:

```python
[out1,out2]=myFunc(4)
print(out1)
print(out2)
```

5. We have placed the values RETURNED by ```genBoard()``` into two variables, ```out1``` and ```out2```. Notice that even though these variables are named ```x``` and ```y``` in genBoard, they are not included in our namespace (see the jupyter variables list to be convinced!). We can call this function as many times as we want:

```python
for i in range(10):
	[out1,out2]=myFunc(i+30,i+56)
	print(out1)
	print(out2)
```

## II. Turning a script to a function

1. Adapt the ```board.py``` function we wrote last class to accept these two variables and generate a board. The function should be called genBoard(M,N), where M and N are the number of 1's and the length of the board, respectively. The function should return the board: a NxN numpy array with M ones and NxN - M zeros.

2. This should essentially require you to copy and paste your board.ipynb code into the funciton, and maybe arrange some variable names. End the function with the ```return()``` command. This will exit the function and pass the returning variable either into your standard out, or into a variable. For example, the following function should create a 8x8 numpy array as a variable called ```aBoard``` filled with 0’s and 10 1’s in random positions. 

```python
aBoard = genBoard(10,8)
```

3. We can now call this function from our script – but because python is an interpreted language, the function definition must come before the script calling it! Put the following lines in a new cell after the function definition (def) into ```board.ipynb```:

```python
N=20
M=70
board=genBoard(N,M)
```

# Independent work

We will next write some additional functions. Each function will go in a new cell, and together they will form  an actual python program:

1. The first function should be called ```drawBoard()``` This function accepts an NxN matrix of 0’s and 1’s (we refer to this as a board) and then plots it using matplotlib. See [last week's class](../Class_09/README.md#ii-visualizing-boards) for details on how to do that. Notice that nothing should actuall be returned - so you can just end with an empty ```return()``` statement

2. The second function should be called ```countNear()``` This function accepts a board as input and returns a new board (NxN matrix) where each element contains the number of neighboring 1’s in the original board. This is a jump up in difficulty and requires some careful thinking on how to best implement this task.

	1. A neighbor is defined by a square with a 1 that is immediately adjacent to another square with a 1. Do not count diagonals. 

	2. We assume the board is “infinite” – which means the top row is in contact with the bottom row and the left-most column is in contact with the right-most column. This is sometimes called “periodic boundary conditions” and lets us simulate an infinite system.

	3. See examples below:

<img src=".images/board.png" width=450>

3. You can write these functions in any way you want – there is no wrong way. I strongly recommend you try this yourself before just handing this task off to an LLM. Bonus points if there are no for loops! Hint: you can shift your matrix up/down/left/right by one cell using the np.roll function (see the help file)

4. Once done, your jupyter notebook should start with the three functions, ```genBoard()```, ```drawBoard()```, and ```countNeighbors()```. Then in a new cell write a script that will create a board, visualize it, and return a neighbor matrix by calling the three functions. This is a step up in difficulty – please feel free to discuss with me/each other/ChatGPT/Google on how to approach this challenge! Hints:

<details>
<summary><b>Hints!</b></summary>
<li> Start with SMALL boards where you can easily visualize and count neighbors yourself. 
<li> Implement periodic boundaries only AFTER your code is working without them.
<li> Remember what the input and output should be as you write your code.
<li> 1x1 = 1; 1x0 = 0
</details>

Upload your full script (should include the three functions: genBoard(), drawBoard(),  and countNeighbors(), and the calls to these functions), as well as a screenshot of the visualized board and the neighbor matrix (either visualized or in text form from the iPython console is fine) of a 20x20 matrix with 70 ones.



