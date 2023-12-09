import datetime
import time
import pickle
from playsound import playsound
import threading
import os
import pytz

#TODO
# Alarm - clearing list, clears alarms threads. Import alarms will create threads
# Timer - clearing list clears timers threads. Import timers will create threads
#Fix If the alarm is in the past, set it for the next day
#Fix alarm

def alarm_expired(alarm):
     print()
     print("Alarm has expired\r", end="")
     snooze()

def snooze():
     while True:
          playsound("alarm.mp3", block = False)
          snooze = input("Snooze?")
          if snooze in ["y", "yes"]:
               snooze_time = datetime.datetime.now(minutes=5)
               set_alarm(snooze_time)
               break
          elif snooze in ["n", "no"]:
               break
          
def set_alarm(alarm_time):
  
  global alarms_list
  alarms_list = []
  current_time = datetime.datetime.now()
  
  alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M:%S')
  alarm_time = alarm_time.replace(year=current_time.year,month=current_time.month,day=current_time.day)


  time_until_alarm = (alarm_time - current_time).total_seconds()
  
  if time_until_alarm < 0:
     alarm_time = alarm_time + datetime.datetime.now(days=1)
     time_until_alarm = (alarm_time - current_time).total_seconds()

  hours, remainder = divmod(time_until_alarm, 3600)
  minutes, seconds = divmod(remainder, 60)
  alarm_hms = [hours, minutes, seconds]
  alarm_thread = threading.Timer(time_until_alarm, alarm_expired, args=(alarm_hms,))
  alarm_thread.start()
  alarms_list.append(alarm_hms)
  print("The alarm will ring at: %02d hours %02d minutes %02d seconds" % (hours, minutes, seconds))    

def pick_mode():
    while True:
        try:
            print()
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
def clock_settings():   
    global show_date
    global show_seconds
    global AM_PM_format
    try:
            with open('clock_settings.pkl', 'rb') as settings_file:
                loaded_settings = pickle.load(settings_file)
            show_date, show_seconds, AM_PM_format = loaded_settings
    except:
            show_date = 0
            show_seconds = 0
            AM_PM_format = 0

    print("Current settings: ")
    print(f"Show date: {show_date}")
    print(f"Show seconds: {show_seconds}")
    print(f"12/24 hour format: {AM_PM_format}")

    print("Enter new settings: ")
    while True:
    #ADD error check
        try:
            show_date = int(input("Show date (0 for no, 1 for yes): "))
            show_seconds = int(input("Show seconds (0 for no, 1 for yes): "))
            AM_PM_format = int(input("12 or 24 hour format (0 for 24-hour, 1 for 12-hour): "))
            with open('clock_settings.pkl', 'wb') as settings_file:
                 pickle.dump((show_date,show_seconds,AM_PM_format), settings_file)
            break
        except:
            print("Invalid format, try again")
            continue
def start_timer(hours, minutes, seconds):
     global timers_list 
     timers_list = []
     global timer_thread
     global timer_item
     timer_item = [hours, minutes, seconds]
     timer_duration = hours * 3600 + minutes * 60 + seconds
     timer_thread = threading.Timer(timer_duration, timer_expired, args=(timer_item,))
     timer_thread.start()  
     timers_list.append(timer_item)
     print("Timer set")
     time.sleep(1)
     print()
def timer_expired(item):            
             print()
             print("Timer has expired!\r", end="")
             playsound("alarm.mp3")       
             timers_list.remove(item)
             time.sleep(2)
             print("\r")
def set_timer():
     while True:
                    timer_input = input("Enter time in the format HH:MM:SS or press q to return to the alarm menu: ")
                    if timer_input.lower() == "q":
                        break
                    timer_time = [int(n) for n in timer_input.split(":")]
                    if timer_time[0] >= 24 or timer_time[0] < 0:
                        print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
                        continue
                    if timer_time[1] >= 60 or timer_time[1] < 0:
                        print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
                        continue
                    if timer_time[2] >= 60 or timer_time[1] < 0:
                        print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
                        continue           

                    h_timer = timer_time[0]
                    min_timer = timer_time[1]
                    sec_timer = timer_time[2]
                    start_timer(h_timer, min_timer, sec_timer)
                    break     
clear = lambda: os.system("cls")   
clear()
print("Welcome")    
while True:
    clear()
    print("Clock program mode selection: ")
    print("1: Run Alarm. 2: Run Clock. 3: Run Stopwatch. 4: Run Timer or close program by pressing ctrl + c: ")
    program_mode = pick_mode()
#Alarm
    if program_mode == 1:
        
        clear()
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
                clear()
                print("Alarm setting mode selection: ")
                print("1: Set new alarm. 2: Show active alarms")
                print()
                setting_alarm_mode = two_options()
                
                if setting_alarm_mode == 1:
                    
                    while True:
                        clear()
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

                    set_alarm(alarm_input)

                if setting_alarm_mode == 2:
                    clear()
                    headers = ("Date", "Time")
                    print("{:<10} {:<10}".format(*headers))
                    for alarm in alarms_list:
                        print("{:<10} {:<10}".format(alarm["date"], alarm["time"]))
                print()

            elif alarm_mode == 2:
                 clear()
                 #TODO alarm settings
                 print("Alarm settings")

            elif alarm_mode == 3:
                clear()
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
                clear()
                break
            else:
                 print("This input is invalid. Please enter 1,2,3 or 4.")

