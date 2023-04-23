# 2-3. Personal Message: Use a variable to represent a person’s name, and print 
# a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
name = "eric"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. 
'''Print the quote and the name of its author. Your output should look something like the 
following, including the quotation marks:Albert Einstein once said, “A person who never made a mistake never tried anything new.”
'''
quote = "A person who never made a mistake never tried anything new"
print(f"Albert Einstein once said,\"{quote}\"")


# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the 
'''famous person’s name using a variable called famous_person. Then compose 
your message and represent it with a new variable called message. Print your 
message.'''

famous_person = "Albert Einstein"
his_quote = "A person who never made a mistake never tried anything new."
print(f"{famous_person},once said, \"{his_quote}\"")

'''2-7. Stripping Names: Use a variable to represent a person’s name, and include 
some whitespace characters at the beginning and end of the name. Make sure 
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(), 
rstrip(), and strip().'''

name = " Tobzid Man "
print(name)
print(name.lstrip())
print(name.rstrip())
print("\t Tobzid \n Man")

'''
2-8. Number Eight: Write addition, subtraction, multiplication, and division 
operations that each result in the number 8. Be sure to enclose your operations 
in print() calls to see the results. You should create four lines that look like this:
print(5+3)
Your output should simply be four lines with the number 8 appearing once 
on each line'''

a = 3
b = 5
print(a+b)

c = 2
d = 4
print(c*d)

e = 10
f = 2
print(e-f)

g = 16
h = 2
print(g/h)

'''2-9. Favorite Number: Use a variable to represent your favorite number. Then, 
using that variable, create a message that reveals your favorite number. Print 
that message.'''

T = 10
print(f"My favorite number is {T}")

'''
2-10. Adding Comments: Choose two of the programs you’ve written, and 
add at least one comment to each. If you don’t have anything specific to write 
because your programs are too simple at this point, just add your name and 
the current date at the top of each program file. Then write one sentence 
describing what the program does'''



# 2-11. Zen of Python: Enter import this into a Python terminal session and skim through the additional principles
