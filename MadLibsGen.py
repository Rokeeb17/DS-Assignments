""" 
Project Brief
Inspired by Summer Son’s Mad Libs project with Javascript. The program will first prompt the
user for a series of inputs a la Mad Libs. For example, a singular noun, an adjective, etc. Then,
once all the information has been inputted, the program will take that data and place them into a
premade story template. You’ll need prompts for user input, and to then print out the full story at
the end with the input included.
Concepts to keep in mind:
● Strings
● Variables
● Concatenation
● Print 

Deliverables
A pretty fun beginning project that gets you thinking about how to manipulate user inputted data.
Compared to the prior projects, this project focuses far more on strings and concatenating.
Have some fun coming up with some wacky stories for this!
"""

"""
Description: Random Story
Author: Rokeeb 
"""

print('Let Mad Libs begin!') 
name = input('Enter a name: ')  ## collect user inputs for different prompts
adj1 = input('Enter an adjective: ')
adj2 = input('Enter an adjective: ')
adj3 = input('Enter an adjective: ')
verb = input('Enter a verb: ')
noun1 = input('Enter a noun: ')
noun2 = input('Enter a noun: ')
animal = input('Enter an animal: ')
food = input('Enter a food: ')
fruit = input('Enter a fruit: ')
superhero = input('Enter a superhero: ')
country = input('Enter a country: ')
dessert = input('Enter a dessert: ')
year = input('Enter a year: ')

story1 = (f"This morning {name} woke up feeling {adj1}. 'It is going to be a {adj2} day!' Outside, a bunch of {animal}s were protesting to keep \
      {food} in stores. They began to {verb} to the rhythm of the {noun1}, which made all the {fruit}s very {adj3}. Concerned, {name} texted \
        {superhero}, who flew {name} to {country} and dropped {name} in a puddle of frozen {dessert}. {name} woke up in the year {year}, in a \
            world where {noun2}s ruled the world.")

print(story1)


