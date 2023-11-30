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
            print("1: Set alarm. 2: Set alarm options. 3: Delete all alarms. 4: Change clock mode")
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
                        elif alarm_input.lower() == "q":
                            break
                        else:

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
                        
                            #alarm_threads = []
                            #for alarm_seconds in alarms_list:
                            #    alarm_thread = threading.Thread(target=alarm_sound, args=(alarm_seconds,))
                            #    alarm_thread.start()
                            #    alarm_threads.append(alarm_thread)              
                            #break

                if setting_alarm_mode == 2:
                    headers = ("Date", "Time")
                    print("{:<10} {:<10}".format(*headers))
                    for alarm in alarms_list:
                        print("{:<10} {:<10}".format(alarm["date"], alarm["time"]))
                print()
            elif alarm_mode == 2:
                 #alarm settings
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
        print("TEST")

    #Stopwatch
    elif program_mode == 3:
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
            elif mode == 4:
                break
            else:
                 print("This input is invalid. Please enter 1,2,3 or 4.")

    elif program_mode == 4:
        print("TEST")



    

        