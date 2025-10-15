import random 

words = ['Python', 'java', 'kotlin', 'javascript','ruby','html','go']
word = random.choice(words)

print(word)

jumble = "".join(random.sample(word,len(word)))


chances = 5
print("~"*20)
print("Welcome to Jumble Bumble")
print("~"*20)

while chances!=0:
    print("The word is",jumble)
    guess = input("Enter your guessed word: ",).lower()
    if guess == word:
        print("You won!")
        print()
        break
    else:
        chances -= 1
        print("Incorrect Guess!!")
        print("Remaining chances:",chances)
        print()
else:
    print("All you chances are exhausted")
    print("You lose")
    print("The correct word is:",word)


print("Thank you for playing!!")