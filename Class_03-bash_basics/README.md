# CHEM260 F23 Class 3

What we’ll cover today: 
* [The linux philosphy](#the-linux-philosophy)
* [The bash shell](#the-bash-shell)

# The linux philosophy
1. Commands do just one thing, but do it well
2. Allow each command to act as a filter so commands can be easily connected to do more powerful operations
3. Interfacing with the linux system is text-based, through the command line (aka the shell)
4. Using Avoid “captive” command interfaces to allow “scripting”

# The bash shell
We will now work independently with linux commands. Remember that you can't cause any catastrophies (you do not have permissions to alter any files other than the ones in your home directory)
## 1. How to escape when you're stuck

6. Programming example, make 200 directories under current directory. Take note that this is the first time we’re using a for loop – this is an essential tool!:

```bash
cd ~/CHE600/class02**
for i in {1..200}  
do  
mkdir dir.$i  
done
```

Did it work? type ```ls``` and see what you got!

6. Programming example, make a hierarchy of 10 directories under current directory:

```bash
for i in {1..10}  
do  
mkdir rdir.$i  
cd rdir.$i**
done
pwd
```

9. An asterisk “\*” is a wildcard for any number of any characters – you can use this to make multiple matches for a single command
10. More on wildcards later
11. List files:**ls** _path/filename/pattern_  
    **ls –lh** _path/filename/pattern (_A more informative file list. Will tell you if a file is a directory and its permissions)

**ls -ltrh** _path/filename/pattern (_same as -lh but lists in reverse chronological order (most recent file last))

**l** (a non-standard but useful shortcut for **ls -ltrh)**

**ls -d \*/** (list only directories)

1. Copy files:**cp** _filename destination_ (note there are 2 arguments)
2. Remove files:**rm** _filename/pattern_ (remove file or files)**rm -r** _directory/pattern_ (remove all files and directories below _directory_)

**rm -rf** _directory/pattern_ (force remove all files and directories. Careful with this one‼)

1. Size of a file (line/word/character count):  
    **wc** _filename/pattern_ (number of lines/words/characters in the file)

**wc \-l** _filename/pattern_ (number of lines only in the file)

Scroll through a file:  
**cat** _filename/pattern_

**more** _filename/pattern_

1. Filename auto-completion (**Tab** or **2xTab** for list of matches)
2. **Now use these commands to get rid of all the directories you made!** Make sure you don’t delete everything in your directory! (Though if you do it’s not a big deal – we can restore it easily!). Also make sure you are running your commands in the right directory!
3. One of the reasons linux is so powerful is that commands can be strung together. We will use this ability extensively throughout the course.
4. Pipes transfer the output of one command into the next command:  
    _command1_ | _command2_

In the example below, the results of the directory listing shortcut **l** are piped into the word count command **wc** (you can always type **wc --help** to see more info about the command)  
**l | wc**

1. Redirects direct the output of a certain command to a specific location or file instead of to your screen  
    _command_ > _outfile_ (Makes new outfile)  
    _command_ >> _outfile_ (Appends to existing outfile)

In the example below the output of the directory listing shortcut **l** are directed to a file called wc.out

**ls > l.out**

1. In the **getProteomeDisorder.sh** there are several pipes and redirects used to format the output from the proteome files. We will make extensive use of them later over the next few classes.

**IV. In-class Mini Project—collecting data from multiple proteomes**

- - 1. Please make sure you read the line, think about what it will do, then type it into your terminal. If you don’t know what a command does, or expected something but something else happened, please scroll back and review what we learned, or use google the command/use the **man** command/type the command with the flag **\--help** at the end
        2.  Create and go to a subdirectory called proteomes:

**cd ~/CHE600/class02**

**mkdir proteomes**

**cd proteomes**

- - 1. Download proteomes.dat from Canvas, and place it in this directory. I can help with this if you don’t know how to find the correct directory!
        2.  In the terminal, use the **cat** command to see the contents of that file and do the same for another file:

**cat proteomes.dat**

- - 1. We want to feed the output of the cat command into our **getProteomeDisorder.sh** script to extract the disorder for the proteome of different organisms. To do this, we iteratively feed the **proteomes.dat** file into the variable **i** with a **for** loop. Let’s first print out the variable **i** just to get a feel:

**for i in \`cat proteomes.dat\`**

**do**

**echo "this proteome code is $i"**

**done**

The echo command prints a string to the terminal (kind of like a “print” command)

- - 1. Next, adapt this loop in such a way that instead of printing out the value of **i**, we will use it as a parameter for **getProteomeDisorder.sh**. Make sure you have the script in your current directory, or otherwise call it from the correct directory.
        2.  If you ran it properly, the command should take a little while to run as you pull entire proteomes off the MobiDB website!
        3.  Once the script has finished running, report how many proteins exist in each proteome using the **wc -l \*.dc** command. Redirect this result into a file called **proteomes.len**
        4.  Next, calculate the average disorder of each proteome by using the **awk** script we’ve used in class (it’s still in your history! No need to type it in from scratch again). You can do this manually, but it would be best if you can do this with a for loop! How can you do that?
        5.  One you’re sure your awk script works properly, **redirect** (**\>**) the results into a file called **proteomes.dc**
        6.  Paste all the files starting with “proteomes” together using **paste:**

**paste proteomes\* > proteomes.all**.

- - 1. Print out proteomes.all using the cat command. Which proteome is most disordered? Which is least disordered? You can always look up which proteome is which by googling the proteome code! Upload proteomes.dc and answer these questions using the submission link for class 2 in Canvas.

Didn’t finish the exercises? Please be sure you are finished with everything by next week! I’m **always** happy to help once you’ve given it a few tries!