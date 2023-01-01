import time

def time_convert(sec):
    mins=sec//60
    sec=sec%60
    hours=mins//60
    mins=mins%60
    print(f'Time Lapsed {int(hours)}:{int(mins)}:{int(sec)}')

input('Press Enter To Start')
start_time=time.time()

input('Press Enter To Stop')
end_time=time.time()

time_lapsed=end_time-start_time
time_convert(time_lapsed)
