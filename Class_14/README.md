CHE 600 - Class 14

Topics today:
Fitting a physical model – overview
Designing a model
Turning the model to a function
Fitting experimental data with the function
Homework #2 submission instructions

# Fitting a physical model

Last class we've seen how to an arbitrary function and fit it to experimental data. While the function can be informative (e.g. provide a decay constant, find the peak or the midpoint of a curve, etc.), it reveals very little about the underlying behavior of the system that ultimately generates the data. 

1. To gain true mechanistic insight about our system requires us to think of a mathematical model that determines the behavior of the system given some initial conditions. Inmportantly in our case, we want the model to produce the same observable our experiment measures. This could be the concentration of a specific chromophore, the pH of the system, the change in temperature, or any other expeirmentally accessible variable. 

2. Our approach is as follows: 
    1. Create a model (in practice: define a function) that accepts initial conditions as input and the experimental observable as output
    2. The model will include constants that define the behavior of the system
    3. Test your model with the initial conditions of your experiment and a reasonable range of values for the constant to see if it works as expected
    4. Finally, use the initial conditions of your experiment and FIT the constants to reproduce your experimental data
    5. The fitting results now reveal the value of the real physical constants underlying your system (as opposed to details about the shape of your data)

3. Modelling a system in this way is the ultimate way to leverage experimental results: If your fit doesn't work, or produces unrealistic constants, it means your experiment behaves by a different set of rules than what you expect. 

4. Importantly, even if your model **does** work, it does not mean you've captured all the nuance that might be present in the experiment! It only means you've found one way to explain the behavior of your system. 

# Designing a model

We write models based on our physical/chemical/biological knowledge. Models are extremely powerful to connect macroscopic observables with microscopic behavior. Models can be used to rule out specific mechanisms, verify others, and back out constants that would otherwise not be accessible.

## I. Setting the ground for the model

1. In today’s class, we will take experimental data from my lab, and try to fit it to a physical model. The data is the FRET signal from cells expressing a specific FRET-labeled protein. The donor-to-acceptor ratio (D/A) is the ratio of the donor and acceptor fluorophore emissions, and is measured using live cell microscopy. The concentration on the x-axis is measured by the intensity of the acceptor flurophore. Each point on the scatter plot below is a single cell.

<img src="./images/DA_exp.png" width=450>

2. Here’s where our expertise as scientists come into play. We need to integrate what we know about the system we’re studying, about the method used to obtain the data, and our intuition about what is going on to propose a model. 

3. In this case, my student was surprised to see a concentration dependence of the D/A signal – because naively we would assume the signal is coming from an individual molecule. My student suggested that this may be due to interaction between proteins – meaning labeled proteins would interact with each other in the cell to form DIMERS with a different D/A signal than monomers. 

4. We now have a hypothesis based on a physical intuition: As concentration increases in the cell, more of the labeled protein population would exist as a dimer with a lower D/A. We want to fit this model to our experimental data above. If it doesn’t work – meaning the fit is poor – the hypothesis is ruled out. If it works, it indicates the hypothesis might be correct – it does not prove it outright!

5. We would need to:
    1. Write the model as a function
    2. Test the function with some reasoable values
    3. Use this function, together with ```scipy.optimize.curve_fit()```, to fit our experimental data

## II. Turning our model into equations

Equations are what let us turn an idea into a quantitative prediction. In any model you must turn your intuition/thoughts/concepts that you believe are key to explaining your system into a set of equations. In this case, the ideas revolve around a monomer dimer equilibrium in our system. Remember also that ultimately you will need to model the observable - in this case the D/A ratio.

1. The first thing we need to think about is how we turn the composition of our system into our observable – in this case a D/A fluorescence ratio. For that, we will assume that the entire protein population is divided into two states, and that each state has an average D/A value that is associated with it. The final equation would be:

$$D/A=\frac{[monomer]}{[total]}D/A_{monomer} + \frac{[dimer]}{[total]}D/A_{dimer}$$

* Note that this assumption need not be true – it’s possible there are higher order oligomers, or that the initial state is a dimer, or that there are stable oligomeric states.. but all these can be tested down the line. 

