# Lab Assignment 1
# Task 2
# Replace one Human player with rule based AI Program. Simple Reflex Agent 

board = [' ' for _ in range(10)]

def printBoard(board):
  print('   |   |   ')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('   |   |   ')
  print('-----------')
  print('   |   |   ')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('   |   |   ')
  print('-----------')
  print('   |   |   ')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('   |   |   ')

def isWinner(b, l):
  return (b[1]==l and b[2]==l and b[3]==l) or \
    (b[4]==l and b[5]==l and b[6]==l) or \
    (b[7]==l and b[8]==l and b[9]==l) or \
    (b[1]==l and b[4]==l and b[7]==l) or \
    (b[2]==l and b[5]==l and b[8]==l) or \
    (b[3]==l and b[6]==l and b[9]==l) or \
    (b[1]==l and b[5]==l and b[9]==l) or \
    (b[3]==l and b[5]==l and b[7]==l)

def spaceIsFree(pos):
  return board[pos] == ' '

def insertLetter(letter, pos):
  board[pos] = letter

def playerMove(symbol):
  run = True
  while run:
    move = input('Please select a position to place an \'' + symbol + '\' (1-9): ')
    try:
      move = int(move)
      if move > 0 and move < 10:
        if spaceIsFree(move):
          run = False
          insertLetter(symbol, move)
        else:
          print('This postion is already occupied!')
      else:
        print('Please type a number within the range!')
    except:
      print('Please type a number!')

# no of total moves = 9
# no of players = 2
# no of moves per player = 9/2 = 4.5
# no of moves per player = 4

def isBoardFull(board):
  spaceCount = board.count(' ')
  # print(spaceCount)
  if spaceCount > 1:
    return False
  else:
    return True
  
def selectRandom(li):
  import random
  ln = len(li)
  r = random.randrange(0, ln)
  return li[r]

def canPlayerWin(board, symbol):
  for i in range(1, 10):
    if spaceIsFree(i):
      boardCopy = board[:]
      boardCopy[i] = symbol
      if isWinner(boardCopy, symbol):
        return i
  return -1

def getComputerMove():
  move = canPlayerWin(board, 'O')
  if move != -1:
    return move
  else:
    move = canPlayerWin(board, 'X')
    if move != -1:
      return move
    else:
      if spaceIsFree(5):
        return 5
      else:
        move = selectRandom([1, 3, 7, 9])
        if spaceIsFree(move):
          return move
        else:
          return selectRandom([2, 4, 6, 8])
        
def getComputerMove2():
  # explicitly define all the possible moves where oponent can win and block them
  # if no such move is found then select a random move
  # if no random move is found then return -1
  if(board[1]=='X' and board[2]=='X' and board[3]==' '):
    return 3
  elif(board[1]=='X' and board[2]==' ' and board[3]=='X'):
    return 2
  elif(board[1]==' ' and board[2]=='X' and board[3]=='X'):
    return 1
  
  elif(board[4]=='X' and board[5]=='X' and board[6]==' '):
    return 6
  elif(board[4]=='X' and board[5]==' ' and board[6]=='X'):
    return 5
  elif(board[4]==' ' and board[5]=='X' and board[6]=='X'):
    return 4
  
  elif(board[7]=='X' and board[8]=='X' and board[9]==' '):
    return 9
  elif(board[7]=='X' and board[8]==' ' and board[9]=='X'):
    return 8
  elif(board[7]==' ' and board[8]=='X' and board[9]=='X'):
    return 7
  
  elif(board[1]=='X' and board[4]=='X' and board[7]==' '):
    return 7
  elif(board[1]=='X' and board[4]==' ' and board[7]=='X'):
    return 4
  elif(board[1]==' ' and board[4]=='X' and board[7]=='X'):
    return 1
  
  elif(board[2]=='X' and board[5]=='X' and board[8]==' '):
    return 8
  elif(board[2]=='X' and board[5]==' ' and board[8]=='X'):
    return 5
  elif(board[2]==' ' and board[5]=='X' and board[8]=='X'):
    return 2
  
  elif(board[3]=='X' and board[6]=='X' and board[9]==' '):
    return 9  
  elif(board[3]=='X' and board[6]==' ' and board[9]=='X'):
    return 6
  elif(board[3]==' ' and board[6]=='X' and board[9]=='X'):
    return 3
  
  elif(board[1]=='X' and board[5]=='X' and board[9]==' '):
    return 9
  elif(board[1]=='X' and board[5]==' ' and board[9]=='X'):
    return 5
  elif(board[1]==' ' and board[5]=='X' and board[9]=='X'):
    return 1
  
  elif(board[3]=='X' and board[5]=='X' and board[7]==' '):
    return 7
  elif(board[3]=='X' and board[5]==' ' and board[7]=='X'):
    return 5
  elif(board[3]==' ' and board[5]=='X' and board[7]=='X'):
    return 3
  
  else:
    return -1
  
def getRandomMove(board):
  possibleMoves = []
  for i in range(1, 10):
    if spaceIsFree(i):
      possibleMoves.append(i)
  move = selectRandom(possibleMoves)
  return move
        
# def main():
#   printBoard(board)
#   while not(isBoardFull(board)):
#     if not(isWinner(board, 'O')):
#       playerMove('X')
#       printBoard(board)
#     else:
#       print('Sorry, O\'s won this time!')
#       break
    
#     if not(isWinner(board, 'X')):
#       move = getComputerMove()
#       if move == -1:
#         print('Tie Game!')
#       else:
#         insertLetter('O', move)
#         print('Computer placed an \'O\' in position', move, ':')
#         printBoard(board)
#     else:
#       print('X\'s won this time! Good Job!')
#       break
      
#   if isBoardFull(board):
#     print('Tie Game!')

def main():
  printBoard(board)
  for _ in range(5):
    playerMove('X')
    printBoard(board)
    if isWinner(board, 'X'):
      print('X won!')
      break
    if isBoardFull(board):
      print('Tie game!')
      break
    move = getComputerMove2()
    if move == -1:
      insertLetter('0', getRandomMove(board))
      print('Computer placed an \'O\' in position', move, ':')
      printBoard(board)
    else:
      insertLetter('O', move)
      print('Computer placed an \'O\' in position', move, ':')
      printBoard(board)
    if isWinner(board, 'O'):
      print('O won!')
      break

if __name__ == '__main__':
  main()