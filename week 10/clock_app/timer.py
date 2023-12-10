import datetime
import time
import pickle
from playsound import playsound
import threading
import os
import pytz
import sys
from io import StringIO

global alarms_list
alarms_list = []

global timers_list 
timers_list = []

global timer_threads_list
timer_threads_list = []

global alarm_threads_list
alarm_threads_list = []

global stopwatch_records
stopwatch_records = []

sound_file = None

#TODO
# Alarm Settings
#Clock comments mode 2
def load_files():
    global stopwatch_records
    
    #Load alarms set during previous program launches
    try:
        with open('alarms.pkl', 'rb') as alarms_file:
            alarms_list = pickle.load(alarms_file)

        #Start alarms that were set during previous program launches    
        for alarm in alarms_list:
            set_alarm(alarm)

    #If there are none, create empty list of alarms           
    except:
        alarms_list = []

    #Load stopwatch records made during previous program launches
        try:
            with open('stopwatch_records.pkl', 'rb') as stopwatch_file:
                stopwatch_records = pickle.load(stopwatch_file)

        #If there are none, create empty list of timers 
        except:
            stopwatch_records = []    

    #Load timers set during previous program launches
    try:
        with open('timers.pkl', 'rb') as timer_file:
            timers_list = pickle.load(timer_file)

        #Start timers that were set during previous program launches    
        for timer in timers_list:
            start_timer(timer[0],timer[1],timer[2])

        #If there are none, create empty list of timers        
    except:
        timers_list = []

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

def clear_threads__and_lists(threads_list, file_name):
    for thread in threads_list:
       thread.cancel()
    threads_list.clear()

    # Clear timers file
    with open(file_name, 'wb') as file:
       pickle.dump([], file)

#Alarm functions

def set_alarm(alarm_time):
  
  current_time = datetime.datetime.now()
  
  #Convert the alarm time from a string to a datetime object
  alarm_time = datetime.datetime.strptime(":".join(map(str, alarm_time)), '%H:%M:%S')

  #Set the year, month, and day of the alarm time to the current date
  alarm_time = alarm_time.replace(year=current_time.year,month=current_time.month,day=current_time.day)

  #Calculate the time until the alarm in seconds
  time_until_alarm = (alarm_time - current_time).total_seconds()
  
  #If the alarm is in the past, set it for the next day
  if time_until_alarm < 0:
     alarm_time = alarm_time + datetime.timedelta(days=1)
     time_until_alarm = (alarm_time - current_time).total_seconds()

  #Get date from alarm_time
  alarm_date = alarm_time.strftime('%d-%m-%Y')
  
  #Get time from alarm_time
  alarm_time = alarm_time.strftime('%H:%M:%S')

  alarm_item = [alarm_date, alarm_time]
  #Create a thread that will call the alarm_expired function after the time until the alarm
  alarm_thread = threading.Timer(time_until_alarm, alarm_expired, args=(alarm_item,))

  alarm_thread.start()
  
  #Append alarms and threads to lists
  if alarm_item not in alarms_list:
     alarms_list.append(alarm_item) 
  alarm_threads_list.append(alarm_thread) 

  #Export list of alarms to file
  with open('alarms.pkl', "wb") as alarms_file:
          pickle.dump(alarms_list, alarms_file)

  #Convert the time until the alarm from seconds to hours, minutes, and seconds
  hours, remainder = divmod(time_until_alarm, 3600)
  minutes, seconds = divmod(remainder, 60)

  print("The alarm will ring at: %02d hours %02d minutes %02d seconds" % (hours, minutes, seconds))   
  time.sleep(1.5)

def alarm_expired(alarm):
     print()
     print("\r")
     print("Alarm has expired", end="")
     alarms_list.remove(alarm)  
     snooze_thread = threading.Thread(target=snooze)
     snooze_thread.start()

# def play_alarm(sound_file):
#    try:
#        if sound_file is not None:
#            playsound(f"{sound_file}")
#            time.sleep(1)
#        else:
#            playsound("alarm.mp3")
#    except Exception as error:
#        print(f"Error playing sound file: {error}")

