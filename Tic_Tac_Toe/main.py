import pygame, sys
import time
from constants import *
from drawer import *
from check_board import *
from check_win import check_win
from restart import restart


pygame.init()


draw_lines()


player = 1
game_over = False


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)

			if available_square(clicked_row, clicked_col):
				mark_square(clicked_row, clicked_col, player)
				if check_win(player):
					game_over = True
				else:
					game_over = is_board_full()
				player = player % 2 + 1
				draw_figures()	

		if game_over:
			if event.type == pygame.MOUSEBUTTONUP:
				time.sleep(2)
				restart()
				player = 1
				game_over = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				game_over = False

	pygame.display.update()