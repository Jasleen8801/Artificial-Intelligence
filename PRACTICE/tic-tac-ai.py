import random

board = [' ' for x in range(10)]

def printBoard(board):
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

def isSpaceFree(pos):
  return board[pos]==' '

def insertLetter(let, pos):
  board[pos] = let

def isWinner(b, l):
  return (b[1]==l and b[2]==l and b[3]==l) or \
    (b[4]==l and b[5]==l and b[6]==l) or \
    (b[7]==l and b[8]==l and b[9]==l) or \
    (b[1]==l and b[4]==l and b[7]==l) or \
    (b[2]==l and b[5]==l and b[8]==l) or \
    (b[3]==l and b[6]==l and b[9]==l) or \
    (b[1]==l and b[5]==l and b[9]==l) or \
    (b[3]==l and b[5]==l and b[7]==l) 

def isBoardFull(board):
  cnt = board.count(' ')
  if cnt>1:
    return False
  return True

def playerMove(sym):
  run = True
  while run:
    pos = int(input('Enter pos (1-9): '))
    try:
      if pos>0 and pos<10:
        if isSpaceFree(pos):
          run = False
          insertLetter(sym, pos)
        else:
          print('Filled')
      else:
        print('Out of range')
    except:
      print('Error')
    
def aiMove(sym):
  poss = [x for x, let in enumerate(board) if let==' ' and x!=0]

  for move in poss:
    boardcpy = board[:]
    boardcpy[move] = sym
    if isWinner(boardcpy, sym):
      return move
  
  oppSym = 'O' if sym=='X' else 'X'
  for move in poss:
    boardcpy = board[:]
    boardcpy[move] = oppSym
    if isWinner(boardcpy, oppSym):
      return move
    
  if 5 in poss:
    return 5
  
  corner = [1,3,7,9]
  availCor = [cor for cor in corner if cor in poss]
  if availCor:
    return random.choice(availCor)
  
  sides = [2,4,7,9]
  availSides = [side for side in sides if side in poss]
  if availSides:
    return random.choice(availSides)
  
def main():
  printBoard(board)
  while not isBoardFull(board):
    if not isWinner(board, 'X'):
      playerMove('O')
      printBoard(board)
    else:
      print('X win')
      break
    if not isWinner(board, 'O'):
      move = aiMove('X')
      if move == 0:
        print('Tie')
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