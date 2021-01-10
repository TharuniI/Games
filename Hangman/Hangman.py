'''
Hangman- By Tharuni Iranjan
The user will be given a random word to guess based on the category they choose.
Blanks will indicate the length of the word. The user has to guess letters in order 
to solve for the word. If they guess correctly it will be revealed where that letters
are within the word. If not, a body part of a stick person will appear. If the full body
has been "hunged" they lose. If they can solve before that, the user wins.
'''
#DISPLAY
#The title of the game is printed
speed(100)
penup()
setposition(-110, 140)
pendown()
color("Blue")
standard= ("Arial", 40, "normal")
__turtle.write("Hangman", font= standard)
#This prints the scaffold in which the stick man is "hung"
penup()
setposition(-80, -50)
pendown()
color("black")
pensize(3)
forward(100)
right(180)
forward(50)
right(90)
forward(130)
right(90)
forward(50)
right(90)
forward(10)
left(90)
penup()
setposition(500, 500)
color("red")
#This creates the head of the stick man
def head():
    penup()
    setposition(20, 70)
    pendown()
    pensize(2)
    right(180)
    for i in range(313):
        forward(0.25)
        left(1.15)
    right(180)
    penup()
    setposition(500, 500)
#This creates the body of the man
def body():
    penup()
    setposition(20, 45)
    pendown()
    pensize(3)
    right(90)
    forward(45)
    left(90)
    penup()
    setposition(500, 500)
#This creates one of the legs of the man
def leg1():
    setposition(20, 0)
    pendown()
    pensize(3)
    right(45)
    forward(20)
    left(45)
    penup()
    setposition(500, 500)
#This creates the second leg of the man
def leg2():
    setposition(20, 0)
    pendown()
    pensize(3)
    right(135)
    forward(20)
    left(135)
    penup()
    setposition(500, 500)
#This creates an arm for the man
def arm1():
    setposition(20, 20)
    pendown()
    pensize(3)
    left(45)
    forward(20)
    penup()
    right(45)
    setposition(500, 500)
#This creates another arm for the man
def arm2():
    setposition(20, 20)
    pendown()
    pensize(3)
    left(135)
    forward(20)
    right(135)
    penup()
    setposition(500, 500)

#Various categories are set up for the user to choose from    
import random
country= ["Afghanistan", "Barbados", "Canada", "Cameroon", "Guatemala", "Iceland", "Kyrgyzstan", "Maldives", "Madagascar", "Philippines", "Romania", "Thailand", "Ukraine", "Yemen", "Venezuela"]
food= ["Burrito", "Chocolate", "Guacamole", "Honeydew", "Ice Cream", "Kale", "Lemonade", "Okra", "Panini", "Quinoa", "Ravioli", "Spaghetti", "Stir Fry", "Waffle"]  
kitchen= ["Apron", "Bowl", "Crockpot", "Dishwasher", "Fork", "Grinder", "Juicer", "Knife", "Kettle", "Leftovers", "Microwave", "Oven", "Refrigerator", "Sponge", "Table"] 
colors= ["Amber", "Beige", "Blue", "Charcoal", "Indigo", "Khaki", "Lavender", "Mahogany", "Magenta", "Olive", "Orange", "Peach", "Rainbow", "Tan", "Silver"] 

#Here the user choses one fo the four categorys
print "A) Country   B) Food   C) In the Kicthen   D) Colors"
category= str(input("Select a Category: "))
if category == "A":
    topic= country
    print "A random word in the topic Country has been selected"
elif category == "B":
    topic= food
    print "A random word in the topic Food has been selected"
elif category == "C":
    topic= kitchen
    print "A random word in the topic In the Kitchen has been slected"
elif category == "D":
    topic= colors
    print "A random word in the topic Colors has been selected"
else:
    print "That is not a category option!\n"
    category= str(input("Select a Category: "))
    if category == "A":
        topic= country
        print "A random word in the topic Country has been selected"
    elif category == "B":
        topic= food
        print "A random word in the topic Food has been selected"
    elif category == "C":
        topic= kitchen
        print "A random word in the topic In the Kitchen has been slected"
    elif category == "D":
        topic= colors
        print "A random word in the topic Colors has been selected"
print ""

#A word will be randomly chosen based on the category they have chosen
secret_word = random.choice(topic)
secret_word = secret_word.lower()

#Some set of variables are assigned a value
dash= []
guess1= ""

#Function update_dashes is defined
def update_dashes(secret_word, dashes, guess1):
    #This determines if guess is in the secret word and if so reveals where it is
    if guess1 in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess1:
                dash[i] = list(secret_word)[i]
    return "".join(dash)

#Dashes for the length of the secret word is created and printed
for i in range(len(secret_word)):
    dash.append("-")
print " ".join(dash)

#Function get_guess is defined
def get_guess():
    x = True
    guesses_left = 6
    #while loop runs until x== False
    while x == True:
        #This asks the user to enter a letter
        guess = input("Guess a letter: ")
        z = update_dashes(secret_word, dash, guess)
        #This runs if guesses is invalid
        if not guess.islower():
            print "Your guess must be a lowercase letter!\n"
        elif len(guess)!= 1:
            print "Your guess must have exactly one character!\n"
        #This determines whether or not guess is in the secret word
        elif guess in list(secret_word):
            print "That letter is in the word!"
            print (" "*35), "Guesses left:", str(guesses_left)
            print z
        elif guess not in list(secret_word):
            print "That letter in not in the word!"
            #This decreses the number of trys when the user guesses incorecctly 
            guesses_left -= 1
            #Depending on how many tries the user has left a body part will appear the screen
            if guesses_left == 5:
                head()
            elif guesses_left == 4:
                body()
            elif guesses_left == 3:
                leg1()
            elif guesses_left == 2:
                leg2()
            elif guesses_left == 1:
                arm1()
            elif guesses_left == 0:
                arm2()
            print (" "*35), "Guesses left:", str(guesses_left)
            print z
        #This asks the user whether they want to solve or continue guessing
        solve_or_guess = str(input("Enter s to solve or g to guess: "))
        #If the user wants to solve they enter what they think the word is 
        if solve_or_guess == "s":
            solve = str(input("Enter the word: "))
            if solve == secret_word:
                x= False
        #If they want to guess the while loop goes back to the beginning
        elif solve_or_guess == "g":
            print (" "*35), "Guesses left:", str(guesses_left)
            print z
            continue
        #If the user enters neither s or g it will continue to ask the user for guesses
        else:
            print "Invalid Input"
            print (" "*35), "Guesses left:", str(guesses_left)
            print z
        #This exits the function if the user guesses the word correctly
        if dash == list(secret_word):
            x = False
        #This exists the function if the user runs out of guesses
        if guesses_left == 0:
            x = False
    #This tells the user if they won or not 
    if ((dash == list(secret_word)) or (solve == secret_word)):
        return "Congrats, you win! The word was: " + str(secret_word)
    elif guesses_left == 0:
        return "Sorry you lost! The word was: " + str(secret_word)
    
#This runs the function get_guesses
print get_guess()

#This prints the final Game Over onto the screen
setposition(-130, -170)
color("Blue")
__turtle.write("Game Over", font= standard)
penup()
setposition(500, 500)
