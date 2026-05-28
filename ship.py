from PIL import ImageDraw

PINK_COLOR = (246, 71, 255)
SPEED_THRESHOLD = 100

class Spaceship:
    def __init__(self, name, x: int, y: int, width: int, height: int, speed: int, color: tuple=PINK_COLOR):
        self.name = name
        self._x = x
        self._y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        #para animação estacionária
        self._direction = 1  
        self._idle_factor = 0.25  # Reduz a velocidade para a animação estacionária
        self._idle_range = 7  # Alcance do movimento para a animação estacionária
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def speed(self):
        return self._speed 
    
    @property
    def idle_range(self):
        return self._idle_range
    
    @speed.setter
    def speed(self, value):
        if abs(value) < SPEED_THRESHOLD:
            self._speed = value
        else:
            self._speed = SPEED_THRESHOLD if value > 0 else -  SPEED_THRESHOLD

    def draw(self, drawer:ImageDraw.ImageDraw):
        top_left_x = self.x - (self.width // 2)
        top_left_y = self.y - (self.height // 2)
        bottom_right_x = self.x + (self.width // 2)
        bottom_right_y = self.y + (self.height // 2)

        drawer.rectangle((top_left_x, top_left_y, bottom_right_x, bottom_right_y), fill=self.color)

    def idle_target(self, bounds):
        return (bounds[0] // 2, bounds[1] // 2)

    def update_idle(self, bounds: tuple):
        self._y += self._speed * self._direction * self._idle_factor
        
        target = self.idle_target(bounds)
        if abs(self._y - target[1]) > self._idle_range:
            self._direction *= -1  # Inverte a direção para criar o movimento de vai e vem

    def update_intro(self, bounds: tuple):
        target_y = bounds[1] // 2

        if self._y > target_y:
            self._y -= self.speed

    def update_outro(self):
        if self._y + self.height // 2 > 0:
            self._y -= self.speed