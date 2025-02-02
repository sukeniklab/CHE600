# Chem 260 Class 7 – Python intro!

Today we start working with Python - which will be the language of choice for the rest of the semester. 
Topics include:	
1. [Python Overview](#python-overview)
2. [Running python](#)
    * [The python shell]
    * [the VSCode integrated working environment]
    * [Jupyter notebooks]
5. [Variables]
6. [Loops and conditionals]
7. [First coding exercise: random walk]

# Python Overview

## I. History ##

1. Python was developed in the 80's as a hobby. It emphasized code readability (ie the ability of someone who didn't write the code to understand what it does). Modern python can be run:
    * In a structured (procedural) way - line by line
    * By calling specific defined functions (we will see this today)
    * Using Object-Oriented architecture (we will see this towards the end of the semester)

2. Python is designed to be a highly readable language with a clean and uncluttered syntax. Unlike languages that rely on curly brackets and semicolumns to define code blocks, Python uses indentation for structure. Additionally, Python has fewer syntactic exceptions and special cases compared to languages like C.

3. Python is routinely one of the most sought after programming language in any data science/research job. It is also the _lingua franca_ of machine learning.

3. For further reading on history and philosophy of the language, see [here](https://www.geeksforgeeks.org/history-of-python/)

## II. Libraries ##

1. One of the best aspects of python is the availability of libraries. These are code written by others that one can import into your own python script/program

2. The library introduces new functions and data structures that dramatically expand the options provided by the standard (aka _vanilla_) python interpreter.

3. All one has to do is install the library locally (we will see how to do this), then _import_ the library into the code. All functions from the library become immediately accessible

## II. Version ##

1. We will be using Python 3.13 - this is the latest "stable" - fully supported - version of the code. The versions are meaningful. Trying to run python 2.X code in a python 3 environment will result in an error, and vice versa. 

2. Another major tenet of Python is backwards compatbility - meaning every subsequent version should support all syntax and function of previous versions. Though this is obviously best, some libraries (more about this later) require a specific python version to work (though this is rare, especially in popular and well-maintained libraries).

# Running python
## I. The python terminal

1. Last week we've installed the python interpreter and VSCode on our computers. Let's start by running the python interpreter. Open your start menu, search for python - make sure you select Python 3.13, and run it. 

<img src="./images/shell_01.png" width=350>

2. The shell should look like this:

<img src="./images/shell_02.png" width=350>

3. In the shell, try the follow:

```python
print("Hello world!")
```

```python
a=20
```

```python
b=300
```

```python
a*b
a/b
```


