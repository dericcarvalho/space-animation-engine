from PIL import ImageDraw
from PIL import Image
from utils import rotation_matrix
import numpy as np
import os

class Shield:
    def __init__(self, x:int, y:int, radius:int, 
                 theta:int,
                 speed: int,
                 orbit:int, 
                 color:tuple):
        self._x = x
        self._y = y
        self.radius = radius
        self.theta = theta
        self.speed = speed
        self.color = color
        self.orbit = orbit

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def draw(self, drawer:ImageDraw.ImageDraw):
        cx = self.orbit + self.radius
        cy = 0
        rot = rotation_matrix(self.theta) @ np.array([cx, cy])
        rot += np.array([self.x, self.y])

        drawer.circle(rot, self.radius, self.color)



if __name__== '__main__':
    outdir = "runs/debug"
    w, h = 720, 1080
    color = (220, 20, 60)
    orbit = 100
    for theta in range(0, 360, 2):
        img = Image.new('RGB', (w, h), (0, 0, 0))
        drawer = ImageDraw.Draw(img)
        shield = Shield(w//2, h//2, 40, theta, orbit, color)
        shield.draw(drawer)
        img.save(os.path.join(outdir, f"{theta:04d}.png"))
    print("DONE!")