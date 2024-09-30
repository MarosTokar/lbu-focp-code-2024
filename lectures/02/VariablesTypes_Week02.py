total = 100

total = total + 99
print("The Total IS:", total)

total -= 1
print("The total is", total)

total *= 4
print("The total is", total)

total /= 2
print("The total is", total)

total = 90.2
count = 5

# add your extra code here
sum = total + count

average = sum / 2
print("The Average Is", average)

# Results From Python Interpreter
# >>> type(False)
# <class 'bool'>
# >>> type(1000)
# <class 'int'>
# >>> type(100.111)
# <class 'float'>
# >>> type("Hello")
# <class 'str'>
# >>> type(True)
# <class 'bool'>
# >>> type(100 / 5)
# <class 'float'>
# >>> type(100 // 5)
# <class 'int'>

# >>> "ABC" * 10
# 'ABCABCABCABCABCABCABCABCABCABC'

name = "MarosTokar"
address = "123 Street Lane"
contact = "0123456789"

print("Your Name Is", name, "It Is", len(name), "Characters Long")
print("Your Address Is", address, "It Is", len(address), "Characters Long")
print("Your Contact Is", contact, "Is Is", len(contact), "Characters Long")

# TASK: Input the following code, when asked to type your age input a numeric value such as 20.
# Does this program work? If not, why?
# age = input("Enter your age ")
# print("in one year your age will be", age + 1)
# The program is trying to add an integer to a string

# value1 = input("Enter your first value: ")
# value2 = input("Enter your second value: ")
# value1 = int(value1)
# value2 = int(value2)
# print(value1, "*", value2, "=", value1 * value2)

# TASK: Try writing the above assignment statement but only use double quotes instead of single
# quotes as the string delimiter. What is the result?
# >>> comment = "I would have "thought" you knew better!"
#   File "<stdin>", line 1
#     comment = "I would have "thought" you knew better!"
#                              ^^^^^^^
# SyntaxError: invalid syntax
# >>>


# TASK: Write some code that calls a print() function, which takes a single string argument that results in the
# following text being displayed (exactly as shown).
print("This text includes characters such as '\\' \t\n\t'\"' \t\n\t\t'\'' ")

# TASK: Write some code that calls a print() function, which takes a single string argument that results in the
# following text being displayed (exactly as shown).

slash = "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
print(slash, "\n Hello There! \n", slash)

# TASK: Write some code that calls a print() function, which takes a single string argument that results in the
# following text being displayed (exactly as shown). Do this without the use of any escape sequences.

print("""This text spans three lines, \n and includes both single ('), \n and double quotes ("). """)

# TASK: Rewrite the above example, so that the third letter of the ‘surname’ is accessed rather than the first,
# then print this letter to the screen.

surname = "Palin"
initial = surname[2]
print(initial)

# TASK: Rewrite the above example, so that the tenth letter of the ‘surname’ is accessed, and note the result.

# surname = "Palin"
# initial = surname[9]
# print(initial)

# String index out of range \ Process finished with exit code 1

# TASK: Rewrite the above example, so that the second from last letter of the ‘surname’ is accessed rather than the last
# ,then print this letter to the screen.

surname = "Palin"
last = surname[-2]
print(last)


# TASK: Rewrite the above example, so that all the characters of the ‘surname’ except the first character are sliced
# and then displayed on the screen.

surname = "Palin"
middle = surname[1:5]
print(middle)

# TASK: Write code that accesses and prints all characters of  the ‘surname’ except the last character.

surname = "Palin"
middle = surname[:4]
print(middle)

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Write code that uses slicing to access then print the first four prime numbers defined within the ‘primes’ list given
# above. Note: you will have to input that list first for testing purposes.

print(primes[0:4])

# TASK: Write code that uses slicing to insert two new names just before the final name within the  ‘names’ list.

names[5:5] = ["Tom", "Jerry", "Timothy"]
print(names)

names.append("Jim")
print(names)

names = names + ["Mark"]
print(names)

names += ["Jacob"]
print(names)


