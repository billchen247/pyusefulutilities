import pyautogui
import time
import threading
import random
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

# Function to create a basic icon
def create_image():
    image = Image.new("RGB", (64, 64), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((16, 16, 48, 48), fill="green")
    return image

# Activity simulation function
def keep_active(interval_minutes, stop_event):
    while not stop_event.is_set():
        x, y = pyautogui.position()
        dx = random.randint(-3, 3)
        dy = random.randint(-3, 3)
        pyautogui.moveRel(dx, dy, duration=0.1)
        pyautogui.moveRel(-dx, -dy, duration=0.1)
        time.sleep(interval_minutes * 60)

# Start the background thread
def run_tray_app():
    stop_event = threading.Event()
    thread = threading.Thread(target=keep_active, args=(3, stop_event), daemon=True)
    thread.start()

    def on_quit(icon, item):
        stop_event.set()
        icon.stop()

    menu = Menu(MenuItem("Quit", on_quit))
    icon = Icon("Teams Keeper", create_image(), "Teams Status Keeper", menu)
    icon.run()

# Start everything
if __name__ == "__main__":
    run_tray_app()

