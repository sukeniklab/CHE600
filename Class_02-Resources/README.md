# CHEM260 F23 Class 2

## Resources

What we’ll cover today: What resources should you use during this course (and for when you're coding for your own purposes)

## **I. Google searches**

## **II. LLMs**

## **III. Syllabus**

## **IV. Text books/online documents**

## **V. Logging in to the course server:**

1. The course has a dedicated server (a.k.a Virtual Machine or <b>VM</b>) managed by IT. To log in, you will need to use either:
    1. the Remote Desktop Server (RDS) (see details [here](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941534/Remote+Desktop+Services+RDS))
    2. A computer in the computer room
    3. Another computer managed by SU IT
2. Connecting to VM using the RDS:
    1. Open the start menu and type in "putty" - you can pin the app to your start bar
    2. In the first ("Session") window, insert the VM's ip address: as-che600-lvm.ad.syr.edu <br><img src="./images/putty_01.png" width="300"/>
    3. Next, go to the "X11 option in the option tree, and mark "Enable X11 Forwarding". This will allow Putty to transmit graphics<br><img src="./images/putty_02.png" width="300"/>
    4. Finally, go back to the "Session" window. Type "CHE600" in the "Saved Sessions" textbox, and hit "Save"<br><img src="./images/putty_03.png" width="300"/>
    5. Now, double click the CHE600 session, and a window will open up<br><img src="./images/putty_04.png" width="300"/>
    6. You should be able to log in using your SUID and password!<br><img src="./images/putty_05.png" width="300"/>
3. If you are using a manged computer running OS/X or Linux you can use your own shell and connect directly with: 
    ```bash
    ssh as-che600-lvm.ad.syr.edu
    ```
