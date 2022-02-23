import sys
import time

time_start = time.time()
seconds = 0
minutes = 0

running = True

while running:
    try:
        # print('Time Gone By:', end=' ')
        sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(
            minutes=minutes, seconds=seconds))
        sys.stdout.flush()
        time.sleep(1)
        seconds = int(time.time() - time_start) - minutes * 60
        if seconds >= 60:
            minutes += 1
            seconds = 0
    except KeyboardInterrupt as e:
        running = False
        print('\n[+] Exiting...')
