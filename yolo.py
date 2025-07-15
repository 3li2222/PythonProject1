import pygame
import numpy as np
from ultralytics import YOLO

# Model yükleniyor (önceden eğitilmiş veya senin eğittiğin)
model = YOLO("yolov8n.pt")  # veya kendi modelin yoluyla değiştir

def surface_to_numpy(surface):
    """Pygame Surface → NumPy RGB image"""
    raw = pygame.image.tostring(surface, "RGB")
    return np.frombuffer(raw, dtype=np.uint8).reshape((surface.get_height(), surface.get_width(), 3))

def contains_human(surface):
    """YOLO ile insan içerip içermediğini kontrol eder"""
    image = surface_to_numpy(surface)
    results = model.predict(image, verbose=False)

    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:  # class 0 = person (COCO dataset)
                return True
    return False
