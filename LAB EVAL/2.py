# Lab Assignment 1
# Task 2

import random

board = [' ' for x in range(10)]

def printBoard(board) -> None:
  print('  |   |   ')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('  |   |   ')
  print('----------')
  print('  |   |   ')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('  |   |   ')
  print('----------')
  print('  |   |   ')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('  |   |   ')
  
def isWinner(b, l) -> bool:
  return (b[1]==l and b[2]==l and b[3]==l) or \
    (b[4]==l and b[5]==l and b[3]==l) or \
    (b[7]==l and b[8]==l and b[9]==l) or \
    (b[1]==l and b[4]==l and b[7]==l) or \
    (b[2]==l and b[5]==l and b[8]==l) or \
    (b[3]==l and b[6]==l and b[9]==l) or \
    (b[1]==l and b[5]==l and b[9]==l) or \
    (b[3]==l and b[5]==l and b[7]==l)

def isSpaceFree(pos) -> bool:
  return board[pos]==' '

def insertLetter(letter, pos) -> None:
  board[pos] = letter

def playerMove(sym) -> None:
  run = True
  while run:
    move = int(input(f'Please select a position to enter the {sym} (0-9): '))
    try:
      if move>0 and move<10:
        if isSpaceFree(move):
          run = False
          insertLetter(sym, move)
        else:
          print('Sorry, this space is Occupied!!!')
      else:
        print('Enter a fucking number betweeen 0 and 9')
    except:
      print("enter a damn number!!!")

def aiMove(sym) -> int:
  poss = [x for x, letter in enumerate(board) if letter==' ' and x!=0]

  for move in poss:
    boardCopy = board[:]
    boardCopy[move] = sym
    if isWinner(boardCopy, sym):
      return move
  
  oppSym = 'O' if sym=='X' else 'X'
  for move in poss:
    boardCopy = board[:]
    boardCopy[move] = oppSym
    if isWinner(boardCopy, oppSym):
      return move
    
  if 5 in poss:
    return 5
  
  corners = [1,3,7,9]
  availCorners = [corner for corner in corners if corner in poss]
  if availCorners:
    return random.choise(availCorners)
  
  sides = [2,4,6,8]
  availSides = [side for side in sides if side in poss]
  if availSides:
    return random.choice(availSides)

def isBoardFull(board) -> bool:
  cnt = board.count(' ')
  if cnt>1:
    return False
  else: 
    return True
  
def main():
  print('Welcome to AI GAME')
  printBoard(board)
  while not isBoardFull(board):
    if not isWinner(board, 'X'):
      playerMove('O')
      printBoard(board)
    else:
      print('X wins')
      break
    if not isWinner(board, 'O'):
      move = aiMove('X')
      if move==0:
        print('Tie Game')
      else:
        insertLetter('X', move)
        printBoard(board)
    else:
      print('O wins')
      break
  if isBoardFull(board):
    print('Tie Game')

if __name__ == '__main__':
  main()