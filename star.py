import random
from PIL import ImageDraw

STAR_COLOR = (255, 255, 255)
STAR_SIZES = (1, 2, 3)
STAR_SPEEDS = (1, 2, 3)

class Star:
    def __init__(self, center, size, speed, color=STAR_COLOR):
        self.x, self.y = center
        self.center = center
        self.size = size
        self.speed = speed
        self.color = color

    @staticmethod
    def create_random_star(xmax, ymax, color=STAR_COLOR):
        x = random.randint(0, xmax)
        y = random.randint(0, ymax)
        size = random.choice(STAR_SIZES)
        speed = random.choice(STAR_SPEEDS)
        return Star((x, y), size, speed, color)
    
    def draw(self, drawer: ImageDraw.ImageDraw):
        center = (self.x, self.y)
        drawer.circle(center, self.size, self.color)

    def update_position(self, bounds):
        self.y += self.speed  # Move the star downwards
        if self.y > bounds[1]:  # If the star goes beyond the bottom
            self.y = 0  # Reset to the top
            self.x = random.randint(0, bounds[0])  # Randomize x position

