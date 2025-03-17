CHE600 - Class 16

Topics today:
1. Intro Object Oriented programming in python
2. Object Orientd program demo: Card wars
3. Independent work: adding new strategies

# Intro to Object oriented programming

So far we've been writing "sequential" code, with occasional function definitions that are then called within this code. This form of programming is ideally suited for some tasks (i.e. visualizations, writing short data analysis scripts, etc.) However, some programs require hundreds of lines of code and a much higher level of organization to maintain readability. Object-oriented programming (OOP) is a common paradigm to write more sphisticated programs.

## I. General example of class-based programming

Let’s say we are trying to simulate the behavior of a farm. We need to populate this with animals. The way we have been writing code, we will need to write lines for each animal we have on the farm – dog, sheep, cat, etc. 

1. Using OOP, Instead of writing all these lines of code, we can realize that all creatures are "animals," and as such have common elements, and so there’s no point in rewriting the code over and over. Instead, we’ll create a _class_ – a blueprint for animal that can take on the properties of any animal we want. 

2. Let’s give some tangible examples for what we want to see in the class ```animal```. These will be its _attributes_ – properties that can be defined and called. For example:
    1. type (string:dog/cat/sheep) 
    2. sound (string:woof/meow/baah) 
    3. milk (float)
    4. speed (float)
    5. position (2-element numpy array)
    6. strength (float)

3. Now let's give the animals an ability to perform actions - these of course will be _functions_. For example: 
    1. makeSound() – print out the sound of the animal behavior
    2. move(moveBy) – changes the position of the object
    3. fight(animal) – fights another animal object
    4. milk(volume) - removed milk from the animal

