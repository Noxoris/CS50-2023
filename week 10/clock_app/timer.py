import datetime
import time
import pickle
from playsound import playsound
#import threading


def alarm_sound(alarm_seconds):
   while True:
       now = datetime.datetime.now()
       now_in_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
       if now_in_seconds == alarm_seconds:
           playsound("alarm.mp3")
           user_input = input("Type 'stop' or 'snooze': ")
           if user_input.lower() == 'stop':
               break
           elif user_input.lower() == 'snooze':
               time.sleep(300) # Snooze for 5 minutes
           else:
               print("Invalid input. Please type 'stop' or 'snooze'.")

def pick_mode():
    while True:
        try:
            mode = int(input("Please choose a mode 1,2,3,4 or close program by pressing ctrl + c: "))
            return mode
        except ValueError:
            print("This input is invalid")
def two_options():
    while True:
        try:
            mode = int(input("Please choose a mode 1,2 or close program by pressing ctrl + c: "))
            return mode
        except ValueError:
            print("This input is invalid")
def timer(h, m, s):
     timer_seconds = h * 3600 + m * 60 + s
     print("Timer is set!")
     start = time.time()
     while True:
          current_time = time.time()
          elapsed_time = current_time - start
          if elapsed_time >= timer_seconds:  
            print("Time is up!")
            playsound("alarm.mp3")
            break
def clock_settings():
    global show_date
    global show_seconds
    global AM_PM_format
    show_date = 0
    show_seconds = 0
    AM_PM_format = 0

    #Show settings, not working
    #print("Current settings: ")
    #print(f"Show date: {show_date}")
    #print(f"Show seconds: {show_seconds}")
    #print(f"12/24 hour format: {AM_PM_format}")

    print("Enter new settings: ")
    while True:
    #ADD error check
        try:
            show_date = int(input("Show date (0 for no, 1 for yes): "))
            show_seconds = int(input("Show seconds (0 for no, 1 for yes): "))
            AM_PM_format = int(input("12 or 24 hour format (0 for 24-hour, 1 for 12-hour): "))
            break
        except:
            print("Invalid format, try again")
            continue

