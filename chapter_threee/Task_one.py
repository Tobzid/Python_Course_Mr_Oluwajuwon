# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
friends = ['Billionaire', 'Macavelli', 'Aristotle', 'Newton', 'Money', 'perfect']
for name in friends:
    print(name)

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.

friends = ['Billionaire', 'Macavelli', 'Aristotle', 'Newton', 'Money', 'perfect']
for name in friends:
    print(f"{name}, is one of my very good friend.")

#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
#  Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

cars = ['Honda','Benz','BMW','Camry','Corolla']
for car in cars:
    if 'Honda' in car:
        print("I don't like Honda cars")
    elif 'Benz' in car:
        print("I love Benz cars")
    elif 'BMW' in car:
        print("I would like to own a BWM car")
    elif 'Camry' in car:
        print("I love Camry cars")
    elif 'Corolla' in car:
        print("I love Corolla cars too!!!")
    else:
        print(" These are the list of cars that we have")

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

Friends = ['Wale','Biodun','Bolu','Kola']
print(f"{Friends[0]}, You are invited to a dinner")
print(f"{Friends[1]}, You are invited to a dinner")
print(f"{Friends[2]}, You are invited to a dinner")
print(f"{Friends[3]}, You are invited to a dinner")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite

Friends[0] = "Favour"
print(Friends)
print(sorted(Friends))

# Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it
Friends = ['Wale','Biodun','Bolu','Kola']
print(f"{Friends[0]}, is the name of the friend that can't be at the dinner.")

# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
Friends = ['Favour', 'Biodun', 'Bolu', 'Kola']
Friends.sort()
print(Friends)

# Print a second set of invitation messages, one for each person who is still in your list
Friends = ['Favour', 'Biodun', 'Bolu', 'Kola']
print(f"\nDear {Friends[0]}, This is to formerly invites you to the up coming dinner ")
print(f"Dear {Friends[1]}, This is to formerly invites you to the up coming dinner ")
print(f"Dear {Friends[2]}, This is to formerly invites you to the up coming dinner ")
print(f"Dear {Friends[3]}, This is to formerly invites you to the up coming dinner ")

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
Friends.append("Baddo")
Friends.append("Osama")
Friends.append("Gobe")
print("\nFriends")

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger dinner table
Friends = ['Favour', 'Biodun', 'Bolu', 'Kola']
print(f"\n{Friends[0]}, i found a bigger dinner table")
print(f"{Friends[1]}, i found a bigger dinner table")
print(f"{Friends[2]}, i found a bigger dinner table")
print(f"{Friends[3]}, i found a bigger dinner table")

#  Use insert() to add one new guest to the beginning of your list
#  Use insert() to add one new guest to the middle of your list.
#Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list
Friends.insert(0,"Baddo")
Friends.insert(1,"Osama")
Friends.append("Gobe")
print(f"\n{Friends[0]}, This is a new dinner invitation message to you")
print(f"{Friends[1]}, This is a new dinner invitation message to you")
print(f"{Friends[2]}, This is a new dinner invitation message to you")
print(f"{Friends[3]}, This is a new dinner invitation message to you")
print(f"{Friends[4]}, This is a new dinner invitation message to you")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and you have space for only two guests 
# ** Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
print("\n I can only invite only two people for dinner")

# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.
Friends = ['Favour', 'Biodun', 'Bolu', 'Kola']
Friendd = Friends.pop()
print(Friends)
Friends.pop()
print(Friends)

#Print a message to each of the two people still on your list, letting them know they’re still invited
print(f"\n{Friends[0]}, You are still valid for the dinner!")
print(f"{Friends[1]}, You are still valid for the dinner!")

# Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end of your program
del Friends
# print(Friends)

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit
# Store the locations in a list. Make sure the list is not in alphabetical order
places = ['USA','China','Germany', 'Japan','Kenya']
#Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list
places.sort()
print("\n")
print(places)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(places))

# Show that your list is still in its original order by printing it.
places = ['USA','China','Germany', 'Japan','Kenya']
print(places)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
places.reverse()
print("\n")
print(places)
#print(sorted(places))

# Show that your list is still in its original order by printing it again.
places = ['USA','China','Germany', 'Japan','Kenya']
print(places)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print("\n")
print(places)
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places.reverse()
print(places)
#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print("\n")
print(places)

# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
places.sort()
print("\n")
print(places)

#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42),
#  use len() to print a message indicating the number of people you are inviting to dinner.
places = ['USA','China','Germany', 'Japan','Kenya']
print(len(places))

# 3-10. Every Function: Think of something you could store in a list. For example, 
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
cities = ['Lagos','Abuja','Abeokuta','Ife','Akure']
cities.sort()
print(cities)
