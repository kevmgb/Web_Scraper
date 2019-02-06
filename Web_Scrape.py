#Fibonnaci
# a, b= 0, 1
#
# for i in range(0,10):
#     print (a)
#
#     a, b = b, a+b

#----------------------------------------------------------------------------------------------------------------------#

 # Fizzbuzz

# for num in range(0,50):
#     if num %5 == 0 and num %3 ==0:
#         print ("FizzBuzz")
#     elif num %5 == 0:
#         print ("Fizz")
#     elif num%3 == 0:
#         print ("Buzz")
#     else:
#         print (num)

#----------------------------------------------------------------------------------------------------------------------#

# import datetime
#
# name = input("Whats your name: ")
# age = int(input ("What is your age? "))
# years_left = 100 - age
# this_year = datetime.datetime.now().year
# one_hundred = this_year + years_left
# print ("Your name is " +name, "You will be one hundred years old in the year ", +one_hundred)

#----------------------------------------------------------------------------------------------------------------------#

#Odd or even
# number = int(input("Enter a number: "))
#
# if number %2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd")
#
# if number %4 == 0:
#     print("The number is a multiple of four")

#----------------------------------------------------------------------------------------------------------------------#


# Printing elements in a list

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# new_list =[]
# user_number = int(input("Enter a number "))
#
# for elements in a:
#     if elements < user_number:
#         # print(elements)
#         new_list.append(elements)
#         print(new_list)

#----------------------------------------------------------------------------------------------------------------------#


# list1 = ['physics', 'chemistry', 1997, 2000];
# list2 = [1, 2, 3, 4, 5 ];
# list3 = ["a", "b", "c", "d"]
#
# print ("list1[0]: ",( list1[0]))
# print(list2[1:5])

#----------------------------------------------------------------------------------------------------------------------#


#Divisors Check
# num = int(input("Please choose a number to divide: "))
#
# listRange = list(range(1,num+1))
#
# divisorList = []
#
# for number in listRange:
#     if num % number == 0:
#         divisorList.append(number)
#
# print(divisorList)

#----------------------------------------------------------------------------------------------------------------------#

# Common elements in lists
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# new_list = []
# for i in a and b:
#     if i in a and b:
#         new_list.append(i)
# print(new_list)

#----------------------------------------------------------------------------------------------------------------------#

#Palindrome Check

# # word_list=[]
# #
# word = input("Enter a word to check: ")
# #
# # word_list.append(word)
#
# wrd = str(word)
# reverse = word[::-1]
# print("You entered:", reverse)
#
# if wrd == reverse:
#     print ("This is a Palindrome")
#
# else:
#     print("This isn't a palindrome")

#----------------------------------------------------------------------------------------------------------------------#


# #List comprehension
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# b = []
#
# # for elements in a:
# #     if elements%2 == 0:
# #         b.append(elements)
# # print (b)
#
# b = [elements for elements in a if elements % 2 ==0]

# print (b)

#----------------------------------------------------------------------------------------------------------------------#

# import random
#
# numlist = []
# list_length = random.randint(5, 15)
#
# while len(numlist) < list_length:
#     numlist.append(random.randint(1, 75))
#
# evenlist = [number for number in numlist if number % 2 == 0]
#
# print(numlist)
# print(evenlist)

#----------------------------------------------------------------------------------------------------------------------#

# Rock Paper Scissors

# import sys
#
# user1 = input("What's your name? ")
# user2 = input("And your name? ")
# user1_answer = input("%s, do yo want to choose rock, paper or scissors? " % user1)
# user2_answer = input("%s, do you want to choose rock, paper or scissors? " % user2)
#
# def compare(u1, u2):
#     if u1 == u2:
#         return "It's a tie!"
#     elif u1 == 'rock':
#         if u2 == 'scissors':
#             return "Rock wins!"
#         else:
#             return "Paper wins!"
#     elif u1 == 'scissors':
#         if u2 == 'paper':
#             return"Scissors win!"
#         else:
#             return "Rock wins!"
#     elif u1 == 'paper':
#         if u2 == 'rock':
#             return "Paper wins!"
#         else:
#             return "Scissors win!"
#     else:
#         return "Invalid input! You have not entered rock, paper or scissors, try again."
#         sys.exit()
#
# print(compare(user1_answer, user2_answer))


