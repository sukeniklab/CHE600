# CHEM260 F23 Class 3

What we’ll cover today: 
* [Linux native text editors](#linux-text-editors)
* [Slicing and dicing text files](#slicing-and-dicing-text-files)
* [System commands](#system-commands)


# **Linux text editors**
Often we will want to edit text in our shell. This lets us quickly make changes to files with the need to download or upload files to the server. Since there is no graphical user interface (GUI) for our shell, there are several text-based editors available be default.

## **I. Reminder about printing out text files**
Remember from class - we learned about the ```cat``` and ```more``` commands to print out the contents of a text file. These are very useful, but only let us view, and not edit the contents. We will continuously use these tools, but now we want to edit!

## **II. The nano text editor**
A simple, native text editor we can use in linux is ```nano```. The functionalities are very basic, but it is also very easy and intuitive to use.

1. First, create a new directory in the ```~/CHE600``` directory called ```class03``` (See how to do this in [class 2](https://github.com/sukeniklab/CHE600/tree/main/Class_02-Resources#ii-the-linux-directory-system)).

2. ```cd``` into the class03 directory, and creat a new file using nano editor by typing:

```bash
nano text1.txt
```

3. In nano, put your name in one line, then date of birth in the next line. Then hit ctrl+s to save, and ctrl+x to exit the editor.

4. Use ```cat``` to display the contents of ```text1.txt``` and make sure it's all there. Congrats, you've just used a native text editor in linux! We will next use this text editor to write our own scripts!

5. For any kind of help or reference you can refer to this [cheatsheet](https://www.nano-editor.org/dist/latest/cheatsheet.html)

## **III. emacs, vi, and other editors**

There are many other editors available in linux. One popular one is ```vi``` which is more powerful but much less user-friendly than ```nano```. Another is emacs, which is also powerful and a bit more user-friendly than bi, but has a graphical interface. You are free to use any editor you want, but in general ```nano``` is the one I recommend for beginners.

# **Slicing and dicing text files**

Most of our data comes in text format, so it is a good idea to learn how to manipulate files of this type. Lets go over some basic linux commands to chop or parse text files.

1. Let's use a quick for loop (more on this later!) to make a text file. Put the following code into your shell prompt, but make sure you are in your ```~/CHE600/class03``` directory!

```bash
for i in $(seq 1 30); do echo "this is line $i" >> count.txt; done
```
Notice that previously we used the single direct operator (```>```) to direct output to a file. This time we use the double direct operator (```>>```) - this is because a single direct will overwrite an existing file, while the double direct appends to the bottom!

2. Use ```nano```, ```cat```, or ```more``` to check that the ```count.txt``` file contains the text it should.

## **I. Display parts of a file with head and tail**
Many times we will need to display information, rather than the entire contents of a file. Here are some command to do this:

1.	The ```head``` and ```tail``` commands let us look at the first or last few lines of a file. Try it out:

```bash
head -n 2 count.txt
head -n 10 count.txt
head -n -2 count.txt
```
Notice that last command displays the entire file EXCEPT the **last** 2 lines! The counterpart command is ```tail```:

```bash
tail -n 2 count.txt
tail -n +5 count.txt
```
Notice that the last command displays the entire file except the ***first*** 5 lines.

2. Remember that you can always direct the output to a new file. Use the double direct operator ()```>>```) and the ```head``` and ```tail``` commands to write a text file called ```topbot.txt``` that contains the first and last line of ```count.txt```.

## **II. word counts with wc**
1. Sometimes we would like to count words or lines in a file. The ```wc``` command does all of this, and has specific paramters depending on what output you want.

```bash
wc count.txt
```
the output here will be 3 numbers and the file name. The first is the number of lines, the second is number of words, and the last is number of characters. 

2. We can get each one of these individually using paramters (```-l``` for lines, ```-w``` for words, and ```-c``` for chatacters):

```bash
wc -l count.txt
wc -w count.txt
wc -c count.txt
```

## **III. Search with grep**
Sometimes we would like search for a specific word or pattern in our file. For this we use the ```grep``` command, which is a super powerful search engine for text documents. To see the power of this, let's get some more extensive text files:

1.	Use ```cp``` to copy ```1UBQ.pdb``` from ```/usr/CHE600/class03``` into your own class03 directory (```~/CHE600/class03```). Use ```cat``` or ```more``` to view the contxts of this file.

The file ```1UBQ.pdb``` contains the crystal structure of an ubiquitin - a domain that targets proteins for degredation. Let's display the coordinates of atoms belonging to glycine (Gly) amino acids in the structure. To do this, we will simply search for the expression ```GLY``` in the file:

```bash
grep GLY 1UBQ.pdb
```

2. Notice that the output has a bunch of lines that do NOT contain coordinates. We want to get rid of these and keep only lines that start with "ATOM" - but how? Remember that we can string together commands in linux (sometimes called piping). Let's pipe together together two grep commands to display only lines that contain "GLY" and "ATOM":

```bash
grep GLY 1UBQ.pdb | grep ATOM
```

3. Finally, let's count the number of atoms in this glycine residues. Since every atom is a single line, all we need to do is pipe the same command again through the ```wc -l``` command. Try this yourself, and direct the output of the entire command to a file called ```N_gly.txt```.

## **IV. Manipulating tabulated data**

Often, our data will be tabulated - this means that the data is in fields seperated by tabs (tsv - tab seperated values), commas (csv - comma seperated values), or similar format. Linux contains a bunch of commands that can help split these tabulated data into individual columns.

1. Copy the file "rests.csv" from the ```/usr/CHE600/class03``` directory to your own class03 directory. The ```rests.csv``` file contains comma seperated tabulated data from an experiment. 

2.	Let's use the ```cut``` command to cut file by fields and extract the second column (-d specifies column separator, -fn indicates which column)

```bash
cut –d "," -f 2 rests.csv
```
Let's keep only the 3rd and 5th columns of the data
```bash
cut -d "," -f 2,5 rests.csv
```
3. Let's raondimze the lines in ```rests.csv```:

```bash
sort -R rests.csv
```
Note that sort has many options – have a look with the --help flag

4.	Notice that line 7 in ```rests.csv``` is duplicated. Let's remove any duplicate lines from the data using the ```uniq``` command:
```bash
uniq rests.csv
```
Notice that up to now, we haven't made any actual changes to the file, and didn't create any new files - all the slicing and dicing was only displayed in our shell, and not directed to a file.

5. On your own: 
    * Let's turn the first 4 columns of ```rests.csv``` into a "stacked" file where all the columns turn into a single columns. 
    * First, use ```cut``` to extract each column of ```rests.csv``` and direct the output into a file called ```col1```, ```col2```, etc. 
    * Then, use the ```cat``` command to print the columns one after the other: 
```bash
cat col1 col2 col3 col4 > stacked.txt
```

6. you can use the paste command to combine the seperate columns in a different order:
```bash
paste -d "," col4 col3 col2 col1 > stser.txt
```
7. Please make sure that ```stacked.txt``` and ```stser.txt``` are in your class03 directory - this is part of your class work and will be checked!

# **System commands**
Ultimately, bash is an operating system that runs a computer, and we need to be able to display information about the computer. For example, which jobs are running, how much hard disk space is available, etc. Let's go over a few basics that can be important:

## **I. Job management**

Linux can run jobs in the background, exactly like any windows/mac machine. 

1. Let's send a running program to the background. We can use the ```man``` command to enter the manual viewer. Type ```man ls```, then use ctrl+z to return to the prompt, sending the man command to the background. You will see a line like this:

```bash
[1]+  Stopped                 man ls
```
This tells you that the job ```man ls``` has been stopped. Let's run one more man jobs by running ```man pwd```, and again exit to the prompt using ctrl+z. Notice this is now jobs #2, as denotd by the number in the square brackets.

```bash
[2]+  Stopped                 man pwd
```

2. We can list all current jobs using the ```jobs``` or ```ps``` commands. The jobs command gives only information about programs running in your bash. ps will provide information on all processes, including those initiated by the linux kernel. Try both of these, or try ```ps aux``` to see a list of all jobs, not just those associated with your account.

3. We can return back to a job that has been stopped or sent to the background. To do this, we use the ```fg``` (foreground) command. To return to the man ls command (job #1), type:

```bash
fg %1
```

4. Return back to the prompt using ctrl+z. Now let's kill this command. To do this, type ```kill %1```. The following will appear:

```bash
[1]-  Terminated              man ls
```

5. Typing ```jobs``` again now shows only job #2 still remains. Kill that one as well.

6. Sending jobs to the background and recalling them is extremely useful when we are editing multiple files or when we are debugging code. Try and use it as often as you can. 

## **II. Disk quota**
When working on a server, you have a limitd amount of resources. Often, especially when working with large datasets or big computational jobs, you need to be sure there is enough space. Crashing a linux server is very hard, but one easy way to do it is to completely fill up the hard drive, which then does not let linux create neccessary files for operating.

1. The disk usage (```du```) command will summarize the disk usage of every file and directory in the current (working) directory. Check the usage of your home directory (```~```) with the following command:

```bash
du -h ~
```
this will list the usage of every directory. If you want to just get the bottom line (e.g. how much disk am I using in total) try the following:

```bash
du -sh ~
```

2. To check the total amount of storage available on the entire system, we can use the ```df``` command:

```bash
df  -h
```

Unless otherwise noted, the main storage is under the root directory (```/```). This has 2 TB of available space.

3. Beyond disk storage, the system has other resources like memory and cache. To view the usage here, use the ```top``` command. The top command in Linux is a system monitoring tool that displays real-time information about system processes and resource usage. It provides a dynamic, real-time view of system activity, including CPU usage, memory usage, and process information. Press ctrl+c to exit the viewer.

4. If you want to see who else is logged in and working on the server, you can do so with the ```who``` command. Redirect the output of this command to a file called ```"who.txt"```