while True:
    print("Clock program mode selection: ")
    print("1: Run Alarm. 2: Run Clock. 3: Run Stopwatch. 4: Run Timer or close program by pressing ctrl + c: ")
    print()
    program_mode = pick_mode()

    if program_mode == 1:
        #ALARM CODE
        while True:
            

            try:
                with open('alarms.pkl', 'rb') as alarms_file:
                        alarms_list = pickle.load(alarms_file)
            except FileNotFoundError:
                    alarms_list = []
            print("Alarm mode selection: ")
            print("1: Set alarm. 2: Set alarm options. 3: Delete all alarms. 4: Change program mode")
            print()
            alarm_mode = pick_mode()

            if alarm_mode == 1:
                print("Alarm setting mode selection: ")
                print("1: Set new alarm. 2: Show alarms")
                print()
                setting_alarm_mode = two_options()
                
                if setting_alarm_mode == 1:
                    #setting alarms code
                    
                    while True:
                        alarm_input = input("Enter time in the format HH:MM:SS or press q to return to the alarm menu: ")
                        if alarm_input.lower() == "q":
                            break
                        alarm_time = [int(n) for n in alarm_input.split(":")]
                        if alarm_time[0] >= 24 or alarm_time[0] < 0:
                            print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
                            continue
                        elif alarm_time[1] >= 60 or alarm_time[1] < 0:
                            print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
                            continue
                        else:
                            break
                    # Number of seconds in an Hour, Minute, and Second
                    seconds_hms = [3600, 60, 1]

                    # Convert the alarm time to seconds
                    alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
                    now = datetime.datetime.now()
                    now_in_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
                    time_until_alarm = alarm_seconds - now_in_seconds
                    if time_until_alarm < 0:
                        time_until_alarm += 86400 # number of seconds in a day

                    alarms_list.append(time_until_alarm)
                    print("Alarm is set!")
                            
                    hours, remainder = divmod(time_until_alarm, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    print("The alarm will ring at: %02d hours %02d minutes %02d seconds" % (hours, minutes, seconds))

                        
                    with open('alarms.pkl','wb') as alarms_file:
                         pickle.dump(alarms_list, alarms_file)

                    #TODO add working threading, setting alarm, snooze    
                    #alarm_threads = []
                    #for alarm_seconds in alarms_list:
                    #    alarm_thread = threading.Thread(target=alarm_sound, args=(alarm_seconds,))
                    #    alarm_thread.start()
                    #    alarm_threads.append(alarm_thread)              
                        

                if setting_alarm_mode == 2:
                    headers = ("Date", "Time")
                    print("{:<10} {:<10}".format(*headers))
                    for alarm in alarms_list:
                        print("{:<10} {:<10}".format(alarm["date"], alarm["time"]))
                print()

            elif alarm_mode == 2:
                 #TODO alarm settings
                 print("Alarm settings")

            elif alarm_mode == 3:
                while True:
                    try:
                        confirmation = input("Are you sure? There is no going back from this (y/n) / (yes/no): ")
                        confirmation = confirmation.lower()
                        if confirmation in ["y", "yes"]:
                            with open('alarms.pkl', 'wb') as alarms_file:
                                pickle.dump([], alarms_file)
                            print("Records deleted")
                            print()
                            break
                        elif confirmation in ["n", "no"]:
                            break
                        else:
                            print("Invalid input. Please enter y, yes, n, or no.")
                    except ValueError:
                            print("This input is invalid. Please enter y, yes, n, or no.")

            elif alarm_mode == 4:
                break
            else:
                 print("This input is invalid. Please enter 1,2,3 or 4.")


    elif program_mode == 2:
        #Clock mode

        while True:
            
            try:
                with open('clocks.pkl', 'rb') as clock_file:
                        clock_list = pickle.load(clock_file)
            except FileNotFoundError:
                    clock_list = []
            print("Clock mode selection: ")
            print("1: Show current time. 2: Show time in diffrent time zones. 3: Set clock options. 4: Change program mode.")
            print()
            clock_mode = pick_mode()

            if clock_mode == 1:
                settings = {
                     (0,0,0): "%H:%M",
                     (1,0,0): "%H:%M %d/%m/%Y",
                     (0,1,0): "%H:%M:%S",
                     (0,0,1): "%I:%M %p",
                     (1,1,0): "%H:%M:%S %d/%m/%Y",
                     (1,0,1): "%I:%M %p %d/%m/%Y",
                     (0,1,1): "%I:%M:%S %p",
                     (1,1,1): "%I:%M:%S %p %d/%m/%Y",
                }

                clock_now = datetime.datetime.now(tz=None)
                settings = settings.get((show_date, show_seconds, AM_PM_format))

                if settings:
                     print("Current time:")
                     print(clock_now.strftime(settings))
                     print()
                else:
                     print("Invalid settings")


            elif clock_mode == 2:
                #TODO
                print("TEST")

            elif clock_mode == 3:
                
                clock_settings()
                print("Settings set")
                print()                
                   
            elif clock_mode == 4:
                break
            else:
                 print("This input is invalid. Please enter 1,2,3 or 4.")

#Stopwatch DONE
    elif program_mode == 3:
         while True:
            stopwatch_records = []

            try:
                with open('stopwatch_records.pkl', 'rb') as record_file:
                        stopwatch_records = pickle.load(record_file)
            except IOError:
                    pass
            print("Stopwatch mode selection: ")
            print("1: Run stopwatch. 2: Show stopwatch records. 3: Delete all stopwatch records. 4: Change program mode")
            
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
                        stopwatch_duration = round(endtime - start_time, 2)

                        print("The time elapsed:" ,stopwatch_duration, 'secs')

                        stopwatch_records.append({
                        "date": start_date,
                        "time": start_time_record,
                        "duration": stopwatch_duration})

                        with open('timer_records.pkl', 'wb') as record_file:
                            pickle.dump(stopwatch_records, record_file)

                        stopwatch_records.reverse()
                        headers = ("Date", "Time", "Duration")

                        print("{:<10} {:<10} {:<10}".format(*headers))

                        for record in stopwatch_records:
                            print("{:<10} {:<10} {:<10}".format(record["date"], record["time"], record["duration"]))
                        break

            elif mode == 2:

                headers = ("Date", "Time", "Duration")

                print("{:<10} {:<10} {:<10}".format(*headers))

                for record in stopwatch_records:
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
            elif mode == 4:
                break
            else:
                 print("This input is invalid. Please enter 1,2,3 or 4.")

#Timer TODO
    elif program_mode == 4:
        while True:
            try:
                with open('timers.pkl', 'rb') as timer_file:
                        timers_list = pickle.load(timer_file)
            except FileNotFoundError:
                    timers_list = []
            print("Timer mode selection: ")
            print("1: Set timer. 2: Show timers. 3: Delete all timers. 4: Change clock mode")
            print()
            timer_mode = pick_mode()

            if timer_mode == 1:
                while True:
                    timer_input = input("Enter time in the format HH:MM:SS or press q to return to the alarm menu: ")
                    if timer_input.lower() == "q":
                        break
                    timer_time = [int(n) for n in timer_input.split(":")]
                    if timer_time[0] >= 24 or timer_time[0] < 0:
                        print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
                        continue
                    elif timer_time[1] >= 60 or timer_time[1] < 0:
                        print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
                        continue
                                      
                    h = timer_time[0]
                    m = timer_time[1]
                    s = timer_time[2]

                    #TODO apply working threading, timer, adding timers to timers_list 
                    #timer_thread = threading.Thread(target=timer, args=(h,m,s))
                    #timer_thread.start()

            #if timer_mode == 2:
            #        headers = ("Hours", "Minutes", "Seconds")
            #        print("{:<10} {:<10} {:<10}".format(*headers))
            #        for timer in timers_list:
            #            print("{:<10} {:<10} {:<10}".format(timer["hours"], timer["minutes"], timer["seconds"]))