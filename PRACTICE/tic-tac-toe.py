board = [' ' for x in range(10)]

def printBoard(board):
  print('  |   |   ')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('  |   |   ')
  print('-----------')
  print('  |   |   ')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('  |   |   ')
  print('-----------')
  print('  |   |   ')

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
  return board[pos]==' '

def insertLetter(letter, pos):
  board[pos] = letter

def playerMove(sym):
  run = True
  while(run):
    move = int(input('Please select pos (1-9): '))
    try:
      if move>0 and move<10:
        if spaceIsFree(move):
          run = False
          insertLetter(sym, move)
        else:
          print('pos filled')
      else:
        print('number out of range')
    except:
      print('Error!!')

def isBoardFull(board):
  cnt = board.count(' ')
  if cnt>1:
    return False
  else:
    return True
  
def main():
  printBoard(board)
  while not isBoardFull(board):
    if not isWinner(board, 'X'):
      playerMove('O')
      printBoard(board)
    else:
      print('X won')
      break
    if not isWinner(board, 'O'):
      playerMove('X')
      printBoard(board)
    else:
      print('O won')
      break
  if isBoardFull(board):
    print('Tie')

if __name__ == '__main__':
  main()