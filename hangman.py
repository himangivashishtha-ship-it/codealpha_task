import random

words = ["python", "apple", "india", "coding", "laptop"]
word = random.choice(words)

guessed = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_guesses:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed.append(guess)
    else:
        wrong_guesses += 1
        print("Wrong guess! Attempts left:", max_guesses - wrong_guesses)

if wrong_guesses == max_guesses:
    print("Game Over! The word was:", word)
