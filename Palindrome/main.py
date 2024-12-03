

x = ""
# x's value is the word you will be checking, change to whatever word you'd like
list = []
# creating an empty array that will store the letters of the word being checked


for i in x.lower():
    list.append(i)
# adds each letter of the word into the list previously created
print(list)

reversed_word = list[::-1]
# uses slicing to slice the contents of the previous list in reverse order, effectively reversing the list
print(reversed_word)
if reversed_word == list:
# checks if new reversed list has the same contents as the original's
    print(f"{x} is a palindrome!")
else:
    print(f"{x} is not a palindrome. Try again") 

