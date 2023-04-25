'''
Name: Rayyan Aseef
Email: Rayyanusername@Gmail.com
Teacher: Mr.Mah
'''

import pygame

pygame.init()
# This varaible sets the size of the window
size = (498,500)
screen = pygame.display.set_mode(size)

# Caption
# This sets the Title of the game on the window top
pygame.display.set_caption("The Tail of the Serpant")

# Variables
# If this variable becomes true level 1 starts
level1 = False
#RGB Colour value that equals white
white = (255,255,255)
#RGB Colour value that equals black
black = (0,0,0)
#RGB Colour value that equals green
green = (0,255,0)
#RGB Colour value that equals red
red = (255,0,0)
#RGB Colour value that equals blue
blue = (0,0,255)
#Number of rows in the height
rows_h = 6
#Number of rows in the width
rows_w = 5
# Where the body partss and head move
direction = 0
# x cordinates for the head
startx = 4
# y cordinates for the head
starty = 4
# x cordinates for the body 1
body1x = 3
# y cordinates for the body 1
body1y = 4
# x cordinates for the body 2
body2x = 2
# y cordinates for the body 2
body2y = 4
# x cordinates for the body 3
body3x = 2
# y cordinates for the body 3
body3y = 3
# Save the right turn the head moved by the player
turn_r = True
# Save the left turn the head moved by the player
turn_l = False
# Save the up turn the head moved by the player
turn_u = False
# Save the down turn the head moved by the player
turn_d = False

# Creates the grid
def grid(width, rows1, rows2, screen):
    global white, gap_btwn_x,gap_btwn_y
    gap_btwn_x = width // rows1
    gap_btwn_y = width // rows2
    x = 0
    y = 0
    for lx in range(rows1):
        x = x + gap_btwn_x
        pygame.draw.line(screen, white,(x,0),(x,width))

    for ly in range(rows2):
        y = y + gap_btwn_y
        pygame.draw.line(screen, white,(0,y),(width,y))