#----------------------------------------------------------------------------------------------------------------------#


# def check(value):
#     if value == a:
#         return "Your correct!, great guess!"
#     elif value < a:
#         return "Your guess is too low, try again"
#     elif value > a:
#         return "Your guess is too high, try again"
#     else:
#         return "Invalid input"
#     sys.exit()

#----------------------------------------------------------------------------------------------------------------------#

# import random
#
# a = random.randint(1,9)
#
# user = 0
# counter = 0
#
# while user !=a and user != "exit":
#
#     user = int(input("Guess a number that's between one and nine,(You can type exit to quit): "))
#
#     if user == "exit":
#         break
#
#     counter +=1
#     if user == a:
#         print("Your correct!, you took",counter,"tries")
#     elif user < a:
#         print("Your guess is too low, try again")
#     elif user > a:
#         print("Your guess is too high, try again")
#     else:
#         print("Invalid input")

#----------------------------------------------------------------------------------------------------------------------#

# common elements
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c=[]
#
# for elements in a and b:
#     if elements in a and b:
#         c.append(elements)
# print(c)
# result = [i for i in a if i in b], will result in duplicate 1

#----------------------------------------------------------------------------------------------------------------------#

# import random
#
# a = random.sample(range(1,30), 12)
# b = random.sample(range(1,30), 16)
# c= [i for i in set(a) if i in b]
# print(c)

#----------------------------------------------------------------------------------------------------------------------#

#Prime number function

# import sys
# number = input("Please enter a number" + "\n" + ">>>")
# number = int(number)
# prime = False #initiate boolean for true false, default false
# if number > 0:
#     for x in range (2, number - 1): #this range excludes number and 1, both of which number is divisible by
#         if number % x != 0: #If number isn't evenly divisible by x, start over with the next one
#             continue
#         elif number % x == 0: #If number is evenly divisible by x, it can't be prime
#             sys.exit("The number is not prime.")
#     sys.exit("The number is prime.") #number wasn't evenly divisible by any x, so it's prime
# elif number == 0:
#     sys.exit("The number is not prime.") #According to the Google, 0 is not prime
# else:#if number is less than 0, the number is not prime (according to the Google).
#     sys.exit("The number is not prime.")

# Python program to check if the input number is prime or not

# take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1

# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
#
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#     print(num, "is not a prime number")

#----------------------------------------------------------------------------------------------------------------------#

# default arguments in python


# def get_integer():
#     return int(input("Give me a number: "))
#
# age = get_integer()
# days = get_integer()
# print(age , days)

# def get_integer(help_text = "Give me a number: "):
# #     return int(input(help_text))
# #
# #
# # age = get_integer("Whats your age: ")
# # year= get_integer()
# # print (age)

#----------------------------------------------------------------------------------------------------------------------#

# Remove first and last elements in the list
# a = [5, 10, 15, 20, 25]
#
# leng = a.__len__()
#
# new = [a[0], a[leng - 1]]
# b= a[0]
# c= a[leng - 1 ]

# new = []
#
# new.append(b)
# new.append(c)

# a = [5, 10, 15, 20, 25]
#
# def remove_list_elements(list):
#     leng = a.__len__()
#     new = [a[0], a[leng - 1]]
#     print(new)
#
#
# remove_list_elements(a)

#----------------------------------------------------------------------------------------------------------------------#

# #Fibonnaci
# def fibonnaci():
#     num = int(input("enter how many numbers in the sequence you want: "))
#     a, b= 0, 1
#     for i in range(0,num):
#         print (a)
#         a, b = b, a+b
#
# fibonnaci()

#----------------------------------------------------------------------------------------------------------------------#

#Lists with non repeated elements

# Using sets

# a = [5, 10, 15, 20, 25, 20, 5, 4, 10]
#
# b = set()
#
# for elements in a:
#     b.add(elements)
# b = list (b)
# print(b)

# Using loops

# a = [5, 10, 15, 20, 25, 20, 5, 4, 10]
#
# b = []
#
# for i in a:
#     if i not in b:
#         b.append(i)
# print (b)

#----------------------------------------------------------------------------------------------------------------------#

# Reverse a sentence

# test_string = "this is a test"
#
# result = tests_tring.split(" ")
# reverse = result[::-1]
# print(reverse)

