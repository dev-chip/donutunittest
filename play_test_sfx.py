
import os
import sys
real_path = os.path.dirname(os.path.realpath(__file__))
from playsound import playsound
import random


def play_homer_test_failed():
    sfx_path = os.path.join(real_path, "sfx", "simpsons")
    sfx_options = [f for f in os.listdir(sfx_path) if ".wav" in f]
    if len(sfx_options) > 0:
        filepath = os.path.join(sfx_path,sfx_options[random.randint(0,len(sfx_options)-1)])
        playsound(filepath)
    else:
        print("Failed to play homer SFX: No .wav files found")


def play_test_success():
    sfx_path = os.path.join(real_path, "sfx", "success")
    filepath = os.path.join(sfx_path, "success.wav")
    playsound(filepath)


if __name__ == "__main__":
    print("playing success...")
    play_test_success()
    print("playing fail...")
    play_homer_test_failed()
