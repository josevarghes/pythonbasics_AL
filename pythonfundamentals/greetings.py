'''Task 1 :
You will write two functions: one that greets a single person and another that greets a group of people.
Define a function called greet(name):
The function should take one parameter called name.
Inside the function, print a greeting message that says "Hello, <name>!".
Call the function greet() with different names to see the output.
Define a second function called greet_all(names):
The function should take one parameter, which is a list of names.
Inside the function, use a for loop to iterate over each name in the list.
For each name in the list, call the greet() function to print a personalized greeting.
Call the greet_all() function with a list of names to greet all the people in that list.'''

def greet(name):
    print(f"Hello {name}")


greet("Alan")

def greet_all(names) :
    for i in names :

        greet(i)

greet_all(["alan","jose","varghese"])
