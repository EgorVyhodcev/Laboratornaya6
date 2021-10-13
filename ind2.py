word1, word2 = input("Enter the two words: ").split()
if word1 == word2:
    print("All of the characters from these words are the same!")
    exit(0)
else:
    k = 0
    for i in range(len(word1)):
        if word1[i] in word2[i]:
            k += 1
        else:
            break
print(f"There are {k} of the same first letters in these two words")
