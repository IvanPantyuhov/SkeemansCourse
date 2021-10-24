from random import choice

WORDS = ['rabbit', 'computer', 'samsung']
word = choice(WORDS).lower()
lives = 7
guessed_letters = []

while True:
    for c in word:
        if c in guessed_letters:
            print(c.upper(), end=' ')
        else:
            print('_', end=' ')
    print()
    print(f'Lives left: {lives}')
    print(f'Guessed Letters {guessed_letters}')

    guess = input("Enter the letter: ").lower()
    if len(guess) != 1:
        print('The letter should be only with 1 symbol')
        continue
    if not guess.isdigit():
        print('The letter should be only with 1 symbol')

    guessed_letters.append(guess)
    if guess in word:
        print('You guessed')
    else:
        lives -= 1
        print("You are wrong")
    if len(set(guessed_letters) & set(word)) == len(set(word)):
        print(f"You won. Word {word} is correct!")
        break
    elif lives == 0:
        print(f"Game over! You out of lives. The word was {word}")
        break



