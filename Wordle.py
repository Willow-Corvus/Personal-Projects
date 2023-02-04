#Import Utilities
import random
#Generates a random number to choose a word
randoms = random.randrange(1,32)
#Players number of guesses
guess = 0
#Chooses a random word for the wordle
def chooseWord():
    if(randoms == 1):
        wordle = "catch"
    elif(randoms == 2):
        wordle = "hatch"
    elif(randoms == 3):
        wordle = "batch"
    elif(randoms == 4):
        wordle = "slice"
    elif(randoms == 5):
        wordle = "ample"
    elif(randoms == 6):
        wordle = "foyer"
    elif(randoms == 7):
        wordle = "flair"
    elif(randoms == 8):
        wordle = "aloud"
    elif(randoms == 9):
        wordle = "inept"
    elif(randoms == 10):
        wordle = "waltz"
    elif(randoms == 11):
        wordle = "flout"
    elif(randoms == 12):
        wordle = "clout"
    elif(randoms == 13):
        wordle = "sneak"
    elif(randoms == 14):
        wordle = "grove"
    elif(randoms == 15):
        wordle = "spade"
    elif(randoms == 16):
        wordle = "equal"
    elif(randoms == 17):
        wordle = "ionic"
    elif(randoms == 18):
        wordle = "valid"
    elif(randoms == 19):
        wordle = "enjoy"
    elif(randoms == 20):
        wordle = "sloth"
    elif(randoms == 21):
        wordle = "snake"
    elif(randoms == 22):
        wordle = "kazoo"
    elif(randoms == 23):
        wordle = "baron"
    elif(randoms == 24):
        wordle = "baton"
    elif(randoms == 25):
        wordle = "bento"
    elif(randoms == 26):
        wordle = "brain"
    elif(randoms == 27):
        wordle = "robin"
    elif(randoms == 28):
        wordle = "abort" 
    elif(randoms == 29):
        wordle = "morel"
    elif(randoms == 30):
        wordle = "motel"
    elif(randoms == 31):
        wordle = "total"
    elif(randoms == 32):
        wordle = "metro"    
    else:
        wordle = "Null Value"
    
    return wordle

#Sets a global variable that runs a function to choose a word
wordle = chooseWord()

#Plays the game     
def play(mode):
    global wordle
    #Sets how many guesses a person has on easy mode
    if(mode.lower() == "easy"):
        
        guess = 20
    #Sets how many guesses a person gets on medium    
    elif(mode.lower() == "medium"):
        
        guess = 10
    #Secret mode that sets the game to Hatsune Miku Mode with the word being "Miku " and the guesses being 11
    elif("miku" in mode.lower() ):
        print("\n\n\n")
        print("　　 　 　  /＾&gt》,_____＜＾\\")
        print("　　　　　 /:::::/,≠´::::_;ヽ.:\\")
        print(".　　　　 /:::::〃::/|::ノ:ハ:::\\")
        print("　　　　 /::::::{|／ |ノ   |:|:::\\")
        print("　 　 　/::::::瓜イ● ´  ● ﾉ:ﾉ:::::\\")
        print(". 　 　/::::::|ﾉﾍ|､ っ  ノ:ﾉﾉ::::::\\")
        print("　　　/:::::::| /|｀不´|'   |:::::::\\")
        print("\n\n\n")
        print("Welcome to Hatsune Miku mode\n\n")
        
        wordle = "Miku "
        guess = 11
    #Sets how many guesses a person gets on hard Mode    
    else:
        
        guess = 6
    #How many guesses the player has taken on this iteration of the game
    player_guesses = 0
    #Loops the game 
    while(True):
        #Asks for an input that is 5 characters long
        while(True):
            #User input guess
            word_guess = input("Enter your guess\n")
            #Checks if the word is 5 characters long
            if(len(word_guess) == 5):
                break
        #Prints the hint after you guess    
        print(check(word_guess))
        #Adds to player guess count  
        player_guesses += 1
        #Breaks the loop if the guess is correct
        if(check(word_guess)==wordle):
            print("\n\nThe word was " + wordle + "\n\nIt took you " + str(player_guesses) + " guesses")
            break
        #Breaks the loop if number of guesses are exceeded
        if(player_guesses == guess):
            print("\n\nYou ran out of guesses the word was " + wordle)
    #Loops to prevent invalid inputs    
    while(True):
        #User input to play again
        play_again = input("Play again\nPlay or End\n")
        #Restarts game
        if(play_again.lower() == "play"):
            start_game()
            break
        #Ends game
        elif(play_again.lower() == "end"):
            break    
    
    
             
#Checks the guess against user input
def check(word_guess):
    global guess
    awnser = ""
    #Uses iteration over a string to see if it is a correct awnser
    for i in range(len(word_guess)):
        lt = word_guess[i:i+1] 
        #If letter is correct spot and letter       
        if(lt == wordle[i:i+1]):
            awnser += lt
        #Letter is in wrong spot     
        elif(lt in wordle):
            awnser += "~"
        #There is no letter in the word    
        else:
            awnser += "_"
    #Returns a statment that tells hints you towards the correct awnser          
    return awnser        
                
#Function to run the game   
def start_game():
    #Welcome message
    print("Welcome to Wordle\nDisplay the Rules or continue")
    
    #While loop to allow people to play multiple times
    while(True):
        #Intro
        rule = input("Read the rules\nYes or No\n")
        #Rules
        if(rule.lower()=="yes"):
            print("1. Type a 5 letter word")
            print("2. If there is a letter in the word it will display and ~\n     If it is in the correct space it will display the letter in the correct place\n          If it is not in the correct space or a letter it will display _")   
            print("3. There are three mode easy, medium, and hard\n     easy 20 guesses\n     medium 10 guesses\n     hard 6 guesses")
        break
    
    #Select gamemode(Secret gamemode Miku)
    mode = input("Select your difficulty\nEasy,Medium,Hard\n")
    
    #Where the guessing occurs
    play(mode)
    

#Where it starts   
start_game()