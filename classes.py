from pygame import*
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
        
        bullet = Bullet(player)
        
        self.bullets.add(bullet)
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
        
        
    def fire_bullet(self):
        self.bullet = Bullet(self)
            
        self.bullets.add(self.bullet)
    

class Bullet(sprite.Sprite):
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