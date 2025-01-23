# CHEM260 F23 Class 4

Today's class will introduce us to script writing in bash. What we’ll cover today: 
* [Basics of script writing](#basics-of-script-writing)
* [iterations and loops](#iteration-and-loops)
* [Creating executables with input and output](#creating-executables-with-input-and-output)
* [Conditionals](#conditionals)

# **Basics of script writing**

## **I. What elements do we need to create powerful, flexible scripts?**

1. Generally, a script will need one or more of the following:
    a.	Ability to pass information to the script, such as names of files, options, etc.
    b.	Ability to loop over different values or files
    c.	Ability to make decisions to do different things based on the input or data
    d.	Ability to store values in variables
    e.	Ability to display results in clearly formatted outputs

2. In this class we will write many scripts. Our first scripts will be with the syntax of the linux shell (aka bash). Our scripts will generally not include completely new functions. Instead, they will bundle a set of bash commands (which we've learned about in the past few classes) in a useful way. In addition, our scripts:
    a. Can includes loops over sets of files or input values
    b. Can include conditionals (if statements) to do different things under different conditions
    c. Can contain variables – a value that can change, depending on conditions or on information passed to the program

## **II. Script formats: command line or executable##

In bash, we can write scripts in two ways. The first one is through the command line. In general, commands there will be seperatd by a semi-column (```;```). For example:

```bash
for i in $(seq 1 20); do echo "I just counted to $i"; done
```

Alternatively, we can write scripts (like the ```getProteomeDisorder.sh``` that we've used before). Which one to use depends on the complexity of the script, your need for reusability, and your convenience!

## **III. Variables in bash**

Variables are critical to any code. They allow you to store information and recall it within the memory of your application, without writing anything to the disk. 

1. Defining a variable is easy, simply use the equal sign: ```variable_name="this is the value of the variable"```. Try this (**notice you can't have any spaces next to the equal sign!**):

```bash
myVar="This is my variable"
```
```bash
echo myVar
```
```bash
echo $myVar
```
```bash
myVar
```
```bash
$myVar
```

What are the differences between the different commands? Notice that to actuall call your variable you need to preface it by a ```$``` sign.

2. We can also direct output into a variable. This is a bit different from directing output to a file, and looks like this:

```bash
myOtherVar=$(pwd)
echo $myOtherVar
```

3. Variables can be called as many times as you want and will remain in memory and can be called so long as you do not log out. They are overwritten if they are defined again. If you want to retain the original value, make sure you include it:

```bash
myOtherVar=$(echo "the first var was " $myOtherVar)
echo $myOtherVar
```

## **IV. Let’s write our first script:**

1. Create a new directory called ```class04``` in your ```~/CHE600``` directory, and move into that directory using ```cd```

2. Use ```nano``` to create a file called ```files.sh```

3. The first line of the script needs to be ```#!/bin/bash```  – this is called a “hashbang” and tells the shell which scripting language to use. This time it’s bash (being called from an executable that’s in the directory /bin). Later in the course we will also see this being used for python, and it can be used for any code interpreter.

4. With the exception of the first line, we use "#" to comment out a line (Helpful for debugging scripts or adding explanatory comments). Add a comment on line 2:

```bash
#This is a comment and will not be parsed
```

5. Add the following 3 lines to the script after the hashbang: 

```bash
thisDir=$(pwd)
numFiles=$(ls | wc -w)
echo "Directory $thisDir has $numFiles files and dirs"
```

6. Now save the file (**ctrl+s**) and exit nano (**ctrl+x**). Before running this – what do you think the output might be? Experiment with typing these commands and using different combinations of piping.

7. We need to tell the system that ```files.sh``` is an executable. We've done this before in [class 2](../Class_02-Resources/README.md/#bashing-on-your-own---class-assignment). To do this, make sure the new script file is in your working directory. Then we'll make the script runnable by giving it “execute” permission. ```chmod``` changes the permissions for the file. +x makes the file executable:

```bash
chmod +x files.sh
```

7. Finally, run the script by typing:

```bash
./files.sh
```
You can run this program in another directory as well. For example, let's run it in our ```~/CHE600/class03``` directory:

```bash
cd ~/CHE600/class03
../class04/files.sh
```

# **Iteration and loops**
Often we need to perform the same task repeatedly. If you've ever worked with a large number of excel sheets where you had to do the same operation on each, you know how frustrating that can be. Using bash, it is very easy to carry out the same operation repeatedly in a single line of code!

## **I. The bash for syntax**
Programmed iteration usually uses the ```for``` keyword. In bash, the format is as follows:

```bash
for iterating_variable in iteration_list
do
operation 1
operation 2
...
operation n
done
```
    * iterating_variable can be any string. It will hold the current value of the iteration_list.
    * iteration_list can be any string seperated by space or line break. It can also be generated by a command like ```ls``` or ```cat```
    * operations can be anything and can use any variable previously defined, including the iterating variable

## **II. Using a for loop in flat notation**

Before we start, make sure you are in your ```~/CHE600/class04``` directory.

1. A simple iteration list can be a list of strings or numbers seperated by space or line breaks. For example, try:

```bash
for i in A B C D E; do echo "now on $i"; done
```

```bash
for i in 1 2 3 4 5; do echo "now on $i"; done
```

```bash
for i in ALA CYS GLU LYS HIS; do echo "now on $i"; done
```

2. We can use the ```seq``` command to iterate over numbers. First, understand how it works. Try typing:

```bash
seq 1 10
```

```bash
seq 3 4 100
```

3. now let's use the ```seq``` command to create our iterating variable. We'll start with a "flat", command prompt notation. The command would look like this:

```bash
for i in $(seq 1 10); do echo "now on iteration $i"; done
```
Notice that semi-columns seperate the different parts of the loop. Also notice, that similar to when we defined a variable, putting a command in ```$()``` tells bash to interpret the command and use its output, rather than use the string directly. (you can try replacing ```$(seq 1 10)``` with ```seq 1 10``` and see what happens).

4. Here we used a command to generate the iteration list, but we can use any other text that contains multiple lines. for example, lets direct the results of ```seq 1 10``` into a file called ```sequence```, then iterate over each line by using ```cat``` to generate the iteration list:

```bash
seq 1 10 > sequence
for i in $(cat sequence); do echo "iteration $i from sequence" > $i.txt; done
```

Notice that we now created a bunch of text files! How are their names defined? What do they contain? Does it make sense?

5. As another example, we can use ```ls``` to generate the iteratin list and perform operations on all files in a directory:

```bash
for i in $(ls *.txt); do echo "backing up file $i"; cp $i $i.bak; done
```

Notice in this list we ran two commands for every iteration loop: ```echo``` and ```cp```. We have now used this loop to back up every single file in our directory! Type ```ls``` to make sure it happened.

## **III. Using a for loop in a script**

1. Let's try to modify this simple script to run as an executable. Use ```nano``` to edit a file called ```first.sh```. The file should contain the following:

```bash
#! /bin/bash
for i in $(seq 1 10)
do
    echo "now on iteration $i"
    res=$(expr $i + 15)
    echo "the result is $res"
done
```

2. Pay attention to the hasbang (```#!```), and the format of our for loop. This script is a bit more complicated, and has three different operations, and the semi-columns have now been replaced by enters. 
    i. First we echo a message
    ii. Next, we create a variable called ```res``` by using the ```expr``` command which evaluates (very) basic math operations.
    iii. Finally, we echo the result of the "calculation".

3. Let's see if our script works. Save the file (ctrl+s) and exit back to the prompt (ctrl+x). We next have to make this file executable using the ```chmod``` command:

```bash
chmod +x first.sh
```

then we run it by typing

```bash
./first.sh
```

# **Creating executables with input and output**
The script we created could be more useful if we could provide arguments when we run it. This is very easy to do in bash.

## **I. Basic input in scripts**
1. Use ```nano``` to edit a new file called ```adlib.sh```. Paste the following into this file:

```bash
#!/bin/bash
echo "Let’s all go to the $1! We can buy some $2"
```
$1 and $2 stand for two variables that will be supplied by the user following the command. They should be separated by a space. These are similar to other variables in bash that are called using the \$ sign, but \$1, \$2, and all numbers cannot be used for variables since they are used for argument passing.

2. Make the file executable using 

```bash
chmod +x adlib.sh
```

3. Now try running it by typing the following variations
```bash
./adlib.sh store mangos
./adlib.sh store mangos, oranges, and bananas
./adlib.sh store “mangos, oranges, and bananas”
```
What are the differences between the different arguments?

4. There are other values from the command line that are also available inside a shell script:
    1. ```$1```, ```$2```, etc. – The individual command line parameters
    2. ```$*``` - List of all parameters passed to the script ($1, $2, etc.)
    3. ```$0``` - Name of the shell script being executed.
    4. ```$#``` - Number of arguments specified in the command line.
    5. ```$?``` - Exit status of the last command


## **II. Independent work: count amino acids**
Now you will work independently to create a script. The goal of this script is to count the number of amino acids of a specified type in a given PDB file. Your script should be called ```countAA.sh```

1. First, get acquianted with a new command: ```wget```. This command retrieves a file from a web address. The protein data bank (PDB) allows you to download any crystal structure using the wget command. The format is:

```bash
wget https://files.rcsb.org/download/1UBQ.pdb
```
and this line will get the crystal structure file with the code "1UBQ" - which is the ubiquitin we've used in class03.

2. Your script will require 2 inputs, the 4-letter pdb code (like 1UBQ) and a 3-letter abbreviation of the amino acid. The script should be called count_aa.sh and run it as follows:

```bash
count_aa.sh <pdb code> <3-letter amino acid> 
```

3. The output should be ```<pdb code> has <number> <amino acid>```

4. How do you do this? Your script will need to first download the file using the ```wget``` command. It will then need to search for lines containing the specific amino acid code (GLY for example). Remember that we've done this before when we learned about the ```grep``` command. The counted number will need to passed into a variable (see below), and that variable used as output.

    **Hint 1:** It is highly recommended to try out the commands from the command line first to see if it works – before writing it into your script.

    **Hint 2:** searching for “ALA” will return all atoms that belong to alanine residues – there are many. But each amino acid has only one atom named “CA”

    **Hint 3:** tune your grep command such that you get a single line for every amino acid in the PDB file. Then all you need to do is count lines by piping your output through wc -l

    **Hint 4:** Once your one-liner throws out the correct number, you’re good to implement it into your script. To do that, you’ll need to place that number into a variable.

5. Run the script on the following pdbs, and use your script to get the number of ALA in each one. Redirect the output to a results file (use ```>>```) called ```countALA.txt```:
    1. 1UBQ
    2. 1PGK
    3. 9D61
    4. 8YDS
    5. 9GPW
    6. 8QM6

# **Conditionals**
Conditionals are statements that get evaluated by the interpreter, and performs one action if true and another if false. Scripts often use conditionals as a way to check if a certain condition is met, and by combining conditionals we can get complicated decision trees in our scripts.

## **I. Using conditionals to "sanitize" user input**

1. The script you've written is great, but what happens if we pass the wrong number of arguments when we run it? Try it out:

```bash
./countAA.sh too many arguments
```

2. This causes the script to crash, and the user gets no information about why it crashed. Let’s improve the script ```countAA.sh``` script by adding some conditionals to test for issues that might arise, such as bad user input. A list of all conditionals in bash is available [here](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html)

3. Edit the script and add the following right after the first line (right after the hashbang)

```bash
if [ $# -ne 2 ]; then
	echo "Script takes 2 arguments, a pdb code and a 3-letter amino acid code"
	exit 1
fi
```

4. Here the conditional performs the following function: 
    a. Checks if the number of arguments ($#) does not equal (-ne) 2
    b. If true – echo error text, then exit with an exit code of 1. (The exit code can help debug a script)
    c. If false – the script just continues on without exiting. You don’t need an “else” statement here (though those are possible)
    d. The fi command terminates the conditional.
    e. The tabs are not neccessary for bash (which is not true for other languages such as python), but they don't hurt and they increase the readability of our script.

5. Now test the script with the wrong number of arguments. What happens?

# **Bonus script: Count all amino acids:**

The goal here is to adapt your count_aa.sh script to a new script that counts the number of each amino acid in a pdb file. 

1. First copy the first script you wrote to a new one called ```count_all_aa.sh```. Note that When you copy a file – all permissions are copied as well, so this new file will also be executable (have the +x flag).

2. The script should iterate over a list of all amino acids (feel free to google the list of three-letter amino acid codes!), and count the number of each of them using the same approach we've seen before. 

3. The input should be:

```bash
./count_all_aa.sh <pdb code>
```
Remember to adjust your conditionals if needed!

4. The output should be a comma separated value (csv) file with the following format:

```
Amino acid,count
ALA,12
GLY,28
CYS,0
…
TRP,3
```