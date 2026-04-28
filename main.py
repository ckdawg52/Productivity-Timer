import time

def countdown():
    print("Starting timer...")
    time.sleep(1.2)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

def timer(count):
    start_time = time.time()
    while time.time() - start_time < count:
        time_left = (count - (time.time() - start_time)) // 1
        print(f"Time left: {time_left} seconds")
        time.sleep(1)

def timer_loop(duration, interval):
    cycles = duration // interval
    count = 1
    countdown()
    for i in range(cycles):
        if count > 1:
            print(f"Timer {count}")
        count += 1
        timer(interval)

timer_loop(60, 10)
