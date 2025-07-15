from grid import Cell
from yolovision import contains_human
from settings import CELL_SIZE

class Vehicle:
    def __init__(self, start_pos, path):
        self.pos = start_pos
        self.path = path  # [(x, y), (x, y), ...]
        self.step = 0

    def get_next_position(self):
        if self.step < len(self.path):
            return self.path[self.step]
        return None

    def get_front_cells(self):
        if not self.get_next_position():
            return []

        r, c = self.pos
        nr, nc = self.get_next_position()
        dr, dc = nr - r, nc - c

        if dr == -1:  # yukarı
            return [(r-1, c), (r-1, c-1), (r-1, c+1)]
        elif dr == 1:  # aşağı
            return [(r+1, c), (r+1, c-1), (r+1, c+1)]
        elif dc == -1:  # sola
            return [(r, c-1), (r-1, c-1), (r+1, c-1)]
        elif dc == 1:  # sağa
            return [(r, c+1), (r-1, c+1), (r+1, c+1)]
        return []

    def check_front_for_humans(self, screen):
        front_cells = self.get_front_cells()
        for r, c in front_cells:
            if 0 <= r < 10 and 0 <= c < 10:
                sub_surface = screen.subsurface(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE).copy()
                if contains_human(sub_surface):
                    return True
        return False

    def move(self, screen):
        next_pos = self.get_next_position()
        if next_pos and not self.check_front_for_humans(screen):
            self.pos = next_pos
            self.step += 1

    def draw(self, surface):
        car_img = Cell(self.pos[0], self.pos[1], "car").image
        surface.blit(car_img, (self.pos[1]*CELL_SIZE, self.pos[0]*CELL_SIZE))