# Creates the circle you want to be in
def circle_here(colour, width, rows1, rows2, screen, box_x = 0, box_y = 0):
    global green, red, gap_btwn_x, gap_btwn_y
    linespace_x = 0
    linespace_y = 0
    if box_x > 0:
        box_x = box_x - 1
        linespace_x = 1
    if box_y > 0:
        box_y = box_y - 1
        linespace_y = 1
    box_x = box_x * gap_btwn_x
    box_y = box_y * gap_btwn_y
    x = (box_x + gap_btwn_x // 2) + linespace_x 
    y = (box_y + gap_btwn_y // 2) + linespace_y
    if x - box_x > y - box_y:
        r = y - box_y - 1
    elif y - box_y > x - box_x:
        r = x - box_x - 1
    pygame.draw.circle(screen, colour, (x,y), r)

# creates the head
def head(gridx = 0,gridy = 0):
    global blue, gap_btwn_x, gap_btwn_y,direction
    if gridx > 0:
        gridx = gridx - 1
    if gridy > 0:
        gridy = gridy - 1
    gridx = gridx * gap_btwn_x
    gridy = gridy * gap_btwn_y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if turn_l == True:
                if body1y == body2y == body3y == starty and turn_l == True:
                    direction = ((gridx + gap_btwn_x - 1,gridy + 1),(gridx + gap_btwn_x - 1,gridy + gap_btwn_y - 1),(gridx - 2,gridy + gap_btwn_y // 2))
                else:
                    pass
            else:
                direction = ((gridx + 1,gridy + 1),(gridx + 1,gridy + gap_btwn_y - 1),(gridx + gap_btwn_x - 2,gridy + gap_btwn_y // 2))    
        if event.key == pygame.K_LEFT:
            if turn_r == True:
                if body1y == body2y == body3y == starty and turn_r == True:
                    direction = ((gridx + 1,gridy + 1),(gridx + 1,gridy + gap_btwn_y - 1),(gridx + gap_btwn_x - 2,gridy + gap_btwn_y // 2))
                else:
                    pass
            else:
                direction = ((gridx + gap_btwn_x - 1,gridy + 1),(gridx + gap_btwn_x - 1,gridy + gap_btwn_y - 1),(gridx - 2,gridy + gap_btwn_y // 2))
        if event.key == pygame.K_DOWN:
            if turn_u == True:
                if body1x == body2x == body3x == startx and turn_u == True:
                    direction = ((gridx + 1,gridy + gap_btwn_y - 1),(gridx + gap_btwn_x - 1,gridy + gap_btwn_y - 1),(gridx + gap_btwn_x // 2,gridy - 2))
                else:
                    pass
            else:
                direction = ((gridx + 1,gridy + 1),(gridx + gap_btwn_x - 1,gridy + 1),(gridx + gap_btwn_x // 2,gridy + gap_btwn_y - 2))
        if event.key == pygame.K_UP:
            if turn_d == True:
                if body1x == body2x == body3x == startx and turn_d == True:
                    direction = ((gridx + 1,gridy + 1),(gridx + gap_btwn_x - 1,gridy + 1),(gridx + gap_btwn_x // 2,gridy + gap_btwn_y - 2))
                else:
                    pass
            else:
                direction = ((gridx + 1,gridy + gap_btwn_y - 1),(gridx + gap_btwn_x - 1,gridy + gap_btwn_y - 1),(gridx + gap_btwn_x // 2,gridy - 2))    
    pygame.display.update()

# Creates the body
def body(width, rows1, rows2, screen, box_x = 0, box_y = 0):
    global white, gap_btwn_x, gap_btwn_y
    linespace_x = 0
    linespace_y = 0
    if box_x > 0:
        box_x = box_x - 1
        linespace_x = 1
    if box_y > 0:
        box_y = box_y - 1
        linespace_y = 1
    box_x = box_x * gap_btwn_x
    box_y = box_y * gap_btwn_y
    x = (box_x + gap_btwn_x // 2) + linespace_x 
    y = (box_y + gap_btwn_y // 2) + linespace_y
    if x - box_x > y - box_y:
        r = y - box_y - 5
    elif y - box_y > x - box_x:
        r = x - box_x - 5
    pygame.draw.circle(screen, white, (x,y), r)

# Makes the dragon move
def move(r_barrier,l_barrier,u_barrier,d_barrier,r_barrier2,l_barrier2,u_barrier2,d_barrier2):
    global turn_l,turn_r,turn_u,turn_d
    global startx,starty,body1x,body1y,body2x,body2y,body3x,body3y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if turn_l == True:
                if body1y == body2y == body3y == starty and turn_l == True:
                    if body3x == r_barrier2:
                        pass
                    else:
                        startx = body1x
                        starty = body1y
                        body1x = body2x
                        body1y = body2y
                        body2x = body3x
                        body2y = body3y
                        body3x = body3x + 1
            else:
                number_r = (startx * gap_btwn_x) + gap_btwn_x - 2
                if number_r == r_barrier:
                    pass
                else:
                    body3x = body2x
                    body3y = body2y
                    body2x = body1x
                    body2y = body1y
                    body1x = startx
                    body1y = starty
                    startx = startx + 1
                    turn_r = True
                    turn_u = False
                    turn_d = False
        if event.key == pygame.K_LEFT:
            if turn_r == True:
                if body1y == body2y == body3y == starty and turn_r == True:
                    if body3x == l_barrier2:
                        pass
                    else:
                        startx = body1x
                        starty = body1y
                        body1x = body2x
                        body1y = body2y
                        body2x = body3x
                        body2y = body3y
                        body3x = body3x - 1
            else:
                number_l = startx * gap_btwn_x - 2
                if number_l == l_barrier:
                    pass
                else:
                    body3x = body2x
                    body3y = body2y
                    body2x = body1x
                    body2y = body1y
                    body1x = startx
                    body1y = starty
                    startx = startx - 1
                    turn_l = True
                    turn_u = False
                    turn_d = False
        if event.key == pygame.K_UP:
            if turn_d == True:
                if body1x == body2x == body3x == startx and turn_d == True:
                    if body3y == u_barrier2:
                        pass
                    else:
                        startx = body1x
                        starty = body1y
                        body1x = body2x
                        body1y = body2y
                        body2x = body3x
                        body2y = body3y
                        body3y = body3y - 1
            else:
                number_u = (starty * gap_btwn_y) - 2
                if number_u == u_barrier:
                    pass
                else:
                    body3x = body2x
                    body3y = body2y
                    body2y = body1y
                    body2x = body1x
                    body1y = starty
                    body1x = startx
                    starty = starty - 1
                    turn_u = True
                    turn_l = False
                    turn_r = False
        if event.key == pygame.K_DOWN:
            if turn_u == True:
                if body1x == body2x == body3x == startx and turn_u == True:
                    if body3y == d_barrier2:
                        pass
                    else:
                        startx = body1x
                        starty = body1y
                        body1x = body2x
                        body1y = body2y
                        body2x = body3x
                        body2y = body3y
                        body3y = body3y + 1
            else:
                number_d = (starty * gap_btwn_y) + gap_btwn_y // 2
                if number_d == d_barrier:
                    pass
                else:
                    body3x = body2x
                    body3y = body2y
                    body2y = body1y
                    body2x = body1x
                    body1y = starty
                    body1x = startx
                    starty = starty + 1
                    turn_d = True
                    turn_l = False
                    turn_r = False

# Sets the starting position for the head
def start_pos(x,y):
    pygame.draw.polygon(screen,blue,(((gap_btwn_x * (x - 1)) + 1,(gap_btwn_y * (y - 1)) + 1),((gap_btwn_x * (x - 1)) + 1,(gap_btwn_y * (y - 1)) + gap_btwn_y - 1),((gap_btwn_x * (x - 1)) + gap_btwn_x - 2,(gap_btwn_y * (y - 1)) + gap_btwn_y // 2)))

# Draws text on the screen
def text(msg,box,text,x,y,w,h,size):
    font = pygame.font.Font("freesansbold.ttf",size)
    text = font.render(msg,True,text,box)
    textRect = text.get_rect()
    textRect.center = (x + (w // 2),y + (h // 2))
    screen.blit(text,textRect)

# Creates a button on the screen
def button(msg,x,y,w,h,Atxt,NAtxt,Abox,NAbox,borderC,size,action = None):
    global black, level1
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen,Abox,(x,y,w,h))
        # This draws text in the middle of the button
        text(msg,Abox,Atxt,x,y,w,h,size)
        if click[0] == 1 and action != None:
            if action == "level1":
                level1 = True
    else:
        pygame.draw.rect(screen,NAbox,(x,y,w,h))
        # This draws text in the middle of the button
        text(msg,NAbox,NAtxt,x,y,w,h,size)
    # all these draw the border for the button
    pygame.draw.rect(screen,borderC,(x,y,5,h))
    pygame.draw.rect(screen,borderC,(x,y,w,5))
    pygame.draw.rect(screen,borderC,(x + w - 5,y,5,h))
    pygame.draw.rect(screen,borderC,(x,y + h - 5,w,5))
    
while True:
    # Makes the overall screen black
    screen.fill(black)
    for event in pygame.event.get():
        # check if they clicked the cross button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            # creates the level 1 button on the screen
    button("Level 1",150,50,200,50,blue,green,green,blue,white,32,action = "level1")
    while level1:
        # Makes the overall screen black
        screen.fill(black)
        grid(500,rows_h, rows_w,screen)
        # The code from here
        if body1x == 4 and body1y == 2 or body2x == 4 and body2y == 2 or body3x == 4 and body3y == 2:
            circle_here(green, 500, rows_h, rows_w, screen, 4, 2)
            bodyhere1 = True
        else:
            circle_here(red, 500, rows_h, rows_w, screen, 4, 2)
            bodyhere1 = False
        if body1x == 5 and body1y == 2 or body2x == 5 and body2y == 2 or body3x == 5 and body3y == 2:
            circle_here(green, 500, rows_h, rows_w, screen, 5, 2)
            bodyhere2 = True
        else:
            circle_here(red, 500, rows_h, rows_w, screen, 5, 2)
            bodyhere2 = False
        if body1x == 5 and body1y == 3 or body2x == 5 and body2y == 3 or body3x == 5 and body3y == 3:
            circle_here(green, 500, rows_h, rows_w, screen, 5, 3)
            bodyhere3 = True
        else:
            circle_here(red, 500, rows_h, rows_w, screen, 5, 3)
            bodyhere3 = False
            # to here checks if the body are in the circle_here function and changes the clour of the circle here
        # This makes the starting points for the body
        body(500, rows_h, rows_w, screen, body1x, body1y)
        body(500, rows_h, rows_w, screen, body2x, body2y)
        body(500, rows_h, rows_w, screen, body3x, body3y)
        for event in pygame.event.get():
            # check if they clicked the cross button
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            move(579,81,98,550,6,1,1,5)
            head(startx,starty)
        if direction == 0:
            # This resets everything back to wher it was if they do level 1 again
            start_pos(4,4)
            startx = 4
            starty = 4
            body1x = 3
            body1y = 4
            body2x = 2
            body2y = 4
            body3x = 2
            body3y = 3
            turn_r = True
            turn_l = False
            turn_u = False
            turn_d = False
        else:
            pygame.draw.polygon(screen,blue,direction)
        # This checks if all the bodes or in the designated circles and then ends the game
        if bodyhere1 == True and bodyhere2 == True and bodyhere3 == True:
            direction = 0
            level1 = False
        pygame.display.update()
    else:
        pass
    pygame.display.update()

