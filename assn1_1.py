# Lab Assignment 1
# Task 1
#Write a Program for Tic-Tac-Toe game between two human players. The functions for printing Tic-Tac-Toe board, IsWinner() and playerMove() are already given for your help.

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
  print(spaceCount)
  if spaceCount > 1:
    return False
  else:
    return True
  
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
    playerMove('O')
    printBoard(board)
    if isWinner(board, 'O'):
      print('O won!')
      break
    
if __name__ == '__main__':
  main()