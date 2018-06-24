# Exercise 14
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Solution One: Loop and construct a list

a = [1, 1, 2, 3, 3, 5, 8, 13, 21, 34, 34, 55, 89]
b=[]

for i in a:
    if i not in b:
        b.append(i)
        
print(b)

# Solution Two: use sets

a = [1, 1, 2, 3, 3, 5, 8, 13, 21, 34, 34, 55, 89]

b = list(set(a))

print(b)