import datetime
import time
import pickle

def pick_mode():
    while True:
        try:
            mode = int(input("Please choose a mode 1,2,3,4: "))
            return mode
        except ValueError:
            print("This input is invalid")
    
while True:
    timer_records = []

    try:
        with open('timer_records.pkl', 'rb') as record_file:
                timer_records = pickle.load(record_file)
    except IOError:
            pass
    print("Stopwatch mode selection: ")
    print("1: Run stopwatch. 2: Show stopwatch records. 3: Delete all stopwatch records. 4: Change clock mode")
    
    mode = pick_mode()

    if mode == 1:
        while True:
            try:
                start_time = time.time()
                start_date = datetime.datetime.today()
                start_date = start_date.strftime("%d/%m/%y")
                start_time_record = time.strftime("%H:%M:%S")

                print("Stopwatch has started")

                while True:
                    print("Time elapsed: ", round(time.time() - start_time, 0), 'seconds', end="\n")
                    time.sleep(1)

            except KeyboardInterrupt:
                print("Timer has stopped")

                endtime = time.time()
                timer_duration = round(endtime - start_time, 2)

                print("The time elapsed:" ,timer_duration, 'secs')

                timer_records.append({
                "date": start_date,
                "time": start_time_record,
                "duration": timer_duration})

                with open('timer_records.pkl', 'wb') as record_file:
                    pickle.dump(timer_records, record_file)

                timer_records.reverse()
                headers = ("Date", "Time", "Duration")
                
                print("{:<10} {:<10} {:<10}".format(*headers))

                for record in timer_records:
                    print("{:<10} {:<10} {:<10}".format(record["date"], record["time"], record["duration"]))
                break

    elif mode == 2:

        headers = ("Date", "Time", "Duration")

        print("{:<10} {:<10} {:<10}".format(*headers))

        for record in timer_records:
                print("{:<10} {:<10} {:<10}".format(record["date"], record["time"], record["duration"]))
        
        print()

    elif mode == 3:
        while True:
            try:
                confirmation = input("Are you sure? There is no going back from this (y/n) / (yes/no): ")
                confirmation = confirmation.lower()
                if confirmation in ["y", "yes"]:
                    with open('timer_records.pkl', 'wb') as record_file:
                        pickle.dump([], record_file)
                    print("Records deleted")
                    print()
                    break
                elif confirmation in ["n", "no"]:
                    break
                else:
                    print("Invalid input. Please enter y, yes, n, or no.")
            except ValueError:
                    print("This input is invalid. Please enter y, yes, n, or no.")

    else:
        print("!")