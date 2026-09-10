## This is a Python Syntax review hand typed for muscle memory and growth

# fundamentals and variables.
name = "Alexander"
age = 34
height_cm = 173.5
is_learning = True
nothing = None

print(f'{name} is {age} years old and {height_cm} cm tall')

# basic numerical operations:
a= 17
b = 5
print('To add', a+b)
print('to subtract', a-b)
print('to multiplay', a*b)
print('to Divide', a/b)
print('Floor divide', a//b)
print ('Modelo Division', a%b)
print('exponants', a**2)

# Augmentation
score = 10
score += 5
score -= 1
score *= 3
print('final score is ', score)
# Remember the augmentations can be use for iterations as well

# Comparison and Logic
x = 10
y = 20
print (x<y and y>0) 
print(x==y or y !=0)
print(not (x>y))
# you should know the answer to all the above.

# strings and their respective methods:
sentence ="Who are you, I'm from ancient Greece!!"
print(sentence.strip())
print(sentence.lower())
print(sentence.upper())
print(sentence.strip().replace('Greece','Rome'))
print(len(sentence))

#fstring and formatting

pi = 3.14159265 #approx
print(f'Pi rounded is {pi:2f}')
print(f"Padded number: {7:04d}") #a reminder of what padded numbers are.

# Slicing:
word = "Analytics"
print(word[0])
print(word[-1])
print(word[0:4])
print(word[::-1])
# remember that all strings function as lists as well, and indexing.

line = "id,name,score"
fields = line.split(',')
print(fields)
rejoin = '-'.join(fields)
print(rejoin)

#tuples and sets

locations =(11.3,20,3)
x_cord, y_cord = locations
print(f"{x_cord},{y_cord}")

try:
    locations[0] = 99
except TypeError as e:
    print("You know why", e)

tags_uni = {'Rust',"Rust",'Aqua',"Popcorn"}
print(tags_uni)

tags_uni.add('Love')
tags_uni.discard('Aqua')

set_a = {1,2,3,4}
set_b = {3,4,5,6}
print('union', set_a | set_b)
print('Intersection', set_b & set_b)
print('Difference,', set_a - set_b)

# Dictionaries:

person = {
    "name": "Mania",
    "stratagy": "Focus and love",
    "exp" : 232,
    "skills": ['Focus','love','beauty']
}

print(person["name"])
print(person["stratagy"])

person["exp"] += 21
person["level"] = 3
print(person)

for key in person:
    print(key,"->" , person[key])

for key, value in person.items():
    print(f"{key}: {value}")

#Dict comprehension
squared_map = {n: n**2 for n in range(1,6)}
print(squared_map)

# Conditionals

exp = 1222

if exp < 300:
    rank = "Beginner"
elif exp < 1000:
    rank = "Apprentice"
elif exp < 2000:
    rank = "Expert"
else:
    rank = "Master"

print(f"Your rank is {rank}")

#Ternary expression

status = "active" if exp > 0 else "Inactive"
print(status)

#loops and iteration:

for i in range(6):
    print("loop Iternation, ", i)

count = 0
while count <3:
    print("we are counting, ", count)
    count +=1

# Loop Contorl:
for n in range (10):
    if n ==3:
        continue
    if n ==7:
        break
    print('"Filtered n: ', n)

# Enumirate and Zip:
tracks = ["logic", "math", "stratagy"]
for index, track in enumerate(tracks, start=1):
    print(f"{index}, {track}")

exp_values= [232,122,212]
for track, exp in zip(tracks, exp_values):
    print(f"{track}: {exp} EXP")

# Functions and forms

def greet(person_name):
    return f"Hello, {person_name}"

print(greet('Union'))

def add_exp(current, amount= 50):
    return current + amount

print(add_exp(1000))
print(add_exp(1000,200))

def summerize_tracks(*tracks):
    return f"You are tracking {len(track)} skills: {', '.join(tracks)}"

print(summerize_tracks ("SQL","PYTHON","EXCEL"))

def build_profile(**details):
    for key, value in details.item():
        print(f"{key}: {value}")

build_profile(name= 'Fahad', city = "Vermont", focus = "Coding")

def is_it_odd(n):
    if n%2 ==0:
        return "no"
    return "yes"

result = [is_it_odd(n) for n in range(6)]
print(f'is{n} odd?, {result}')

#Lambda Functions:
double = lambda n: n*2
print(double(20))

sort_by_length = sorted(tracks, key=lambda t: len(t))

def safe_divider(numer, demo):
    try:
        result = numer/demo
    except ZeroDivisionError:
        print('we do not divide by zero, silly')
        return None
    else:
        ('It has been divided')
        return result
    finally:
        print("Dividing has ended")

print(safe_divider(10,2))
print(safe_divider(10/0))

# File I/0:

with open('sample_output.txt', "w") as f:
    f.write('what file? it was written in the practice\n')
    f.write("this is line number 2.\n")

with open('sample_output.txt', "r") as f:
    content = f.read()

print(content)

#------------------
#   E  N  D
#------------------


