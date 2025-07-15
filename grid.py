import pygame

class Cell:
    def __init__(self, row, col, cell_type="empty"):
        self.row = row
        self.col = col
        self.type = cell_type  # "empty", "car", "pedestrian", "wall", "goal", "start"
        self.image = self.load_image()

    def load_image(self):
        path_map = {
            "empty": "assets/empty.png",
            "car": "assets/car.png",
            "pedestrian": "assets/human.png",
            "wall": "assets/wall.png",
            "goal": "assets/goal.png",
            "start": "assets/start.png"
        }
        image_path = path_map.get(self.type, "assets/empty.png")
        try:
            return pygame.transform.scale(pygame.image.load(image_path), (50, 50))
        except:
            print(f"⚠️ Resim yüklenemedi: {image_path}")
            return pygame.Surface((50, 50))  # Boş yüzey döner

    def set_type(self, new_type):
        self.type = new_type
        self.image = self.load_image()

    def draw(self, surface, cell_size):
        surface.blit(self.image, (self.col * cell_size, self.row * cell_size))
