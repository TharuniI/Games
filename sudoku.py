'''
Sudoku- By Tharuni Iranjan
This is a take on the Sudoku game. In this version the Sudoku grid will be displayed
on the screen using Python Turtle. The user will be asked to enter a row number, column
number, and the number they think should be in that position. If that postition contains a
preset number, 'invalid position' will be printed on the screen. If they enter the right number
for that position, it will be displayed on the screen. Or else they number of tries goes down by one.
If they correctly fill all the boxes they win. If they run out of tries they lose.
'''
#DISPLAY
#repeated commands created into functions
def forward_right_396():
    right(90)
    forward(396)

def forward_left_396():
    left(90)
    forward(396)

def forward_right_132():
    right(90)
    forward(132)

def forward_left_132():
    left(90)
    forward(132)

#function for lines made for the unbolded areas of grid
def in_unbolded():
    for i in range(3):
        forward_right_396()
        left(90)
        forward(44)
        forward_left_396()
        right(90)
        penup()
        forward(88)
        pendown()

#function for lines for the bolded areas of the grid
def in_bolded():
    forward_right_132()
    forward_right_396()
    forward_left_132()
    forward_left_396()
    pensize(1)
    forward_right_132()

#This def function draws all the grid for the sudoku
def draw_sudoku():
    #Sets speed, color, and position of turtle
    speed(100)
    penup()
    color("black")
    setposition(-199.5, 199)
    pendown()
    left(90)

    #Outerbox
    pensize(8)
    for i in range(4):
        forward_right_396()

    #Inside bolded lines vertically
    in_bolded()

    #Inside bolded lines horizontally
    in_bolded()
    right(90)
    forward(44)

    #Inside unbolded lines vertically
    in_unbolded()
    right(180)
    forward(44)

    #Inside unbolded lines horizontally
    left(90)
    forward(44)
    in_unbolded()

#This def function prints all numbers not provided by the user
def print_numbers():
    #Row numbers
    penup()
    setposition(-195, 187)
    right(90)
    num1= 1
    for i in range(9):
        __turtle.write(str(num1))
        penup()
        forward(44)
        pendown()
        num1 += 1
    #Column numbers
    penup()
    setposition(-195, 145)
    right(90)
    num2= 2
    for i in range(8):
            __turtle.write(str(num2))
            penup()
            forward(45)
            pendown()
            num2 += 1

    #Given numbers
    penup()
    setposition(-185, 168)
    standard= ("Arial", 20, "normal")
    __turtle.write("8", font= standard)

    setposition(-98, 80)
    __turtle.write("6", font= standard)

    setposition( -10, 168)
    __turtle.write("3", font= standard)

    setposition(-50, 83)
    __turtle.write("9", font=("Arial", 20, "normal"))

    setposition(-50, 168)
    __turtle.write("6", font= standard)

    setposition(35, 125)
    __turtle.write("8", font= standard)

    setposition(80, 125)
    __turtle.write("7", font= standard)

    setposition(80, 83)
    __turtle.write("4", font= standard)

    setposition(165, 163)
    __turtle.write("1", font= standard)

    setposition(-144, -10)
    __turtle.write("3", font= standard)

    setposition(-144, -52)
    __turtle.write("4", font= standard)

    setposition(-98, -52)
    __turtle.write("5", font= standard)

    setposition(-50, -10)
    __turtle.write("4", font= standard)

    setposition(35, -10)
    __turtle.write("9", font= standard)

    setposition(80, 30)
    __turtle.write("1", font= standard)

    setposition(125, 30)
    __turtle.write("5", font= standard)

    setposition(125, -10)
    __turtle.write("2", font= standard)

    setposition(-185, -182)
    __turtle.write("4", font= standard)

    setposition(-97, -102)
    __turtle.write("7", font= standard)

    setposition(-97, -142)
    __turtle.write("1", font= standard)

    setposition(-50, -142)
    __turtle.write("2", font= standard)

    setposition(-10, -182)
    __turtle.write("9", font= standard)

    setposition(35, -182)
    __turtle.write("7", font= standard)

    setposition(35, -102)
    __turtle.write("6", font= standard)

    setposition(80, -102)
    __turtle.write("5", font= standard)

    setposition(165, -182)
    __turtle.write("3", font= standard)

    setposition(-300, 300)

#This prints the grid with numbers
draw_sudoku()
print_numbers()

"---------------------------------------------------------------------------------------------------------------------------"
#Intro
#prints the title and instructions
print ("           Sudoku- Intermediate Level")

