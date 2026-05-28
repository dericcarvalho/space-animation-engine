from ship import Spaceship, PINK_COLOR
from PIL import ImageDraw
from shield import Shield

class Rocket(Spaceship):
    def __init__(self, name, x, y, width, height, speed, color=PINK_COLOR, acc=0.0, shield: Shield=None):
        super().__init__(name, x, y, width, height, speed, color)
        self.acceleration = acc
        self.shield = shield

    def draw(self, drawer: ImageDraw.ImageDraw):
        super().draw(drawer)

        # Coordenadas centrais e dimensões
        cx, cy = self.x, self.y
        w, h = self.width, self.height
        base_y = cy + h // 2   # ponto inferior do corpo, onde a chama começa

        # Chama tripla
        flame_w = w * 0.6
        flame_h = h * 0.5

        # Chama externa (vermelha, maior)
        drawer.polygon([
            (cx - flame_w / 2, base_y),
            (cx + flame_w / 2, base_y),
            (cx, base_y + flame_h)
        ], fill=(220, 20, 20))

        # Chama intermediária (laranja)
        flame_w2 = flame_w * 0.7
        flame_h2 = flame_h * 0.8
        drawer.polygon([
            (cx - flame_w2 / 2, base_y),
            (cx + flame_w2 / 2, base_y),
            (cx, base_y + flame_h2)
        ], fill=(255, 140, 0))

        # Chama interna (amarelo claro)
        flame_w3 = flame_w * 0.4
        flame_h3 = flame_h * 0.6
        drawer.polygon([
            (cx - flame_w3 / 2, base_y),
            (cx + flame_w3 / 2, base_y),
            (cx, base_y + flame_h3)
        ], fill=(255, 255, 100))

        # Janela da cabine
        window_radius = w * 0.15
        window_cy = cy - h * 0.1  # ligeiramente acima do centro
        drawer.ellipse([
            cx - window_radius, window_cy - window_radius,
            cx + window_radius, window_cy + window_radius
        ], fill=(135, 206, 250), outline=(0, 0, 100), width=2)

        # Aletas estabilizadoras
        fin_w = w * 0.2
        fin_h = h * 0.3
        fin_y_top = cy + h // 2 - fin_h

        # Aleta esquerda
        drawer.polygon([
            (cx - w // 2, fin_y_top),
            (cx - w // 2 - fin_w, cy + h // 2),
            (cx - w // 2, cy + h // 2)
        ], fill=(120, 120, 120), outline=(60, 60, 60))

        # Aleta direita
        drawer.polygon([
            (cx + w // 2, fin_y_top),
            (cx + w // 2 + fin_w, cy + h // 2),
            (cx + w // 2, cy + h // 2)
        ], fill=(120, 120, 120), outline=(60, 60, 60))

        self.shield._x = self.x
        self.shield._y = self.y
        self.shield.draw(drawer)

    def update_intro(self, bounds):
        super().update_intro(bounds)
        self.shield.theta += self.shield.speed

    def update_idle(self, bounds):
        super().update_idle(bounds)
        self.shield.theta += self.shield.speed

    def update_outro(self):
        super().update_outro()
        self.speed += self.acceleration
        self.shield.theta += self.shield.speed 