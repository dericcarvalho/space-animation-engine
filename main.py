from PIL import Image, ImageDraw
from star import Star
import os
from ship import Spaceship
from rocket import Rocket
from shield import Shield

BLACK = (0, 0, 0)
WIDTH = 720
HEIGHT = 1280
NUM_STARS = 50
MAX_FRAMES = 300

def save_gif(frames_dir, filepath, exclude=False, fps=30):
    filelist = sorted([f for f in os.listdir(frames_dir) if f.endswith(("png", "jpg", "jpeg"))])
    frames = [Image.open(os.path.join(frames_dir, f)) for f in filelist]
    frames[0].save(
        filepath,
        save_all=True,
        append_images=frames[1:],
        duration=1/fps,
        loop=0
    )
    if exclude:
        print("Excluding frames originais...")
        for f in filelist:
            os.remove(os.path.join(frames_dir, f))

def is_visible(ship: Spaceship, bounds) -> bool:
    left = ship.x - (ship.width // 2)
    right = ship.x + (ship.width // 2)
    top = ship.y - (ship.height // 2)
    bottom = ship.y + (ship.height // 2)  

    horizontal = right > 0 and left < bounds[0]
    vertical = bottom > 0 and top < bounds[1]
    return horizontal and vertical

def generate_animation(ship: Spaceship, idle_duration_frames=90):
    frames = []
    stars = [Star.create_random_star(WIDTH, HEIGHT) for i in range(NUM_STARS)]
    
    bounds = (WIDTH, HEIGHT)
    # for frame_idx in range(NUM_FRAMES):
    animation = "intro"
    idle_frames = 0
    frame_idx = 0
    while animation != "done" and frame_idx < MAX_FRAMES:
        img = Image.new("RGB", (WIDTH, HEIGHT), BLACK)
        drawer = ImageDraw.Draw(img)
        for star in stars:
            star.draw(drawer)
            star.update_position(bounds)

        if animation == "intro":
            ship.update_intro(bounds)
            if ship.y - ship.idle_target(bounds)[1] < ship.idle_range:
                animation = "idle"
        elif animation == "idle":
            ship.update_idle(bounds)
            idle_frames += 1
            if idle_frames >= idle_duration_frames:
                animation = "outro"
        elif animation == "outro":
            ship.update_outro()
            if not is_visible(ship, bounds):
                animation = "done"
        ship.draw(drawer)
        frames.append(img)
    return frames

def main(output_dir: str):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    ship = Spaceship("Hallship", WIDTH // 2, HEIGHT, 60, 90, 7)
    shield = Shield(WIDTH // 2, HEIGHT, 25, 0, 7, 90 + 8, (220, 20, 60))
    ship = Rocket("Atlas", WIDTH // 2, HEIGHT, 60, 90, 7, color=(71, 138, 255), acc=1, shield=shield)
    frames = generate_animation(ship)
    print("Animação finalizada")
    [img.save(os.path.join(output_dir, f"{frame_idx:04d}.png")) for frame_idx, img in enumerate(frames)]
    print("Gerando GIF...")
    filename = f"{ship.name}.gif"
    gifpath = os.path.join("runs", "gifs", filename)
    save_gif(output_dir, gifpath, exclude=True)
    print(f"GIF salvo em {gifpath}")

if __name__ == "__main__":
    output_dir = "runs/frames"
    main(output_dir)