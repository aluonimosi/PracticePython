#A solution using string reversal

word = "hannah"

for i in word:
    print (i)
    
print ("the forwards is ", word)
rvs = word[::-1]
print ("the backwards is ", rvs)

if word == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
    
# A solution using for loops

word = "hanna"

def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
        return x

x = reverse(word)
if x == word:
        print("This word is a palindrome")
else:
    print("This word is not a palindrome")