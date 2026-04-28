import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--duration", type=float)
parser.add_argument("-i", "--interval", type=float)
args = parser.parse_args()

duration = args.duration
interval = args.interval

if duration is None:
    duration = float(input("How long would you like your focus session? "))
if interval is None:
    interval = float(input("How long would you like the intervals to be? "))

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
    while time.time() - start_time < count + 1:
        time_left = ((count - (time.time() - start_time)) // 1) + 1
        if time_left > 60:
            minutes = time_left // 60
            seconds = time_left % 60
            print(f"Time left: {minutes} minutes and {seconds} seconds\r", end = "")
            time.sleep(1)
        else:
            print(f"Time left: {time_left} seconds                     \r", end = "")
            time.sleep(1)

def minutes_to_seconds(minutes):
    return minutes * 60


def timer_loop(duration, interval):
    duration = minutes_to_seconds(duration)
    interval = minutes_to_seconds(interval)
    cycles = int(duration) // int(interval) 
    count = 1
    countdown()
    for i in range(cycles):
        if count > 1:
            print(f"\nTimer {count}")
        count += 1
        timer(int(interval))


timer_loop(duration, interval)
