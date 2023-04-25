from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w = 200, h = 100):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 600:
            self.rect.y += self.speed        

        
class Player2(GameSprite):
    def update(self):
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 600:
            self.rect.y += self.speed


class Enemy(GameSprite):
    def update(self):
        '''self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(80, 620)
            self.rect.y = 0'''

blue = (200,255,255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('pygame window')
clock = time.Clock()
FPS = 60


player1 = Player('platform.png',10,50,4,20,500)
player2 = Player2('platform.png',660,50,4,20,500)
ball = Enemy('ball.png',100,200,4,140,80)

run = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys = key.get_pressed()
    if run != True:
        window.fill(blue)
        clock.tick(FPS)
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()



    display.update()