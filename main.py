from plyer import notification
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import ImageTk, Image
import datetime
import time
import threading

# fetching current time from PC 
current_time = datetime.datetime.now()
hr = current_time.hour
# print(hr)
mi = current_time.minute
# print(min)

# converting time in minutes
init_time = (hr*60) + mi
# print(init_time)


root = Tk()

root.title('SOLIS')

#to set background color of the root window
#you could also specify it via RGB like hex color codes in HTML, e.g, #49A or #0059b3.
root.configure(bg='#fff')

# 'width x hight'
root.geometry('300x200')

# width, hight
# root.minsize(640, 480)
# root.maxsize(720, 720) 

def notifyMe(title, message, app_icon, timeout):
    notification.notify(
        title = title,
        message = message,
        app_icon = app_icon,
        timeout = timeout
    )


def launch():
    t1=threading.Thread(target=launchthread)
    t1.start()
    root.iconify()

def launchthread():
    
    while(True):
        
        submit_button["state"] = DISABLED
        # launch_button.update()
        
        current_time = datetime.datetime.now()
        hr = current_time.hour
        # print(hr)
        mi = current_time.minute
        # print(min)
        curr_time = (hr*60) + mi
        
        if(check_value1.get() == 1):
            if(abs(curr_time - init_time)%20 == 0):
                notifyMe("LOOK AWAY.","Ask blind people the importance of Eyes.", "./eyes.ico", 2)

        if(check_value2.get() == 1):
            if(abs(curr_time - init_time)%60 == 0):
                notifyMe("Have a Sip.","pani peelo fraands", "./water.ico", 2)
        
        if(check_value3.get() == 1):
            if(abs(curr_time - init_time)%30 == 0):
                notifyMe("dawa","dawa khake mar jao fraands", "./medicine.ico", 2)
        
        if(check_value4.get() == 1):
            if(abs(curr_time - init_time)%180 == 0):
                notifyMe("IMP","chullu bhar paani me doob maro fraands", "", 2)
        time.sleep(60)


        
# //////////////////////////////////////////////////////////
user = Label(root, text="SOLIS", bg='#00BFA5', padx=125, pady=5, font=('cosmicsansms', 12, 'bold'))
user.grid(row=0, padx=0, pady=0, columnspan=2 )

check_value1 = IntVar()
check = Checkbutton(text="EYES", variable= check_value1, bg='#fff', font=('cosmicsansms', 10))
check.grid(row=1, column=0, padx=10, pady=10)

check_value2 = IntVar()
check = Checkbutton(text="WATER", variable= check_value2, bg='#fff', font=('cosmicsansms', 10))
check.grid(row=1, column=1, padx=10, pady=10)

check_value3 = IntVar()
check = Checkbutton(text="1/2 HOUR", variable= check_value3, bg='#fff', font=('cosmicsansms', 10))
check.grid(row=2, column=0, padx=10, pady=10)

check_value4 = IntVar()
check = Checkbutton(text="3 HOUR", variable= check_value4, bg='#fff', font=('cosmicsansms', 10))
check.grid(row=2, column=1, padx=10, pady=10)

submit_button = Button(root, text='Launch', command=launch, padx=100, pady=5, bg='#00BFA5',relief=SUNKEN, font=('cosmicsansms', 8, 'bold'))
submit_button.grid(row=6, column=0, padx=0, pady=10, columnspan=2)


root.mainloop()
