# CHEM260 F23 Class 4

Today's class will introduce us to script writing in bash. What we’ll cover today: 
* [Defining and working with variables](#variables-in-bash)
* [Basics of script writing](#basics-of-script-writing)
* [for loops]()
* [Creating executables with input and output](#creating-executables-with-input-and-output)
* [Conditionals](#conditionals)

# **Variables in bash**

Variables are critical to any code. They allow you to store information and recall it within the memory of your application, without writing anything to the disk. 

1. Defining a variable is easy, simply use the equal sign: ```variable_name="this is the value of the variable"```. Try this (notice you can't have any spaces next to the equal sign!):

```bash
myVar="This is my variable"
echo myVar
echo $myVar
wc -c $myVar
```

2. We can also direct output into a variable. This is a bit different from directing output to a file, and looks like this:

```bash
myOtherVar=$(pwd)
echo $myOtherVar
```

3. Variables can be called as many times as you want and will remain in memory and can be called so long as you do not log out. They are overwritten if they are defined again. If you want to retain the original value, make sure you include it:

```bash
myOtherVar=$(echo "the first var was " $myOtherVar)
```
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

3. In bash, we can write scripts in two ways. The first one is through the command line. In general, commands there will be seperatd by a semi-column (```;```). For example:



## **II. Let’s write our first script:**

1. Create a new directory called ```class04``` in your ```~/CHE600``` directory, and move into that directory using ```cd```

2. Use ```nano``` to create a file called ```files.sh```

3. The first line of the script needs to be ```#!/bin/bash```  – this is called a “hashbang” and tells the shell which scripting language to use. This time it’s bash (being called from an executable that’s in the directory /bin). Later in the course we will also see this being used for python, and it can be used for any code interpreter.

4. With the exception of the first line, we use "#" to comment out a line (Helpful for debugging scripts or adding explanatory comments)

5. Add the following 3 lines to the script after the hashbang: 

```bash
echo "Directory contains this many files and dirs:"
pwd
ls | wc -w
```
Before running this – what do you think the output might be? Experiment with typing these commands and using different combinations of piping.

6. Before we actually execute this file, we need to tell the system it is in executable. We've done this before in class02. To do this, make sure the new script file is in your working directory. Then we'll make the script runnable by giving it “execute” permission. chmod changes the permissions for the file. +x makes the file executable:

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

# **Creating executables with input and output**
The script we created is not very useful. For example, usability would be increased if we could tell the script what directory we want it to operate on. To do this, we need the script to be able to accept arguments when we it.

## **I. Basic input in scripts**
1. move back to your ```~/CHE600/class04``` directory, and use ```nano``` to edit a new file called ```adlib.sh```. Paste the following into this file:

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

6. Edit the file again and add the following lines after the wget command:

if [ ! –f $2.pdb ]; then
	echo "There is no file $2"
	exit 1
fi

# **for loops**




Here the conditional checks if a filename does not exist (! -f ) with the name of our second argument ($2) Test the script with a misspelled file name

J.	To bring everything together, run your script count_aa.sh using a for loop that will run over the amino acids GLU GLN GLY ALA and PHE. Put the output of this loop into aacids.out
for i in GLU GLN GLY ALA PHE
do 
count_aa.sh  $i  TEAD.pdb
done

III.	Miniproject 2: Count all amino acids:

A.	Copy the first script you wrote to a new one:

cp count_aa.sh ./count_all_aa.sh

When you copy a file – all permissions are copied as well, so this new file will also be executable (have the +x flag).

B.	Edit the new script using text editor or nano

C.	Use this template to write a new script that will count not just one, but all of the amino acids in a pdb file (feel free to google the list of three-letter amino acid codes!). 

D.	Input should be:

./count_all_aa.sh <pdb filename>

Remember to adjust your conditionals if needed!

E.	Output should be a comma separated value (csv) with the following format:
Amino acid,count
ALA,12
GLY,28
CYS,0
…
TRP,3

F.	Upload your count_all_aa.sh script, and a screenshot of the output, to the submission link on catcourses

G.	Optional for even fancier functionality – have an option to automatically download a file from the protein databank (PDB) – a repository for all experimentally-determined protein structures – and perform this analysis automatically. The input should then be just the PDB code you are interested in. For example:

count_all_aa.sh 1UBQ

this will download the 1UBQ.pdb file from the PDB, and count all amino acids on it.

To download a PDB, use the following line:

curl -o <pdb code>.pdb https://files.rcsb.org/download/<pdb code>.pdb

