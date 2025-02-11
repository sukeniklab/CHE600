# CHE600 - Class 10 - defining functions

Today we'll learn how to define functions in scripts. We've mentioned in the beginning that python can be run "sequentially" (i.e. line-by-line) which is what we've done so far. Today we'll learn how to create our own functions that will accept parameters and return specific results.


# defining functions

## I. The def keyword

Python allows you to define functions in scripts. In this way, you can call the function from anywhere in your script, any number of times. The function, like others we’ve used can accept any inputs you define, and return anything that has been created during its executation as output.

1. Let’s start by writing a function called genBoard that accepts two variables, N and M, and generates an NxN 2D matrix with zeros and M ones. Start a new jupyter notebook in class10 directory called make_board.ipynb. 

2. Import numpy and matplotlib.pyplot into it in the first cell. 

3. In a new cell, define a new function using the ```def``` keyword. Note that when you run this cell nothing will happen. This is because we only DEFINE the function, but do not actuall call it!

```python
def genBoard(N,M):
	# print a line every time the function runs
	print('genBoard is now running!')
	# return two variables: N-2 and M+2
	return(N-2,M+2)
```

4. This function is called by calling genBoard(), and accepts two arguments – M and N. Notice the format here is like a for loop or conditional – everything following def with an indent will be a part of this function! Let's now call the function and observe the output. In a new cell, type:

```python
[out1,out2]=genBoard(30,56)
print(out1)
print(out2)
```

5. We have placed the values RETURNED by ```genBoard()``` into two variables, ```out1``` and ```out2```. Notice that even though these variables are named ```M``` and ```N``` in genBoard, they are not included in our namespace (see the jupyter variables list to be convinced!). We can call this function as many times as we want:

```python
for i in range(10):
	genBoard(i,i+45)
```


3. Adapt the ```board.py``` function to accept these two variables and generate a board. The function should terminate with the return keyword:

```python
return(<variable name(s)>)
```

This will exit the function and pass the returning variable either into your standard out, or into a variable. For example:

```python
aBoard = genBoard(10,10)
```

will create a 10x10 numpy array filled with 0’s and 10 1’s in random positions. Like in conditionals and for loops, you can also break out of functions, or have several return instances based on conditionals

e.	Now, adapt your own board.py implementation into this function. Remember to use the variables passed into it (M and N) in your code, and to return the final numpy “board” array at the end of the function.

f.	We can now call this function from our script – but because python is an interpreted language, the function definition must come before the script calling it! Put the following lines in a new cell (#%%) after the function definition (def) into board.py:

```python
N=20
M=70
board=genBoard(N,M)
```

This script, to be executed AFTER the function genBoard() has been defined, should generate a variable called board, which is a 20x20 numpy array with 70 1’s and all other elements 0’s. 


3.	Independent work: Write two functions: 
a.	The first function should be called drawBoard() This function accepts an NxN matrix of 0’s and 1’s (we refer to this as a board) and then plots it using matplotlib. 

b.	The second function should be called countNeighbors() This function accepts a board as input and returns a new board (NxN matrix) where each element contains the number of neighboring 1’s in the original board. 

c.	For now, a neighbor is defined by a square with a 1 that is immediately adjacent to another square with a 1. Do not count diagonals. 

d.	We assume the board is “infinite” – which means the top row is in contact with the bottom row and the left-most column is in contact with the right-most column. This is sometimes called “periodic boundary conditions” and lets us simulate an infinite system.

e.	See examples below:

Input board:
0	0	0
0	1	0
0	0	0
	0	1	0
1	1	0
0	0	0
	0	1	1
0	1	1
0	0	0
	1	1	0
1	1	1
0	1	1


Output neighbor matrix:
0	1	0
1	0	1
0	1	0
	2	1	0
1	2	2
1	2	0
	1	1	2
2	2	1
0	1	1
	2	3	4
2	4	3
0	2	2




f.	You can write these functions in any way you want – bonus points if there are no for loops! Hint: you can shift your matrix up/down/left/right by one cell using the np.roll function (see the help file)

g.	Put these functions in a single script together with your genBoard function. The file should start with the three functions, (ie, 3 def commands to define the functions) then in a new cell (#%%) write a script that will create a board, visualize it, and return a neighbor matrix by calling the three functions.

h.	This is a step up in difficulty – please feel free to discuss with me/each other/ChatGPT/Google on how to approach this challenge! Hints:

i.	Start with SMALL boards where you can easily visualize and count neighbors yourself. 
ii.	Implement periodic boundaries only AFTER your code is working without them.
iii.	Remember what the input and output should be as you write your code.
iv.	1x1 = 1; 1x0 = 0

Upload your full script (should include the three functions: genBoard(), drawBoard(),  and countNeighbors(), and the calls to these functions), as well as a screenshot of the visualized board and the neighbor matrix (either visualized or in text form from the iPython console is fine) of a 20x20 matrix with 70 ones.



