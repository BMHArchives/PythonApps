'''
Created on Jul 6, 2017

@author: Brandon
'''
print("Welcome to Tic Tac Toe Game")
p1Name = ""
p2Name = ""
PlayerMoves = []
WhosTurn = ""
def ShowBoard(PlayerMove,Player,CurrentTurn):
    PlayerPiece = ""
    if (Player == "P1"):
        PlayerPiece = "X"
    else:
        PlayerPiece = "O"
        
    P1 = "1"
    P2 = "2"
    P3 = "3"
    P4 = "4"
    P5 = "5"
    P6 = "6"
    P7 = "7"
    P8 = "8"
    P9 = "9" 
    if(PlayerMove == 0):
        print("_ _{} _ _| _ _{} _ _ | _ _{} _ _\n_ _{} _ _| _ _{} _ _ | _ _{} _ _\n_ _{} _ _| _ _{} _ _ | _ _{} _ _".format(P1,P2,P3,P4,P5,P6,P7,P8,P9));
    else:
        ''' Loop through the PlayersMoves list '''
        PlayerMoves.append(Player+':'+ PlayerMove)
        
        
        
         
        for PlayerMove in PlayerMoves:
            playerPos = PlayerMove.split(':')[1]
            player = PlayerMove.split(':')[0]
            if(player == "P1"):
                PlayerPiece = "X"
            else:
                PlayerPiece = "O"
            #print("PlayerMove {}".format(PlayerMove[key].Player))
            #print("PlayerMove {}".format(PlayerMove[key].Position))
            if(playerPos == "1"):
                P1 = PlayerPiece
            if(playerPos == "2"):
                P2 = PlayerPiece
            if(playerPos == "3"):
                P3 = PlayerPiece
            if(playerPos == "4"):
                P4 = PlayerPiece
            if(playerPos == "5"):
                P5 = PlayerPiece
            if(playerPos == "6"):
                P6 = PlayerPiece
            if(playerPos == "7"):
                P7 = PlayerPiece
            if(playerPos == "8"):
                P8 = PlayerPiece
            if(playerPos == "9"):
                P9 = PlayerPiece
                
        print("_ _{} _ _| _ _{} _ _ | _ _{} _ _\n_ _{} _ _| _ _{} _ _ | _ _{} _ _\n_ _{} _ _| _ _{} _ _ | _ _{} _ _".format(P1,P2,P3,P4,P5,P6,P7,P8,P9));
        
        #Check if we have a winner #
        for PlayerMove in PlayerMoves:
            playerPos = PlayerMove.split(':')[1]
            player = PlayerMove.split(':')[0]
            if(P1 == "X" and P2 == "X" and P3 == "X"):
                return "P1"
                break
            elif (P4 == "X" and P5 == "X" and P6 == "X"):    
                return "P1"
                break
            elif (P7 == "X" and P8 == "X" and P9 == "X"):    
                return "P1"
                break
            elif (P1 == "X" and P5 == "X" and P9 == "X"):    
                return "P1"
                break
            elif (P3 == "X" and P5 == "X" and P7 == "X"):    
                return "P1"
                break
            elif (P1 == "X" and P4 == "X" and P7 == "X"):    
                return "P1"
                break
            elif (P2 == "X" and P5 == "X" and P8 == "X"):    
                return "P1"
                break
            elif (P3 == "X" and P6 == "X" and P9 == "X"):    
                return "P1"
                break
            elif (P1 == "O" and P2 == "O" and P3 == "O"):
                return "P2"
                break
            elif (P4 == "O" and P5 == "O" and P6 == "O"):    
                return "P2"
                break
            elif (P7 == "O" and P8 == "O" and P9 == "O"):    
                return "P2"
                break
            elif (P1 == "O" and P5 == "O" and P9 == "O"):    
                return "P2"
                break
            elif (P3 == "O" and P5 == "O" and P7 == "O"):    
                return "P2"
                break
            elif (P1 == "O" and P4 == "O" and P7 == "O"):    
                return "P2"
                break
            elif (P2 == "O" and P5 == "O" and P8 == "O"):    
                return "P2"
                break
            elif (P3 == "O" and P6 == "O" and P9 == "O"):    
                return "P2"
                break
                
            
                
                
print("This is a two player game.") 
print("Based use the numbers on the board to set your tic or tac values onto the board.")
p1Name = input("Player 1, please enter your name")
p2Name = input("Player 2, please enter your name")

print('Welcome {}, you are playing as player 1 and will be using X has you player piece.'.format(p1Name))
print('Welcome {}, you are playing as player 2 and will be using O has you player piece.'.format(p2Name))

PlayerTurn = "P1"
ShowBoard(0,"",0)
Winner = ""
for num in range(9):
    
    if (PlayerTurn == "P1"):
        p1Move = input("{} its your turn. Please choose a position to set your X piece on.".format(p1Name))
        Winner = ShowBoard(p1Move,"P1",num)
        PlayerTurn = "P2"
        if(Winner == "P1"):
            break;
        
    else:
        p2Move = input("{} its your turn. Please choose a position to set your X piece on.".format(p2Name))
        Winner = ShowBoard(p2Move,"P2",num)
        PlayerTurn = "P1"
        if(Winner == "P1"):
            break;
        
   
                
if(Winner == "P1"):
    print("Congruations {}, you won!!!!".format(p1Name))
elif(Winner== "P2"):
    print("Congruations {}, you won!!!!".format(p2Name))
else:
    print("You both tied. Maybe next time")