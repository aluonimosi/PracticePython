a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [i for i in a if i%2 == 0]

print (b)

# to creat a random list for this project

a = random.sample(range(1,1000), 10)

b = [i for i in a if i%2 == 0]

print(a)
print (b)