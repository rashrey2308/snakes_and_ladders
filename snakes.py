import random

snakes={17 : 7, 54 : 34, 62 : 19, 98 : 79}
ladders={3 : 38, 24 : 33, 42 : 93, 72 : 84}

player1_position=0
player2_position=0

step=0
mode=0

def random_number_generator():  #used to generate a random number b/w 1 to 6 for auto mode
    return random.randint(1,6)

def select_mode(): #Accepts user's choice of mode    
    global mode
    mode = input('''This game supports two modes: 
    1. Auto Mode: In this mode the computer will generate a random number between 1 to 6 after you type \"Roll\"
    2. Manual Mode: In this mode you have to enter a number between 1 and 20
    Enter 1 for Auto Mode and 2 for Manual Mode: ''')
    while(True):
        if mode=='1' or mode=='2':  #A check for valid mode
            break
        mode=input("Invalid Input: Please enter 1 for Auto Mode and 2 for Manual Mode ")
            
    mode=int(mode)        

def checkchoice(choice):  #Checks if the user's input is valid according to the chosen mode
    global step
    if mode==1:
        while True:
            if choice.lower()=='roll':  
                break
            else:
                choice=input('Invalid input: Enter "Roll": ')
        step=random_number_generator()

    else:
        while True:
            try:
                choice=int(choice)
                if choice<1 or choice>20:
                    choice=input("Invalid Input. Enter a number between 1 and 20: ") 
                else:
                    step=choice
                    break    
            except ValueError:
                choice=input("Invalid Input. Enter a number between 1 and 20: ")        


def player_move(player_num):  #Accepts the user's input according to the chosen mode
    print("Player ",player_num,":", end=" ")
    choice=input()
    checkchoice(choice)
    print("You got a ",step)


def check_for_snakes_and_ladders(new_position):  #Checks if there is a snake or ladder present at the user's updated position
    if new_position in snakes:
        print("Oh no! You got bit by a snake")
        return (snakes[new_position])            #Returns the new position after snake has been encountered
    elif new_position in ladders:
        print("Wohoo! You climbed up a ladder")
        return(ladders[new_position])            #Returns the new position after ladder has been encountered
    else:
        return new_position        

def update_position(player_num):  #updates the position of the player after each turn
    if(player_num==1):
        global player1_position
        new_position=player1_position+step
        if new_position<=100:     #A check for not exceeding the 100th position 
            player1_position=check_for_snakes_and_ladders(new_position)
        print("Your final position is: ",player1_position)    
    else:
        global player2_position
        new_position=player2_position+step
        if new_position<=100:     #A check for not exceeding the 100th position
            player2_position=check_for_snakes_and_ladders(new_position)
        print("Your final position is: ",player2_position)       
         
def iswinner():  #Checks if any of the players have won the game
    return(player1_position==100 or player2_position==100)

if __name__ == "__main__":

    print("""###### Welcome to Snakes & Ladders Game ######""")
    print()
    select_mode()
    print()
    player1_name=input("Enter the name of Player 1: ")
    player2_name=input("Enter the name of Player 2: ")
    print()
    print("###### Let us start ######")
    print()
    
    while not(iswinner()) :   #To keep playing until one of the player wins
        player_move(1)
        update_position(1)
        print()

        if(iswinner()):
            break

        player_move(2)
        update_position(2)
        print()            

    
    if(player1_position==100):
            print("Player 1: ", player1_name," won the game")
    elif(player2_position==100):
            print("Player 2:", player2_name," won the game")
    print("###### Game Successfully Finished ######")    

