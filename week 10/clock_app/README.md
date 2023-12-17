![Static Badge](https://img.shields.io/badge/Python-%23FFD23F?logo=python&labelColor=%23FFD03D&color=%23336D9C)
![Static Badge](https://img.shields.io/badge/License-GPLv3-blue)


# Clock in python
#### Video Demo:  https://youtu.be/i9aU7-I17Ts
## Description:

This program is a simple clock done fully in python. It uses cli or command line interface. It has four modes and supports **threading** so that user can use program after alarm or timer has been set. It also **exports** and **imports** data such as alarms / timers set, settings for diffrent modes or stopwatch records.

Built-in libraries used:
* datetime - get and operate on time and date.
* time - sleep function to make alarm and timer.
* pickle - easiest way to export and import data like lists of alarms, timers, records or settings.
* threading - necessary to allow using other functions of program after setting the alarm.
* os  used to clear terminal window for clarity if the interface. Also used to set absolute paths for default sound files, to prevent errors.

**Not** built-in libraries:
* pygame - used to play sound when alarm and timer expires.
* pytz - necessary to show time and date based on region and city.

### Biggest problems faced

Alarm sound were not playing or played once.
Expiry of timer inputed into menus.
Exported files were not importing correctly.
Input from menus catched input provided for snooze alarm input.

## Usage
First thing is the main menu which operates by entering input from 1 - 4.

### All modes and their respective functions:

#### Alarm
Functions:
1. Set alarm or show active alarms. After expiring it will inform user about it, then start playing sound and delete this alarm from the list of alarms. Next it will ask if user wants to snooze alarm, which creates new alarm for snooze duration (default 5 minutes). After user decides it will stop playing sound.
2. Set alarm options. Include custom sound and snooze time.
3. Delete all active alarms and their threads.
4. Go back to main menu.
#### Clock
Functions:
1. Show current time based on settings
2. Show time in diffrent timezones. Uses format Region/City.
For example Europe/Paris.
Some of the regions are: Africa, America, Antarctica, Arctic, Asia, Atlantic, Australia, Brazil, Canada, Chile, ETC, Europe, Indian, Mexico, Pacific, US.
You can find list of all possible inputs here: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
3. Format settings. Include show seconds, date and 12/24 hour format. Can be combined. For example you can have 12 hour format with seconds.
4. Go back to main menu.
#### Stopwatch
1. Set stopwatch. Can be stopped using ctrl + c. After it stops, shows table with all stopwatch records.
2. Show list of stopwatch records.
3. Clear list of records.
4. Go back to main menu.
#### Timer
1. Set timer. After it expires it will inform user about it and play sound once. Then it deletes this timer's record from list of timers.
2. Show active timers.
3. Delete all active timers and their threads.
4. Go back to main menu.

### Contact
 If you have any questions or suggestions, you can leave a comment on github.