#Clock DONE
    elif program_mode == 2:
        while True:
            clear()   
            print("Clock mode selection: ")
            print("1: Show current time. 2: Show time in diffrent time zones. 3: Set clock options. 4: Change program mode.")
            print()
            clock_mode = pick_mode()

            if clock_mode == 1:
                clear()
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
                settings_format = settings.get((show_date, show_seconds, AM_PM_format))

                if settings:
                     print("Current time:")
                     print(clock_now.strftime(settings))
                     print()  
                else:
                     print("Invalid settings")


            elif clock_mode == 2:
                clear()
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
                city = input("Type city name in Region/City format: ")
                print()
                city_tz = pytz.timezone(city)
                current_time = datetime.datetime.now(city_tz)
                settings_format = settings.get((show_date, show_seconds, AM_PM_format))
                formatted_time = current_time.strftime(settings_format)
                print(formatted_time)
                clear()   
            elif clock_mode == 3:
                clear()
                clock_settings()
                print("Settings set")
                           
                   
            elif clock_mode == 4:
                clear()
                break
            else:
                 print("This input is invalid. Please enter 1,2,3 or 4.")

#Stopwatch DONE
    elif program_mode == 3:        
         while True:
            clear()
            stopwatch_records = []

            try:
                with open('stopwatch_records.pkl', 'rb') as stopwatch_file:
                        stopwatch_records = pickle.load(stopwatch_file)
            except IOError:
                    pass
            print("Stopwatch mode selection: ")
            print("1: Run stopwatch. 2: Show stopwatch records. 3: Delete all stopwatch records. 4: Change program mode")
            
            mode = pick_mode()

            if mode == 1:     
                while True:
                    clear()
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

                        with open('timer_records.pkl', 'wb') as stopwatch_file:
                            pickle.dump(stopwatch_records, stopwatch_file)

                        stopwatch_records.reverse()
                        headers = ("Date", "Time", "Duration")

                        print("{:<10} {:<10} {:<10}".format(*headers))

                        for record in stopwatch_records:
                            print("{:<10} {:<10} {:<10}".format(record["date"], record["time"], record["duration"]))
                        break

            elif mode == 2:
                clear()
                headers = ("Date", "Time", "Duration")

                print("{:<10} {:<10} {:<10}".format(*headers))

                for record in stopwatch_records:
                        print("{:<10} {:<10} {:<10}".format(record["date"], record["time"], record["duration"]))
                
                print()

            elif mode == 3:
                clear()
                while True:
                    try:
                        confirmation = input("Are you sure? There is no going back from this (y/n) / (yes/no): ")
                        confirmation = confirmation.lower()
                        if confirmation in ["y", "yes"]:
                            with open('stopwatch_records.pkl', 'wb') as stopwatch_file:
                                pickle.dump([], stopwatch_file)
                            stopwatch_records = []
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
                clear()
                break
            else:
                 print("This input is invalid. Please enter 1,2,3 or 4.")

#Timer almost done
    elif program_mode == 4:
        try:
            with open('timers.pkl', 'rb') as timer_file:
                    timers_list = pickle.load(timer_file)
        except FileNotFoundError:
            timers_list = []
        while True:
            clear()
            print("Timer mode selection: ")
            print("1: Set timer. 2: Show timers. 3: Delete all timers. 4: Change clock mode")
            print()
            timer_mode = pick_mode()

            if timer_mode == 1:
                clear()
                set_timer()               
                pass
            elif timer_mode == 2:
                 clear()
                 headers = ("Hours", "Minutes", "Seconds")
                 print("{:<6} {:<8} {:<5}".format(*headers))
                 for timer in timers_list:
                    print("{:<6} {:<8} {:<5}".format(timer[0], timer[1], timer[2]))
                 print()
                 list_sleep = input("Press anything to go back")
            elif timer_mode == 3:
                 clear()
                 while True:
                    try:
                        confirmation = input("Are you sure? There is no going back from this (y/n) / (yes/no): ")
                        confirmation = confirmation.lower()
                        if confirmation in ["y", "yes"]:
                            with open('timers.pkl', 'wb') as timer_file:
                                pickle.dump([], timer_file)                                                 
                            timers_list = []
                            print("Records deleted")
                            time.sleep(2)
                            break
                        elif confirmation in ["n", "no"]:
                            break
                        else:
                            print("Invalid input. Please enter y, yes, n, or no.")
                    except ValueError:
                            print("This input is invalid. Please enter y, yes, n, or no.")
            elif timer_mode == 4:
                 clear()
                 break
            else:
                 print("This input is invalid. Please enter 1,2,3 or 4.")   