# def reverse_func():
#     user_input = input("Enter the sentence to be reversed: ")
#     user_input = str(user_input)
#
#     result = user_input.split(" ")
#     reverse = result [::-1]
#     reversed_word = " ".join(reverse)
#     print(reversed_word)
#
# reverse_func()

#----------------------------------------------------------------------------------------------------------------------#

# Password generator
# import string
# from random import *
#
# # print (string.ascii_letters)
# # print(string.digits)
# # print(string.punctuation)
#
# characters = string.ascii_letters + string.digits + string.punctuation
# password = "".join(choice(characters) for x in range (randint(8,16)))
# print (password)


# import random
# import string
#
# characters = string.ascii_letters + string.digits + string.punctuation
# passlength = 8
# #password = "".join(random.sample(characters,passlength))
# new = random.sample(characters,passlength)
# password = "".join(new)
# print (password)

#----------------------------------------------------------------------------------------------------------------------#

# Decode a web page

# import requests
# from bs4 import BeautifulSoup
#
# base_url = "http://www.nytimes.com"
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text, 'html.parser')
#
# for story_heading in soup.find_all('p'):
#     if story_heading.a:
#         print(story_heading.string)
#     else:
#         print(story_heading.get_text())


import requests
r = requests.get("http://www.nytimes.com")
rraw = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(rraw, 'html.parser')

filename = "HeadLines.txt"

with open(filename, 'w') as f:
    for x in soup.find_all('p'):
        if x.string != None:
            f.write(x.string)
        else:
            f.write(x.get_text())



#----------------------------------------------------------------------------------------------------------------------#

# # import the requests Python library for programmatically making HTTP requests
# # after installing it according to these instructions:
# # http://docs.python-requests.org/en/latest/user/install/#install
# import requests
#
# # import the BeautifulSoup Python library according to these instructions:
# # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
# # use this syntax as described on the documentation page:
# # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup
# from bs4 import BeautifulSoup
#
# # the URL of the NY Times website we want to parse
# base_url = 'http://www.nytimes.com'
#
# # the syntax (according to the documentation) for how to
# # "load" a webpage through Python
# r = requests.get(base_url)
#
# # how to decode the text of the HTML of the NY Times homepage
# # website. r comes from the requests request above
# soup = BeautifulSoup(r.text, "html.parser")
#
# # find and loop through all elements on the page with the
# # class name "story-heading"
# for story_heading in soup.find_all(class_="story-heading"):
#     # for the story headings that are links, print out the text
#     # and format it nicely
#     # for the others, take the contents out and format it nicely
#     if story_heading.a:
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else:
#         print(story_heading.contents[0].strip())

#----------------------------------------------------------------------------------------------------------------------#

# # Cows and Bulls
#
# import random
#
# def compare_numbers(number, user_guess):
#     cowbull = [0,0] #cows, then bulls
#     for i in range(len(number)):
#         if number[i] == user_guess[i]:
#             cowbull[1]+=1
#         else:
#             cowbull[0]+=1
#     return cowbull
#
# if __name__=="__main__":
#     playing = True #gotta play the game
#     number = str(random.randint(0,9999)) #random 4 digit number
#     guesses = 0
#
#     print("Let's play a game of Cowbull!") #explanation
#     print("I will generate a number, and you have to guess the numbers one digit at a time.")
#     print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
#     print("The game ends when you get 4 bulls!")
#     print("Type exit at any prompt to exit.")
#
#     while playing:
#         user_guess = input("Give me your best guess!")
#         if user_guess == "exit":
#             break
#         cowbullcount = compare_numbers(number,user_guess)
#         guesses+=1
#
#         print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
#
#         if cowbullcount[1]==4:
#             playing = False
#             print("You win the game after " + str(guesses) + "! The number was "+str(number))
#             break #redundant exit
#         else:
#             print("Your guess isn't quite right, try again.")


# import tensorflow as tf
# mnist = tf.keras.datasets.mnist
#
# (x_train, y_train),(x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0
#
# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(input_shape=(28, 28)),
#   tf.keras.layers.Dense(512, activation=tf.nn.relu),
#   tf.keras.layers.Dropout(0.2),
#   tf.keras.layers.Dense(10, activation=tf.nn.softmax)
# ])
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# model.fit(x_train, y_train, epochs=5)
# model.evaluate(x_test, y_test)