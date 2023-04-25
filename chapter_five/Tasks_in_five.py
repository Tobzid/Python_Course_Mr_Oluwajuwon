# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test
#  and your prediction for the results of each test. Your code should look something like this:

#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')

team = 'chelsea'
print("Is team == chelsea, I predict it to be yes")
print(team == "chelsea")
print("is team == car?, i predict it to be NO")
print("team == car")

#5-2. More Conditional Tests: You don’t have to limit the number of tests you create to ten. If you want to try more comparisons,
#  write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:


#Tests for equality and inequality with strings
teams = "Band"
print("teams == band, will give us False.")
teams == "band"
print("teams == Band, will give us True.")
teams == "Band"

# Tests using the lower() method
Braid = "wigs"
Braid.lower() == "wigs"
print("This will return True.")

# Numerical tests involving equality and inequality, greater than and 
# less than, greater than or equal to, and less than or equal to
num1 = 10
num2 = 15
num1 < num2
print("num1 < num2 will give True.")
num1 <= num2
print("num1 <= num2 will give True")
num1 > num2
print("num1 > num2 will give False.")
num1 >= num2
print("num1 >= num2 will give False.")

#Tests using the and keyword and the or keyword






# Tests weather an items is in a list
game = ['play_station', 'sega', 'ludo','chess', 'sport']
item1 = "sport"
for item in game:
    if item1 in item:
        print(f"{item1}, is in the list")


game = ['play_station', 'sega', 'ludo','chess', 'sport']
item1 = "sport"
for item in game:
    if item1 in item:
        print(f"{item1}, is in the list")
    else:
        print(f"{item} is also in the list")

# Test weather an item is not in a list.
cars = ["Benz", "BMW", "AUDI", "Honda"]
car1 = "Porche"
if car1 not in cars:
    print(f"{car1}, is not in the list")

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# Write an if statement to test whether the alien’s color is green. If it is, print 
# a message that the player just earned 5 points.
 
alien_color = "green"
if alien_color == "green":
    print("Your just earn a 5points.")

# Write one version of this program that passes the if test and another that 
# fails. (The version that fails will have no output.)
alien_color = "green"
if alien_color == "gold":
    print("Your just earn a 5points.")
else:
    print("THis outcome will fail.")

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
#write an if-else chain
alien_color = "green"
if alien_color == "gold":
    print("Your just earn a 5points.")
else:
    print(" You missed the color!.")

# If the alien’s color is green, print a statement that the player just earned 5 points
# for shooting the alien.

# If the alien’s color isn’t green, print a statement that the player just earned 
# 10 points
alien_color = "green"
if alien_color == "gold":
    print("Your just earn a 5points.")
else:
    print("You just earn a 10points.")

# Write one version of this program that runs the if block and another that 
# runs the else block
alien_color = "green"
if alien_color == "green":
    print("Your just earn a 5points.")
else:
    print("You just earn a 10points.")

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

#If the alien is green, print a message that the player earned 5 points
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points
alien_color = "green"
if alien_color == "red":
    print("You just earn 15points")
elif alien_color == "yellow":
    print("You just earn 10points")
else:
    print("you just earn 5points")

# Write three versions of this program, making sure each message is printed 
#for the appropriate color alien
alien_colors = ["green", "yellow", "red"]
for alien_color in alien_colors:
    if "green" in alien_color:
        print("you just earn 5points")
    if "yellow" in alien_color:
        print("You just earn 10points")
    if "red" in alien_color:
        print("you just earn 15points")
    else:
        print("Thank you Boss.")

#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
#stage of life. Set a value for the variable age, and then:
# 1. If the person is less than 2 years old, print a message that the person is a baby.
# 2. If the person is at least 2 years old but less than 4, print a message that the person is a toddler
# 3. If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# 4. If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# 5. If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# 6. If the person is age 65 or older, print a message that the person is an elder

age = 10
if age <= 2:
    print("This person is a baby")








# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
#independent if statements that check for certain fruits in your list
# 1. 	 Make a list of your three favorite fruits and call it favorite_fruits
# 2. Write five if statements. Each should check whether a certain kind of fruit 
# is in your list. If the fruit is in your list, the if block should print a statement, 
# such as You really like bananas!
fruits = ["mango","banana", "orange", "grape"]
for fruit in fruits:
    if "mango" in fruit:
        print("you really like mangoes")
    if "banana" in fruit:
        print("you really like bananas")
    if "orange" in fruit:
        print("you really like oranges")
    else:
        print(f"you really love {fruit} ")


# 5-8. Hello Admin: Make a list of five or more usernames, including the name 
# 'admin'. Imagine you are writing code that will print a greeting to each user 
#after they log in to a website. Loop through the list, and print a greeting to 
#each user
# 1. If the username is 'admin', print a special greeting, such as Hello admin, 
# would you like to see a status report?
# 2. Otherwise, print a generic greeting, such as Hello Jaden, thank you for 
# logging in again
usernames = ["Tobzid", "Zino", "Davido", "Admin", "Ronaldo"]
for username in usernames:
    print(f"Hello {username}, thank you for logging in again")
    if "Admin" in username:
        print(f"Hello {'Admin'}, would you like to see a status report?")


# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
#not empty
# 1. If the list is empty, print the message We need to find some users!
# 2. Remove all of the usernames from your list, and make sure the correct 
#message is printed

username = []
if len(username) <= 0:
    print("list is empty, we need to find some users!")

# 5-10. Checking Usernames: Do the following to create a program that simulates 
# how websites ensure that everyone has a unique username
# 1. Make a list of five or more usernames called current_users
# 2. Make another list of five usernames called new_users. Make sure one or 
#two of the new usernames are also in the current_users list.
# 3. Loop through the new_users list to see if each new username has already 
#been used. If it has, print a message that the person will need to enter a 
#new username. If a username has not been used, print a message saying 
#that the username is available.

current_usernames = ["Tobzid", "Dangote", "Davido", "Admin", "Ronaldo"]
new_users = ["Admin", "Ronaldo", "Wande", "Bobo", "Tsg"]
for name in current_usernames:
    print(f"{name}, your username is available")
    if name in new_users:
        print(f"{name}, you need to enter a new username")

        # this code below also give the same output
current_usernames = ["Tobzid", "Dangote", "Davido", "Admin", "Ronaldo"]
new_users = ["Admin", "Ronaldo", "Wande", "Bobo", "Tsg"]
for name in current_usernames:
    print(f"{name}, your username is available")
    for new in new_users:
        if name in new:
            print(f"{new}, you need to enter another username")



# 5. Make sure your comparison is case insensitive. If 'John' has been used, 
#'JOHN' should not be accepted. (To do this, you’ll need to make a copy of 
#current_users containing the lowercase versions of all existing users.




# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such 
#as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# 1. Store the numbers 1 through 9 in a list
# 2. Loop through the list
# 3. Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read "1st 2nd 3rd 4th 5th 6th 
#7th 8th 9th", and each result should be on a separate line
ordinal_numbers = [1,2,3,4,5,6,7,8,9]
for number_position in ordinal_numbers:
    if ordinal_numbers[0] == 1:
        print("1st position")
    elif ordinal_numbers[1] == 2:
        print("2nd position")
    elif ordinal_numbers[2] == 3:
        print("3rd position")
    elif ordinal_numbers[3] == 4:
        print("4th position")
    elif ordinal_numbers[4] == 5:
        print("5th position")
    elif ordinal_numbers[5] == 6:
        print("6th position")
    elif ordinal_numbers[6] == 7:
        print("7th position")
    elif ordinal_numbers[7] == 8:
        print("8th position")
    else:
        print("9th position")

