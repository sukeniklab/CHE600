CHE600 - Class 18

Topics today:

1.	[Object Oriented programming in python: Iterated Prisoner’s Dilemma](#the-iterated-prisoners-dillema)
2. [Understanding the logic of OO code](#understanding-the-oo-logic)
3. [Using pre-written classes]

Takehome lessons:

1.	Some strategies for understanding a pre-written program
2.	Expanding our use of OOP in python
3.	A simple evolutionary algorithm



# The iterated prisoner’s dillema: 

The [prisoner’s dilemma](http://en.wikipedia.org/wiki/Prisoner's_dilemma) (PD) is a “game” in which two players are asked to cooperate or defect in a particular transaction, with the following payoff matrix:

<img src="./images/Picture1.png" width=450>
 

The iterated prisoner’s dilemma (IPD) version of this game each player plays against multiple players, including playing against the same players multiple times.  Players can remember the outcome of previous encounters with other players and tailor their strategies accordingly.  The winning player is the one who has the most aggregate payoff after many rounds of play, but one can also consider average score of whole population.

# Understanding the OO logic

1. I have implemented an object-oriented version of the IPD. The class files are contained in the file ipd_class.py which you can download from Canvas. Let’s have a look together. 

2. The main class is called _actor_ and represents an individual player. The actor has the following properties: 
    * ID
    * a strategy
    * a score
    * a tally of the number of transactions (games) it has been through. 
    
3. The actor also has a ```pay()``` function which increments the score according to the payoff rules in the table above

4.	A number of _strategy_ classes. These hold the details of how an _actor_ plays the game. Each strategy includes a few standard properties: 
    * The total number of actors in the game
    * the ID of the actor the strategy is associated with
    * the name of the strategy

5. The _strategy_ clss  also includes several functions:
    * A ```response()``` function which will pass a defect or cooperate after evaluating some conditions
    * An ```inform()``` function which lets the player remember what happened in the last game with a specific opponent. Not all strategies use the inform function.

6. We have three built-in strategies: always defect, always cooperate, and 'tit-for-tat'. Look at the code and figure out how each strategy works. (For a longer list of IPD strategies and an online pairwise tournament, see http://www.iterated-prisoners-dilemma.net/)

# Using classes effectively

It is clear that as it is currently written, the classes do not do much. We will need to program the game manually. 

1. Let's start simple: Create two _actors_ with two defined _strategies_, and have them play a single game. To do this, place [ipd_class.py](./files/ipd_class.py) in the same directory as a new notebook, and import the file in the first cell.

```python
from ipd_class import *
# this imports all classes to the main namespace (i.e. we wont have 
# to call ipd_class.actor(), we can just call actor() directly.)
```
```python
# set up the payoff matrix
payoff={("Defect","Defect"):(1,1), \
("Cooperate","Defect"):(0,3), \
("Defect","Cooperate"):(3,0), \
("Cooperate","Cooperate"):(2,2)}
```
```python
# create two actors, bob and alice
bob = actor(0,cooperate(2,0))
alice = actor(1,defect(2,1))

# get their responses
bob_response = bob.strategy.response(1)
alice_response = alice.strategy.response(0)

# calculate payoff by looking up the payoff matrix
bob_payoff,alice_payoff=payoff[(bob_response,alice_response)]

# print the outcome
print("bob  : %i \n alice: %i"%(bob_payoff,alice_payoff))
```

2. Now let's expand our game to multiple rounds:

```python
# list to store our actors
actorList=[]
# number of actors
N_actors=3
# how many rounds they'll play
rounds=10
# define payoff matrix
payoff={("Defect","Defect"):(1,1),
        ("Cooperate","Defect"):(0,3),
        ("Defect","Cooperate"):(3,0),
        ("Cooperate","Cooperate"):(2,2)}

# create the two actors with specifc strategies
strat_0 = cooperate
strat_1 = defect
strat_2 = tit_for_tat
# actorID 0
actorList.append(actor(0,strat_0(N_actors,0)))
# actorID 1
actorList.append(actor(1,strat_1(N_actors,1)))
# actorID 2
actorList.append(actor(2,strat_2(N_actors,2)))
print(actorList)
```

3. In the third cell, let's run the game:

```python
for i in range(10):
    random.shuffle(actorList)
    actor_0 = actorList[0]
    actor_1 = actorList[1]
    
    # get responses from both players
    response_0 = actor_0.strategy.response(actor_1.myid)
    response_1 = actor_1.strategy.response(actor_0.myid)
    
    # inform the actors of each other's response
    actor_0.strategy.inform(actor_1.myid,response_1)
    actor_1.strategy.inform(actor_0.myid,response_0)
    
    #assign pay
    payoff_0,payoff_1=payoff[(response_0,response_1)]
    actor_0.pay(payoff_0)
    actor_1.pay(payoff_1)
    
    #report on outcome:
    print('round %i\n---------' % (i+1))
    print('id\'s \t\t %i \t\t\t %i' % (actor_0.myid,actor_1.myid))
    print('strat \t\t %s \t %s' % (actor_0.name,actor_1.name))
    print('response \t %s \t %s' % (response_0,response_1))
    print('payoff \t\t %i \t\t\t %i' % (payoff_0,payoff_1))
    print('score \t\t %i \t\t %i' % (actor_0.score,actor_1.score))
    print('---------')
```

5. Now let's try to follow the total score of each strategy. To do this, we will get the score of all actors at the very end:

```python
# dictionary containing all strategies
scores = {'defect':0,'tit_for_tat':0,'cooperate':0}
N_actors = {'defect':0,'tit_for_tat':0,'cooperate':0}
# loop over all actors and add up their score
for actor in actorList:
    N_actors[actor.name]+=1
    scores[actor.name]+=actor.score

# print the results
print("strategy,no. actors,avg. score")
for key in scores.keys():
    print("%s,%i,%i"%(key,N_actors[key],scores[key]/N_actors[key]))
```

5. Finally, let's expand the game to 50 players with randomly chosen strategies and 1,000 rounds, and look at the scoring again! To do this, we'll expand our actorList:

```python
actorList=[]
strats=[cooperate,defect,tit_for_tat]
for i in range(50):
    actorList.append(actor(i,random.choice(strats)(50,i)))
print(actorList)
```

4. Pay attention to the final scores – specific match ups end up being very skewed! It is clear that some strategies do well against a subset of other strategies, but not against all.

5. Let's try skewing the playing field a bit. Increase the number of players who defect by adding a couple more defect strategies to the strats list - this will increase the probability of choosing it! 

```python
strats=[cooperate,defect,defect,defect,defect,defect,defect,tit_for_tat]
```

6. What happens to the overall score? Do the same thing by having more players cooperate. What happens then?

5. Let's write some new strategies. Design the following new strategy classes:
    1. random - will randomly pick Defect or Cooperate
    2. waffler - switches every time, starting from cooperate
    3. tat_for_tit - the opposite of tit for tat - starts by defecting and always does the oposite of what another actor has done to them. So if actor 1 has defected, next round against actor 1 will be cooperate

6. Incoporate these to your actors, and let's see how they do! Assuming all strategies are distributed equally, what is the best strategy to pick for this game?

7. Let's change the payoff matrix slightly:

```python
payoff={("Defect","Defect"):(1,1),
        ("Cooperate","Defect"):(0,4),
        ("Defect","Cooperate"):(4,0),
        ("Cooperate","Cooperate"):(3,3)}
```

What strategy will win now? Explain.

7. Submit your notebook, including answers to question in 6, 7, and 8.