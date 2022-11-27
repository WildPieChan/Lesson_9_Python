from constants import *
from drawer import *

def restart():
	screen.fill(BG_COLOR)
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0