4. We can now define a variable (let's call it ```babe```) that is an _instance_ of our animal class. For example:

```python
babe = animal(type='pig',sound='oink',milk=0,speed=0.5,position=[1,1],strength=3)
```
 
5. The variable ```babe``` has all the _attributes_ and _functions_ defined in the animal _class_. Notice the hierarchy here, and also notice that you can create as many instances of the class animal as you want!

## II. Advantages of OOP

Writing object-oriented code has several advantages over the standard “line-by-line” scripts we’ve written previously.

1. It simplifies programming by hiding the algorithmic detail of each component of the program (but makes it more difficult to debug while writing)

2. It offers improved reliability since each instance of a class is identical and can be created as many times as neccessary 

3. Improved code reuse and sharing since you only need to remember the class “interface” and don’t need to know the details of how the code is implemented.

4.	We use classes/objects all the time in Python – we’ve already seen this! For example, can you think of an example of a _class_ and some of its _attributes_ and _functions_ from the numpy library?

5. The art of effective OO programming is picking the right class and the right attributes and functions to interact with objects from this class. In some cases – OO may not be the right choice. In others, this makes your program much more efficient and streamlined. Experience is a major factor in choosing which one to use!


# Object Oriented program for card games

We'll now see how this approach works by designing an object-oriented card game. We'll pick the simplest game of "war": There are two players with a full deck of 52 cards each. Every turn each player draws one card. The player with the highest value card places both cards at the bottom of their deck.

1. To do this, will design two classes:
    1. Card: Holds a single card
	2. Deck: Holds and manipulates a list of cards

2. Think like an OO programmer: 
    * What are the attributes for the card object? 
    * What are the functions of the card object? 
    * What are the attributes of the deck object? 
    * What are the functions of the deck object?

3. Let’s code these into a class. The format for creating a class is fixed: 
    1. Define the class name using the ```class``` keyword
    2. The first function must be the __init__ function. This function is called automatically every time an instance (object) of that class is created. Initializing the class sets all the properties assigned to the class. If the user is supposed to provide values to these properties, they need to be part of the function definition.
    3. After assigning the init function, we add any functions that class may have. The self keyword is used whenever we want to access properties or functions of the class (which we do by calling self.property) 

## I. The card class
We'll start by building the card class:

1. In a notebook called cards.ipynb, write up the following code:

```python
class card:
    '''
    card class
    '''
    def __init__(self, suit, type, value):
        self.cardsuit=suit
        self.cardtype=type
        self.cardvalue=value
    
    def printcard(self): 
 	print("%2s %s %2d"%(self.cardtype, self.cardsuit, self.cardvalue))
```

2. The class itself is like an empty form. We need to create an instance of a card, with instructions on how to fill it. Once you’ve run the script, you can create an instance of the card class like so:

```python
acard = card("S","A",14)
acard.cardsuit #this is an attribute
acard.printcard() #this is a function
```

3. ```acard``` is an instance of the ```card``` class, with a property suite "S" (spade), a property type "A" (Ace), and a numeric property value of 14 (that allows convenient comparison between cards). Think about the usability of this class. Could our card accept any value of suite or type? Do we actually need to define the value? How would you improve this object?

## II. The deck object

Next, let’s plan the other object, a deck. The deck will hold card objects. Because we’re going to program a game of war – each player should initially have a full, 52-card deck, but the decks need to be able to add and remove cards. What functions should ```deck``` have?

1. An __init__ function that defines all the deck's attributes

```python
def __init__(self):
    #initialize the deck - essentially an empty list
    self.deck=[]
    # possible values for suits and rank
    suits=['S','C','H','D']
    ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # a dictionary to map rank to a numerical value
    values={'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
    # generate a full deck of cards - all suites of each rank:
    for suit in suits:
        for rank in ranks:
            # add a card object to the self.deck list for every suit/rank combo
            self.deck.append(card(suit,rank,values[rank]))
```

2. A function that will shuffle the deck (```shuffle()```)

```python
def shuffle(self):
    #shuffle the deck
    newdeck=[]
    randCard=np.arange(len(self.deck))
    np.random.shuffle(randCard)
    for i in range(len(randCard)):
        print(i, randCard[i])
        newdeck.append(self.deck[randCard[i]])
    self.deck=newdeck
```
3. A function that will let us look at thewhole deck:

```python
def printdeck(self):
    #print the contents of the deck
    i=0
    for card in self.deck:
        print("%3d "%(i))
        card.printcard()
        i+=1
```

4. A function that will deal a card from the top of the deck (```dealCard()```)

```python
def dealcard(self): 
    #deal a card from the TOP deck
    return(self.deck.pop())
```

5. A function that will add a card to the bottom of the deck (```addCard()```)

```python
def addcard(self,card):
    #add a card to the BOTTOM of the deck
    self.deck.insert(0,card)
```

6. A function to print out how many cards are left in the deck (```cardsleft()```) 

```python
def cardsleft(self): 
    return len(self.deck)
```

## III. Bringing it all together
We'll now combine the deck and card classes to a single library called cards.py, and code our game of war into a jupyter notebook called way.ipynb

1. Copy and paste the card and deck classes into a single file called ```cards.py```, and place it in the same directory as your notebook. Note this is file should not be a jupyter notebook, just a regular python library (notebooks can't be easily imported!). 

2. Next, we'll import it and program a game of war:

```python
# cards.py must be in the same directory as your notebook!
import cards

#create and shuffle two decks
adeck=cards.deck()
adeck.shuffle()
bdeck=cards.deck()
bdeck.shuffle()

#play five rounds of "war"
for i in range(1000):
    print("--------round %i---------"%i)
    acard=adeck.dealcard()
    bcard=bdeck.dealcard()
    print("Player a: %s | Player b: %s"% (acard.cardtype,bcard.cardtype))
    if acard.cardvalue>bcard.cardvalue:
        print("Player a has the higher card")
        adeck.addcard(acard)
        adeck.addcard(bcard)
    elif acard.cardvalue<bcard.cardvalue:
        print("Player b has the higher card")
        bdeck.addcard(acard)
        bdeck.addcard(bcard)
    else:
        print("cards equal")
        adeck.addcard(acard)
        bdeck.addcard(bcard)
    print("Player a has %i cards left "%adeck.cardsleft())
    print("Player b has %i cards left "%bdeck.cardsleft())
```

4. In an actual game of card war, when there is a tie, players draw three more cards, with the last one face up. The player with the highest-value face up card takes all the cards. Code this routine into the game, and run the game for another five rounds.

5. Upload your notebook 
