import pygame
pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 750
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30,30)
player = pygame.Rect(1180, (screen_height / 2) - 70, 15, 150)
enemy = pygame.Rect(10, (screen_height / 2) - 70, 15, 150)

# Players
print("Player Name: ")
Player = input()
print("Enemy Name: ")
Enemy = input()

# Game Timer
start_ticks = pygame.time.get_ticks()

ball_speed_x = 3
ball_speed_y = 3

# Text vars
text_x = screen_width / 2 - 150
text_y = 60
player_score = 0
enemy_score = 0
win = "How did you see the source code?"
game_font = pygame.font.Font("04B_19.ttf", 32)
rules = pygame.font.Font("04B_19.ttf", 16)

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.colliderect(player) or ball.colliderect(enemy):
        ball_speed_x *= -1

def character_bordering():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if enemy.top <= 0:
        enemy.top = 0
    if enemy.bottom >= screen_height:
        enemy.bottom = screen_height

run =  True
start =  False
while run:
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Player Movement
    if keys[pygame.K_SPACE]:
        start = True

    if keys[pygame.K_DOWN]:
        player.y += 7
    if keys[pygame.K_UP]:
        player.y -= 7

    if keys[pygame.K_s]:
        enemy.y += 7
    if keys[pygame.K_w]:
        enemy.y -= 7
    if keys[pygame.K_q]:
        run = False
    if keys[pygame.K_RSHIFT]:
        player_score += 1
    
    # Special Conditionals
    if start:
        ball_animation()
    if ball.left <= 0:
        start = False
        ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30,30)
        player_score += 1
    if ball.right >= screen_width:
        start = False
        ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30,30)
        enemy_score += 1
    if player_score > enemy_score:
        win = "{} Is Winning!".format(Player)
    if player_score < enemy_score:
        win = "{} Is Winning!".format(Enemy)
    if player_score == enemy_score:
        win = "It's currently a tie!"
    if player_score >= 5:
        win = "{} won!\nPlay Again?".format(Player)
        if keys[pygame.K_SPACE]:
            enemy_score = 0
            player_score = 0
    if enemy_score >= 5:
        win = "{} won! \nPlay Again?".format(Enemy)
        if keys[pygame.K_SPACE]:
            enemy_score = 0
            player_score = 0
    if seconds == 210:
        win = "Time Is Up"
        ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30,30)
        enemy_score = 0
        player_score = 0
        pygame.time.delay(5000)
        run = False
    if seconds == 200:
        timer = game_font.render(f"{seconds}", False, (255, 200, 200))
        window.blit(timer, (screen_width / 2 - 15, 100))
    character_bordering()
    # time shit
    pygame.display.update()
    clock.tick(120)
    # Visuals
    window.fill((50, 50, 50))
    pygame.draw.ellipse(window, (255, 255, 255), ball)
    pygame.draw.rect(window, (255, 255, 255), player)
    pygame.draw.rect(window, (255, 255, 255), enemy)
    pygame.draw.aaline(window, (pygame.Color('lightgrey')), (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.ellipse(window, (255, 255, 255), ball)

    enemy_text = game_font.render(f"{enemy_score}", False, (200, 200, 200))
    window.blit(enemy_text, (screen_width / 2 - 100, 10))
    player_text = game_font.render(f"{player_score}", False, (200, 200, 200))
    window.blit(player_text, (screen_width / 2 + 100, 10))
    win_text = game_font.render(f"{win}", False, (200, 200, 200))
    window.blit(win_text, (text_x, text_y))
    if not seconds == 200:
        timer = game_font.render(f"{seconds}", False, (200, 200, 200))
        window.blit(timer, (screen_width / 2 - 15, 100))
    disclaimer = rules.render("If the timer reaches 210 You both Lose", False, (200, 200, 200))
    window.blit(disclaimer, (screen_width / 2 - 150, 600))
        
    
pygame.quit()