def snooze():    
     sys.stdin = StringIO('a')
     print("\r")
     while True:
          
          #Simulate input to fix input block

          # Play the alarm sound, don't wait until it finishes to continue
          #threading.Thread(target=play_alarm, args=(sound_file,)).start()

          # Ask the user if they want to snooze the alarm
          snooze = input("Snooze (y or yes / no)? ").strip().lower()
          if snooze in ["y", "yes"]:
               
               #Add 5 minutes to current time
               snooze_time = datetime.datetime.now() + datetime.timedelta(minutes=5)

               #Convert to a string in the format HH:MM:SS
               snooze_time = snooze_time.strftime("%H:%M:%S")

               #Create alarm 5 minutes from now
               set_alarm(snooze_time)             
               break

          elif snooze in ["n", "no"]:
               break
          else:
              continue     

#Clock functions

def clock_settings():   
    global show_date
    global show_seconds
    global AM_PM_format
    try:    
            #Load settings from file
            with open('clock_settings.pkl', 'rb') as settings_file:
                loaded_settings = pickle.load(settings_file)
            show_date, show_seconds, AM_PM_format = loaded_settings
    except:
            #If there is no file, reset settings
            show_date = 0
            show_seconds = 0
            AM_PM_format = 0

    #Display current settings
    print("Current settings: ")
    print(f"Show date: {show_date}")
    print(f"Show seconds: {show_seconds}")
    print(f"12/24 hour format: {AM_PM_format}")
    print()
    print("Enter new settings: ")
    print()
    while True:
        try:

            #Prompt for new settings
            show_date = int(input("Show date (0 for no, 1 for yes): "))
            show_seconds = int(input("Show seconds (0 for no, 1 for yes): "))
            AM_PM_format = int(input("12 or 24 hour format (0 for 24-hour, 1 for 12-hour): "))           

            #Check if the inputs are valid
            if show_date not in [0, 1] or show_seconds not in [0, 1] or AM_PM_format not in [0, 1]:
               raise ValueError("Invalid input. Please enter 0 or 1.")
            
            #Export them to file
            with open('clock_settings.pkl', 'wb') as settings_file:
                 pickle.dump((show_date,show_seconds,AM_PM_format), settings_file)
            break

        except:
            print("Invalid format, try again")
            continue

#Timer functions

def get_time():
     while True:
       time_input = input("Enter time in the format HH:MM:SS or press q to return to the alarm menu: ")
       if time_input.lower() == "q":
           return None

       time_split = [int(n) for n in time_input.split(":")]
       if time_split[0] >= 24 or time_split[0] < 0:
           print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
           continue
       if time_split[1] >= 60 or time_split[1] < 0:
           print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
           continue
       if time_split[2] >= 60 or time_split[1] < 0:
           print("Invalid input. Please enter time in the format HH:MM:SS or press q to return to the alarm menu.")
           continue

       return time_split

def set_timer():
     while True:

        time_of_timer = get_time()
        if time_of_timer is None:
           break
        
        #Take hours, minutes and seconds from input
        h_timer = time_of_timer[0]
        min_timer = time_of_timer[1]
        sec_timer = time_of_timer[2]

        start_timer(h_timer, min_timer, sec_timer)
        break     

def start_timer(hours, minutes, seconds):
     global timer_thread
     global timer_item
     timer_item = [hours, minutes, seconds]

     #Calculate duration of the timer in seconds
     timer_duration = hours * 3600 + minutes * 60 + seconds
     
     #Start thread to activate timer with delay of timer duration
     timer_thread = threading.Timer(timer_duration, timer_expired, args=(timer_item, len(timer_threads_list)))

     timer_thread.start()  
     
     #Append timers and threads to lists
     if timer_item not in timers_list:
        timers_list.append(timer_item) 
     timer_threads_list.append(timer_thread) 

     #Export list of timers to file
     with open('timers.pkl', "wb") as timer_file:
          pickle.dump(timers_list, timer_file)
     print("Timer set")

def timer_expired(item, timer_index):            
             sys.stdin = StringIO('a')
             print("\r")
             print("Timer has expired!")
             playsound("alarm.mp3")

             #Remove timer and it's thread from lists       
             timers_list.remove(item)
             timer_threads_list.pop(timer_index)

             time.sleep(1.5)
             print("\r")