#User Input
'''''''''''''''''''''''
This class assigns and x and y positions
for each of the coordinates in the sudoku
'''''''''''''''''''''''
class SetPosition:
    position_x = 0
    position_y = 0

    def __init__(self, user_number):
        self.user_number = user_number

    def put_number(self, row_number, column_number):
        self.row_number = row_number
        self.column_number = column_number

        #this sets a y position for each of the boxes going down the sudoku
        if row_number == 1 :
            SetPosition.position_y = 168
        elif row_number == 2:
            SetPosition.position_y = 125
        elif row_number == 3:
            SetPosition.position_y = 80
        elif row_number == 4:
            SetPosition.position_y = 30
        elif row_number == 5:
            SetPosition.position_y = -10
        elif row_number == 6:
            SetPosition.position_y = -52
        elif row_number == 7:
            SetPosition.position_y = -102
        elif row_number == 8:
            SetPosition.position_y = -142
        elif row_number == 9:
            SetPosition.position_y = -182

        #this sets a x position for each of the boxes going across the sudoku
        if column_number == 1:
            SetPosition.position_x = -185
        if column_number == 2:
            SetPosition.position_x = -144
        if column_number == 3:
            SetPosition.position_x = -97
        if column_number == 4:
            SetPosition.position_x = -50
        if column_number == 5:
            SetPosition.position_x = -10
        if column_number == 6:
            SetPosition.position_x = 35
        if column_number == 7:
            SetPosition.position_x = 80
        if column_number == 8:
            SetPosition.position_x = 125
        if column_number == 9:
            SetPosition.position_x = 165
        self.set_position = (SetPosition.position_x, SetPosition.position_y)

