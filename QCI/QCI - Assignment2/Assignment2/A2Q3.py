def forbidden_word(word):
    forbidden_letters = ['a', 'e', 'i', 'o', 'u']
    for letter in forbidden_letters:
        if letter in word:
            return (f'you cant use the word {word} because it contains the letter {letter}')
        elif letter.upper() in word:
            return (f'you cant use the word {word} because it contains the letter {letter.upper()}')
    return (f'you can use the word {word} because it does not contain any forbidden letters')

# Get input from user
word = input("Enter a word: ")
print(forbidden_word(word))