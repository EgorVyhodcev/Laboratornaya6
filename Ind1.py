word = input("Enter the word: ")
k = len(word)
print(f"The length of this word is: {k}")
word = k * '*' + word + k * '*'
print(word)
