player1_position=0
player2_position=0
mode=0

def select_mode():
    print('''This game supports two modes: 
    1. Auto Mode: In this mode the computer will generate a random number between 1 to 6 after you type \"Roll\"
    2. Manual Mode: In this mode you have to enter a number between 1 and 20
    Enter 1 for Auto Mode and 2 for Manual Mode''')
    mode=input()
    if mode!='1' or mode!='2':
        while(True):
            mode=input("Invalid Input: Please enter 1 for Auto Mode and 2 for Manual Mode")
            if mode=='1' or mode=='2':
                break
    mode=int(input)        

def player_move(player_num):
    run=True
    while(run):
        choice=input("Player ",player_num,":")
        if mode==1:

    pass    


def iswinner():
    return(player1_position==100 or player2_position==100)

if __name__ == "__main__":

    print("###### Welcome to Snakes & Ladders Game ######")
    select_mode()
    player1_name=input("Enter the name of Player 1: ")
    player2_name=input("Enter the name of Player 2: ")
    print("###### Let us start ######")
    
    if not(iswinner()) :
        pass

    else:
        if(player1_position==100):
            print("Player 1 won the game")
        else:
            print("Player 2 won the game")
        print("###### Game Successfully Finished ######")    
