# MINI PYTHON REFERENCE GUIDE. FOR PYTHON 3
########################################################################################################################
# Single line comments start with a '#'

'''
multi-line comments start and end with 3 apostrophes or quotation marks
Sections in this mini guide:
VARIABLES, PRINTING/TYPE-CASTING, IMPORT STATEMENTS, LISTS, WHILE, FOR, IF/ELIF/ELSE, INPUT/TRY...EXCEPT, FUNCTIONS,
    DICTIONARIES, CLASSES, STRING SPLICING
'''

########################################################################################################################
# DECLARING VARIABLES - Can be string, int, float, boolean (or other types: dict, list, set, tuple, byte, etc)
dog_type = "good"  # can use apostrophes or quotation marks, it doesnt matter
dog_color = 'green'
doggo_count = 99999
good_dogs = 34.291
is_good_dog = True  # or False, notice the capitalization!
your_life = None  # like 'null' in java

########################################################################################################################
# PRINTING + TYPE CASTING 
print(good_dogs)
#       34.291
print("Hello " + dog_type + " dog!")
#         Hello good dog!
print("Hello\nBob")  # Escape character - new line '\n'
#       Hello
#       Bob

# Typecasting - int(), str(), float(), bool()
print("Hello " + str(doggo_count) + " " + dog_type + " dogs!")
#            Hello 99999 good dogs!

########################################################################################################################
# IMPORT STATEMENTS - let's say we want to access time.sleep(), a function which pauses the program for a set time
import time

time.sleep(.1)
# or, you could do this:
from time import sleep

sleep(.2)
# or even this
from time import sleep as hamburger

hamburger(.5)

########################################################################################################################
# LISTS - like arrays but more flexible. Starts at index 0 
cat_list = []
dog_list = [dog_type, good_dogs, "some string", 4134214, 'something  ', 3.14]

print(dog_list[0])  # "good", the first item in the list
print(len(dog_list))  # len() prints the length of the list: 6
print(dog_list[len(dog_list) - 1])  # prints the last item of the list: 3.14

dog_list.append("heckin good")  # appends this string to the end of the list

########################################################################################################################
# WHILE LOOPS 
while True:  # indent whatever's within the loop
    print("True foreverrr")
    break # breaks out of the loop because we actually dont want an infinite loop :P
while 7 <= 8:
    print("Infinity and beyond!")
    break # Oh wait, not infinity. We just broke the loop

########################################################################################################################
# FOR LOOPS
for i in dog_list: # reminder: dog_list = [dog_type, good_dogs, "some string", 4134214, 'something  ', 3.14]
    if i == "some string":
        continue # Move on in the loop - (won't hit the print(i) statement)
    print(i)  # Loops through dog_list and prints every item itself

for j in range(0, 100):
    print(j)  # Prints numbers in the range from 0 to 99

for some_var in range(0, len(dog_list) - 1):
    print(some_var)  # Prints the index number of every item in the list (0 through 5)

for index, item in enumerate(dog_list):
    print("INDEX: " + str(index) + ", ITEM: " + str(item))  # prints the index and item at the same time
    
########################################################################################################################
# IF STATEMENTS
if 7 == 7:  # True
    print("duh")
if "blah" == "blah":  # True
    print("trueee")

if 300 < 999:  # Note that only the first print statement would print because the rest are elifs/else
    print("It's True!")
elif 555 < 999:
    print("This is True")
elif 33333 >= 555555:
    print("aaaaaaaaaaaa")
else:
    print("I dont even know anymore")

some_list = [3, 4, 5, "some string", "whatever"]
if "whatever" in some_list:  # True
    print("This is true!!!")

if "ham" in "hamburger":  # True
    print("This is also trueeeeeeee!!!")

blah = True
if blah:  # True
    print("This is Trueee!!!!")
blerg = False
blork = None

if blah and not blerg:  # Use 'and', 'or', and 'not'. True statement.
    print("trurreeeee")
if blork is None:  # True
    print("tttrrrruueee. blork is indeed None")
########################################################################################################################
# USER INPUT AND TRY...EXCEPT
while True: # Putting this in an infinite loop until a good input is entered.
    my_input = input("Enter a number:") # my_input is a string! Lets convert it to an int.
    # Normally we would do converted_value = int(my_input)  
    # But what if we can't convert the input to an integer (user enters a letter/something else)?
    #   It will throw an exception if can't convert the value, so let's catch the exception.
    try:
        converted_value = int(my_input) # Try to convert it, if it fails then we move to the except block
        break # Exit the while loop because the conversion was successful!
    except Exception as e: # (broadly) catch the exception and store the error message in 'e'
        print("Invalid Input:" + str(e)) # Print the error message and restart the loop

# Note that when catching exceptions it's good practice to be more specific in what type of exception you're catching.
# 'except Exception as e' catches MOST exception types, but we might want to deal with each exception type differently
# 'except ValueError as e' is better practice, but it doesn't really matter in this example.
########################################################################################################################
# FUNCTIONS/METHODS - note that a method is a function, but inside a class
def doggo_speak(number_of_borks_to_give):  # Declare the function with a single parameter
    for i in range(number_of_borks_to_give):
        print("BORK!")


doggo_speak(5)  # call the function!


def steak_for_doggo(steak_count, worthy_doggo=True):  # Making the last parameter automatic/optional
    if worthy_doggo:
        doggo_speak(steak_count)  # Pass the number of steaks to doggo_speak. Doggo will bork a lot.
    else:
        print("DOGGO IS ANGERY! NO STEAK FOR DOGGO???!")


steak_for_doggo(3)  # worthy_doggo will automatically become True if not specified
steak_for_doggo(9999, False)  # NO STEAK FOR DOGGO!?

########################################################################################################################
# SOME OTHER STUFF
########################################################################################################################
# DICTIONARIES 
# These can be a pain to use and arent nearly as flexibile as lists are. May require googling if you want to use.
test_dict = {}
another_dict = {"good_doggerino": True,
                "a": 93424,
                6: "hamburger"}

print(another_dict['a'])  # 93424
another_dict["something_else"] = False  # This adds "something_else" : False to another_dict

########################################################################################################################
# CLASSES 
# Not necessary in small programs. Often can get the same functionality through normal functions
# Note that 'getter' and 'setter' methods are completey unecessary in Python classes since variables can't really be private

class Hamburger:
    def __init__(self, burger_count, burger_color):  # Constructor. 'self' = 'this' in Java
        self.burger_count = burger_count
        self.burger_color = burger_color

    def extreme_burger_multiplier(self, multiplier):  # A method. Must have 'self' in its parameters!
        self.burger_count *= multiplier  # Multiplies and sets burger_count to the product
        if self.burger_count > 9000:
            print("ITS OVER an acceptable limit of burgers we are allowed to carry")


muh_burgers = Hamburger(10, "blue")  # Instantiate the Hamburger class with 10 burgers and the color blue
muh_burgers.extreme_burger_multiplier(33)
print(muh_burgers.burger_count)  # Results in 330

########################################################################################################################
# SLICING (of strings)

some_str = "a very nice long juicy string"
# Now lets say we want everything up to the 4th character
print(some_str[:4])  # "a ve"
# Now we want everything after it
print(some_str[4:])  # "ry nice long juicy string"
# And now from the 4th to 6th characters
print(some_str[4:6])  # "ry"

########################################################################################################################
