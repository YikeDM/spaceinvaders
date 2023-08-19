import pygame, sys, random

random.seed()

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = [self.x, self.y, 10, 10]
        self.state = 1
        self.speed = 15
        self.image = pygame.image.load("bullet.bmp")
        self.rect = self.image.get_rect(center = (self.x + 50, self.y))

    def movebullet(self):
        if self.state:
            for i, x in enumerate(enemy):
                if self.rect.colliderect(enemy[i].rect):
                    enemy[i].ishit()
                    self.state = 0

            
            self.rect[1] -= 15

    def initialize(self):
        if self.state:
            screen.blit(self.image, self.rect)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 1
        self.image = pygame.image.load("player.bmp")
        self.speed = 15

    def initialize(self):
        screen.blit(self.image, (self.x, self.y))
    
    def fire(self):
        global bullet_list
        bullet_list.append(Bullet(self.x, self.y))
        global previous_time
    
    def move(self, a):
        if a == 1:
            if self.x > 0 and self.x < 1000:
                self.x -= self.speed
            else:
                self.x += self.speed*2

        if a == 0:
            if self.x > 0 and self.x < 1000:
                self.x += self.speed
            else:
                self.x -= self.speed*2

class Alien:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 5
        self.hit_box = [self.x, self.y, 100, 50]
        self.state = 1
        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect(center = (self.x + 50, self.y))
    
    def ishit(self):
        self.health -= 2.5

        if self.health == 0:
            self.state = 0
        
    #initalize more accurately update, this goes for all initalize in project.
    def initialize(self):
        if self.state:
            screen.blit(self.image, self.rect)

    #this update function is for moving randomly on state, more accurately update_position
    def update(self):
        if self.state != 0:
            #move down randomly towards player
            if random.randint(1, 40) == 1:
                move_enemy()
            pygame.draw.rect(screen, (255,0,0), self.hit_box, 2)
        else:
            self.image = 0
            #draw visible hitbox

def endgame(a):
    global game
    game = 0
    if a:
        screen.blit(winner, (0,0))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
    else:
        screen.blit(loser, (0,0))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

def updatesprites():
    temp = 0

#moves enemy, enemy.y is obsolete as using rect to blit
def move_enemy():
    global enemy
    for i, x in enumerate(enemy):
        enemy[i].y += 10
        enemy[i].rect[1] += 10
        enemy[i].hit_box[1] += 10
        if enemy[i].y > 600:
            endgame(0)


pygame.init()

# pre game setup
screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Space Invaders")
mainmenu = pygame.image.load("mainmenu.png")
background = pygame.image.load("background.png")
winner = pygame.image.load("winner.png")
loser = pygame.image.load("loser.png")
previous_time = pygame.time.get_ticks()


while 1:
    game = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            if mouse[0] in range(330, 750) and mouse[1] in range(440, 620):
               # pygame.draw.rect(mouse[0], mouse[1])   
                game = 1

    # add menu here

    if game == 1:
        enemy = [Alien(100, 30), Alien(200,30), Alien(300,30), Alien(400, 30), Alien(500, 30), \
        Alien(600, 30), Alien(700, 30), Alien(800,30), Alien(900,30)]

        bullet_list = []

        player1 = Player(540, 600)  
        while game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE:
                        current_time = pygame.time.get_ticks()
                        if current_time - previous_time > 1000:
                            player1.fire()
                            previous_time = current_time

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player1.move(1)
            
            if keys[pygame.K_d]:
                player1.move(0)


            screen.blit(background, (0, 0))

            count1 = 0
            for i, x in enumerate(enemy):
                enemy[i].initialize()
                if enemy[i].state:
                    count1 += 1
            
        

            if count1 == 0:
                endgame(1)

            for i, x in enumerate(bullet_list):
                bullet_list[i].movebullet()
                bullet_list[i].initialize()

            player1.initialize()

            for Alien in enemy:
                Alien.update()
            
            pygame.display.flip()
            pygame.time.wait(30)
            

    
    screen.fill((255,255,255))
    screen.blit(mainmenu, (0,0))



    pygame.display.update()
    # above ^^

