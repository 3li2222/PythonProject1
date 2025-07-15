# pedestrian.py

import random
from settings import ROWS, COLS, DIRECTIONS, CELL_SIZE
from grid import Cell
import pygame

class PedestrianManager:
    def __init__(self):
        self.positions = []  # [(row, col), ...]

    def add_pedestrian(self, pos):
        if pos not in self.positions:
            self.positions.append(pos)

    def move_pedestrians(self, grid_matrix, car_pos):
        new_positions = []
        for r, c in self.positions:
            random.shuffle(DIRECTIONS)
            moved = False
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if grid_matrix[nr][nc].type == "empty" and (nr, nc) not in self.positions and (nr, nc) != car_pos:
                        new_positions.append((nr, nc))
                        moved = True
                        break
            if not moved:
                new_positions.append((r, c))  # hareket edemediyse yerinde kal
        self.positions = new_positions

    def draw(self, surface):
        for r, c in self.positions:
            human_img = Cell(r, c, "pedestrian").image
            surface.blit(human_img, (c * CELL_SIZE, r * CELL_SIZE))
