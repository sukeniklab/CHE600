# CHEM260 F23 Class 2

What we’ll cover today: 
* [resources](#resources) you should you use during this course
* [logging in](#logging-in) to the remote server
* [first taste](#first-taste-of-linux) of linux command line


# **Resources**

## **I. Google searches**
Googling how to write code is easy and convenient. Google now integrates results from it's LLM Gemini into the search, so that is also helpful (see below).
1. A useful thing to google is the syntax of linux commands or python functions. To do this, simply write the function name (with the language if there's multiple hits). [Example](https://www.google.com/search?q=echo+linux)  for the linux echo command
2. Another useful thing to look up are errors. For this, you will want to search the error in quotes. Sometimes (especially in python), error messages can be very long, and it will take some skill to identify the cause, which you can then google. We will go over this.
3. Identifying how to fix errors is probably one of the most useful things to google. In general it will bring you to a website that details questions from other coders, like [Stack Overflow](https://stackoverflow.com). It is worthwhile going over the structure of this website to understand where to look for the answer. See example [here](https://stackoverflow.com/questions/38835483/confusion-about-pandas-copy-of-slice-of-dataframe-warning)
4. Googling specific tasks (e.g. plugging in a homework assignment to the google search bar) is generally very ineffective. LLMs are much better for open ended questions.

## **II. LLMs**
In the past two years LLMs have entered every aspect of our life. Coding is no exception - programming itself is a language like any other, and with countless examples on line, this is one of the best uses of LLMS.
1. Since LLMs like [Claude](https://claude.ai/new) or [chatGPT](https://chatgpt.com/) have a conversation history, it makes sense to keep your coding conversation in the same window. It will remember past code, libraries you used, and variables.
2. Make sure you specify what language you want your code in! (bash/python/something else)
3. When asking an LLM for a bit of code, it's important to break the task down into smaller bits. Think of each coding task as a function, explain what the input is (including syntax) and what you want the output to be (including syntax).
4. Once you get a bit of code from the LLM, try running it. If any errors are thrown, you can report these to the LLM in the same conversation, and it will try to debug it.
5. Finally, make sure you can test that the code works the way you want it. In many cases, you will be able to run "sanity checks" to see if things work as they should.
6. For complicated tasks, or when you use uncommon libraries or commands, LLMs may not be able to help. Even when that's the case, they will try to, by making up code that won't work as intended or using commands that don't actually exist in the code.

## **IV. Text books/online documents**
* There are a few good online textbooks for [bash](https://books.goalkicker.com/BashBook/) and [python](https://pythonbooks.org/free-books/) that are available as free pdf's.
* There are good books printed on dead trees - but I'm not sure you need to use those. If you really want to have a hard copy, O'Reilly books are highly recommended.

# **Logging in**
1. Our first task is to log in to the CHE600 server. This has been an issue on Tuesday, but should have been sorted out!
2. The dedicated server (a.k.a Virtual Machine or <b>VM</b>) is managed by IT. Unfortunately, because of security concerns, you cannot log into it from anywhere. 
3. To log in, you will need to use either:
    * [the Remote Desktop Server](#i-remote-desktop-server) (RDS, see below)
    * [A computer in the computer room](#ii-a-computer-in-the-computer-room)
    * Another computer managed by SU IT (see me for details)


## **I. Remote desktop server**
1. SU provides all faculty and staff with a "remote desktop" - a windows computer that is housed on a server and to which you can log in to from anywhere using your netid.
2. You can log in through a [remote desktop web server](http://rds.syr.edu), or through a [dedicated app](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941283/Connecting+to+RDS+using+the+Windows+App) that will run on your computer (available for Mac or Windows)
3. Use your netid and password to log in
4. The server should have a program called "Putty" that will let you connect to the server (see item III)
5. If Putty can't be located, please come see me.

## **II. A computer in the computer room**
1. The lab takes place in LSC 215 which is a computer class
2. You can log in to any of the computers using your netid and password - this will log you on to your remote desktop
3. It doesn't matter whcih computer you use - the desktop is associated with your account!

## **III. Connecting to CHE600 server (aka virtual machine, VM):**
1. Once you are on one of these "IT-managed" computers, you will need to connect to the VM. To do this, we use a protocol called ssh (acronym for "secure shell"). This is a network protocol that allows secured communication between two computers.
2. While there are many ssh commands, I recommend you use a software called [Putty](https://www.putty.org/) to connect to the VM. All remote desktops and classroom computers should have Putty installed. If not - please let me know!
3. Open the start menu and type in "putty" - this will search for the [putty app]. you can pin the app to your start bar
4. In the first "Session" window, insert the VM's ip address: as-che600-lvm.ad.syr.edu <br><img src="./images/putty_01.png" width="300"/>
5. Next, expand to the "SSH" option in the option tree, then to "X11", then on the righthand side mark "Enable X11 Forwarding". This will allow Putty to transmit graphics<br><img src="./images/putty_02.png" width="300"/>
6. Finally, go back to the "Session" window. Type "CHE600" in the "Saved Sessions" textbox, and hit "Save"<br><img src="./images/putty_03.png" width="300"/>
7. Now, double click the CHE600 session, and a window will open up<br><img src="./images/putty_04.png" width="300"/>
8. You should be able to log in using your **netid** and password!<br><img src="./images/putty_05.png" width="300"/>

# **First taste of linux**

## ** I. The linux philosophy **

1. Commands do just one thing, but do it well
2. Commands can be stringed together to perform powerful operations
3. Commands are meant to be run with all parameters provided. In this way, commands never wait for user input.

## **II. The linux file and directory system**

1. In any operating system (OSX, Windows, or linux), files are stored in directories. 
    - Any directory can contain multiple files.
    - Any directory can contain other directories, which will be <i>subdirectories</i> of the that directory.

2. Most linux systems have the following directory structure:
<img src="./images/linux_tree.png" width="600"/>

3. When you log in to the VM, by default you will be in your own home directory. To make sure you are there, print out your current directory using ```pwd``` (aka "print working directory") - a specialized linux command that does one thing: it prints out the full <i>path</i> of your current directory. The output from pwd should be a directory like ```/home/yournetid```.

4. Next, we will create a subdirectory for the course. To do this, we use the ```mkdir``` command, and move into it (using ```cd```, the change directory command)

```bash
mkdir CHE600
cd CHE600
```

5. We'll make one more subdirectory in the /CHE600 directory called class02.

```bash
mkdir class02
cd class02
```

6. Make sure you’re in the right place by printing the working directory (using pwd again). This should return something like (yournetid will be your own netid)

```bash
/home/yournetid/CHE600/class02
```

7. In the directory structure / is the main directory (aka the "root" of the directory tree). 
    - Then home/ is the directory that holds all user folders
        - yournetid/ is your own home directory. 
            - CHE600/ is a subdirectory in your home directory 
                - class02/ is a subdirectory within that subdirectory! 

All this directory structure is important because you'll need to keep it in mind as you navigate. For example:

```bash 
cd ..
```

will bring you up ONE directory. When you type pwd, you should be in the CHE600/ directory.

```bash
cd ../..
```

will bring you up ANOTHER TWO directories. You will now be in the home/ directory! The ~ sign is a shortcut for home directory, so any time you want to return to your own home directory, you can simply type ```cd ~``` to go home! 

8. Finally, you can specify exact folders to go to. For example, to go back into our class02 directory from any directory you're currently in, simply type:

```bash
cd ~/CHE600/class02
```

9. Note that you only have full permissions in your own home directory – which means that you can delete all your work, but you can’t delete anyone else’s work (or the entire filesystem or the root!) without admin privileges.

10. Now that we've got a handle on how to maneuver within the linux system, we can start working!

## **III. Task 1: Example of real-world scientific workflow using Bash and Python**
The first task is really just a demonstration of how we can use powerful linux commands to create useful tools. As I've told you, my lab is interested in disordered proteins. There are thousands of proteins, but it's not always easy to know what parts of those proteins is well-folded and what parts do not have a structure. Luckily, there is a database called [Mobidb](https://mobidb.org) that has predictions of disordered for nearly every known protein. It has these predictions even for entire proteomes. We can view it online, but can we turn this into numbers that we can then analyze?

1. We will pull data from an online database and calculate the average disordered in the SARS-CoV-2 proteome
    1. On the local browser (**not the Putty shell!**) go to:

[https://mobidb.bio.unipd.it/](https://mobidb.bio.unipd.it/%20)

2. Scroll down to “Proteomes”, and click on the SARS-CoV-2 proteome

<img src="./images/mobidb_CoV2_proteome.png" width="300"/>

3. Look at the list of proteins – there are 15 proteins listed. Click on any one of them

4. The entry contains information about the sequence – primarily whether the sequence is disordered.

5. The MobiDB website contains a RESTful API (application programming interface). Essentially, this allows you to access this database from the linux command line by formatting the correct address string. Many bioinformatic databases use this format.

6. We can use this interface to look at the dirsorder prediction for a single protein. For example, the SARS-CoV2 nucleoprotein. Enter the following address into your browser: (ok to copy and paste or just click the link!)

[**https://mobidb.bio.unipd.it/api/download?proteome=UP000464024**](https://mobidb.bio.unipd.it/api/download?proteome=UP000464024)

7. This output is just barely human-readable, and if we had to parse dozens of these it would be very difficult. Instead, let’s do this programmatically! We will now download the entire SARS-CoV-2 proteome to a subdirectory within our home directories. 

8. Let’s get the proteome from MobiDB using the ```curl``` command. The ```curl``` command pulls up data from a HTTP address. We need to provide an output file name (using the -o <i>flag</i>). This will be the file in which to write the contents of the http address. We'll name it ```CoV2.dat```. The final command should look like this (all in one line):

```bash
curl -o CoV2.dat <https://mobidb.org/api/download?proteome=UP000464024>
```

9. Now let's list the content of the current directory using the ```ls``` command. Can you see the CoV2.dat file?
You can also see more information about the files with some flags:

```bash
ls -ltrh
```

10. To look at the contents of the CoV2.dat file we can use the ```more``` command. This is a viewer for text files:

```bash
more CoV2.dat
```
(press space to scroll down)

11. Seems like a mess, right? Do you identify anything in this? Turns out using some handy bash commands. I’ve compiled some parsing commands into a handy script called ```getProteomeDisorder.sh```. This is available in ```/usr/CHE600/class02``` directory.

12. To copy the script to your class02 directory, use the copy (```cp```) command. This will copy from the source (first argument) to the target (second argument). For the source we use the full path. For the target, we use the shortcut for our home directory (~) followed by the subdirectory for class02. Notice that if the directory doesn't exist, the command will throw an error.

```bash
cp /usr/CHE600/getProteomeDisorder.sh ~/CHE600/class02
```

13. Now go to you class02 directory using ```cd``` and list the files using ```ls```. The getProteomeDisorder.sh file should be there. Let’s look at the contents of this script by using another program that prints our file contents, ```cat```:

```bash
cat getProteomeDisorder.sh
```

* note that ```cat``` and ```more``` are not the same. cat will print out the file and scroll down the window, never stopping. More waits for you to press the spacebar once it filled the screen before moving on to the next screen. You'll be surprised that each is useful for specific purposes.

14. **getProteomeDisorder.sh** is a bash shell script (indicated by the “shebang” notation in the first line: **#!/bin/bash**.

The script runs several linux commands which we will cover later, including ```sed```, ```grep```, and ```cut```. Each of these commands manipulates the initial download to extract some information. In the end we use the paste command to attach everything together. Notice that in several places in the script we use the wildcard **$1** – this is a reserved variable name for the first argument passed to this script (see below).

15. Before running this script, we need to tell linux that it can be executed (is an executable). Note that unlike Windows or Macs, linux doesn't care what the file name is - you can execute any file (or try to!) so long as you mark it as an executable. To do this with the change mode command ```chmod```. Make sure you are in the /class02 directory and type:

```bash
ls -ltrh
chmod +x getProteomeDisorder.sh
ls -ltrh
```

16. Notice that before and after the change mode an “x” was added to the file permissions in the file list. Now run the Bash script to get the proteome of the SARS-CoV-2 virus and map protein names and disorder:

```bash
./getProteomeDisorder.sh UP000464024
```

Note that ./ is a notation telling linux to run the executable located in “this directory”. This will only work if **getProteomeDisorder.sh** file is in the current working directory.

17. Did any new files pop up as a result of running the script? Check by looking for new files in your directory (using the ```ls -ltrh``` command)

18. The output file ```UP000464024.dc``` is a csv (comma separated value) file with protein ID, protein name, length, and disordered amino acid fraction fields. Type it out with the ```more``` or ```cat``` command. 

19. What happened? Using a few simple one-line commands and access to a well-curated online database we downloaded relevant bioinformatic data, parsed it from its initial, barely readable format, extracted the information we wanted. This was all done by **creating a custom tool that can be used again to extract the proteome of any organism**!

20. We now want to get the average disorder fraction in all these proteins. To do that, paste the following command into your shell:

```bash
awk '{FS=",";sum += $4; count += 1}END{print sum/count}' UP000464024.dc
```

21. This command uses the ```awk``` program. We will learn all about it in the coming weeks – this is just meant as a demonstration of the power of bash! What is the average fraction of disordered proteins in the SARS-CoV-2 proteome?

# **III. The bash shell - a bit deeper**

1. Before we start, we need to know how to kill or exit running programs so we don’t get stuck. Some keys to press when you find yourself stuck on a Linux system:
    * ctrl-c (i.e. hold the Ctrl key and hit “c”; kills current command)
    * :q (To exit certain programs like vi, less, and man)
    * Esc (i.e. the Esc key on the upper left of your keyboard; escape input mode)
    * Ctrl-z (put current process in background)
    * Ctrl-d to exit some applications (eg python shell)

2. Your shell prompt is customized to tell you the name of the computer you are on and the directory you are currently in:

    ```ssukenik@as-che600-lvm:~$``` (“ssukenik” will be your own username, “@as-che600-lvm” is the server name, and “~” means your home directory)

    ```ssukenik@as-che600-lvm:~/CHE600/class02$``` (same as above but you’re in the ```/CHE600/class02``` directory.

3. Command history is always accessible, and should be used!
    * You can scroll through your previous commands by using the “up” and “down” arrows on the keyboard. You can edit a command using the “left” or “right” arrows and the “Delete” and “Backspace” keys. Try it now.
    * You can look through your entire history by typing history. This will be powerful in conjunction with some text finding programs like grep which we will learn later in the course.
    * You can also use the reverse-i-search by hitting “ctrl-r” – this will search through your history for the most recent command the contains the string you type into it. Keep hitting ctrl-r to go further back in history.

4. Completion of filenames is available upon hitting the **tab** key. If there are more than one matches, hit the tab key twice to get a list of all matches. This is very useful, and you are encouraged to get used to doing this instead of typing the full file name every time!

5. Getting help about any Linux commands is easy. Try using one of the options below (won’t work on everything!) (**note that when you see italic text you need to replace the text with your own input to run the command!)**
    * google search on “_command_” or “_command_ tutorial”
    * ```man``` _command_
    * _command_ ```\--help```
    * _command_ ```-h```

6. Filenames
    * File names can be any combination of letters, numbers and symbols (avoid /><:&|)
    * You cannot use spaces in file names!! Underscore “\_” is a common replacement.
    * All file and directory names are Case sensitive ("Hello" is not the same as "hello")
    * Suffixes (the bit at the end of the file name) don’t matter, but are helpful when used to indicate the file type, for example:
        1. .sh (a bash shell script)
        2.  .py (a python script)
        3.  .c (a C program)

## **IV. Bashing on your own**

1. To try and assimilate the exercises we went through today, let's do an individual exercise. You'll notice that when we ran the ```getProteomeDisorder.sh``` command, we provided it with a proteome accession number (UPUP000464024). We could run this on any proteome code we wanted, and following the same awk command and workflow, calculated the average disorder for multiple organisms. This is what you'll need to do!

2. Adapt the commands and get the average disorder for the following organisms: 

| Proteome Id | Organism |
| --- | --- |
| UP000150494 | Rhinolophus affinis coronavirus |
| UP000154720 | BtRf-BetaCoV/HeB2013 |
| UP000118579 | SARS coronavirus PUMC02 |
| UP000168969 | SARS coronavirus Sino3-11 |
| UP000174731 | Bat SARS-like coronavirus YNLF_31C |
| UP000827403 | Staphylococcus phage vB_SarS_BM31 |
| UP000000354 | Severe acute respiratory syndrome coronavirus (SARS-CoV) |
| UP000128606 | BtRs-BetaCoV/YN2013 |
| UP000147828 | SARS coronavirus PUMC03 |
| UP000170944 | SARS coronavirus PUMC01 |
| UP000099142 | SARS coronavirus ZJ02 |