'''''''''''''''''''''''
This class checks whether or not the
user put the right number for the
right position and tells them the
number of tries they have left
'''''''''''''''''''''''
class Validate:
    number= 0

    def __init__(self, user_number ):
        self.user_number= user_number

    def num_position(self, row_number, column_number):
        self.row_number= row_number
        self.column_number= column_number
        #rows in sudoku
        row1= ["8", "7", "4", "6", "3", "5", "2", "9", "1"]
        row2= ["2", "9", "3", "1", "4", "8", "7", "6", "5"]
        row3= ["5", "1", "6", "9", "7", "2", "4", "3", "8"]
        row4= ["7", "2", "9", "8", "6", "3", "1", "5", "4"]
        row5= ["1", "3", "8", "4", "5", "9", "6", "2", "7"]
        row6= ["6", "4", "5", "7", "2", "1", "3", "8", "9"]
        row7= ["9", "8", "7", "3", "1", "6", "5", "4", "2"]
        row8= ["3", "5", "1", "2", "8", "4", "9", "7", "6"]
        row9= ["4", "6", "2", "5", "9", "7", "8", "1", "3"]

        #This defines each number in the sudoku
        #row1
        if row_number == 1 and column_number == 1:
            Validate.number= row1[0]
        elif row_number == 1 and column_number == 2:
            Validate.number= row1[1]
        elif row_number == 1 and column_number == 3:
            Validate.number= row1[2]
        elif row_number == 1 and column_number == 4:
            Validate.number= row1[3]
        elif row_number == 1 and column_number == 5:
            Validate.number= row1[4]
        elif row_number == 1 and column_number == 6:
            Validate.number= row1[5]
        elif row_number == 1 and column_number == 7:
            Validate.number= row1[6]
        elif row_number == 1 and column_number == 8:
            Validate.number= row1[7]
        elif row_number == 1 and column_number == 9:
            Validate.number= row1[8]

        #row2
        if row_number == 2 and column_number == 1:
            Validate.number= row2[0]
        elif row_number == 2 and column_number == 2:
            Validate.number= row2[1]
        elif row_number == 2 and column_number == 3:
            Validate.number= row2[2]
        elif row_number == 2 and column_number == 3:
            Validate.number= row2[2]
        elif row_number == 2 and column_number == 4:
            Validate.number= row2[3]
        elif row_number == 2 and column_number == 5:
            Validate.number= row2[4]
        elif row_number == 2 and column_number == 6:
            Validate.number= row2[5]
        elif row_number == 2 and column_number == 7:
            Validate.number= row2[6]
        elif row_number == 2 and column_number == 8:
            Validate.number= row2[7]
        elif row_number == 2 and column_number == 9:
            Validate.number= row2[8]

        #row3
        if row_number == 3 and column_number == 1:
            Validate.number= row3[0]
        elif row_number == 3 and column_number == 2:
            Validate.number= row3[1]
        elif row_number == 3 and column_number == 3:
            Validate.number= row3[2]
        elif row_number == 3 and column_number == 3:
            Validate.number= row3[2]
        elif row_number == 3 and column_number == 4:
            Validate.number= row3[3]
        elif row_number == 3 and column_number == 5:
            Validate.number= row3[4]
        elif row_number == 3 and column_number == 6:
            Validate.number= row3[5]
        elif row_number == 3 and column_number == 7:
            Validate.number= row3[6]
        elif row_number == 3 and column_number == 8:
            Validate.number= row3[7]
        elif row_number == 3 and column_number == 9:
            Validate.number= row3[8]

        #row4
        if row_number == 4 and column_number == 1:
            Validate.number= row4[0]
        elif row_number == 4 and column_number == 2:
            Validate.number= row4[1]
        elif row_number == 4 and column_number == 3:
            Validate.number= row4[2]
        elif row_number == 4 and column_number == 3:
            Validate.number= row4[2]
        elif row_number == 4 and column_number == 4:
            Validate.number= row4[3]
        elif row_number == 4 and column_number == 5:
            Validate.number= row4[4]
        elif row_number == 4 and column_number == 6:
            Validate.number= row4[5]
        elif row_number == 4 and column_number == 7:
            Validate.number= row4[6]
        elif row_number == 4 and column_number == 8:
            Validate.number= row4[7]
        elif row_number == 4 and column_number == 9:
            Validate.number= row4[8]

        #row5
        if row_number == 5 and column_number == 1:
            Validate.number= row5[0]
        elif row_number == 5 and column_number == 2:
            Validate.number= row5[1]
        elif row_number == 5 and column_number == 3:
            Validate.number= row5[2]
        elif row_number == 5 and column_number == 3:
            Validate.number= row5[2]
        elif row_number == 5 and column_number == 4:
            Validate.number= row5[3]
        elif row_number == 5 and column_number == 5:
            Validate.number= row5[4]
        elif row_number == 5 and column_number == 6:
            Validate.number= row5[5]
        elif row_number == 5 and column_number == 7:
            Validate.number= row5[6]
        elif row_number == 5 and column_number == 8:
            Validate.number= row5[7]
        elif row_number == 5 and column_number == 9:
            Validate.number= row5[8]

        #row6
        if row_number == 6 and column_number == 1:
            Validate.number= row6[0]
        elif row_number == 6 and column_number == 2:
            Validate.number= row6[1]
        elif row_number == 6 and column_number == 3:
            Validate.number= row6[2]
        elif row_number == 6 and column_number == 3:
            Validate.number= row6[2]
        elif row_number == 6 and column_number == 4:
            Validate.number= row6[3]
        elif row_number == 6 and column_number == 5:
            Validate.number= row6[4]
        elif row_number == 6 and column_number == 6:
            Validate.number= row6[5]
        elif row_number == 6 and column_number == 7:
            Validate.number= row6[6]
        elif row_number == 6 and column_number == 8:
            Validate.number= row6[7]
        elif row_number == 6 and column_number == 9:
            Validate.number= row6[8]

        #row7
        if row_number == 7 and column_number == 1:
            Validate.number= row7[0]
        elif row_number == 7 and column_number == 2:
            Validate.number= row7[1]
        elif row_number == 7 and column_number == 3:
            Validate.number= row7[2]
        elif row_number == 7 and column_number == 3:
            Validate.number= row7[2]
        elif row_number == 7 and column_number == 4:
            Validate.number= row7[3]
        elif row_number == 7 and column_number == 5:
            Validate.number= row7[4]
        elif row_number == 7 and column_number == 6:
            Validate.number= row7[5]
        elif row_number == 7 and column_number == 7:
            Validate.number= row7[6]
        elif row_number == 7 and column_number == 8:
            Validate.number= row7[7]
        elif row_number == 7 and column_number == 9:
            Validate.number= row7[8]

        #row8
        if row_number == 8 and column_number == 1:
            Validate.number= row8[0]
        elif row_number == 8 and column_number == 2:
            Validate.number= row8[1]
        elif row_number == 8 and column_number == 3:
            Validate.number= row8[2]
        elif row_number == 8 and column_number == 3:
            Validate.number= row8[2]
        elif row_number == 8 and column_number == 4:
            Validate.number= row8[3]
        elif row_number == 8 and column_number == 5:
            Validate.number= row8[4]
        elif row_number == 8 and column_number == 6:
            Validate.number= row8[5]
        elif row_number == 8 and column_number == 7:
            Validate.number= row8[6]
        elif row_number == 8 and column_number == 8:
            Validate.number= row8[7]
        elif row_number == 8 and column_number == 9:
            Validate.number= row8[8]

        #row9
        if row_number == 9 and column_number == 1:
            Validate.number= row9[0]
        elif row_number == 9 and column_number == 2:
            Validate.number= row9[1]
        elif row_number == 9 and column_number == 3:
            Validate.number= row9[2]
        elif row_number == 9 and column_number == 3:
            Validate.number= row9[2]
        elif row_number == 9 and column_number == 4:
            Validate.number= row9[3]
        elif row_number == 9 and column_number == 5:
            Validate.number= row9[4]
        elif row_number == 9 and column_number == 6:
            Validate.number= row9[5]
        elif row_number == 9 and column_number == 7:
            Validate.number= row9[6]
        elif row_number == 9 and column_number == 8:
            Validate.number= row9[7]
        elif row_number == 9 and column_number == 9:
            Validate.number= row9[8]

