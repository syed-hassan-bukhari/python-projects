import time
import pygame
import os

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def Alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}⏳ Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    # Play Alarm sound
    pygame.mixer.init()
    sound_path = os.path.join(os.path.dirname(__file__), "Alarm.mp3")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)  # Loop until stopped

    print("\n🔔 ALARM! Press Enter to stop.")
    input()
    pygame.mixer.music.stop()
    print("✅ Alarm stopped. Goodbye!")

# Ask user how many minutes to wait
minutes = int(input("How many minutes to wait: "))
Alarm(minutes * 60)
