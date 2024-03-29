# Lab Assignment 1
# Tic Tac Toe AI Game 

board = [' ' for x in range(10)]

def printBoard(board) -> None:
  '''Prints the Tic-Tac-Toe board'''
  print('  |   |   ')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('  |   |   ')
  print('-----------')
  print('  |   |   ')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('  |   |   ')
  print('-----------')
  print('  |   |   ')

def isWinner(b, l) -> bool:
  '''b: board, l: letter/player'''
  return (b[1]==l and b[2]==l and b[3]==l) or \
    (b[4]==l and b[5]==l and b[6]==l) or \
    (b[7]==l and b[8]==l and b[9]==l) or \
    (b[1]==l and b[4]==l and b[7]==l) or \
    (b[2]==l and b[5]==l and b[8]==l) or \
    (b[3]==l and b[6]==l and b[9]==l) or \
    (b[1]==l and b[5]==l and b[9]==l) or \
    (b[3]==l and b[5]==l and b[7]==l)

def spaceIsFree(pos) -> bool:
  '''pos: position'''
  return board[pos] == ' '

def insertLetter(letter, pos) -> None:
  '''letter: player symbol, pos: position'''
  board[pos] = letter

def playerMove(sym) -> None:
  '''sym: player symbol'''
  run = True
  while run:
    move = input('Please select a position to place an \'' + sym + '\' (1-9): ')
    try:
      move = int(move)
      if move > 0 and move < 10:
        if spaceIsFree(move):
          run = False
          insertLetter(sym, move)
        else:
          print('This postion is already occupied!')
      else:
        print('Please type a number within the range!')
    except:
      print('Please type a number!')

def isBoardFull(board) -> bool:
  cnt = board.count(' ')
  if cnt > 1:
    return False
  else:
    return True

def main():
  print('Welcome to Tic Tac Toe!')
  printBoard(board)
  while not isBoardFull(board):
    if not isWinner(board, 'X'):
      playerMove('O')
      printBoard(board)
    else:
      print('X won this time!')
      break
    if not isWinner(board, 'O'):
      playerMove('X')
      printBoard(board)
    else:
      print('O won this time!')
      break
  if isBoardFull(board):
    print('It\'s a tie!')

if __name__ == '__main__':
  main()