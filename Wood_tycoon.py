import pygame

pygame.init()

# Set tab size
width = 800
height = 600
size = (width,height)
screen = pygame.display.set_mode(size)

# Set caption and icon
pygame.display.set_caption("Wood Tycoon")

# Variables
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
orange = (255,69,0)
black_brown = (125,75,0)
dark_brown = (186,136,61)
brown = (196,146,71)
pickaxe_brown = (176,126,51)
light_blue = (0,150,255)
blue = (0,0,255)
dark_green = (0,230,0)
purple = (200,0,255)
gold = (255,233,100)
grey = (230,230,230)
green = (0,255,0)
wait = 500
wood = 0
cash = 4150
menu = False
typeC = brown
menuP = False
menuI= False
mode1 = "Unequip"
mode2 = "Equip"
mode3 = "Equip"
mode4 = "Equip"
mode5 = "Equip"
mode6 = "Equip"
buy2 = False
buy3 = False
buy4 = False
buy5 = False
buy6 = False
mode21 = "Picked"
mode22 = "Pick"
mode23 = "Pick"
mode24 = "Picked"
mode25 = "Pick"
mode26 = "Pick"
buy22 = False
buy23 = False
buy25 = False
buy26 = False
worth = 1
TC = dark_brown
LC = dark_green
worth1 = 1
multipliyer = 1

def ground(h):
    global ground_level
    ground_level = h
    screen.fill(brown,(0,h,800,600))

def sky():
    global ground_level
    screen.fill(light_blue,(0,0,800,ground_level))

def tree(w,cT,cL):
    global ground_level
    tree_level = ground_level - 300
    top_tree = tree_level - 100
    tree_height = ground_level - 150
    screen.fill(cT,(w,150,50,tree_height))
    screen.fill(cL,(w - 100,100,250,50))
    screen.fill(cL,(w - 50,50,150,50))

def human(w):
    global ground_level
    global head_level
    global face_X
    head_level = ground_level - 125
    face_X = w
    screen.fill(brown,(w + 5,ground_level - 125,25,25))
    screen.fill(blue,(w,ground_level - 100,35,50))
    screen.fill(green,(w,ground_level - 50,35,50))
    screen.fill(green,(w + 5,head_level + 5,3,3))
    screen.fill(black,(w + 5,head_level + 15,5,3))

def background(x,wT,wH,cT,cL):
    ground(x)
    sky()
    tree(wT,cT,cL)
    human(wH)

def pickaxe(hit,colour):
    global ground_level
    global head_level
    global face_X
    startx = face_X - 30
    starty = head_level - 50
    hitx = startx - 75
    hity = head_level + 15
    if hit == True:
        screen.fill(pickaxe_brown,(hitx,hity,75,10))
        pygame.draw.polygon(screen,colour,((hitx+3,hity-15),(hitx+12,hity-15),(hitx+12,hity+10),(hitx+15,hity+15),(hitx-3,hity+15),(hitx+3,hity+10)))
    else:
        screen.fill(pickaxe_brown,(startx,starty,10,75))
        pygame.draw.polygon(screen,colour,((startx+15,starty+3),(startx+15,starty+12),(startx-10,starty+12),(startx-15,starty+15),(startx-15,starty-3),(startx-10,starty+3)))

