def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter.lower())
        
        # Build display string
        display = ""
        all_guessed = True
        for char in secret_word:
            if char.lower() in guesses:
                display += char
            else:
                display += "_"
                all_guessed = False
        
        print(display)
        return all_guessed
    
    return hangman_closure

# Mainline implementation
if __name__ == "__main__":
    word = input("Enter the secret word: ").strip()
    game = make_hangman(word)
    
    won = False
    while not won:
        guess = input("Guess a letter: ").strip()
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        won = game(guess)
        
    print("Congratulations! You guessed the word.")