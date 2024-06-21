import random

words = ['python', 'bubble', 'javascript', 'game']

# Randomly chose a word from the words list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 8

print("Welcome to Hangman game!")
print("You have 8 attempts to guess the word.")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("The letter you guessed is not in the word!! Try again!!")
        attempts -= 1

if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You win the game!!")
else:
    print("You ran out of attempts!!")
    print("You lost!! Now you will be hanged!!")
