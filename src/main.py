import time
import os
import argparse
import alive_progress
from terminaltexteffects.effects.effect_waves import Waves
from terminaltexteffects.effects.effect_slide import Slide

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--duration", type=float)
parser.add_argument("-i", "--interval", type=float)
args = parser.parse_args()

duration = args.duration
interval = args.interval

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def wave_animated_text(text: str) -> str:
    effect = Waves(text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol = " ") as terminal:
        for frame in effect:
            terminal.print(frame)

def slide_animated_prompt(prompt_text: str) -> str:
    effect = Slide(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
    return input()

if duration is None and interval is None:
    text1 = """
 __        _______ _     ____ ___  __  __ _____   _____ ___  
 \ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \ 
  \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |
   \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| | 
    \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/ 
"""
    text2 = """
  _____ ___   ____ _   _ ____    _____ ___ __  __ _____ ____  
 |  ___/ _ \ / ___| | | / ___|  |_   _|_ _|  \/  | ____|  _ \ 
 | |_ | | | | |   | | | \___ \    | |  | || |\/| |  _| | |_) |
 |  _|| |_| | |___| |_| |___) |   | |  | || |  | | |___|  _ < 
 |_|   \___/ \____|\___/|____/    |_| |___|_|  |_|_____|_| \_\\


"""
    clear()
    wave_animated_text(text1 + text2)


if duration is None:
    duration = float(slide_animated_prompt("How long would you like your focus session in minutes? "))
if interval is None:
    interval = float(slide_animated_prompt("How long would you like the intervals to be in minutes? "))

def countdown():
    print("Starting timer...")
    time.sleep(1.2)
    print("3\r", end = "")
    time.sleep(1)
    print("2\r", end = "")
    time.sleep(1)
    print("1\r", end = "")
    time.sleep(1)

def timer(count):
    start_time = time.time()
    with alive_progress.alive_bar(count + 1) as bar:
        
        while time.time() - start_time < count + 1:
            time_left = ((count - (time.time() - start_time)) // 1) + 1
            if time_left > 60:
                minutes = time_left // 60
                seconds = time_left % 60
                #print(f"Time left: {minutes} minutes and {seconds} seconds\r", end = "")
                time.sleep(1)
                bar()
            else:
                #print(f"Time left: {time_left} seconds                     \r", end = "")
                time.sleep(1)
                bar()

def minutes_to_seconds(minutes):
    return minutes * 60


def timer_loop(duration, interval):
    duration = minutes_to_seconds(duration)
    interval = minutes_to_seconds(interval)
    cycles = int(duration) // int(interval) 
    count = 1
    focus = """
  _____ ___   ____ _   _ ____  
 |  ___/ _ \ / ___| | | / ___| 
 | |_ | | | | |   | | | \___ \ 
 |  _|| |_| | |___| |_| |___) |
 |_|   \___/ \____|\___/|____/ 
                               
\n
"""
    finish = """
  _____ ___ _   _ ___ ____  _   _ _____ ____  
 |  ___|_ _| \ | |_ _/ ___|| | | | ____|  _ \ 
 | |_   | ||  \| || |\___ \| |_| |  _| | | | |
 |  _|  | || |\  || | ___) |  _  | |___| |_| |
 |_|   |___|_| \_|___|____/|_| |_|_____|____/ \n                                              
"""
    countdown()
    for i in range(cycles):
#       if count > 1:
#          print(f"\nTimer {count}")
        count += 1
        timer(int(interval))
        clear()
        if count < cycles:
            wave_animated_text(focus)
        else:
            wave_animated_text(finish)



timer_loop(duration, interval)
