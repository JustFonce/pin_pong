from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

rocket1 = Player('player.png', 30, 200, 100, 100, 50)
rocket2 = Player('player.png', 520, 200, 100, 100, 50)
ball = GameSprite('ball.png', 200, 200, 50, 50, 10)

speed_x = 3
speed_y = 3

font.init()
GameFont = font.Font(None, 35)
player1_win = GameFont.render('PLAYER 1 WON', True, (180, 0, 0))
player2_win = GameFont.render('PLAYER 2 WON', True, (180, 0, 0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rocket1.update_l()
        rocket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(player1_win, (150, 250))
        if ball.rect.x > win_width:
            finish = True
            window.blit(player2_win, (150, 250))
        rocket1.reset()
        rocket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)