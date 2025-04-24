import pyautogui
import time
import random

def keep_active(interval_minutes=5):
    print("Starting Teams availability keeper. Press Ctrl+C to stop.")
    try:
        while True:
            x, y = pyautogui.position()
            move_x = random.randint(-3, 3)
            move_y = random.randint(-3, 3)
            pyautogui.moveRel(move_x, move_y, duration=0.1)
            pyautogui.moveRel(-move_x, -move_y, duration=0.1)
            print(f"Simulated activity at {time.strftime('%H:%M:%S')}")
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("Stopped.")

# Run the script
keep_active(interval_minutes=3)

