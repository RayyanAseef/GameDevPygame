import pygame
import numpy

pygame.init()

(w,h) = (700,600)
(rows,cols) = (6,7)

global board
board = numpy.zeros((rows,cols))

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Connect 4")

blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
lightYellow = (255,255,0)
yellow = (225,225,0)
lightRed = (255,150,150)
red = (255,0,0)

spacingY = h / 6
spacingX = w / 7
circleX = spacingX / 2
circleY = spacingY / 2

positionValid = True
clicked = False
place = False
winPlayer1 = False
winPlayer2 = False
turn = 0
stop = 2000

def grid(w,h,board):
  color = yellow
  for verLineNum in range(7,0,-1):
    verLine = (verLineNum-1)*spacingX + circleX
    
    for horzLineNum in range(6,0,-1):
      horzLine = (horzLineNum-1)*spacingY + circleY
      if (board[horzLineNum-1][verLineNum-1] == 0):
        color = white
      if (board[horzLineNum-1][verLineNum-1] == 1):
        color = yellow
      if (board[horzLineNum-1][verLineNum-1] == 2):
        color = red

      pygame.draw.circle(screen, black, (verLine,horzLine), circleX-1)
      pygame.draw.circle(screen, color, (verLine,horzLine), circleX-3)

def mouseDet(mX,c,p,board):
  global place, turn, positionValid, winPlayer1, winPlayer2
  for numX in range(7):
    mouseBarX = numX*spacingX
    if mouseBarX < mX < mouseBarX+spacingX:
      if place == True:
        if turn == 0:
          placePos(numX,1)
          winPlayer1 = win(board,1)
          place = False
          turn = 1
        elif turn == 1:
          placePos(numX,2)
          winPlayer2 = win(board,2)
          place = False
          turn = 0
      emptySpace = 0
      for i in range(6):
        if board[i][numX] == 0:
          emptySpace += 1

      if stop > 1001:
        for numY in range(emptySpace):
          horzLine = numY*spacingY
          if numY <= (emptySpace-1):
            if c == False:
              if numY == emptySpace-1:
                colour = yellow
              else:
                colour = lightYellow
            elif c == True:
              if numY == emptySpace-1:
                colour = red
              else:
                colour = lightRed
          
          pygame.draw.circle(screen, colour, (mouseBarX+circleX,horzLine+circleY), circleX-15)

def placePos(numX,value):
  global positionValid
  for x in range(6,0,-1):
    if board[0][numX] == 1 or board[0][numX] == 2:
      print("!!!!!!!!!!!!!!!!\nPosition Invalid\n!!!!!!!!!!!!!!!!")
      positionValid = False
      break
    elif board[x-1][numX] == 0:
      board[x-1][numX] = value
      positionValid = True
      break

def win(board,piece):
  global rows, cols, stop
  for c in range(cols-3):
    for r in range(rows):
      if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        stop = 0
        return True
  for c in range(cols):
    for r in range(rows-3):
      if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        stop = 0
        return True
      
  for c in range(cols-3):
    for r in range(rows-3):
      if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        stop = 0
        return True

  for c in range(cols-3):
    for r in range(rows-3):
      if board[r][c+3] == piece and board[r+1][c+2] == piece and board[r+2][c+1] == piece and board[r+3][c] == piece:
        stop = 0
        return True

while True:
  screen.fill(blue)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if positionValid == True:
        if clicked == True:
          clicked = False
        elif clicked == False:
          clicked = True
      place = True
      
  (mousePosX,mousePosY) = pygame.mouse.get_pos()

  grid(w,h,board)
  mouseDet(mousePosX,clicked,place,board)

  if winPlayer1 == True and stop == 1000:
    print("Yellow Player Has Won")
    print("Game Over")
    break
  elif winPlayer2 == True and stop == 1:
    print("Red Player Has Won")
    print("Game Over")
    break

  stop += 1
  pygame.display.update()  

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
