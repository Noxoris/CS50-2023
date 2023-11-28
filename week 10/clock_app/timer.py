import datetime
import time

timer_records = {}
while True:
    try:
        start_time = time.time()
        #start_date = datetime.datetime.now(tz=None)
        #start_date = start_date.strftime('%d/%m/%y %H:%M:%S')

        print("Stopwatch has started")
        while True:
            print("Time elapsed: ", round(time.time() - start_time, 0), 'seconds', end="\n")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Timer has stopped")
        endtime = time.time()
        timer_duration = round(endtime - start_time, 2)
        print("The time elapsed:" ,timer_duration, 'secs')
        timer_records["date"] = start_date
        timer_records["time"] = start_time
        timer_records["duration"] = timer_duration

        headers = list(timer_records.keys())

        print(f'{headers[0].capitalize(): <10}{headers[1].capitalize(): <15}')

        for key, value in timer_records.items():
            print(f'{value}')
        break

    #Separate date from time