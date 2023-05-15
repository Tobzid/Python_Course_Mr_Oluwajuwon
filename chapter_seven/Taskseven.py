# 7-1. Rental Car: Write a program that asks the user what kind of rental car they 
# would like. Print a message about that car, such as “Let me see if I can find you 
# a Subaru.”

car = "what kind of rental car do you want"
car += "we can help you in finding it. "
name = input(car)
print(f"Let me see if we can find you {name}")

# 7-2. Restaurant Seating: Write a program that asks the user how many people 
# are in their dinner group. If the answer is more than eight, 
# print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

dinner = "How many people are in your dinner group"
dinner += "\nIf they are more than eight!, they will have to wait for a table"
question = input(dinner)
question = int(question)
if question >= 8:
    print("You\'ll have to wait for a table")
else:
    print("Your table is ready")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not
number = input("kindly input a random number: ")
number = int(number)
if number%10 == 0:
    print("The number given is a multiple of 10")
else:
    print("The number given is not a multiple of 10")

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value. As they enter each topping, 
# print a message saying you’ll add that topping to their pizza.
prompt = "Please enter a series of pizza toppings"
prompt += "\nEnter 'quit' to end the program. "
message = " "
while message != 'quit':
    message = input(prompt)
    print(f"\nyou’ll add {message} topping to their pizza.")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
# a person’s age. If a person is under the age of 3, the ticket is free; if they are 
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
# $15. Write a loop in which you ask users their age, and then tell them the cost 
# of their movie ticket

prompt = "We charge different prices for our movie ticket depending on your age. "
prompt += "\nKindly input your age to get the price of your movie ticket."
age = " "
active = True
while active:
    age = input(prompt)
    if age == "quit":
        active = False
    elif age != "quit":
        age = int(age)
        if age <= 3:
            print("Hi, your ticket is free")
        elif (age >=3) and (age <=12):
            print("Hi, your ticket fee is $10")
        elif age > 12:
            print("Hi, your ticket fee is $15")


# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5  #picking Exercise 7-4
# that do each of the following at least once:
# Use a conditional test in the while statement to stop the loop.

prompt = "Please enter a series of pizza toppings"
prompt += "\nEnter 'quit' to end the program. "
message = " "
while message != 'quit':
    message = input(prompt)
    print(f"\nyou’ll add {message} topping to their pizza.")

# Use an active variable to control how long the loop runs.
prompt = "Please enter a series of pizza toppings"
prompt += "\nEnter 'quit' to end the program. "
message = " "
active = True
while active:
    message = input(prompt)
    if message != "quit":
        print(f"\nyou’ll add {message} topping to their pizza.")
    elif message == "quit":
        active = False
    else:
        print("Thanks and goodbye")


# Use a break statement to exit the loop when the user enters a 'quit' value
prompt = "Please enter a series of pizza toppings"
prompt += "\nEnter 'quit' to end the program. "
message = " "
while True:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print(f"\nyou’ll add {message} topping to their pizza.")


# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press 
# ctrl-C or close the window displaying the output.)



''' 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches. Loop through the list of sandwich 
orders and print a message for each order, such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made'''





