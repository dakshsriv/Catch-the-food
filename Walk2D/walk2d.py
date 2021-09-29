import pygame, time
pygame.init()

win = pygame.display.set_mode((1920,1080))

pygame.display.set_caption("Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
smallkey = pygame.image.load('smallkey.jpeg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

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
text = myfont.render(f'x {key_found}', 1, (10,10,10))
run = True
bg = pygame.image.load("walls_base_img.jpg")
bg = pygame.transform.scale(bg, (1900, 1060))
g = pygame.image.load("floor.jpeg")
g = pygame.transform.scale(g, (1500, 760))
ld = pygame.image.load("locked-door.png")
ld = pygame.transform.scale(ld, (770,440))
d = pygame.image.load("door.png")
d = pygame.transform.scale(d, (770,440))
smallkey = pygame.transform.scale(smallkey, (70, 70))
pleft = False
pright = False
pstanding = True
room = 1
vel = 5
walkCount = 0
dct = {"1" : "k n n 1l n"} # keys = room numbers, values = "object up right down left")"
dct2 = {"1l": "l"}
#mainloop



def redrawGameWindow(walkCount, key_found, x, y, room):
     
    win.blit(bg, (0,0))
    win.blit(g, (210, 170))
    #keys2 = myfont.render(f" x {keys}", False, (0, 0, 0))
    #win.blit(keys2, (0, 780))
    if room != 15:
        parts = dct[str(room)].split()
        if parts[0] == "k":
#            print(ll)
#             
            if not key_found:
                print("yeahblit")
                win.blit(smallkey, (410, 410))
                if x > 360 and x < 460 and y > 360 and y < 460: 
                    #print("flag")
                    key_found = True
             
        if parts[1] == "d":
            win.blit(d, (750, 50))
        elif parts[1] in dct2.keys():
            win.blit(ld, (750, 50))
        if parts[2] == "d":
            win.blit(d, (1800, 450))
        elif parts[2] in dct2.keys():
            win.blit(ld, (1800, 450))
        if parts[3] == "d":
            win.blit(d, (750, 950))
        elif "1l" in dct2.keys():
            i = parts[3]
            c = dct2[i]
            #print(c)
            if c == "l":
                win.blit(ld, (600, 700))
                print(x, y)
                if x > 700 and x < 800 and y > 700 and y < 800 and key_found:
                    print("Sharp")
                    dct2["1l"] = "o"
                    key_found = False
            if c == "o":
                win.blit(d, (600, 700))
                if x > 550 and x < 650 and y > 650 and y < 750:
                    pass
                    # room += 3
                    # y -= 300
        if parts[4] == "d":
            win.blit(d, (1800, 50))
        elif parts[4] in dct2.keys():
            win.blit(ld, (1800, 50))

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
    return key_found


run = True
while run:
    #print(f"ks: {key_found}")
    clock.tick(27)
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
    elif key[pygame.K_DOWN] and y < 980 - height - vel:
        y += vel
        pright = False
        pleft = False       
    elif key[pygame.K_UP] and y > vel:
        y -= vel
        pright = False
        pleft = False
    #print(f"3, {key_found}")       
    key_found = redrawGameWindow(walkCount, key_found, x, y, room)

