print("Welcome to the game of life!! Insert the size of the board to play the game :)")
answer=input() 

# 1. PRINT BOX FUNCTION
def board_print(board,size): #takes a board and a size
 for rows in range(size +2):
  print("-", end="")
 print("\n", end="")
 for rows in range(size):
  print("|", end="")
  for columns in range(size):
   if board[rows][columns]==1:
    print("1", end="")
   else:
    print("0", end="")
  print("|\n", end="")
 for rows in range(size +2):
  print("-", end="")
 print("\n", end="")
 
 
# 2. COMPUTE THE NEIGHBOURS FUNCTION

def compute_neighbours(board,size,rows,columns):
# VERTICAL LEFT
 if columns==0:  #The vertical left side is along the first column (column==0)
  if rows==0: #corner top left
   neighbours = board[rows][columns+1] + board[rows+1][columns] + board[rows+1][columns+1] 
  elif rows== size-1: #corner bottom left
   neighbours = board[rows-1][columns] + board[rows-1][columns+1] + board[rows][columns+1] 
  else: #rest of the vertical column
   neighbours = board[rows-1][columns] + board[rows-1][columns+1] + board[rows][columns+1] + board[rows+1][columns] + board[rows+1][columns+1]
 
# VERTICAL RIGHT
 elif columns==size-1: #The vertical right side is along the last column (column==size-1)
  if rows == 0: #corner top right
   neighbours = board[rows][columns-1] + board[rows+1][columns-1] + board[rows+1][columns] 
  elif rows== size-1: #corner bottom right
   neighbours = board[rows-1][columns] + board[rows-1][columns-1] + board[rows][columns-1] 
  else:  #rest of the vertical column
   neighbours = board[rows-1][columns] + board[rows-1][columns-1] + board[rows][columns-1] + board[rows+1][columns-1] + board[rows+1][columns] 

# TOP HORIZONTAL 
 elif rows==0 and columns!=0 and columns!= size -1: #The top horizontal row is the row==0 and I am not taking the corners as I took them with the verticals
  neighbours = board[rows][columns-1] + board[rows][columns+1] + board[rows+1][columns-1] + board[rows+1][columns] + board[rows+1][columns+1]  
 
#BOTTOM HORIZONTAL
 elif rows== size -1 and columns!=0 and columns!= size -1: #The bottom horizontal row is the row==size -1 and I am not taking the corners as I took them with the verticals
  neighbours = board[rows-1][columns] + board[rows-1][columns-1] + board[rows-1][columns+1] + board[rows][columns-1] + board[rows][columns+1]

#ANY POSITION IN THE MIDDLE    
 else: # the positions that are not in the borders have all the possible 8 neighbours
  neighbours = board[rows-1][columns-1] + board[rows-1][columns] + board[rows-1][columns+1] + board[rows][columns-1] + board[rows][columns+1] + board[rows+1][columns-1] + board[rows+1][columns] + board[rows+1][columns+1]   
 
 return neighbours # returns the sum of the neighbours
 
 
#3. COMPUTE THE NEXT BOARD FUNCTION
def board_compute_next_step(board,size):
 next_board=[[ 0 for x in range(size)] for y in range(size)] # Generation of an empty matri
 for rows in range(size):  # loop to itinerate through every position of the board matrix in the compute_neighbours function
  for columns in range(size):
   neighbours = compute_neighbours(board,size,rows,columns) #it sums the number of neighbours (number of "1"), for each position in the matrix. 
   #Then we print a death (0) or alive (1) cell in the next board depending on the number of neighbours:
   
# Dead cells   
   if board[rows][columns]==0:
## Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.      
    if neighbours ==3:
     next_board[rows][columns]=1
    else:
     next_board[rows][columns]=0   

# Alive cells
   if board[rows][columns]==1:  
## Any live cell with fewer than two live neighbors dies, as if by under-population.    
    if neighbours<2:
     next_board[rows][columns]=0
## Any live cell with more than three live neighbors dies, as if by overpopulation.     
    if neighbours>3:
     next_board[rows][columns]=0 
## Any live cell with two or three live neighbors lives on to the next generation.          
    if neighbours==2 or neighbours==3:
     next_board[rows][columns]=1    
   
 return next_board
 

#4. DECLARE THE GAME OF LIFE BOARD
import random #this is just so the random.randit works
size = int(answer)
board = [[random.randint(0,1) for x in range(size)] for y in range(size)] #random.radint produces a random integer(0 or 1) in the range specified 
while True :
 board_print(board,size) # calls board print function (which prints the board)
 print("Continue simulation (y/n)?")
 x=input() 
 if x=="n": #if the input is "n" break the loop
  break
 else: # otherwise reset the board
  next_board = board_compute_next_step(board,size)
  board=next_board 
   
   

   
   