7. What parameters here can we obtain from our experimental data (assuming the model is correct?)

Clearly there is some relationship between [monomer], [dimer], and [total]. Let’s build a model to account for this. The model will assume that the FRET reporter population in each cell is at equilibrium (another assumption!) according to the equilibrium equation:

[dimer]⇌2[monomer],   (2)

which obeys the following equilibrium constant:

K_d=[monomer]^2/[dimer]    (3)

We do NOT know the dimer and monomer concentrations. HOWEVER – we know the TOTAL concentration of protein in each cell (that’s out x-axis!). We can back out individual concentrations if we know the Kd by using a simply quadratic:

[total]=2×[dimer]+[monomer]   (4)

From here follows that:

[dimer]=([total]-[monomer])/2  (5)
And:

K_d=[monomer]^2/(([total]-[monomer])/2)  (6)

This rearranges to a second degree polynomial:

-2[monomer]^2-K_d [monomer]+K_d [total]=0   (7)

Which is solvable using a quadratic formula, where a=-2, b=-K_d, c=K_d [total], and x=[monomer]. Reminder that the quadratic formula is x_1,2=(-b±√(b^2-4ac))/2a

In other words, we can now supply our function with Kd and [total] (our x axis – the vector containing the total concentration of protein in uM), and we will get the monomer and dimer concentration from:
solving the quadratic in Eq. 7 to obtain [monomer]
plugging in [monomer] into Eq. 4 to get [dimer]
plugging in [monomer] and [dimer] to Eq. 1 to get the observable.


Putting it all together:

Looking back, the parameters we need to plug into our model are:
[total] – this is the x axis
D/A_monomer and D/A_dimer – these are free parameters in Eq. 1
K_d – another free parameter in Eq. 4

Code this entire segment according to the following instructions:
Generate [total] values (x-axis) using np.linspace()
Assign values to scalar variables Kd, D/Amonomer, and D/Adimer
¬Code the quadratic equation shown above, and use the monomer and dimer concentrations to calculate D/A.
Plot D/A vs [total] and examine the shape. Change the variables to see what makes sense. Does this seem like a model that can explain the experimental results?

Notice that now you can not only plot the total D/A signal, you can also plot the monomer and dimer concentrations as function of total concentration. See if that makes sense.

Think also about how you would do some sanity checks: 

For example, we know that Kd should remain constant throughout. You can calculate it explicitly using Eq. 3 above, and see if it remains constant for every [total] concentration. 
We also want [total] to stay constant – you can check that by summing the monomer and dimer concentrations (Eq. 4) to see if they are not changing.


Turning the model to a function

Now that the model works – we need to turn it into a function so that we can use it with scipy.optimize.curve_fit to fit our experimental data. How do you do this? 

Remember that the fitting function needs to return the same observable as our experimental data – that means the output of this function needs to be D/A

What would be the parameters you input to the function?

Code it up and try running it and plotting the results. It’s a good idea to not have this function plot anything, because that would be problematic when you call it iteratively through curve_fit. 

Hint: The end result should be a function that accepts a vector x and 3 scalars and returns a vector of D/A values.



Fitting our model to our data – Homework #2

Import the experimental data (download DA_vs_conc.csv from Canvas) and import it into your python using pandas or numpy.

Plot the experimental data, see if it makes sense.

Call your dimer model function through curve_fit (remember your imports!):

popt,pcov = scipy.optimize.curve_fit(func, x, y, **args)

x and y are the experimental concentration and D/A signal, respectively.

Try fitting it without any arguments. If this doesn’t work, pass some initial starting point using p0, or add some bounds. For example, we know for a fact Kd and D/A can’t be negative.

Plot your fit on top of the experimental data to see how it looks!

If you managed to fit your data: congrats! Not only have you shown that the concentration dependence we see could be explained by our FRET construct dimerizing, you also managed to quantify the Kd for this reaction. 

This analytical dimerization model is a major upgrade for this paper, and gives strong mechanistic insight to an otherwise purely phenomenological observation

To canvas, please upload:

The final script (call it dimerModel.py), including the model function and the fitting script.
A plot of the experimental data overlayed with your model fit
A plot of the monomer and dimer concentrations vs. total concentration.

