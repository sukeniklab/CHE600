# CHEM260 F23 Class 5

Today's class will increase the complexity of tasks we're doing with bash. What we’ll cover today: 

* [Parameter variation with nested loops](#running-executables-with-multiple-parameters)
* [Multiple file processing](#processing-multiple-files) (Using the ```awk``` command)
* [Install VSCode](#installing-vscode)



# **Running executables with multiple parameters**

Researchers often use servers to run computational simulations. These are essentially experiments where the behavior of a complex system is defined, parameters provided, and the result - which is normally too complex to calculate analytically - is calculated numerically by the computer. In this exercise we will do exactly this: we will run a simulation of an ideal gas, providing a range of experimental parameters (namely density and temperature), to **simulate** the diffusion constant of a single gas molecule. We'll validate the result of the simulation by looking at the pressure - the simulation should obey the gas law!

1. The diffusion coefficient is a measure of how quickly an object moves in an isotropic environment (one that is the same in all directions). Here we are simulating an ideal gas, so every particle should be the same and the isotropic environment holds. To calculate diffusion, we will use the Einstein relationship:

$$\langle r^2 \rangle = \langle (r(t) - r(t_0))^2 \rangle$$

$$ D = \frac{1}{6} \lim_{t \to \infty}\langle(\frac{d}{dt}\langle r^2 \rangle)\rangle $$

2. Here, D is the self-diffusion coefficient, t is the time, and r(t) is the 3D position of the molecule at time t. The diffusion coefficient is obtained from the slope of the displacement (in area units) vs time. We will simulate a box of ~ 100 gas particles in a range of conditions, and the software will calculate the $$D$$ paramter by averaging over all displacements for all particles for the entire trajectory.

<img src="./images/MSD.png" width="300"/>

3. The simulation program is called "MDSS", and it sits in the ```/bin``` folder. This means we can execute it from anywhere we'd like. Let's use ```nano``` to look at the code. Notice it is written in python, and contains many lines of code.

```bash
nano /bin/MDSS
```

4. Make a new directory using ```mkdir```, ```~/CHE600/class05```, and ```cd``` into it. Try running ```MDSS```. Look at the message, and try changing your parameters until you get the simulation to run. Notice the output - and notice also the output only goes to the terminal window - no files are written (verify by typing ```ls```). You will need to extract information from this output. How would you do this?

5. Your task is to write a bash script called ```runMDSS.sh``` in your ```~/CHE600/class05``` directory that will iteratively run MDSS providing **all combinations** of the following temperatures and densities. This task should be completed with nested ```for``` loops. One for loop for each temperature, and another for loop for each pressure. Try simple examples using the ```echo``` command to figure out how to do this.


| **Temp (K)** | **Density (mg/mL)** |
| --- | --- |
| 10 | 0.1 |
| 50 | 0.5 |
| 100 | 1 |
| 200 | 1.5 |
| 300 | 2 |
| 400 | 2.5 |


<details>
<summary> <b>Hint on creating your iteration lists</b> </summary> 

We've seen two ways of creating iteration lists. One uses a bash command:

```bash
for i in $(ls); do echo $i; done
```
Another just uses a user provided list, seperated by spaces:
```bash
for i in WORD1 450 WORD3 ORANGES; do echo $i; done
```

Pay attention to the ```$()``` on the first option, and the lack of the in the second ```$()```. Which one should you use here?
</details>

6. Beyond the provided density and temperature, the script will also need to extract the pressure and diffusion constant provided at the end of the run in the output (e.g. "Average pressure=XX"). The average density (which you provided), temperature, pressure, and diffusion constant of each simulation (from the output) will need to be inserted into a csv file called ```simulations.csv```.

7. Look at your results and answer the following: 
    * Does the pressure make sense with the ideal gas law? 
    * How does the diffusion constant change with pressure and temperature? 
    * Write your answers in a file called ```~/CHE600/class05/ideal_gas.txt```

<details>
<summary> <b>spoiler - full code</b> </summary>

```bash
#!/bin/bash
for temp in 10 50 100;
do
        for dens in 0.1 0.5 1
        do
                MDSS $dens $temp > tmp
                finTemp=$(grep "Average temperature=" tmp|cut -d "=" -f 2)
                finPres=$(grep "Average pressure=" tmp|cut -d "=" -f 2)
                finDiff=$(grep " cm^2/s"  tmp|cut -d "=" -f 2)
                echo "$dens,$temp,$finTemp,$finPres,$finDiff"
        done
done
```

</details>