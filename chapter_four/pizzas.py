#4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a for loop to print the name of each pizza
pizzas = ['Dominos','cold stone', 'Mr Biggs']
for pizza in pizzas:
    print(pizza)

# Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. 
# For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
pizzas = ['Dominos','cold stone', 'Mr Biggs']
for pizza in pizzas:
    print(f"\nI Like {pizza} pizza")

#Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
# such as I really love pizza!
pizzas = ['Dominos','cold stone', 'Mr Biggs']
for pizza in pizzas:
    print(f"\nI Like {pizza} pizza")
    print("\n")
    print(f"I really love {pizza} pizza")

# 4-2. Animals: Think of at least three different animals that have a common characteristic.
#  Store the names of these animals in a list, and then use a for loop to print out the name of each animal
animals = ['Hen','Bat','Eagle']
print(f"{animals[0]}")
print(f"{animals[1]}")
print(f"{animals[2]}")

#Modify your program to print a statement about each animal, such as A dog would make a great pet.
animals = ['Hen','Bat','Eagle']
print(f"A {animals[0]} such as A dog would make a great pet.")
print(f"A {animals[1]} such as A dog would make a great pet.")
print(f"A {animals[2]} such as A dog would make a great pet.")

#Add a line at the end of your program stating what these animals have in common. 
# You could print a sentence such as Any of these animals would make a great pet!
animals = ['Hen','Bat','Eagle']
print("\n")
print(f"A {animals[0]} such as A dog would make a great pet.")
print(f"A {animals[1]} such as A dog would make a great pet.")
print(f"A {animals[2]} such as A dog would make a great pet.")
print("All these animals have feathers in common!")
print(f"{animals[0]} would make a great pet")

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive
numbers = []
for number in range(1,21):
    print(number)

#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
numbers = []
print("\n")
for number in range(1,1000001):
     #print("\n")
    print(number)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers.
'''
numbers = list(range(1,1000001))
print("\n")
first = min(digits)
second = max(digits)
print(first + second)
'''
# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
# Use a for loop to print each number.
numbers = list(range(1,21,2))
print("\n")
for number in numbers:
    print(number)

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
numbers = list(range(3,30,3))
for number in numbers:
    print(number)

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube
numbers = []
for number in range(1,10):
    print(number**3)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
numbers = []
for number in range(1,11):
    print(number**3)

#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list
pizzas = ['Dominos','cold stone', 'Mr Biggs', 'coldstone','kilima']
print(pizzas[0:3])

# Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
pizzas = ['Dominos','cold stone', 'Mr Biggs', 'coldstone','kilima']
print(pizzas[1:4])

# Print the message The last three items in the list are:. Use a slice to print the last three items in the list
pizzas = ['Dominos','cold stone', 'Mr Biggs', 'coldstone','kilima']
print(pizzas[2:5])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
#  Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

# 	 Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# 	 Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list.
#  Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza
pizzas = ['Dominos','cold stone', 'Mr Biggs', 'coldstone']
friend_pizza = ['Dominos','cold stone', 'Mr Biggs', 'coldstone','kilima']
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"{pizza} pizza")
    print("\n My friend’s favorite pizzas are:")
    for pis in friend_pizza:
        print(f"{pis} pizza")


