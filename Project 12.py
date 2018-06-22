# Exercise 12
# Write a program that takes a list of numbers 
# and makes a new list of only the first and last elements of the given list.

a = [5, 10, 15,15,2,5, 20, 25]
b=[]

b.append(a[0])

b.append(a[-1])

print (b)

# Inside a function

def first_and_last(a):
    return [a[0], a[-1]]

first_and_last(a)