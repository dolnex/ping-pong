from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


'''class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 85:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 85:
            self.rect.x += self.speed'''

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(80, 620)
            self.rect.y = 0

blue = (200,255,255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('pygame window')
clock = time.Clock()
FPS = 60
window.fill(blue)

player1 = Player()
player2 = Player()
ball = Enemy()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()
