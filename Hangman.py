#Hangman:Beginner level

#welcome the user
name = input("What is your name: ")
print("Welcome "+ name + ", can you guess my word" )

#Secret Word
word = "amazing"

#number of guesses
guesses = ""

#number of turns
turns = 10

while turns > 0:
    #make a counter that starts with zero.Just a flag.
    failed = 0
    
    #for every character in secret_word
    for char in word:

        #print tif the character is in the players guess
        if char in guesses:
            #print the character on the screen
            print(char)
        #if not 
        else:
            #print nothing and add to failed attempts
            print("_")
            failed += 1
    #if you failed 0 times you won  
    if failed == 0:
        print("You won")

        break
    
    print()
    guess = input("guess a character:")
    guesses += guess
    #if the geuss is not in word
    if guess not in word:

        turns -= 1
        print("Wrong Guess")
        print("You have", + turns,'more guesses')

        if turns == 0:

            print("You Lose")

