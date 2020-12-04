import pygame
import random
pygame.init()
window = pygame.display.set_mode((576, 750))
pygame.display.set_caption("New Window")
icon = pygame.image.load('assets/redbird-upflap.png')
pygame.display.set_icon(icon)


# Game variables
game_active = True
cheat_code = False
gravity = 0.20
bird_movement = 0

game_over = pygame.transform.scale2x(pygame.image.load('assets/message.png'))
game_over_rekked_bi = game_over.get_rect(center = (288, 375))

# Background
bg = pygame.image.load('assets/background-day.png').convert()
bg = pygame.transform.scale2x(bg)

window.blit(bg, (0,0))
# Floor
floorx = 0
floor = pygame.image.load('assets/base.png').convert()
floor = pygame.transform.scale2x(floor)
# Bird
bird = pygame.image.load('assets/bluebird-upflap.png').convert()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100,375))
#Pipe
Pipe = pygame.image.load('assets/pipe-green.png')
Pipe = pygame.transform.scale2x(Pipe)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)
pipe_height = [200,300,400]
def redraw_window():
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(120)
def draw_floor():
    window.blit(floor, (floorx,700))
    window.blit(floor, (floorx + 576,700))
def new_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_new_pipe = Pipe.get_rect(topright = (700, random_pipe_pos))
    top_pipe = Pipe.get_rect(bottomright = (700, random_pipe_pos - 300))
    return bottom_new_pipe,top_pipe
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3
    return pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 750:
            window.blit(Pipe, pipe)
        else:
            flip_pipe = pygame.transform.flip(Pipe, False, True)
            window.blit(flip_pipe,pipe)
def check_collision(pipes):
    if not cheat_code:
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                return False
        if bird_rect.top <= -50 or bird_rect.top >= 650:
            return False
        return True
    if cheat_code:
        return True
run = True
while run:
    # User Input
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_RSHIFT]:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                bird_movement = 0
                bird_movement -= 10
                bird = pygame.image.load('assets/bluebird-downflap.png').convert()
                bird = pygame.transform.scale2x(bird)
            if event.key == pygame.K_TAB:
                cheat_code = True
            if event.key == pygame.K_LSHIFT:
                cheat_code = False
            if game_active == False:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    game_active = True
                    pipe_list = []
                    bird_rect = bird.get_rect(center=(100,375))
                    bird = pygame.image.load('assets/bluebird-upflap.png').convert()
                    bird = pygame.transform.scale2x(bird)
                if event.key == pygame.K_TAB:
                    run =  False
                    print('')
                    print("Lmao")
        if event.type == pygame.KEYUP:
            bird = pygame.image.load('assets/bluebird-upflap.png').convert()
            bird = pygame.transform.scale2x(bird)
        if event.type == SPAWNPIPE:
            pipe_list.extend(new_pipe())
    window.blit(bg, (0,0))
    if game_active or cheat_code:
        # Gravity
        window.blit(bird, bird_rect)
        bird_movement += gravity
        bird_rect.centery += bird_movement
        game_active = check_collision(pipe_list)
        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        # floor
        floorx -= 1
        draw_floor()
    else:
        window.blit(game_over, game_over_rekked_bi)
    if floorx == -576:
        floorx = 0
    redraw_window()
pygame.quit()
