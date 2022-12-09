import timeit
start=timeit.timeit()

from colorama import Fore, init
init(autoreset=True)
X=Fore.RED+"X"
O=Fore.RED+"O"

def show():
    for row in game_board:
        for cell in row:
             print(cell, end=" ")
        print() 

def check_game():
     if  game_board[0][0]==X and  game_board[0][1]==X and  game_board[0][2]==X:
          print("** Player 1 Wins **")    
          exit()    
     if  game_board[1][0]==X and  game_board[1][1]==X and  game_board[1][2]==X:
          print("** Player 1 Wins **")    
          exit()  
     if  game_board[2][0]==X and  game_board[2][1]==X and  game_board[2][2]==X:
          print("** Player 1 Wins **")    
          exit() 
     if  game_board[0][0]==X and  game_board[1][1]==X and  game_board[2][2]==X:
          print("** Player 1 Wins **")    
          exit()  
     if  game_board[0][2]==X and  game_board[1][1]==X and  game_board[2][0]==X:
          print("** Player 1 Wins **")    
          exit()    


     if  game_board[0][0]==O and  game_board[0][1]==O and  game_board[0][2]==O:
          print("** Player 2 Wins **")    
          exit()    
     if  game_board[1][0]==O and  game_board[1][1]==O and  game_board[1][2]==O:
          print("** Player 2 Wins **")    
          exit()  
     if  game_board[2][0]==O and  game_board[2][1]==O and  game_board[2][2]==O:
          print("** Player 2 Wins **")    
          exit() 
     if  game_board[0][0]==O and  game_board[1][1]==O and  game_board[2][2]==O:
          print("** Player 2 Wins **")    
          exit()  
     if  game_board[0][2]==O and  game_board[1][1]==O and  game_board[2][0]==O:
          print("** Player 2 Wins **")    
          exit()    
               


game_board=[["_", "_", "_",],
            ["_", "_", "_",],
            ["_", "_", "_",]]
show()
while True:
    print("Player 1")

    while True:
        row=int(input("please enter row : "))
        col=int(input("please enter col : "))
        if 0<=row<=2 and 0<=col<=2 :
            if game_board[row][col]=="_":
                game_board[row][col]=X
                break
            else:
                print( "This house has already been selected, please try again . . .")
        else:
                print(" The selected number must be between 0 and 2 \n Please try again . . .")          
    show()
    check_game()

    print("Player 2")
    
    while True:
        row=int(input("please enter row : "))
        col=int(input("please enter col : "))
        if 0<=row<=2 and 0<=col<=2 :
            if game_board[row][col]=="_":
                    game_board[row][col]=O
                    break
            else:
                 print("This house has already been selected, please try again . . .")
        else:
                 print(" The selected number must be between 0 and 2 \n Please try again . . .")     
    show()
    check_game()

    end=timeit.timeit()
    print("Elapsed time : ",end-start)

