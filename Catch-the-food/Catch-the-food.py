#!/usr/bin/python3

# BTW This took 2 hours 
import pygame
import random
import time

dec = 4
pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((1920,1080))
loops = 0
loss = False
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
myfont = pygame.font.Font(None, 55)
myfont2 = pygame.font.Font(None, 220)
banana = pygame.image.load("banana.png")
apple = pygame.image.load("apple.png")
apple = pygame.transform.scale(apple, (150,150))
apples = int()
bananas = int()
pygame.display.set_caption("DiscDodger")
fruit1Sound = pygame.mixer.Sound('bullet.wav')
run = True
hit = pygame.mixer.Sound("hit.wav")
clock = pygame.time.Clock()
falling = []
bg = pygame.image.load("bg.jpeg")
bg = pygame.transform.scale(bg, (1920, 1080)) 
btime = time.clock()
atime = btime + 1.1
totalfruit = 0
class projectile(object):
    def __init__(self,x,y,fruit):
        self.x = x
        self.y = y
        self.fruit = fruit
        self.catch = False
        self.catchpos = 0

    def draw(self,win):
        #pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        if self.fruit == "apple":
            win.blit(apple, (self.x, self.y))
        else:
            win.blit(banana, (self.x, self.y))
        fruit1Sound.play()

class player(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.acc = 0
        self.vel = 0
        self.left = False
        self.right = False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        #self.hitbox = (self.x + 17, self.y + 11)
        ellipse = pygame.draw.ellipse(win, (255,0,0), (self.x-80, self.y-50, 600, 50))
        #pygame.draw.circle(win, (255,0,0), (self.x, self.y), 35, 0)

    def hit(self, index, totalfruit, apples, bananas):
        hit.play()
        totalfruit += 1
        tf = falling[index]
        if tf.fruit == "apple":
            apples += 1
        else:
            bananas += 1
        return totalfruit, apples, bananas
        
        
text5 = myfont2.render("NICE TRY!", 1, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
disc = player(960, 1000)
while run:
    if loss:
        clock.tick(10)
        pygame.draw.rect(win, (0, 0, 0), (0, 0, 2000, 3000))
        win.blit(text4, (200, 600))
        win.blit(text5, (600, 200))
        for x in range(0, random.randint(4, 8)):
            win.blit(banana, (random.randint(100,1600), 800))
            win.blit(apple, (random.randint(100,1600), 800))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    else:
        text1 = myfont.render(f"Apples: {apples}", 8, (255, 0,0))
        text2 = myfont.render(f"Bananas: {bananas}", 1, (255, 0,0))
        text3 = myfont.render(f"Fruit: {totalfruit}", 1, (255, 0,0))
        clock.tick(60)
        loops += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.blit(bg, (0,0))
        win.blit(text1,(800,100))
        win.blit(text2,(800,150))
        win.blit(text3,(800,200))
        text4 = myfont.render(f"""You survived for {round(loops/60)} secs, and caught {totalfruit} fruits, in which there are {apples} apples and {bananas} bananas.""", 1, (0, 255, 0))
        atime = time.clock()
        if atime - btime > dec:
            dec -= 0.1
            btime = time.clock()
            global fruit1
            x = random.randint(1,2)
            if x == 1:
                fruit1 = projectile(random.randint(100,1800), 0, "apple") # random.randint(100,1800)
            else:
                fruit1 = projectile(random.randint(100,1800), 0, "banana") # random.randint(100,1800)
            falling.append(fruit1)
        for fruit1 in falling:
            fruit1.draw(win)
            if fruit1.y < 1090:
                fruit1.y += 14
                ydiff = disc.y - fruit1.y
                xdiff = disc.x - fruit1.x
                if ydiff < 80 and ydiff > 5 and xdiff > -600 and xdiff < 300 and fruit1.catch == False:
                    tfs, appless, bnn = disc.hit(falling.index(fruit1), totalfruit, apples, bananas)
                    fruit1.catch = True
                    totalfruit = tfs
                    apples = appless
                    bananas = bnn
                if fruit1.catch == True:
                    if fruit1.catchpos == 0:
                        fruit1.catchpos = random.randint(50,450)
                    fruit1.x = disc.x + fruit1.catchpos
                    fruit1.y = disc.y - 170
                    
            else:
                falling.pop(falling.index(fruit1))
                loss = True
        """for fruit1 in falling:
            if fruit1.x < 1930 and fruuit1.x > -10:
                fruit1.x += fruit1.velx
            else:
                falling.pop(falling.index(fruit1))
            if fruit1.y < 1090 and fruit1.y > -10:
                fruit1.y += fruit1.vely
                fruit1.draw(win)
            else:
                try:
                    falling.pop(falling.index(fruit1))
                except:
                    pass"""
        keys = pygame.key.get_pressed()
        z = keys[pygame.K_LEFT]
        y = keys[pygame.K_RIGHT]
        if z:
            disc.acc = -1
            #print(disc.acc)
        elif y:
            disc.acc = 1
            #print(disc.acc)
        if disc.x > 1920:
            disc.x = 1920
            disc.acc = 0
            disc.vel = 0
        if disc.x < 0:
            disc.x = 0
            disc.acc = 0
            disc.vel = 0
        disc.vel = disc.vel + disc.acc
        disc.x += disc.vel
        #disc.x += disc.acc
        disc.draw(win)
        
        
        #fruit1Sound.play()
        #if len(falling) < 5:
        #    falling.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), random.randint(1,12)))
        pygame.display.update()