def text(msg,colour,size,x,y,w,h,rect = True):
    font = pygame.font.SysFont("arial",size)
    text = font.render(msg,True,colour)
    if rect == True:
        textRect = text.get_rect()
        textRect.center = (x + (w // 2),y + (h // 2))
        screen.blit(text,textRect)
    else:
        screen.blit(text,(x,y))

def button(msg,x,y,w,h,size,AC,NAC,AT,NAT,action = None):
    global wood,cash,menu,menuP,menuI,typeC,worth,TC,LC,worth1,multipliyer
    global mode1,mode2,mode3,mode4,mode5,mode6
    global mode21,mode22,mode23,mode24,mode25,mode26
    global buy2,buy3,buy4,buy5,buy6
    global buy22,buy23,buy25,buy26
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen,AC,(x,y,w,h))
        text(msg,AT,size,x,y,w,h)
        if click[0] == 1 and action != None:
            if action == "cash it":
                cash = cash + (wood*(worth1*multipliyer))
                wood = 0
            if action == "menu":
                menu = True
                menuP = True
                menuI = False
            if action == "menu close":
                menu = False
            if action == "menu pickaxe":
                menuP = True
                menuI = False
            if action == "menu island":
                menuP = False
                menuI = True
            if action == "equip1":
                mode1 = "Unequip"
                mode2 = "Equip"
                mode3 = "Equip"
                mode4 = "Equip"
                mode5 = "Equip"
                mode6 = "Equip"
                typeC = brown
                worth = 1
            if action == "equip2":
                mode1 = "Equip"
                mode2 = "Unequip"
                mode3 = "Equip"
                mode4 = "Equip"
                mode5 = "Equip"
                mode6 = "Equip"
                typeC = grey
                worth = 5
            if action == "equip3":
                mode1 = "Equip"
                mode2 = "Equip"
                mode3 = "Unequip"
                mode4 = "Equip"
                mode5 = "Equip"
                mode6 = "Equip"
                typeC = gold
                worth = 10
            if action == "equip4":
                mode1 = "Equip"
                mode2 = "Equip"
                mode3 = "Equip"
                mode4 = "Unequip"
                mode5 = "Equip"
                mode6 = "Equip"
                typeC = blue
                worth = 25
            if action == "equip5":
                mode1 = "Equip"
                mode2 = "Equip"
                mode3 = "Equip"
                mode4 = "Equip"
                mode5 = "Unequip"
                mode6 = "Equip"
                typeC = green
                worth = 50
            if action == "equip6":
                mode1 = "Equip"
                mode2 = "Equip"
                mode3 = "Equip"
                mode4 = "Equip"
                mode5 = "Equip"
                mode6 = "Unequip"
                typeC = purple
                worth = 100
            if action == "buy2":
                if cash >= 150:
                    cash = cash - 150
                    buy2 = True
            if action == "buy3":
                if cash >= 1000:
                    cash = cash - 1000
                    buy3 = True
            if action == "buy4":
                if cash >= 5000:
                    cash = cash - 5000
                    buy4 = True
            if action == "buy5":
                if cash >= 100000:
                    cash = cash - 100000
                    buy5 = True
            if action == "buy6":
                if cash >= 1000000:
                    cash = cash - 1000000
                    buy6 = True
            if action == "pick1":
                mode21 = "Picked"
                mode22 = "Pick"
                mode23 = "Pick"
                TC = dark_brown
                worth1 = 1
            if action == "pick2":
                mode21 = "Pick"
                mode22 = "Picked"
                mode23 = "Pick"
                TC = white
                worth1 = 5
            if action == "pick3":
                mode21 = "Pick"
                mode22 = "Pick"
                mode23 = "Picked"
                TC = black_brown
                worth1 = 10
            if action == "pick4":
                mode24 = "Picked"
                mode25 = "Pick"
                mode26 = "Pick"
                LC = dark_green
                multipliyer = 1
            if action == "pick5":
                mode24 = "Pick"
                mode25 = "Picked"
                mode26 = "Pick"
                LC = red
                multipliyer = 2
            if action == "pick6":
                mode24 = "Pick"
                mode25 = "Pick"
                mode26 = "Picked"
                LC = orange
                multipliyer = 4
            if action == "buy22":
                if cash >= 10000:
                    cash = cash - 10000
                    buy22 = True
            if action == "buy23":
                if cash >= 500000:
                    cash = cash - 500000
                    buy23 = True
            if action == "buy25":
                if cash >= 50000:
                    cash = cash - 50000
                    buy25 = True
            if action == "buy26":
                if cash >= 150000:
                    cash = cash - 150000
                    buy26 = True
    else:
        pygame.draw.rect(screen,NAC,(x,y,w,h))
        text(msg,NAT,size,x,y,w,h)
    pygame.draw.rect(screen,black,(x,y,10,h))
    pygame.draw.rect(screen,black,(x+w-10,y,10,h))
    pygame.draw.rect(screen,black,(x,y,w,10))
    pygame.draw.rect(screen,black,(x,y+h-10,w,10))

def pickaxe_showcase(x,y,colour):
    startx = x
    starty = y
    screen.fill(pickaxe_brown,(startx,starty,10,75))
    pygame.draw.polygon(screen,colour,((startx+15,starty+3),(startx+15,starty+12),(startx-10,starty+12),(startx-15,starty+15),(startx-15,starty-3),(startx-10,starty+3)))

def pickaxe_showcase_all(x,y,w,h,colour,amount,price):
    button("",x,y,w,h,28,white,white,black,black)
    pickaxe_showcase(x+95,y+30,colour)
    text(f"Wood can break: {amount}",black,15,x,y+105,w,30)
    text(f"Price: {price}",black,15,x,y+135,w,30)

def island_showcase(x,y,w,h,colour,colour2,amount,price,type1):
    button("",x,y,w,h,28,colour,colour,black,black)
    text(f"{type1} colour",colour2,15,x,y+80,w,30)
    text(f"Wood worth: {amount}",colour2,15,x,y+105,w,30)
    text(f"Price: {price}",colour2,15,x,y+135,w,30)

def menu_display():
    if menuP == True:
        screen.fill(blue,(25,40,750,550))
        pickaxe_showcase_all(60,110,200,180,brown,1,"Free")
        pickaxe_showcase_all(300,110,200,180,grey,5,150)
        pickaxe_showcase_all(540,110,200,180,gold,10,"1,000")
        pickaxe_showcase_all(60,350,200,180,blue,25,"5,000")
        pickaxe_showcase_all(300,350,200,180,green,50,"100,000")
        pickaxe_showcase_all(540,350,200,180,purple,100,"1,000,000")
        if mode1 == "Equip":
            button(f"{mode1}",60,280,200,40,15,white,white,black,black,action = "equip1")
        else:
            button(f"{mode1}",60,280,200,40,15,green,green,white,white,action = "equip1")
        if buy2 == True:
            if mode2 == "Equip":
                button(f"{mode2}",300,280,200,40,15,white,white,black,black,action = "equip2")
            else:
                button(f"{mode2}",300,280,200,40,15,green,green,white,white,action = "equip2")
        else:
            button("Buy",300,280,200,40,15,red,red,white,white,action = "buy2")
        if buy3 == True:
            if mode3 == "Equip":
                button(f"{mode3}",540,280,200,40,15,white,white,black,black,action = "equip3")
            else:
                button(f"{mode3}",540,280,200,40,15,green,green,white,white,action = "equip3")
        else:
            button("Buy",540,280,200,40,15,red,red,white,white,action = "buy3")
        if buy4 == True:
            if mode4 == "Equip":
                button(f"{mode4}",60,520,200,40,15,white,white,black,black,action = "equip4")
            else:
                button(f"{mode4}",60,520,200,40,15,green,green,white,white,action = "equip4")
        else:
            button("Buy",60,520,200,40,15,red,red,white,white,action = "buy4")
        if buy5 == True:
            if mode5 == "Equip":
                button(f"{mode5}",300,520,200,40,15,white,white,black,black,action = "equip5")
            else:
                button(f"{mode5}",300,520,200,40,15,green,green,white,white,action = "equip5")
        else:
            button("Buy",300,520,200,40,15,red,red,white,white,action = "buy5")
        if buy6 == True:
            if mode6 == "Equip":
                button(f"{mode6}",540,520,200,40,15,white,white,black,black,action = "equip6")
            else:
                button(f"{mode6}",540,520,200,40,15,green,green,white,white,action = "equip6")
        else:
            button("Buy",540,520,200,40,15,red,red,white,white,action = "buy6")
    elif menuI == True:
        screen.fill(red,(25,40,750,550))
        island_showcase(60,110,200,180,dark_brown,white,1,"Free","Tree")
        island_showcase(300,110,200,180,white,black,5,"10,000","Tree")
        island_showcase(540,110,200,180,black_brown,white,10,"500,000","Tree")
        island_showcase(60,350,200,180,dark_green,white,"x1","Free","Leaf")
        island_showcase(300,350,200,180,red,white,"x2","50,000","Leaf")
        island_showcase(540,350,200,180,orange,white,"x4","150,000","Leaf")
        if mode21 == "Pick":
            button(f"{mode21}",60,280,200,40,15,white,white,black,black,action = "pick1")
        else:
            button(f"{mode21}",60,280,200,40,15,green,green,white,white,action = "pick1")
        if buy22 == True:
            if mode22 == "Pick":
                button(f"{mode22}",300,280,200,40,15,white,white,black,black,action = "pick2")
            else:
                button(f"{mode22}",300,280,200,40,15,green,green,white,white,action = "pick2")
        else:
            button("Buy",300,280,200,40,15,red,red,white,white,action = "buy22")
        if buy23 == True:
            if mode23 == "Pick":
                button(f"{mode23}",540,280,200,40,15,white,white,black,black,action = "pick3")
            else:
                button(f"{mode23}",540,280,200,40,15,green,green,white,white,action = "pick3")
        else:
            button("Buy",540,280,200,40,15,red,red,white,white,action = "buy23")
        
        if mode24 == "Pick":
            button(f"{mode24}",60,520,200,40,15,white,white,black,black,action = "pick4")
        else:
            button(f"{mode24}",60,520,200,40,15,green,green,white,white,action = "pick4")
        if buy25 == True:
            if mode25 == "Pick":
                button(f"{mode25}",300,520,200,40,15,white,white,black,black,action = "pick5")
            else:
                button(f"{mode25}",300,520,200,40,15,green,green,white,white,action = "pick5")
        else:
            button("Buy",300,520,200,40,15,red,red,white,white,action = "buy25")
        if buy26 == True:
            if mode26 == "Pick":
                button(f"{mode26}",540,520,200,40,15,white,white,black,black,action = "pick6")
            else:
                button(f"{mode26}",540,520,200,40,15,green,green,white,white,action = "pick6")
        else:
            button("Buy",540,520,200,40,15,red,red,white,white,action = "buy26")
    button("Pickaxe",25,40,150,50,28,red,white,white,black,action = "menu pickaxe")
    button("Island",200,40,150,50,28,red,white,white,black,action = "menu island")
    button("X",700,40,75,50,28,red,white,white,black,action = "menu close")
    text(f"Cash: {cash}",white,28,365,50,150,50,rect = False)
    pygame.draw.rect(screen,black,(25,40,10,550))
    pygame.draw.rect(screen,black,(25+750-10,40,10,550))
    pygame.draw.rect(screen,black,(25,40,750,10))
    pygame.draw.rect(screen,black,(25,40+550-10,750,10))

# Main_loop
while True:
    mouse = pygame.mouse.get_pos()
    screen.fill(white)
    background(450,350,475,TC,LC)
    if wait >= 75:
        pickaxe(False,typeC)
    else:
        pickaxe(True,typeC)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if 650 + 150 > mouse[0] > 650 and 0 + 50 > mouse[1] > 0:
            pass
        else:
            if 650 + 150 > mouse[0] > 650 and 75 + 50 > mouse[1] > 75:
                pass
            else:
                if menu == False:
                    if wait >= 75:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            wait = 0
                            wood = wood + (1*worth)
    wait = wait + 1
    if menu == False:
        button("Cash it",650,0,150,50,28,white,white,black,black,action = "cash it")
        button("Menu",650,75,150,50,28,white,white,black,black,action = "menu")
    else:
        button("Cash it",650,0,150,50,28,white,white,black,black)
        button("Menu",650,75,150,50,28,white,white,black,black)
    text(f"Wood: {wood}",black,28,0,11,150,50,rect = False)
    text(f"Cash: {cash}",black,28,0,86,150,50,rect = False)
    if menu == True:
        menu_display()
    pygame.display.update()
