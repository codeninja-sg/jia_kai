import pygame
import pygame.locals
import pygame.math
import random

class Game:
    def __init__(self, name = "My Game", screensize = (800,600)):
        print ("Loading game: "+name)
        pygame.init()

        Game.game = self


        self.sprites = pygame.sprite.Group()
        
        self.screensize = screensize
        displayoptions = (pygame.HWSURFACE | pygame.SCALED)
        self.display = pygame.display.set_mode(screensize, displayoptions)
        self.clock = pygame.time.Clock()
        self.eventlist = []
        self.background_colour = (250,250,250)
        self.exit = False
        pygame.display.set_caption(name)
    
    def update(self, deltaTime):
        for event in self.eventlist:
            self.processEvent(event)
        self.sprites.update()

    def processEvent(self, event):
        if event.type == pygame.QUIT:
            self.exit = True

    def draw(self):
        self.display.fill(self.background_colour)
        self.sprites.draw(self.display)

    def run(self):
        print("run")
        while not self.exit:
            deltaTime = self.clock.tick(60)
            self.eventlist = pygame.event.get()
            self.update(deltaTime)
            self.sprites.update()
            self.draw()
            pygame.display.update()
        pygame.quit


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x,y):
        print("paddle init")
        super().__init__()
        self.image = pygame.Surface([15,80])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
    

class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super() .__init__()
        self.image = pygame.image.load("pongball.png")
        self.image = pygame.transform.scale(self.image,(15,15))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = pygame.math.Vector2(6,3)

    def bounce(self):

        if self.rect.centerx >= 785:
            self.velocity.x = self.velocity.x *-1

        if self.rect.centerx <= 15:
            self.velocity.x = self.velocity.x *-1
        
        if self.rect.centery >= 585:
            self.velocity.y = self.velocity.y *-1

        if self.rect.centery <= 15 :
            self.velocity.y = self.velocity.y *-1



    
    def update(self):
        #print(self.velocity)
        #print(self.velocity.x)
        vx,vy = self.velocity
        self.rect.centerx += vx
        self.rect.centery += vy     
        self.bounce()
        if Game.game.player1.rect.colliderect(self):
            collision_point = self.rect.centery - Game.game.player1.rect.top
            if collision_point > 40 and collision_point <:
                print("top collide")
            self.velocity.x *= -1
        if Game.game.player1.rect.colliderect(self):
            self.velocity.x += -1
           
            #self.rect.centerx *= random.randint(1,5)
        if Game.game.player2.rect.colliderect(self):
            self.velocity.x = self.velocity.x *-1





class PongGame(Game):
    def __init__(self):
        print("Pong init")
        super().__init__(name = "Pong")
        # self.player1.image = pygame.Surface([15,80])
        # self.player1.image.fill((0,0,0))
        # self.player1.rect = self.player1/image.get_rect()
        self.player1 = Paddle(45,300)
        self.player2 = Paddle(755 ,300)
        self.ball= Ball(400,300)
        self.sprites.add(self.player1 , self.player2 , self.ball) 
        control_up = False
        control_down = False
    
    def collide(self):
        if self.ball.colliderect(self.player1):
            print("hitttttttttttttttttttttttttttttttttt")



    def processEvent(self, event):
        super().processEvent(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("W pressed")
                self.player1.rect.centery = self.player1.rect.centery - 25
                if self.player1.rect.y <= 0 :
                    self.player1.rect.y = 0

            if event.key == pygame.K_s:
                print("S pressed")
                self.player1.rect.centery = self.player1.rect.centery + 25
                if self.player1.rect.y >= 520 :
                    self.player1.rect.y = 520

            if event.key == pygame.K_DOWN:
                print("down arrow pressed")
                self.player2.rect.centery = self.player2.rect.centery + 25
                if self.player2.rect.y <= 0 :
                    self.player2.rect.y = 0

            if event.key == pygame.K_UP:
                print("up arrow pressed")
                self.player2.rect.centery = self.player2.rect.centery - 25
                if self.player2.rect.y >= 520 :
                    self.player2.rect.y = 520

            
        if event.type == pygame.KEYUP:
            if pygame.locals.K_w:
                print("W released") 
            if pygame.locals.K_s:
                print("S released")        






PongGame().run()