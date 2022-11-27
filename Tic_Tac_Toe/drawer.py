import pygame
import numpy as np
from constants import *


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)


# Return a new array of given shape and type, filled with zeros.
board = np.zeros((BOARD_ROWS, BOARD_COLS)) 

def draw_lines():
	# 1 horizontal
	pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), 
                                (WIDTH, SQUARE_SIZE), LINE_WIDTH)
	# 2 horizontal
	pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), 
                                (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
	# 1 vertical
	pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), 
                                (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
	# 2 vertical
	pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), 
                                (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle(screen, CIRCLE_COLOR, 
                                    (int(col * SQUARE_SIZE + SQUARE_SIZE//2), 
                                        int(row * SQUARE_SIZE + SQUARE_SIZE//2)), 
                                                        CIRCLE_RADIUS, CIRCLE_WIDTH)
			elif board[row][col] == 2:
				pygame.draw.line(screen, CROSS_COLOR, 
									(col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
										(col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
											CROSS_WIDTH)	
				pygame.draw.line(screen, CROSS_COLOR, 
									(col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
										(col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
											CROSS_WIDTH)

def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)

def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)

def mark_square(row, col, player):
	board[row][col] = player