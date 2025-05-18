from pygame import *
font.init()
window = display.set_mode((700, 500))
display.set_caption('пинг-понг')  
fon = transform.scale(image.load("fon.jpg"), (700, 500))
speed_x = 3
speed_y = 3
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180,0,0))
font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSE!', True, (180,0,0))
class GameSprite(sprite.Sprite):
   # Создаём новый объект
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))  # загружаем картинку и уменьшаем её
        self.speed = player_speed  # задаём скорость движения
        self.rect = self.image.get_rect()  # получаем прямоугольник, в котором находится картинка
        self.rect.x = player_x  # ставим объект на начальную позицию по горизонтали
        self.rect.y = player_y  # ставим объект на начальную позицию по вертикали
        self.width = size_x
        self.height = size_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

player1 = Player('raketka-Photoroom.png', 550, 20, 140, 120, 5)
player2 = Player('raketka-Photoroom.png', 5, 20, 140, 120, 5)
ball = GameSprite('balle-Photoroom.png', 200, 100, 50, 50, 3)

finish = False
game = True
FPS = 60
clock = time.Clock()

while game:
    for e in event.get():  # проверяем события в игре
        if e.type == QUIT:  # еслaи нажали на крестик
            game = False  # закрываем игру\

    if finish != True:
        window.blit(fon, (0,0))
        player1.update_r()
        player1.reset()
        player2.update_l()
        player2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (250,250))
    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (250,250))
    display.update()
    clock.tick(FPS)