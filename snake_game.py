import pygame
import random
import math
import time

# from Snake import snake
pygame.init()


scl = 25
GREY = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (255, 0, 100)
BLUE = (0,0,255)


# Screen dimension
height = 800
width = 800
tail = []
total = 0
lengthmax = 2
food = []
food.append(random.randrange(50, width-50))
food.append(random.randrange(200, height - 50))

# Display Scrren
screen = pygame.display.set_mode((width, height))
# Game Caption
pygame.display.set_caption('Snake Do Feed')
# Fonts
head_font = pygame.font.Font('freesansbold.ttf', 50)
score_font = pygame.font.Font('freesansbold.ttf', 35)
running = True
food_icon = pygame.image.load('food.png')
snake = []
snake.append(random.randrange(50, width-50))
snake.append(random.randrange(200, height))
x_speed = 1
y_speed = 0

tail = []


def heading():
    Heading_text = head_font.render('Welcome to the Snake Game', True, WHITE)
    screen.blit(Heading_text, (50, 50))


def update_snake():

    global snake, tail, total, update
    if total:
        if total == len(tail):
            tail.pop(0)

    pos = [snake[0], snake[1]]
    append_snake(total, pos)

    if snake[0] > width-scl:
        snake[0] -= 1
        print(1)
    elif snake[0] < 0:
        snake[0] = 0
        print(2)
    elif snake[1] > height-scl:
        snake[1] -= 1
        print(3)
    elif snake[1] < 0:
        snake[1] = 0
        print(4)
    else:
        snake[0] += x_speed
        snake[1] += y_speed


def append_snake(n, pos):
    global tail, snake
    # raise the length of sake
    if n > 0:
        tail.insert(n-1, pos)


def change_dir(x, y):
    global x_speed
    global y_speed
    x_speed = x
    y_speed = y


def pickLocation():
    global food
    food[0] = random.randrange(50, width - 50)
    food[1] = random.randrange(200, height - 50)


def distance(x1, x2, y1, y2):
    res = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
    return res


def eat_change():
    # snake eat
    global total, tail
    dis = math.floor(distance(snake[0], food[0], snake[1], food[1]))

    if(dis < 20):
        total += 20
        return True
    else:
        return False


def show(n):
    # show the snake
    global total
    for i in range(len(tail)):
        pygame.draw.rect(screen, RED, (tail[i][0], tail[i][1], scl, scl))

    pygame.draw.rect(screen, WHITE, (snake[0], snake[1], scl, scl))


game_text = pygame.font.Font('freesansbold.ttf', 70)



def death():
    global tail, snake, total
    pos_cur = [snake[0], snake[1]]
    if total > 20:
        for i, num in enumerate(tail):
            if(num[0] == pos_cur[0]):
                if(num[1] == pos_cur[1]):
                    print('game over')
                    total = 0
                    del tail[:]
                    game_over_text()
            # print(num)


def game_over_text():
    # game pver text
    global running
    text = "GAME OVER"
    over_text = game_text.render(text, True, WHITE)
    screen.blit(over_text, (width/4, height/2))
    running = False
    time.sleep(5)
    
def show_score():
    global total
    score = 'Score = ' +str(total / 20)
    score_text = score_font.render(score, True, BLUE)
    screen.blit(score_text, (width/2-100, height/4-50))

clock = pygame.time.Clock()
while running:
    update = False

    screen.fill(GREY)
    heading()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False
        if event.type is pygame.KEYDOWN:
            # get input
            if event.key == pygame.K_LEFT:
                change_dir(-1, 0)

            elif event.key == pygame.K_RIGHT:
                change_dir(1, 0)

            elif event.key == pygame.K_UP:
                change_dir(0, -1)

            elif event.key == pygame.K_DOWN:
                change_dir(0, 1)

            elif event.key == pygame.K_SPACE:
                total += 20

    if eat_change():
        update = True
        pickLocation()

    
    death()
    update_snake()
    show(total)
    show_score()
    screen.blit(food_icon, (food[0], food[1]))

    pygame.display.update()
