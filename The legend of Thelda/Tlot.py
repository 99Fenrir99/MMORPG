from pygame import *
from random import randint

window = display.set_mode((1000, 1000))
display.set_caption("Shooter")

back_x = 0
back_y = 0

# шрифти і написи
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)
win = font1.render('YOU ARE WIN!', True, (255, 255, 255))
lose = font1.render('YOU ARE LOST', True, (180, 0, 0))
font2 = font.Font(None, 36)

img_back = "back.png"  # фон гри
img_hero = "player.png"  # герой

score = 0 
moveright = False
moveleft = False
moveup = False
movedown = False
quest1 = False
quest1start = False
quest2start = False
haveOak = False
needxp = 100
havexp = 0
talk = False
wait = 200
killedfire = 0
fire1a = True
fire1b = True
fire1c = True
fire1d = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
 
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
     return self.rect.colliderect(rect)
 
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 100:
            global moveleft
            moveleft = True

        if keys[K_d] and self.rect.x < win_width - 160:
            global moveright
            moveright = True

        if keys[K_w] and self.rect.x < win_width - 160:
            global moveup
            moveup = True

        if keys[K_s] and self.rect.x < win_width - 160:
            global movedown
            movedown = True

        if keys[K_e]:
            global talk
            talk = True
 
 
# клас спрайта-ворога
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        
       


win_width = 700
win_height = 700
display.set_caption("TloT")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (7000, 7000))

mixer.init()
mixer.music.load("Ost.mp3")
mixer.music.play()
 
player = Player("Player.png", win_width - 400, win_height - 400, 70, 100, 7)
Quest1 = GameSprite("quest1.png", 1480, 2600, 200, 200, 0)
Quest2 = GameSprite("quest2.png", 3860, 600, 200, 200, 0)
wood = GameSprite("wood.png", 175, 2800, 200, 200, 0)
fire1 = Player("fire_left.png", 5100, 1880, 100, 100, 3)
fire2 = Player("fire_left.png", 5100, 1680, 100, 100, 3)
fire3 = Player("fire_right.png", 6000, 1600, 100, 100, 3)
fire4 = Player("fire_right.png", 6000, 1900, 100, 100, 3)

speedx = 5
speedy = 5


finish = False
run = True 
 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (back_x, back_y))
        text1 = font2.render("Досвід " + str(havexp) + " / " + str(needxp), 1, (255, 255, 255))
        window.blit(text1, (10, 20))
        text1 = font2.render("Рівень " + str(score), 1, (255, 255, 255))
        window.blit(text1, (10, 50))

            
        player.update()

        player.reset()
        Quest1.reset()
        Quest2.reset()
        wood.reset()

        if movedown == True:
            back_y -= 4
            Quest1.rect.y -= 4
            wood.rect.y -= 4
            Quest2.rect.y -= 4
            fire1.rect.y -= 4
            fire2.rect.y -= 4
            fire3.rect.y -= 4
            fire4.rect.y -= 4
            movedown = False
        if moveup == True:
            back_y += 4
            Quest1.rect.y += 4
            wood.rect.y += 4
            Quest2.rect.y += 4
            fire1.rect.y += 4
            fire2.rect.y += 4
            fire3.rect.y += 4
            fire4.rect.y += 4
            moveup = False
        if moveleft == True:
            back_x += 4
            Quest1.rect.x += 4
            wood.rect.x += 4
            Quest2.rect.x += 4
            fire1.rect.x += 4
            fire2.rect.x += 4
            fire3.rect.x += 4
            fire4.rect.x += 4
            moveleft = False
        if moveright == True:
            back_x -= 4
            Quest1.rect.x -= 4
            wood.rect.x -= 4
            Quest2.rect.x -= 4
            fire1.rect.x -= 4
            fire2.rect.x -= 4
            fire3.rect.x -= 4
            fire4.rect.x -= 4
            moveright = False
        
        if player.rect.colliderect(Quest1) and talk == True and quest1start == False:
            text2 = font2.render("Привіт, можешь принести дерево з моєї скрині?", 1, (255, 255, 255))
            text3 = font2.render("Я дам хорошу нагороду", 1, (255, 255, 255))
            window.blit(text2, (10, 300))
            window.blit(text3, (10, 320))
            if wait >= 0:
                wait -=1
            else:
                talk = False
                quest1start = True
                wait = 200


        if player.rect.colliderect(wood) and talk == True and haveOak == False:
            text2 = font2.render('"Ви взяли дерево"', 1, (255, 255, 255))
            window.blit(text2, (10, 300))
            if wait >= 0:
                wait -=1
            else:
                talk = False
                haveOak = True
                wait = 200
        
        if player.rect.colliderect(Quest1) and talk == True and quest1start == True and haveOak == True:
            text2 = font2.render("Дякую, ти дуже допоміг мені", 1, (255, 255, 255))
            text3 = font2.render("Ось нагорода", 1, (255, 255, 255))
            window.blit(text2, (10, 300))
            window.blit(text3, (10, 320))
            if wait >= 0:
                wait -=1
            else:
                talk = False
                quest1start = False
                haveOak = False
                havexp += 800
                wait = 200

        if player.rect.colliderect(Quest2) and talk == True and quest2start == False and score >= 25:
            text2 = font2.render("Привіт, потуши будь ласка моє село", 1, (255, 255, 255))
            text3 = font2.render("Я дам хорошу нагороду", 1, (255, 255, 255))
            window.blit(text2, (10, 300))
            window.blit(text3, (10, 320))
            if wait >= 0:
                wait -=1
            else:
                talk = False
                quest2start = True
                wait = 200

        if quest2start == True and fire1a == True:
            fire1.reset()

        if quest2start == True and fire1b == True:
            fire2.reset()
        
        if quest2start == True and fire1c == True:
            fire3.reset()

        if quest2start == True and fire1d == True:
            fire4.reset()

        if player.rect.colliderect(fire1) and talk == True and quest2start == True:
            killedfire += 1
            fire1a = False
            talk = False

        if player.rect.colliderect(fire2) and talk == True and quest2start == True:
            killedfire += 1
            fire1b = False
            talk = False
        
        if player.rect.colliderect(fire3) and talk == True and quest2start == True:
            killedfire += 1
            fire1c = False
            talk = False
        
        if player.rect.colliderect(fire4) and talk == True and quest2start == True:
            killedfire += 1
            fire1d = False
            talk = False

        if player.rect.colliderect(Quest2) and talk == True and quest2start == True and killedfire >= 4:
            text2 = font2.render("Дякую тобі, ти врятував моє село!", 1, (255, 255, 255))
            text3 = font2.render("Ось, тримай", 1, (255, 255, 255))
            window.blit(text2, (10, 300))
            window.blit(text3, (10, 320))
            if wait >= 0:
                wait -=1
            else:
                talk = False
                quest2start = False
                havexp += 1700
                fire1a = True
                fire1b = True
                fire1c = True
                fire1d = True
                wait = 200 


        

        if score >= 100:
            finish = True
            window.blit(win, (200, 200))

        if havexp >= needxp:
            havexp -= needxp
            needxp += 50
            score += 1

 
        display.update()
    time.delay(7)