#Set clear to clear terminal function
clear = lambda: os.system("cls")   
clear()

#Main program

load_files()

while True:
    #if not snooze_active:
        clear()
        print("Welcome")  
        print("Program mode selection: ")
        print("1: Run Alarm. 2: Run Clock. 3: Run Stopwatch. 4: Run Timer or close program by pressing ctrl + c: ")
        program_mode = pick_mode()

    #Alarm almost done
        if program_mode == 1:
            while True:
                clear()
                
                print("Alarm mode selection: ")
                print("1: Set alarm. 2: Set alarm options. 3: Delete all alarms. 4: Change program mode")
                print()
                alarm_mode = pick_mode()

                #Set alarm
                if alarm_mode == 1:
                    clear()
                    print("Alarm setting mode selection: ")
                    print("1: Set new alarm. 2: Show active alarms")
                    print()
                    setting_alarm_mode = two_options()
                    
                    #Set new alarm
                    if setting_alarm_mode == 1:
                        
                        while True:
                            clear()
                            alarm_input = get_time()
                            if alarm_input is None:
                                break

                            set_alarm(alarm_input)
                            break

                    #Show active alarms
                    if setting_alarm_mode == 2:
                        clear()
                        
                        headers = ("Date", "Time")

                        #Print headers with spaces between them
                        print("{:<10} {:<10}".format(*headers))

                        #Print records under appropriate headers
                        for alarm in alarms_list:
                            print("{:<10} {:<10}".format(alarm[0], alarm[1]))
                        print()
                    #Block going back until entering something
                    list_sleep = input("Press anything to go back")

                #Alarm settings
                elif alarm_mode == 2:
                    clear()
                    print("Change sound of alarm. Write none to reset")
                    print("Note: alarm supports .mp3 and .wav formats")
                    while True:
                        try:
                            sound_file = str(input("Provide path to sound file: "))
                            if sound_file.lower == "none":
                                sound_file = None
                            break
                        except:
                            print("Wrong file path")

                    print("Alarm sound set")
                    time.sleep(1.5)
                    
                #Clearing alarms   
                elif alarm_mode == 3:
                    clear()

                    while True:

                        try:
                            confirmation = input("Are you sure? There is no going back from this (y/n) / (yes/no): ")
                            confirmation = confirmation.lower()
        
                            if confirmation in ["y", "yes"]:

                                clear_threads__and_lists(alarm_threads_list, 'alarms.pkl')
                                print("Alarms deleted")
                                time.sleep(1.5)
                                break

                            elif confirmation in ["n", "no"]:
                                break

                            else:
                                print("Invalid input. Please enter y, yes, n, or no.")

                        except ValueError:
                                print("This input is invalid. Please enter y, yes, n, or no.")

                #Go back to choosing program mode 
                elif alarm_mode == 4:
                    clear()
                    break

                else:
                    print("This input is invalid. Please enter 1,2,3 or 4.")

    #Clock 
        elif program_mode == 2:
            while True:
                clear()   
                print("Clock mode selection: ")
                print("1: Show current time. 2: Show time in diffrent time zones. 3: Set clock options. 4: Change program mode.")
                print()
                clock_mode = pick_mode()

                if clock_mode == 1:
                    clear()

                    #Convert settings to date and time formats
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

                    #Get current date and time
                    clock_now = datetime.datetime.now(tz=None)

                    #Get format from settings
                    settings_format = settings.get((show_date, show_seconds, AM_PM_format))

                    if settings:
                        print("Current time:")

                        #Print current time formatted using settings
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

    #Stopwatch 
        elif program_mode == 3:           
            while True:
                clear()
            
                print("Stopwatch mode selection: ")
                print("1: Run stopwatch. 2: Show stopwatch records. 3: Delete all stopwatch records. 4: Change program mode")
                
                mode = pick_mode()

                #Start stopwatch
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
                                print("Time elapsed: ", round(time.time() - start_time, 0), 'seconds', end="\r")
                                time.sleep(1)

                        #Upon interrupt stop stopwatch
                        except KeyboardInterrupt:
                            clear()
                            print("Stopwatch has stopped")

                            endtime = time.time()

                            #Calculate how long stopwatch was running
                            stopwatch_duration = round(endtime - start_time, 2)

                            print("The time elapsed:", stopwatch_duration, 'seconds')

                            #Add stopwatch to a list of records
                            stopwatch_records.append({
                            "date": start_date,
                            "time": start_time_record,
                            "duration": stopwatch_duration})

                            #Export records to file
                            with open('stopwatch_records.pkl', 'wb') as stopwatch_file:
                                pickle.dump(stopwatch_records, stopwatch_file)

                            #Sort list by newest first
                            stopwatch_records.reverse()

                            headers = ("Date", "Time", "Duration")

                            #Print headers with spaces between them
                            print("{:<10} {:<10} {:<10}".format(*headers))

                            #Print records under appropriate headers
                            for record in stopwatch_records:
                                print("{:<10} {:<10} {:<10}".format(record["date"], record["time"], record["duration"]))
                            print()

                            #Block going back until entering something
                            list_sleep = input("Press anything to go back")
                            break
                            

                elif mode == 2:
                    clear()
                    headers = ("Date", "Time", "Duration")

                    #Print headers with spaces between them
                    print("{:<10} {:<10} {:<10}".format(*headers))

                    #Print records under appropriate headers
                    for record in stopwatch_records:
                            print("{:<10} {:<10} {:<10}".format(record["date"], record["time"], record["duration"]))
                    print()

                    #Block going back until entering something
                    list_sleep = input("Press anything to go back")
                
                #Clearing stopwatch records    
                elif mode == 3:
                    clear()
                    while True:
                        try:
                            confirmation = input("Are you sure? There is no going back from this (y/n) / (yes/no): ")
                            confirmation = confirmation.lower()
                            if confirmation in ["y", "yes"]:

                                #Empty stopwatch records file
                                with open('stopwatch_records.pkl', 'wb') as stopwatch_file:
                                    pickle.dump([], stopwatch_file)

                                stopwatch_records.clear()

                                print("Stopwatch records deleted")
                                time.sleep(1.5)
                                break

                            elif confirmation in ["n", "no"]:
                                break

                            else:
                                print("Invalid input. Please enter y, yes, n, or no.")

                        except ValueError:
                                print("This input is invalid. Please enter y, yes, n, or no.")

                #Go back to choosing program mode                 
                elif mode == 4:
                    clear()
                    break

                else:
                    print("This input is invalid. Please enter 1,2,3 or 4.")

    #Timer
        elif program_mode == 4:
            clear()

            while True:
                clear()
                print("Timer mode selection: ")
                print("1: Set timer. 2: Show timers. 3: Delete all timers. 4: Change clock mode")
                print()
                timer_mode = pick_mode()

                #Set timer
                if timer_mode == 1:
                    clear()

                    set_timer()    
                    
                    time.sleep(1)
                    print()           
                    pass

                #Show set timers
                elif timer_mode == 2:
                    clear()

                    headers = ("Hours", "Minutes", "Seconds")

                    #Print headers with spaces between them
                    print("{:<6} {:<8} {:<5}".format(*headers))

                    #Print records under appropriate headers
                    for timer in timers_list:
                        print("{:<6} {:<8} {:<5}".format(timer[0], timer[1], timer[2]))
                    print()

                    #Block going back until entering something
                    list_sleep = input("Press anything to go back")

                #Clearing timers     
                elif timer_mode == 3:
                    clear()
                    while True:
                        try:
                            confirmation = input("Are you sure? There is no going back from this (y/n) / (yes/no): ")
                            confirmation = confirmation.lower()

                            if confirmation in ["y", "yes"]:

                                clear_threads__and_lists(timer_threads_list, 'timers.pkl')
                                print("Timers deleted")  
                                time.sleep(1.5)                        
                                break

                            elif confirmation in ["n", "no"]:
                                break

                            else:
                                print("Invalid input. Please enter y, yes, n, or no.")

                        except ValueError:
                                print("This input is invalid. Please enter y, yes, n, or no.")

                #Go back to choosing program mode                
                elif timer_mode == 4:
                    clear()
                    break
                
                else:
                    print("This input is invalid. Please enter 1,2,3 or 4.")   