
# - Open the file below, and parse the document into a list of each item.
# - Create a class that the data above could be further parsed into, and create a list of the class instances. (first name, last name, age, hobby)
# The class should have an introduction method that returns the string below.
# "(NAME) is (AGE) years old, and has a hobby of (HOBBY)"


class Person:

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def introduction(self):
        return f'{self.name} is {self.age} years old, and their hobby is {self.hobby}'


people = []
with open('people.txt', 'r') as f:
    for row in f.read().split('\n'):  # reads the file and splits by newlines
        row = row.split(',')  # .split on a string, turns string into a list that we split by
        people.append(row)

del people[-1]

people_instances = []
for person in people:
    person = Person(person[0], person[1], person[2])
    people_instances.append(person)

for person in people_instances:
    print(person.introduction())

