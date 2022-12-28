#screen.blit(walk_right[n], (player.rect.x, player.rect.y))
import pygame
from pygame import *

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600))
width = 800
height = 600
tile = 40
pygame.display.set_caption("Game")

bg = pygame.image.load('bg.png')
player = pygame.image.load('front.png')
walk_right = [
	pygame.image.load('right1.png'),
	pygame.image.load('right2.png')
]

walk_left = [
	pygame.image.load('left1.png'),
	pygame.image.load('left2.png')
]

stay = [
	pygame.image.load('front.png')
]

platform_img = [
	pygame.image.load('tile.png')
]

level = [
	'####################',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#                  #',
	'#              #####',
	'#     #            #',
	'####################'
]

def collision(player_speed_x, player_speed_y, platforms_list):
	for p in platforms_list:
		if player_rect.colliderect(p):
			print(1)
			if player_speed_x > 0:
				player_rect.right = p.rect.left
			elif player_speed_x < 0:
				player_rect.left = p.rect.right
			elif player_speed_y > 0:
				player_rect.bottom = p.rect.top
				player_speed_y = 0
				on_ground = True
			elif player_speed_y < 0:
				player_rect.top = p.rect.bottom
				player_speed_y = 0




def player_move(left, right, jump, platforms_list):
    global on_ground, player_speed_x, player_speed_y, player_x, player_y, jump_count, keys
    if left:
        player_speed_x = -speed
        if n == 0:
            screen.blit(walk_left[n], (player_x, player_y))
        else:
            screen.blit(walk_left[n], (player_x, player_y))
    if right:
        player_speed_x = speed
        if n == 0:
            screen.blit(walk_right[n], (player_x, player_y))
        else:
            screen.blit(walk_right[n], (player_x, player_y))

    if not (left or right):
        screen.blit(stay[0], (player_x, player_y))
        player_speed_x = 0

    if on_ground and jump:
        player_speed_y = -jump_count
        on_ground = False
    if not on_ground:
        player_speed_y += graviti

    player_x += player_speed_x
    collision(player_speed_x, 0, platforms_list)
    player_y += player_speed_y
    collision(0, player_speed_y, platforms_list)


n = 0
count = 0
player_speed_x = 0
player_speed_y = 0
speed = 10
player_x = 80
player_y = 520
graviti = 0.35
on_ground = True
jump_count = 10
FPS = 10
left = False
right = False
jump = False
platforms_list = []

running = True
while running:
	screen.blit(bg, (0, 0))

	player_rect = stay[0].get_rect(topleft=(tile, tile))
	objects = pygame.sprite.Group()

	for y in range(len(level)):
		for x in range(len(level[y])):
			coord_x = x * tile
			coord_y = y * tile

			if level[y][x] == "#":
				tile_sprite = sprite.Sprite()
				tile_sprite.image = image.load("tile.png")
				tile_sprite.rect = Rect(coord_x, coord_y, tile, tile)
				screen.blit(platform_img[0], (tile * x, tile * y))

				platforms_list.append(tile_sprite)
				objects.add(tile_sprite)

	keys = pygame.key.get_pressed()
	for e in pygame.event.get():
		if e.type == QUIT:
			exit()
		if e.type == KEYDOWN and e.key in [K_LEFT, K_a]:
			left = True
		if e.type == KEYDOWN and e.key in [K_RIGHT, K_d]:
			right = True
		if e.type == KEYDOWN and e.key in [K_UP, K_SPACE, K_w]:
			jump = True

		if e.type == KEYUP and e.key in [K_LEFT, K_a]:
			left = False
		if e.type == KEYUP and e.key in [K_RIGHT, K_d]:
			right = False
		if e.type == KEYUP and e.key in [K_UP, K_SPACE, K_w]:
			jump = False

	player_move(left, right, jump, platforms_list)
	collision(player_speed_x, player_speed_y, platforms_list)

	#for p in platforms_list:      #?
		#if player_rect.colliderect(p):         #?
			#on_ground = True            #?
	#else:
		#if player_y < 554:
			#player_y += 1

	keys = pygame.key.get_pressed()

	if n == 1:
		n = 0
	else:
		n += 1

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

	clock.tick(FPS)
