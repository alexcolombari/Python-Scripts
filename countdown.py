import time

time_left = input("Enter the time to countdown (in seconds): ")

try:
    while time_left > 0:
        print(time_left)
        time.sleep(1)
        time_left -= 1
    print("Finished!")
except KeyboardInterrupt:
    print("\nYou canceled the countdown!")
