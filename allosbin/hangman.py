import random
hangman = ['''
               +=======+
               |       |
               O       |
                       |
                       |
                       |
                       |
                       |
                       |
              +========+ ''','''
              +========+
              |        |
              O        |
              |        |
                       |
                       |
                       |
                       |
                       |
              +========+ ''','''
              +========+
              |        |
              O        |
              |        |
             /|\       |
                       |
                       |
                       |
                       |
             +=========+''','''
             +=========+
              |        |
              O        |
              |        |
             /|\       |
            / | \      |
                       |
                       |
                       |
             +=========+''','''
             +=========+
              |        |
              O        |
              |        |
             /|\       |
            / | \      |
              |        |
                       |
                       |
             +=========+''','''
             +=========+
              |        |
              O        |
              |        |
             /|\       |
            / | \      |
              |        |
              |        |
                       |
             +=========+''','''
             +=========+
              |        |
              O        |
              |        |
             /|\       |
            / | \      |
              |        |
              |        |
             / \       |
             +=========+''']
word_to_guess = ['t', 'o', 'r', 'r', 'e', 'n', 't']
guesses = []
tries = 8
while tries < 9:
    print('The word to guess is: t _ r _ _ _ t')
    guess = input('Your first guess: ')
    if guess in word_to_guess:
        guesses.insert(0, guess)
        print('Correct!')
    else:
        print(hangman[0])

    guess = input('Your Second Guess: ')
    if guess in word_to_guess:
        guesses.insert(0, guess)
        print('Correct')
        print(guesses)
    else:
        print(hangman[1])

    guess = input('Your Third Guess: ')
    if guess in word_to_guess:
        guesses.insert(0, guess)
        print('Correct!')
    else:
        print(hangman[2])

    guess = input('Your Fourth Guess: ')
    if guess in word_to_guess:
        guesses.insert(0, guess)
        print('Correct you are!')
    else:
        print(hangman[3])

    guess = input('Your Fifth Guess: ')
    if guess in word_to_guess:
        guesses.insert(0, guess)
        print('Correct Sir!')
    else:
        print(hangman[4])

    guess = input('Your Sixth Guess: ')
    if guess in word_to_guess:
        guesses.insert(0, guess)
        print('Correctly Guessed mate!')
    else:
        print(hangman[5])

    guess = input('Your Last Guess: ')
    if guess in word_to_guess:
        guesses.insert(0, guess)
        print('Correct')
    else:
        print(hangman[6])

    for guess in guesses:
        if guess in word_to_guess:
            print('You have guessesd ', len(guesses), 'words Correctly')
            break
        else:
            print('Sorry but you are to dumb to play this game, YOU ARE OUT!')
            break
