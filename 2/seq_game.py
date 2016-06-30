""" 
The number sequence game starts with a sequence S of N numbers written on a line. Two players alternate turns. At his turn, a player must select and remove either the first or the last number remaining in the sequence. 

The player score is the sum of all the numbers he has taken. Each player attempts to maximize his own sum. 

If N = 4 and S = {1, 2, 10, 3}, then each player maximizes his score as follows:

Player 1: removes the first number (1) 
Player 2: removes the last number from the remaining sequence (3) 
Player 1: removes the last number from the remaining sequence (10) 
Player 2: removes the remaining number (2) 
Player 1 score is 1 + 10 = 11. 
Let F(N) be the score of player 1 if both players follow the optimal strategy for the sequence S = {s1, s2, ..., sN} defined as:

s1 = 0
si+1 = (si2 + 45) modulo 1 000 000 007
The sequence begins with S = {0, 45, 2070, 4284945, 753524550, 478107844, 894218625, ...}

You are given F(2) = 45, F(4) = 4284990, F(100) = 26365463243, F(104) = 2495838522951.

Find F(108).

""" 


import sys
var=[]
mod=1000000007
limit=int(str(sys.argv[1]))
def sequence_game(A,N):
  C = [[0 for j in range(N)] for i in range(N)]
  x=0
  y=0
  z=0
  for k in range(0,N):
    i=0
    for j in range(k,N):
      if ((i+2)< N):
        x =C[i+2][j]
      if((i+1) <= (j-1)):
        y = C[i+1][j-1]  
      if (i <= (j-2)):
        z=C[i][j-2]  
      C[i][j] = max(A[i] + min(x,y),  A[j] + min(y,z))         
      #print C[i][j]
      i=i+1
      j=j+1
    k=k+1
  return C[0][N-1] 


var.append(0)
for x in range(1,limit):
  var.append(((var[x-1]*var[x-1])+45)%mod)
  #print var[x]
print sequence_game(var,len(var))