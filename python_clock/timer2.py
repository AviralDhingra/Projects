import sys
import time

from playsound import playsound

min_time = float(
    input('How much time do you want set the timer to (in minutes)? '))
sec_time = min_time * 60
sec_time2 = sec_time
# time.sleep(sec_time)
for i in range(int(round(sec_time))):
    tic = time.perf_counter()

    sec_time2 = sec_time2 - 1
    if sec_time2 >= 60:
        minutes_left = sec_time2 // 60
        seconds_left = sec_time % 60
    elif sec_time2 < 60:
        minutes_left = 0
        seconds_left = sec_time2

    sys.stdout.write(f'\r{minutes_left} Minutes & {seconds_left} Seconds Left')
    sys.stdout.flush()
    toc = time.perf_counter()
    time.sleep(1 - (toc - tic))  # toc - tic: 0.4f

playsound('beep.mp3')
