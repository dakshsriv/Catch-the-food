import pygame, time
pygame.init()

win = pygame.display.set_mode((1920,1080))

pygame.display.set_caption("Escape the building!")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
smallkey = pygame.image.load('smallkey.png')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

keys = 0
x = 1300
y = 700
width = 64
height = 64
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
key_found = False
pwr = 0
myfont = pygame.font.SysFont("Times New Roman", 50)
run = True
bg = pygame.image.load("walls_base_img.jpg")
bg = pygame.transform.scale(bg, (1900, 1060))
g = pygame.image.load("floor.jpeg")
g = pygame.transform.scale(g, (1500, 760))
ld = pygame.image.load("locked-door.png")
ld = pygame.transform.scale(ld, (770,440))
d = pygame.image.load("door.png")
d = pygame.transform.scale(d, (770,440))
smallkey = pygame.transform.scale(smallkey, (100, 100))
pleft = False
pright = False
pstanding = True
room = 1
vel = 5
walkCount = 0
dct = {"1" : "k n n 1l n"} # keys = room numbers, values = "object up right down left")"
lockedDoors = {"1l": "l"}
#mainloop



def redrawGameWindow(walkCount, key_found, x, y, room, keys):
    text = myfont.render(f'You have {keys} keys', 1, (220,10,10))
    win.blit(bg, (0,0))
    win.blit(g, (210, 170))
    win.blit(text, (1400, 50))
    #keys2 = myfont.render(f" x {keys}", False, (0, 0, 0))
    #win.blit(keys2, (0, 780))
    if room != 15:
        parts = dct[str(room)].split()
        if parts[0] == "k":           
            if not key_found:
                win.blit(smallkey, (410, 410))
                if x > 360 and x < 460 and y > 360 and y < 460: 
                    key_found = True
                    keys += 1
             
        if parts[1] == "d":
            win.blit(d, (750, 50))
        elif parts[1] in lockedDoors.keys():
            win.blit(ld, (750, 50))
        if parts[2] == "d":
            win.blit(d, (1800, 450))
        elif parts[2] in lockedDoors.keys():
            win.blit(ld, (1800, 450))
        if parts[3] == "d":
            win.blit(d, (750, 950))
        elif "1l" in lockedDoors.keys():
            i = parts[3]
            c = lockedDoors[i]
            #print(c)
            if c == "l":
                win.blit(ld, (600, 700))
            if c == "o":
                win.blit(d, (600, 700))
                if x > 800 and x < 1000 and y > 700 and y < 900:
                    #pass
                    #print(keys)
                    keys -= 1
                    room += 3
                    y -= 800
        if parts[4] == "d":
            win.blit(d, (1800, 50))
        elif parts[4] in lockedDoors.keys():
            win.blit(ld, (1800, 50))
        if x > 800 and x < 1000 and y > 800 and y < 1000 and key_found:
                lockedDoors["1l"] = "o"
        #if room == 1: # Bring to front
        #    win.blit(ld, (600,700))
    if pleft:  
        r = pygame.transform.scale(walkLeft[int((walkCount % 27)/3)], (128, 128))
        win.blit(r, (x,y))
        walkCount += 1                       
    elif pright:
        r = pygame.transform.scale(walkRight[int((walkCount % 27)/3)], (128, 128))
        win.blit(r, (x,y))
        walkCount += 1
    else:
        r = pygame.transform.scale(char, (128, 128))
        win.blit(r, (x, y))
    pygame.display.update()
    #print(f"{key_found=}")
    return key_found, keys


run = True
while run:
    #print(f"ks: {key_found}")
    clock.tick(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > vel:
        x -= vel
        pleft = True
        pright = False
        walkCount += 1
    elif key[pygame.K_RIGHT] and x < 1720 - width - vel:
        x += vel
        pright = True
        pleft = False
        walkCount += 1
    if key[pygame.K_DOWN] and y < 980 - height - vel:
        y += vel
        pright = False
        pleft = False       
    elif key[pygame.K_UP] and y > vel:
        y -= vel
        pright = False
        pleft = False
    #print(f"3, {key_found}")       
    key_found, keys = redrawGameWindow(walkCount, key_found, x, y, room, keys)
    keys = keys