# CHEM260 Class 6

Today's class will focus on finishing the tasks from Tuesday, and then setting up a python environment for us to work in for the remainder of class!

* [Multiple file processing](#processing-multiple-files) (Using the ```awk``` command)
* [Install VSCode](#installing-vscode)

# **Processing multiple files**

## **I. Explanation of the scenario**

We have a series of experiments where the data files are text based (csv or tsv) and all structured in the same way. We need to process each of these files in the same way, perform manipulations, and produce some kind of output from these files. 

1. For our dataset, we will use a collection of simulation results. These are results from simulations of a single polypeptide chain in the presence of spherical "crowders" that take up space, limit its movement, and hopefully compress its dimensions (this is what we want to see). First, make a ~/CHE600/class06 directory, and copy this dataset using ```cp``` to your ```class06``` directory. The dataset is in:

```bash
/usr/CHE600/class06/ree.tar.gz
```

2. The dataset is archived in a compressed "tarball" - these files generally have the suffix ```.tar.gz```, and include one or more files that are bundled together and compressed to take up less space. **note** Compression is very effective for text files, but not so effective for binary files. T

3. use the ```tar``` command to untar the file. We use this with the ```-xzvf``` flag: x to extract, z to unzip (decompress), v for "verbose" - show the output of the command, and f to force overwriting if a file already exists in the current directory:

```bash
tar -xzvf ree.tar.gz
```

4. Check out the content of your directory. There are now a bunch of files in this directory. The parameters used to generate the simulation are embedded in the filename (```XX_XX.dat```): The first number is the radius of the monomers in the box; the second number is the number of inert spheres in the simulation box. All boxes contain the same polypeptide (16 repeats of Gly-Ser).

5. Use ```more``` to look at one of these output files. Each file contains a header with a ```@``` prefix. The header is followed by two columns: the frame number and the end-to-end distance of the peptide chain - which represent one metric of the dimensions of the chain. 

6. Your task is to calculate the AVERAGE and STANDARD DEVIATION of the end-to-end distance of each file, and make a csv file with the following header:

```bash
crowder_radius, crowder_conc, Re_avg, Re_std
```

## **II. AWK to the rescue**
As we've seen, linux contains some very powerful programs to manipulate text files. Awk is one of the most powerful. It is essentially a command-line based excel sheet, capable of parsing tabulated files and performing calculations on rows and/or columns, all using a single command. This of course lets us execute the same command on dozens or thousands of files quickly. Let's see how it works.

1. Like the bash shell, awk can be run from the command line directly or using scripting language (in which case the hashbang will have a ```#!/bin/awk``` header!). We're going to primarily use awk from the command line, in a "flat" notation.

2. Let's prepare some files to understand the general format of awk. Paste the following into your shell, but think about what this does before running it. **note:** The ```$RANDOM``` variable is a protected variable name and generates a random integer every time you call it:

```bash
seq 200 > col1
for i in $(seq 200); do echo $RANDOM >> col2; done
paste -d "," col1 col2 > sample.dat
```

3. The awk syntax goes like this:

```bash
awk 'BEGIN{PRE-RUN COMMANDS};{MAIN RUN COMMANDS};END{POST RUN COMMANDS}' filename
```

* The BEGIN block is processed once before the file is processed. You can use it to define variables, limits, etc.
* The main block processes every line, one line at a time.
* The END block is processed once after the last line has been processed. 

4. Remember that rather than working on a specific file, we can set awk to work on the output of another command using pipe:

```bash
command_to_generate_text | awk 'BEGIN{PRE-RUN COMMANDS};{MAIN RUN COMMANDS};END{POST RUN COMMANDS}'
```

5. Let's try and use awk to calculate the average random number generated by bash by analyzing the ```sample.dat``` that we generated. Copy and paste the following to the shell:

```bash
awk 'BEGIN{FS=","; sum=0; print "index,random number,cumulative_sum";};
{sum+=$2; print $1","$2","sum};
END{print "proccessed " NR " rows. Average random number is "sum/NR}' sample.dat
```

Here:
* The BEGIN block defines the Field Seperator (```FS=","```), then defined a variable called sum with a value of 0, (```sum=0```) then prints out a header (```print "index,random number,cumulative_sum"```). Notice that each command is separated by a semi-column (```;```)
* The main block increments the sum variable by the value of the second field (```$2```), then prints out the first field, the second field, and the value of the sum variable seperated by commas.
* The END block prints out text and the average, taken by dividing the value of the sum variable by the Number of Rows (```NR``` - a protected variable name in awk).

6. As usual, the only output for this command it to our terminal - if you want to save it direct (```>``` or ```>>```)it to a file.

## **III. Using awk to get average and std**
So now let's remember our main goal - we want to take the numbers in our extracted files, and calculate their average and standard deviation. We now have the power of awk to do this, but we may need to clean these up a bit. We will first work on the entire chain of commands to clean up a **single file**, then calculate its average + std. Then we'll put these commands in a loop that goes over all the files in one swoop! Pick one and only one file to perform these operations on. You can pipe commands through to other commands if you'd like.

1. Cleanup: Remember that all the files have a header (have a look using ```head```!). If ```awk``` would run on that it would parse it in the same way it would parse the actual data. You'll need to write a code to remove the header lines (those starting with ```@```) so we stay with only two columns.

<details>
<summary>spoiler</summary>

Remember you can use the ```tail``` command to look at all but the top N lines:
```bash
tail -n +20
```
</details>

2. Averaging with awk: On the cleaned up file, run awk to calculate the average. You only need to print it out at the end. Remember that this command needs to operate, either on the file or on the output of another command through a pipe ```|``` 

```bash
awk 'BEGIN{FS=" ";sum=0};{sum+=$2};END{print sum/NR}'
```

3. Calculating standard deviation: Rememver that stdev is the square root of the variance, which is calculated by (sumsq / count) - (mean)^2. Let's add this functionality into our awk code. Notice that awk recognizes the function sqrt (square root):

<details>
<summary>spoiler</summary>

```bash
awk 'BEGIN{FS=" "};{sum+=$2;sumsq+=$2*$2};END{mean=sum/NR;var=sumsq/NR-(mean*mean);stdev=sqrt(var);print mean","var","stdev}'
```
</details>

4. You should now have a one-liner ready to process any of the data files. The next part is to run your command on each file and generate the information requested. Some of the information is stored in the filename, so we will need to extract it. For this, recall the ```cut``` command that can seperate based on a delimiter!

```bash
echo 50_3.dat|cut -d "_" -f 1
```

Remember that you can place the value of the command into a variable and recall it later. Now write the code to extract the sphere size (first number in filename) and concentration (the second number in the filename) to two variables, and then you're ready to loop over all files and prepare your final csv!

<details>
<summary>Pseudo code hints</summary>
Note that this is **not** actual code - you will need to turn this into runnable commands.

```bash
for filename in filelist:
do
    crowder=$(code to extract first number of filename)
    conc=$(code to extract second number from filename)
    avging=$(awk command to print out mean and standard deviation seperated by a comma)
    echo "crowder,conc,avging"
done
```
</details>

5. Save the results (preferably by redirecting) to a filename called ```summary.csv``` - please make sure this is in your ```~/CHE600/class06``` directory for checking!


**Reminding you that all output should be placed in ```~/CHE600/class06``` directory!**

# **Installing VSCode**

For those that have completed today's tasks: we will be moving to python next class. Because IT couldn't help support us working on the server, we will be working locally. This can be done either on your own laptop, or on class computers - whichever you prefer. We will be working with VSCode - a powerful editor for python and other programming languages.

## **I. Installing VSCode on your own laptop**

Download page available [here](https://code.visualstudio.com/download). Pick the download that works for you.


## **II. Installing VSCode on classroom computer**

VSCode can be installed through the "Microsoft store", which lets you installed it on the classroom computer. Link [here](https://apps.microsoft.com/detail/XP9KHM4BK9FZ7Q?hl=en-US&gl=US&ocid=pdpshare)

We will work together to get it working!