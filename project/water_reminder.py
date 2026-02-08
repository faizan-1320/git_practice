import time
from plyer import notification
import os
from playsound import playsound
import threading

# ✅ Get absolute path of icon and sound
icon_path = os.path.abspath("water.ico")
sound_path = os.path.abspath("water.mp3")  # Optional

def play_sound():
    threading.Thread(target=playsound, args=(sound_path,), daemon=True).start()

def remind_water():
    while True:
        notification.notify(
            title="💧 Water Reminder",
            message="Pani Pilo! Hydration zaroori hai 💦",
            app_icon=icon_path,  # ✅ Custom icon
            timeout=10
        )
        play_sound()  # ✅ Optional sound
        time.sleep(900)  # 15 min

if __name__ == "__main__":
    remind_water()
