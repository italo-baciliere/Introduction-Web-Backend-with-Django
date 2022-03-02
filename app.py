# PYTHON BACKEND WEB DEVELOPMENT COURSE (WITH DJANGO)
#https://www.youtube.com/watch?v=jBzwzrDvZ18




# VARIABLES
# name = 'Ítalo'
# age = 24
# print('Hello Word',100)
# print(name,'é do Brasil')
# print(name + '\nIdade:',age)




# STRING
# print('Hi.\nHow are you?')
# print(name.upper())
# print(name.isupper())
# print(name.lower())
# print(name.islower())
# print(name[0])
# print(len(name))
# print(name.index('Í'))
# print(name.replace('Í','í'))




# Numbers
# number = 78
# print(78)
# print(number + 22)
# print(number + 22.432)
# print(number%7)
# print('number is ' + str(number))
# print(abs(-5))
# print(max(4,2, 3, 16))
# print(min(4,2, 3, 16))
# print(round(3.5))
#
# from math import *
# print(bin(334))
# print(sqrt(100))




# GETTING USER'S INPUT
# name = input('Input your name: ')
# age = int(input('Input your age: '))
# print('User name',name, 'and you are ',age,'years old')




# BUILDING A SIMPLE WORD REPLACEMENT PROGRAM
# sentence = input('Enter your sentence: ')
# print(sentence)
# word = input('Enter the word to replace: ')
# replace = input('Enter the word to replace it with: ')
# print(sentence)
# print(sentence.replace(word,replace))




 # LIST IN PYTHON
# countries = ['Brasil', 'Ghana', 'Nigeria', 'Australia']
# print(countries[0])
# print(type(countries))
# print(len(countries))
# print(countries[1:])
# print(countries[1:3])
# countries[3] = 78
# print(countries)
# list = list(('Nigeria', 34, False))
# print(list)




# LIST METHODS
# list1 = [1, 2, 3, 4, 5]
# print(list1)
# list1.reverse()
# print(list1)
# list2 = ['banana', 'apples', 'mango', 'oranges']
# print(list2)
# list2.append('Cherry')
# print(list2)
# list2.insert(1, 'juice')
# print(list2)
# print(list2.index('mango'))
# list2.append('mango')
# print(list2.count('mango'))
# list2.remove('banana')
# print(list2)
# list2.clear()
# print(list2)
# print(len(list2))
# list1.extend(list2)
# print(list1)
# list3 = list1.copy()
# print(list3)
# list1.pop()
# print(list1)
# list4 = ['dino', 'dinos']
# del list4[0]
# print(list4)




# TUPLES

# three_numbers = (1, 2, 3)
# strings = ('home', 'land', 'earth')
# boo = (True, False, True)
# tuples = (True, 'land', 2)
# print(three_numbers)
# print(three_numbers[2])
# # three_numbers[0] = 2 # error
# print(len(three_numbers))
# print(type(three_numbers))
# print(tuples)




# FUNCTIONS

# def greetings_function(name,age,*names):
#     print('Welcome', str(name),'\nYou are',age,'years old')
#     print("here is the names of your friends:",names)
#
# names = ['Lucas', 'John', 'Katrin']
#
# greetings_function('Ítalo',23,names)




# THE RETURN KEYWORD

# def return_function(number1, number2): # statement
#     return number1 + number2
#
# num1 = int(input("Number 1:"))
# num2 = int(input("Number 2:"))
#
# print(return_function(num1,num2))




# IF STATEMENTS

# a = 2
# b = 3
#
# if a > b:
#     print(a,'is greater than',b)
# elif a < b:
#     print(a,'is less than',b)
# else:
#     print(a,'is equal',b)


# value = input('Input a value:')
#
# if type(value) == str:
#     print(value,'is a string')
# elif type(value) == int:
#     print(value,'is a integer')
# elif type(value) == list:
#     print(value,'is a list itens')
# else:
#     print('We don\'t know the data type of',value)


# value = input('Input a value: ')
#
# if type(value) == str:
#     print(value,'is a string')
# else:
#     print(value,'is not a string')




# BUILDING A PYTHON PROGRAM TO CHECK
# IF A NUMBER IS AN EVEN NUMBER

# number = int(input('Enter a number:'))
#
# if number%2 == 0:
#     print('Even number')
# else:
#     print('Odd number')




# DICTIONARIOS IN PYTHON

# dict = {
#     'name': 'Baciliere',
#     'name': 'Ítalo',
#     'age': 24,
#     'nationality': 'Brazil',
#     'friends': ['Peter', 'Marta', 'Precious']
# }
#
# print(dict)
# print(dict['age'])
# print(dict['name'])
# print(len(dict))




