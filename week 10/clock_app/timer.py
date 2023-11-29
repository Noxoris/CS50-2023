import datetime
import time
import pickle
#from playsound import playsound

#terminal and gui versions
#TODO Clock, alarm, timer functionalities
#Clock options: show date (on/off), show seconds (on/off), 12/24h (on/off)
#Alarm options: alarm on hour next day, alarm on selected date, custom sound, delete all alarms
#Timer functionalities: save timers, delete timers, 

#Alarm pseudocode DONE
#prompt for alarm mode DONE
#mode 1:
#set alarm or show alarms
#if set alarms
#prompt for setting hour / date of alarm
##convert to seconds
#display alarm date to user, at what time is alarm set + add functionality to check active timers
#add alarm to pickle file
#if show alarms
#display from pickle file
#at alarm date play sound, prompt "stop" to stop alarm or "snooze" to add 5 minutes
#mode 2:
#prompt for setting
#1 date on/off
#2 show seconds on/off
#3 12/24h on/off
#4 custom sound
#mode 3:
#prompt for confirmation
#if yes, empty alarm files
#if no, comeback to mode selection


def pick_mode():
    while True:
        try:
            mode = int(input("Please choose a mode 1,2,3,4 or close program by pressing ctrl + c: "))
            return mode
        except ValueError:
            print("This input is invalid")

while True:
    print("Clock program mode selection: ")
    print("1: Run Alarm. 2: Run Clock. 3: Run Stopwatch. 4: Run Timer or close program by pressing ctrl + c: ")
    
    program_mode = pick_mode()

    if program_mode == 1:
        #ALARM CODE
        while True:
            alarms = []

            try:
                with open('alarms.pkl', 'rb') as alarms_file:
                        alarms = pickle.load(alarms_file)
            except IOError:
                    pass
            print("Alarm mode selection: ")
            print("1: Set alarm. 2: Set alarm options. 3: Delete all alarms. 4: Change clock mode")
            
            alarm_mode = pick_mode()

            if alarm_mode == 1:
                print("Alarm setting mode selection: ")
                print("1: Set new alarm. 2: Show alarms 3: Change alarm mode")

                setting_alarm_mode = pick_mode()
                if setting_alarm_mode == 1:
                    #setting alarms code
                    
                    
                    while True:
                        try:
                            alarm_time = input("Enter time in the format HH:MM:SS: ")
                            hours, minutes, seconds = map(int, alarm_time.split(':'))
                            if minutes > 60 or seconds > 60:
                                print("Invalid input. Please enter time in the format HH:MM:SS. Do not type minutes or seconds > 60")
                            else:
                                hours, minutes, seconds = map(int, alarm_time.split(':'))
                                break
                        except ValueError:
                            print("Invalid input. Please enter time in the format HH:MM:SS.")
                    seconds_total = (hours * 60 * 60) + (minutes * 60)
                
                                  
                
                    print("Alarm set!")
                elif setting_alarm_mode == 2:
                    #show alarms code
                    print("Show alarms")

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



    

        