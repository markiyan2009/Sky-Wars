# фігня з пулями виправити
from pygame import*
from time import time as timer
from random import randint

font.init()
mixer.init()
main_win = display.set_mode((500,700))
background = transform.scale(image.load("img/background.jpg"),(500,700))
mixer.music.load("background.mp3")

font1 = font.Font(None,80)
font2 = font.Font(None,36) 

nx = 50
ny = 50

class Area():
    def __init__(self,main_win ,x,y,width,height):
        self.main_win=main_win
        self.rect = Rect(x,y,width,height)
        self.fill_color = (255,255,255)
    def fill(self):
        draw.rect(self.main_win,self.fill_color,self.rect)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
class Label(Area):
    def set_text(self,text,fsize=12,text_color=(0,0,0)):
        self.image = font.Font(None,fsize).render(text,True,text_color) 
    def draw(self):
        self.fill()
        self.main_win.blit(self.image,(self.rect.x,self.rect.y))

        

class GameSprite(sprite.Sprite):
    def __init__(self,main_win, p_image,size_x,size_y, x, y, speed,hp,atack,weapon_type,rocket_in_bort):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = "rigth"
        self.hp = hp
        self.atack = atack
        self.bullets = sprite.Group()
        self.num_fire_bullets = 0
        self.rel_time_bullets = False
        self.max_fire_rockets =rocket_in_bort
        self.rockets = sprite.Group()
        self.num_fire_rockets = 0
        self.main_win =main_win
        
        
        
    
    def reset(self):
        
        self.main_win.blit(self.image,(self.rect.x,self.rect.y ))
    



class Plane(GameSprite):
    def update(self): 
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <650:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x <450:
            self.rect.x += self.speed
        if self.hp <= 0:
            self.kill()

        
            
    def fire_bullet(self):
        
        self.bullet = Bullet(player)
        
        self.bullets.add(self.bullet)
    def fire_rocket(self):
        self.rocket = Rocket(self)
        self.rockets.add(self.rocket)

        
class Fashist(GameSprite):
    
    
    def update(self):
        if self.rect.x > nx +200:
            self.direction ="left"
        if self.rect.x < nx -200:
            self.direction ="rigth"
        if self.direction =="rigth":
            self.rect.x +=self.speed
        if self.direction == "up":
            self.rect.y -= self.speed
        if self.direction == "down":
            self.rect.y += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.hp <= 0:
            self.kill()
        if sprite.spritecollide(self,player.bullets,True):
            self.hp -= player.atack
        
        
    def fire_bullet(self):
        self.bullet = Bullet(self)
            
        self.bullets.add(self.bullet)
    

class Bullet():
    def __init__(self,folower_of):
        self.image = transform.scale(image.load("img/bullet.png"),(25,25))
        self.rect = self.image.get_rect()
        self.rect.x = folower_of.rect.centerx
        self.rect.y = folower_of.rect.top
        self.speed = 20
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
class Rocket():
    def __init__(self,folower_of):
        self.image = transform.scale(image.load("img/bullet.png"),(25,25))
        self.rect = self.image.get_rect()
        self.rect.x = folower_of.rect.centerx
        self.rect.y = folower_of.rect.top
        self.speed = 10
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

rocket_atack = 100
finish = False
display.set_caption('Sky Wars')

fps = 30
clock = time.Clock()
shoot = mixer.Sound("fire.ogg")




enemies = sprite.Group()
player = Plane(main_win,"img/plane1.png",75,75,200,200,10,5,1,True,1)
for i in range(1,5):
    enemy = Fashist(main_win,"img/enemy1.png",75,75,nx,ny,5,3,2,True,1)
    nx += 50
    enemies.add(enemy)
mixer.music.play()


WHITE = (0,0,0)
buttonPlay = Label(main_win,200,300,100,50)
buttonPlay.set_text("PLAY",50,WHITE)
buttonExit = Label(main_win,200,400,100,50)
buttonExit.set_text("EXIT",50,WHITE)

def start_game():
    game = True
    while game:
        
        display.update()
        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if player.num_fire_bullets <= 5 and player.rel_time_bullets == False:
                        time.delay(10)
                        shoot.play()
                        player.fire_bullet()
                        player.num_fire_bullets += 1
                    if player.num_fire_bullets >= 5 and player.rel_time_bullets == False:
                        player.rel_time_bullets = True
                        last_time = timer()

                    
            
            
        if finish != True:
            main_win.blit(background,(0,0))
            
            enemies.draw(main_win)
            enemies.update()
            
            player.bullets.draw(main_win)
            player.bullets.update()
            player.reset()
            player.update()
            player.rockets.update()
            if player.rel_time_bullets == True:
                now_time = timer()
                if now_time - last_time <=3:
                    reload = font2.render("Wait reload...",1,(150,0,0))
                    main_win.blit(reload,(200,100))
                else:
                    player.num_fire_bullets = 0
                    player.rel_time_bullets = False
            
                
            display.update()
            
             
        clock.tick(fps)
menu = True
fontMenu = font.Font(None,75).render("SKY WARS  ",True,(0,0,180))

while menu: 
    main_win.blit(fontMenu,(100,100))
    if not finish:
        buttonPlay.draw()
        buttonExit.draw()
        enemies.clear(main_win,background)
        player.kill()
        player.bullets.clear(main_win,background)
        display.update()
        
    for e in event.get():
        if e.type == QUIT:
            menu = False
        if e.type == MOUSEBUTTONDOWN:
            x,y = mouse.get_pos()
            if buttonPlay.collidepoint(x,y):
                start_game()
            if buttonExit.collidepoint(x,y):
                menu = False
    main_win.blit(background,(0,0)) 