# WHILE LOOPS IN PYTHON

# i = 1
#
# while i < 6 or i == 10:
#     print(i)
#     i += 1




# FOR LOOPS IN PYTHON

# for letter in 'Ítalo':
#     print(letter)


# my_list = ['ji', 'ju', 'jo']
# for sentence in my_list:
#     print(sentence)


# dict = {
#     'name': 'Baciliere',
#     'name': 'Ítalo',
#     'age': 24,
#     'nationality': 'Brazil',
#     'friends': ['Peter', 'Marta', 'Precious']
# }
# for value in dict:
#     if(value == 'age'):
#         print('value',dict[value])
#     elif(value == 'nationality'):
#         print('nationality',dict[value])
#         break


# for x in range(3, 7):
#     print(x)

# for x in range(7):
#     print(x)
# else:
#     print('Finished Looping!')




# 2D LISTS AND NESTED LOOPS IN PYTHON

# dimensional list
# list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(list)
# print(list[2])
# print(list[1][2])
#
# for lst in list:
#     for item in lst:
#         print(item)




# COMMENTS IN PYTHON

# one line

'''
block of comments
:*
'''



# BUILDING A BASIC CALCULATOR

# value1 = int(input('Enter first number: '))
# operation = str(input('Enter operator: '))
# value2 = int(input('Enter second number: '))
#
# if operation == '-':
#     print(value1 - value2)
# elif operation == '+':
#     print(value1 + value2)
# elif operation == '/':
#     print(abs(value1 / value2))
# elif operation == '*':
#     print(value1 * value2)
# else:
#     print('Invalid operation!')




# ABS() PYTHON

# link: https://programadorviking.com.br/abs-python-como-obter-o-valor-absoluto-guia-completo/
# int_number = -20
# print('Valor absoluto de',int_number,':',abs(int_number))
#
# float_number = -30.33
# print('Valor absoluto de',float_number,':',abs(float_number))
#
# complex = (3 - 4j)
# print('Magnitude de', complex,':',abs(complex))




# TRY EXCEPT IN PYTHON

# try:
#     x = int(input('Input an integer: '))
#     print(x)
# except ValueError:
#     print('Value not a integer')
# except:
#     print('Something went wrong... Please try again')
# else:
#     print('nothing went wrong')
# finally:
#     print('try except finished')




# READING FILES

# r -read
# w - write
# a - append
# r+ - both reading and writing
# file = open('countries.txt', 'r')

#print('Documente is readable:',file.readable())
#print(file.read())
#print(file.readline()) # read one line
#print(file.readlines())
# for line in file.readlines():
#     print(line)

# file.close()




# WRITING FILES

# file = open('countries.txt', 'a')
# file.write('\nChina')
# file.close()

# create a new file
# file = open('new_file.py', 'a')
# file.write('print(\'This is a new file\')')




# CLASSES AND OBJECTS IN PYTHON

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class People:
#     pass
#
# person = Person('Ítalo', 24)
# print(person.name)
# print(person.age)
# del person.age
# print(person.age)




# INHERITANCE IN PYTHON

# from new_file import Student
#
# class Person(Student):
#     pass
#
# p1 = Person()
# print(p1.name)




# THE PYTHON SHELL

# command
# print('Hope you are enjoying this tutorial?')
# name = 'Tim'
# print(name)
# for letter in 'Tim':
#     print(letter)
# class Person():
#     name = 'John'
# p1 = Person()
# if p1.name == 'John':
#     print('Yes it is')
# def say_hi(name):
#     print('Hi',name)
# say_hi('John')
# try:
#     age = int(input('Enter age:'))
# except:
#     print('except occurred')




# BUILDING A SIMPLE LOGIN AND SIGNUP SYSTEM

# class Account:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
# user = Account('', '')
#
# while user.username == '' or user.password == '':
#     try:
#         print('Create your account')
#         username = input('Input username: ')
#         password = input('Input password: ')
#         user = Account(username, password)
#     except:
#         print('except occurred')
#     finally:
#         print('user \'admin\' created successfully\n')
#
# print('Login now')
# input_username = input('Input username: ')
# input_password = input('Input password: ')
# if input_username == user.username and input_password == user.password:
#     print('Logged in successfully')
# else:
#     print('Invalid credentials')




# (3:31:04) MODULES AND PIP IN PYTHON

import new_file
new_file.say_hi()

# pip install django-deep-serializer

