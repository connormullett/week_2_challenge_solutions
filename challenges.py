
'''
Create 2 variables, divide the first by the second, and print the result
'''

# a = 12
# b = 6
# c = a / b
# print(c)

'''
take two inputs (name and age)
increate the age by 4, and print an interpolated string
ex: '(Name), you will be (AGE INCREASED) in 4 years'
'''

# name = input('Enter your name: ')
# age = input('Enter your age: ')

# age = int(age) + 4
# print(f'{name}, you will be {age} in 4 years')

'''
from 3 to 15 print all numbers that are divisible by 4
'''
# for i in range(3, 15):
#     if i % 4 == 0:
#         print(i)

# [print(i) for i in range(3, 15) if i % 4 == 0]  # list comprehension

'''
from the nested loop, print the statement that will return the number 3
'''
# my_list = [(-1, 0), [1, 2, [3, 4], ], ]  # 3 is inside a list, inside of a list, inside of another list
# print(my_list)  # [(-1, 0), [1, 2, [3, 4]]]
# print(my_list[1])  # [1, 2, [3, 4]]
# print(my_list[1][2])  # [3, 4]
# print(my_list[1][2][0])  # 3

'''
create a variable that tkaes an input and parses into an int
using an exception handler, if the user input something that isnt a number
print please enter a number, make sure the program doesnt break because of the error
'''

# try:
#     user_input = input('Enter a number: ')
#     int(user_input)
#     print('That was a number')  # this will only execute when there was no error
# except:
#     print('Please enter a number, you doof')  # this will execute if there was an error
# finally:  # this will ALWAYS run after the try or except statement
#     print('This is the finally block')
# print('program is done')  # show that the error was handled

'''
using the list supplied grab and print the name and age of each person
IF they are 33 or older, use f strings
'''

# people = [
#         {  # the first person in the loop below
#             'name': 'Thomas Bakersfield',
#             'age': 32,
#         },
#         {  # the second person in the loop
#             'name': 'Beth Harrison',
#             'age': 23
#         },
#         {  # the third person in the loop
#             'name': 'Yyvon Usra',
#             'age': 51
#         },
#         {
#             'name': 'William Williamson',
#             'age': 33
#         }
#     ]

# for person in people:
#     if person['age'] >= 33:
#         print(f"the persons name is {person['name']}, and the persons age is {person['age']} years old")

