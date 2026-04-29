
import argparse
import os
import time
import alive_progress
from terminaltexteffects.effects.effect_slide import Slide
from terminaltexteffects.effects.effect_smoke import Smoke
from terminaltexteffects.effects.effect_waves import Waves

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--duration", type=float)
parser.add_argument("-i", "--interval", type=float)
args = parser.parse_args()

duration = args.duration
interval = args.interval


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wave_animated_text(text: str) -> str:
    effect = Waves(text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)

def smoke_animated_text(text: str) -> str:
    effect = Smoke(text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)

def slide_animated_prompt(prompt_text: str) -> str:
    effect = Slide(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
    return input()

def slide_animated_text(prompt_text: str) -> str:
    effect = Slide(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)


if duration is None and interval is None:
    text1 = r"""
 __        _______ _     ____ ___  __  __ _____   _____ ___
 \ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \
  \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |
   \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| |
    \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/

"""
    text2 = r"""
  _____ ___   ____ _   _ ____    _____ ___ __  __ _____ ____
 |  ___/ _ \ / ___| | | / ___|  |_   _|_ _|  \/  | ____|  _ \
 | |_ | | | | |   | | | \___ \    | |  | || |\/| |  _| | |_) |
 |  _|| |_| | |___| |_| |___) |   | |  | || |  | | |___|  _ <
 |_|   \___/ \____|\___/|____/    |_| |___|_|  |_|_____|_| \_\


"""
    clear()
    wave_animated_text(text1 + text2)
    slide_animated_text("""
This CLI tool is designed to help you reclaim your focus through structured, interval-based work sessions. By combining minimalist time management with high-energy terminal animations, it turns your focus blocks into a more engaging experience.
Whether you are deep-diving into a coding project or grinding through daily tasks, this timer keeps you on track with, interval nudges, visual progress, and a dynamic UI.
Just set your total duration, choose your intervals, and let the timer handle the rest. Stay focused, and stay productive.""")
   

if duration is None:
    duration = float(
        slide_animated_prompt("How long would you like your focus session in minutes? ")
    )
if interval is None:
    interval = float(
        slide_animated_prompt(
            "How long would you like the intervals to be in minutes? "
        )
    )

def countdown():
    clear()
    slide_animated_text(r"""
  ____ _____  _    ____ _____ ___ _   _  ____   _____ ___ __  __ _____ ____              
 / ___|_   _|/ \  |  _ \_   _|_ _| \ | |/ ___| |_   _|_ _|  \/  | ____|  _ \            
 \___ \ | | / _ \ | |_) || |  | ||  \| | |  _    | |  | || |\/| |  _| | |_) |            
  ___) || |/ ___ \|  _ < | |  | || |\  | |_| |   | |  | || |  | | |___|  _ <   _   _   _
 |____/ |_/_/   \_\_| \_\|_| |___|_| \_|\____|   |_| |___|_|  |_|_____|_| \_\ (_) (_) (_)
                                                                                         
                                                                                         
""")
    time.sleep(1.2)
    clear()
    slide_animated_text(r"""  
  _____
 |___ /
   |_ \
  ___) |
 |____/

        """)
    time.sleep(1)
    clear()
    slide_animated_text(r"""
  ____  
 |___ \
   __) |
  / __/
 |_____|

    """)
    time.sleep(1)
    clear()
    slide_animated_text(r"""
  _
 / |
 | |
 | |
 |_|

    """)
    time.sleep(1)
    clear()
    slide_animated_text(r"""
  ____ _____  _    ____ _____
 / ___|_   _|/ \  |  _ \_   _|
 \___ \ | | / _ \ | |_) || |  
  ___) || |/ ___ \|  _ < | |  
 |____/ |_/_/   \_\_| \_\|_|  
                            
    """)

def timer(count):
    start_time = time.time()
    with alive_progress.alive_bar(count + 1, title="Timer active. Stay focused!", spinner=None, receipt=False, monitor=False, elapsed=False, stats=False) as bar:
        while time.time() - start_time < count + 1:
            time_left = ((count - (time.time() - start_time)) // 1) + 1
            if time_left > 60:
                minutes = time_left // 60
                seconds = time_left % 60
                bar.text(f"Time left: {minutes} minutes and {seconds} seconds")
                time.sleep(1)
                bar()
            else:
                bar.text(f"Time left: {time_left} seconds")
                time.sleep(1)
                bar()

def minutes_to_seconds(minutes):
    return minutes * 60

def timer_loop(duration, interval):
    duration = minutes_to_seconds(duration)
    interval = minutes_to_seconds(interval)
    cycles = int(duration) // int(interval)
    count = 1
    focus = r"""
  _____ ___   ____ _   _ ____
 |  ___/ _ \ / ___| | | / ___|
 | |_ | | | | |   | | | \___ \
 |  _|| |_| | |___| |_| |___) |
 |_|   \___/ \____|\___/|____/


"""
    finish = r"""
  _____ ___ _   _ ___ ____  _   _ _____ ____
 |  ___|_ _| \ | |_ _/ ___|| | | | ____|  _ \
 | |_   | ||  \| || |\___ \| |_| |  _| | | | |
 |  _|  | || |\  || | ___) |  _  | |___| |_| |
 |_|   |___|_| \_|___|____/|_| |_|_____|____/


"""
    countdown()
    for i in range(cycles):
        count += 1
        timer(int(interval))
        clear()
        if count <= cycles:
            print("\a")
            smoke_animated_text(focus)
        else:
            print("\a")
            smoke_animated_text(finish)

timer_loop(duration, interval)