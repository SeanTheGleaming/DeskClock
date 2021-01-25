# Made by Sean A. Robinson
# This is a personal project designed to fit as a lightweight and minimalistic desktop clock

    # imports the libraries to create GUIs and know the date and time

import datetime
import os
import sys
import tkinter as tk


# is called to update the info on the window


def updateGUI():
    global scheduler
    global now
    global time
    global school
    global place
    global text
    global textweek

    # sets basic variables related to time

    now = datetime.datetime.now()
    military_time = now.strftime('%H%M')
    scheduler = int(now.strftime('%H%M'))
    hours = int(military_time[0:2])
    minutes = int(military_time[2:4])
    weekday = datetime.datetime.today().weekday()

    # writes the day of the week in text as opposed to 0-6, for display on the clock

    if weekday == 0:
        textweek = 'Monday'
    elif weekday == 1:
        textweek = 'Tuesday'
    elif weekday == 2:
        textweek = 'Wednesday'
    elif weekday == 3:
        textweek = 'Thursday'
    elif weekday == 4:
        textweek = 'Friday'
    elif weekday == 5:
        textweek = 'Saturday'
    elif weekday == 6:
        textweek = 'Sunday'

    # converts from military time to standard time

    if hours >= 12:
        meridian = 'PM'
        hours %= 12
    else:
        meridian = 'AM'
    if hours == 0:
        hours = 12

    # pieces together the clock's text and updates the clock accordingly

    text = now.strftime('{3} %Y/%m/%d {0}:{1}:%S {2}'.format(hours, minutes, meridian, textweek))
    label['text'] = text
    gui.after(1, updateGUI)

    # decides if it is a weekend, in which case place is instantly set to 'Out of School' in the next if statement

    if weekday != 5 and weekday != 6:
        school = 1
    else:
        school = 0

    # determines what class is currently happening based on the time and day of the week

    if school == 1:
        if 830 <= scheduler < 900:
            place = 'Morning Meeting'
        if 1515 <= scheduler <= 1530:
            place = 'Dismissal'
        elif 900 <= scheduler < 1030:
            place = 'Math or Geometry'
        elif 1030 <= scheduler < 1100 and weekday != 2:
            place = 'Break'
        elif 1030 <= scheduler < 1115 and weekday == 2:
            place = 'Math or Geometry'
        elif 1115 <= scheduler < 1130 and weekday == 2:
            place = 'Break'
        elif 1030 <= scheduler < 1100 and weekday != 2:
            place = 'Break'
        elif 1230 <= scheduler < 1330:
            place = 'Lunch and Break'
        elif 1100 <= scheduler < 1230 and weekday == 0:
            place = 'Humanities'
        elif 1100 <= scheduler < 1230 and weekday == 1:
            place = 'Humanities'
        elif 1100 <= scheduler < 1230 and weekday == 3:
            place = 'Science'
        elif 1100 <= scheduler < 1230 and weekday == 4:
            place = 'Science'
        elif 1130 <= scheduler < 1230 and weekday == 2:
            place = 'Spanish'
        elif 1330 <= scheduler < 1430 and weekday == 0:
            place = 'Flex'
        elif 1430 <= scheduler < 1515 and weekday == 0:
            place = 'Spanish'
        elif 1330 <= scheduler < 1515 and weekday == 1:
            place = 'Art'
        elif 1330 <= scheduler < 1515 and weekday == 2:
            place = 'Flex'
        elif 1330 <= scheduler < 1430 and weekday == 3:
            place = 'Computer'
        elif 1430 <= scheduler < 1515 and weekday == 3:
            place = 'Music'
        elif 1330 <= scheduler < 1515 and weekday == 4:
            place = 'Flex'
        else:
            place = 'Out of School'
    Sch['text'] = place


    # a script which helps media files load correctly when building


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


    # assembles the window, title, and icon


gui = tk.Tk()
gui.title('Desktop Clock')
gui.iconbitmap(resource_path('icon.ico'))
gui.configure(background='black')
gui.minsize(975, 935)
gui.geometry('900x935')

# creates the clock, placing it on the window

label = tk.Label(gui, text='Error: Clock Not Loaded Correctly')
label.config(font=('Arial', 44), background='black', fg='snow')
label.pack(side='top')

# creates the class the user should be in, placing it on the window

Sch = tk.Label(gui, text='Error: Class Not Loaded Correctly')
Sch.config(font=('Arial', 15), background='black', fg='snow')
Sch.pack(side='top')

# creates a canvas with the schedule image on top of it, placing it on the window

canvas = tk.Canvas(gui, width = 659, height = 832)
canvas.pack(side="bottom")
img = tk.PhotoImage(file="schedule.png")
canvas.create_image(0,0, anchor='nw', image=img)

# calls the script to update the clock and schedule's data, displaying them on the window

updateGUI()

# declares that the above code is a window, and as such should be displayed on the screen

gui.mainloop()
