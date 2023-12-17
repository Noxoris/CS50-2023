# Clock in python
#### Video Demo:  https://youtu.be/i9aU7-I17Ts
## Description:
This program is a simple clock program in python. It has four modes and supports **multithreading** so that user can use program after alarm or timer has been set. It also **exports** and **imports** data as alarms or timers set, settings for diffrent modes or stopwatch records. 

First thing is the main menu which operates by entering input from 1 - 4.
Modes:
### Alarm
Functions:
1. Set alarm or show active alarms. After expiring it will inform user about it, then start playing sound and delete this alarm from the list of alarms. Next it will ask if user wants to snooze alarm, which creates new alarm for snooze duration (default 5 minutes). After user decides it will stop playing sound.
2. Set alarm options. Include custom sound and snooze time.
3. Delete all active alarms and their threads.
4. Go back to main menu.
### Clock
Functions:
1. Show current time based on settings
2. Show time in diffrent timezones. Uses format Region/City. 
For example Europe/Paris. 
Some of the regions are: Africa, America, Antarctica, Arctic, Asia, Atlantic, Australia, Brazil, Canada, Chile, ETC, Europe, Indian, Mexico, Pacific, US. 
You can find list of all possible inputs here: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
3. Format settings. Include show seconds, date and 12/24 hour format. Can be combined. For example you can have 12 hour format with seconds.
4. Go back to main menu.
### Stopwatch
1. Set stopwatch. Can be stopped using ctrl + c. After stop, shows table with all stopwatch records.
2. Show list of stopwatch records.
3. Clear list of records.
4. Go back to main menu.
### Timer
1. Set timer. After it expires it will inform user about it and play sound once. Then it deletes this timer's record from list of timers.
2. Show active timers.
3. Delete all active timers and their threads.
4. Go back to main menu.

It has protection about wrong input, but if you try hard enough you can break this program. 
That is all. If you have any suggestions, you can leave a comment on github.