'''''''''''''''''''''''
This class checks whether a
number is already given in the sudoku
'''''''''''''''''''''''
class Invalid:
    position= 0
    def __init__(self, row_number, column_number):
        self.row_number= row_number
        self.column_number= column_number
    def __eq__(self, other):
        return self.row_number == other.row_number and self.column_number == other.column_number

#This sets a value for the following variables
num_of_tries= 10
moves= 55

while True:
    #This asks the user for and x and y coordinate
    #It will continuously ask the user if it is not in the range of 1-9
    row_number = int(input("Enter a row number: "))
    while ((row_number <= 0) or (row_number > 9)):
        print ("Number must be from 1-9!")
        row_number = int(input("Enter a row number: "))
    column_number = int(input("Enter a column number: "))
    while ((column_number <= 0) or (column_number > 9)):
        print ("Number must be from 1-9!")
        column_number = int(input("Enter a column number: "))

    #each variable is given a row &column number for a number that’s already given to the user
    #it compares it with the the user's input to see if it is a valid position or not
    iv= Invalid(row_number, column_number)
    invalid1= Invalid(1, 1)
    invalid2= Invalid(1, 4)
    invalid3= Invalid(1, 5)
    invalid4= Invalid(1, 9)
    invalid5= Invalid(2, 6)
    invalid6= Invalid(2, 7)
    invalid7= Invalid(3, 3)
    invalid8= Invalid(3, 4)
    invalid9= Invalid(3, 7)
    invalid10= Invalid(4, 7)
    invalid11= Invalid(4, 8)
    invalid12= Invalid(5, 2)
    invalid13= Invalid(5, 4)
    invalid14= Invalid(5, 6)
    invalid15= Invalid(5, 8)
    invalid16= Invalid(6, 2)
    invalid17= Invalid(6, 3)
    invalid18= Invalid(7, 3)
    invalid19= Invalid(7, 6)
    invalid20= Invalid(7, 7)
    invalid21= Invalid(8, 3)
    invalid22= Invalid(8, 4)
    invalid23= Invalid(9, 1)
    invalid24= Invalid(9, 5)
    invalid25= Invalid(9, 6)
    invalid26= Invalid(9, 9)

    #This prints 'invalid position' if one of the following x and y coordinates are entered
    if (iv == invalid1) or (iv == invalid2) or (iv == invalid3) or (iv == invalid4) or (iv == invalid5) or (iv == invalid6) or (iv == invalid7) or (iv == invalid8) or (iv == invalid9) :
        print ("Invalid position!")
        continue
    elif (iv == invalid10) or (iv == invalid11) or (iv == invalid12) or (iv == invalid13) or (iv == invalid14) or (iv == invalid15) or (iv == invalid16) or (iv == invalid17) or (iv == invalid18) or (iv == invalid19) :
        print ("Invalid position!")
        continue
    elif (iv == invalid21) or (iv == invalid22) or (iv == invalid23) or (iv == invalid24) or (iv == invalid25) or (iv == invalid26):
        print ("Invalid position!")
        continue

    #This asks the user for a number to put in the box
    user_number = int(input("Enter a number: "))
    while ((user_number <= 0) or (user_number > 9)):
        print ("Number must be from 1-9!")
        user_number = int(input("Enter a number: "))

    v= Validate(user_number)
    v.num_position(row_number, column_number)

    #This only runs if the number given by the user matches the number that should to be there
    if (int(user_number) == int(Validate.number)):
        #This decreases the number of moves left in the game by 1
        moves-= 1

        #This calls for the class function SetPosition to place the number where the user requested
        sp = SetPosition(user_number)
        sp.put_number(row_number, column_number)

        penup()
        setposition(SetPosition.position_x, SetPosition.position_y)
        pendown()
        color("dark blue")
        __turtle.write(user_number, font=("Arial", 20, "normal"))
        penup()
        setposition(-250, 250)
        print ((" "*25), "Number of tries left:", num_of_tries)

    #This only runs if the number given by the user does not match the number that's supposed to be there
    elif user_number != Validate.number:
        #This tells the user they are incorrect and decreases the number of tries they have left by 1
        num_of_tries-= 1
        print ("That is incorrect!")
        print ((" "*25), "Number of tries left:", num_of_tries)

    #When the user runs out of tries, it prints you lost and exits the game
    if num_of_tries <= 0:
        print ("")
        print ((" "*12),"You are out of tries!")
        print ((" "*18),"You Lost :(")
        break

    #When moves equals 0, we know the user has run out of moves therefore finishing the game
    #This congratulates the user and exits the game
    if moves <= 0:
        print ("")
        print ("  Congratulations! You've completed the Sudoku :D")
        break
