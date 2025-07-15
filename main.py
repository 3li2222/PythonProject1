import pygame
from settings import WIDTH, HEIGHT, CELL_SIZE, ROWS, COLS, WHITE
from grid import Cell
from astar import astar
from vehicle import Vehicle
from pedestrian import PedestrianManager

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Akıllı Araç Simülasyonu")
clock = pygame.time.Clock()

# Grid matrisi oluştur
grid = [[Cell(r, c) for c in range(COLS)] for r in range(ROWS)]

# Başlangıç değişkenleri
start = None
end = None
vehicle = None
pedestrians = PedestrianManager()
path = []

running = True
while running:
    screen.fill(WHITE)

    # 🎮 Kullanıcı Etkileşimi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // CELL_SIZE, x // CELL_SIZE
            cell = grid[row][col]

            if event.button == 1:  # Sol tık
                if not start:
                    start = (row, col)
                    cell.set_type("start")
                elif not end and (row, col) != start:
                    end = (row, col)
                    cell.set_type("goal")
                    path = astar(start, end, grid)
                    vehicle = Vehicle(start, path)

            elif event.button == 3:  # Sağ tık
                if cell.type == "empty":
                    cell.set_type("pedestrian")
                    pedestrians.add_pedestrian((row, col))

    # 🧍 Yayaları hareket ettir
    if vehicle:
        pedestrians.move_pedestrians(grid, vehicle.pos)

    # 🟨 Grid’i çiz
    for row in grid:
        for cell in row:
            cell.draw(screen, CELL_SIZE)

    # 🚶 Yayaları çiz
    pedestrians.draw(screen)

    # 🚗 Aracı hareket ettir ve çiz
    if vehicle:
        vehicle.move(screen)
        vehicle.draw(screen)

    pygame.display.flip()
    clock.tick(2)

pygame.quit()
