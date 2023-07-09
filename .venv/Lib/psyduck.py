import pyautogui
import random
import tkinter as tk
import keyboard
import sys
import playsound
x = 1550
cycle = 0
check = 1
walk_negative_num = [1,2,3,10,8,16]
walk_positive_num = [4,5,6,12,14]
sitting_headache_num = [7]
psychic_num = [9]
sleeping_num = [11]
standing_headache_num = [13]
waving_num = [15]
event_number = 16 #random.randrange(1,16,1)
impath = 'C:\\Psyduck\\'
def event(cycle,check,event_number,x):
    if event_number in walk_positive_num:
        check = 0
        window.after(300,update,cycle,check,event_number,x) 
    elif event_number in walk_negative_num:
        check = 1
        window.after(300,update,cycle,check,event_number,x) 
    elif event_number in sitting_headache_num:
        check = 2
        window.after(300,update,cycle,check,event_number,x) 
    elif event_number in psychic_num:
        check = 3
        window.after(300,update,cycle,check,event_number,x) 
    elif event_number in sleeping_num:
        check = 4
        window.after(300,update,cycle,check,event_number,x) 
    elif event_number in standing_headache_num:
        check = 5
        window.after(300,update,cycle,check,event_number,x) 
    elif event_number in waving_num:
        check = 6
        window.after(300,update,cycle,check,event_number,x) 

#making gif work 
def gif_work(cycle,frames,event_number,first_num,last_num):
    if cycle < len(frames) -1:
        cycle+=1
    else:
        cycle = 0
        event_number = random.randrange(first_num,last_num+1,1)
    return cycle,event_number 
def update(cycle,check,event_number,x):
    if keyboard.is_pressed("q"):
        print("You pressed q")
        sys.exit()

    if check == 0:
        frame = walk_positive[cycle]
        #IDLE LEFT OR WALK RIGHT OR IDLE TO SLEEP RIGHT - CHECK
        if(x > 1500):
            cycle ,event_number = gif_work(cycle,walk_positive,event_number,1,1)
        else:
            cycle ,event_number = gif_work(cycle,walk_negative,event_number,1,16)
            x += 10
    elif check == 1: #no. 5,6,7,8 = idle facing left
        frame = walk_negative[cycle]
        #IDLE RIGHT OR WALK LEFT OR IDLE TO SLEEP LEFT - CHECK
        if(x < 100):
            cycle ,event_number = gif_work(cycle,walk_positive,event_number,4,4)
        else:
            cycle ,event_number = gif_work(cycle,walk_negative,event_number,1,16)
            x -= 10
    elif check == 2: #no for sitting headache
        frame = sitting_headache[cycle]
        cycle ,event_number = gif_work(cycle,sitting_headache,event_number,1,16)
    elif check == 3: #no for psychic
        frame = psychic[cycle]
        cycle ,event_number = gif_work(cycle,psychic,event_number,1,16)
    elif check == 4: #no for sleeping
        frame = sleeping[cycle]
        cycle ,event_number = gif_work(cycle,sleeping,event_number,1,16)
    elif check == 5: #no for standing headache
        frame = standing_headache[cycle]
        cycle ,event_number = gif_work(cycle,standing_headache,event_number,1,16)
    elif check == 6: #no for waving
        frame = waving[cycle]
        cycle ,event_number = gif_work(cycle,waving,event_number,1,16)
    window.geometry('90x90+'+str(x)+'+960')
    label.configure(image=frame)
    window.after(0,event,cycle,check,event_number,x)
window = tk.Tk()
walk_positive = [tk.PhotoImage(file=impath+'walk_positive.gif',format = 'gif -index %i' %(i)) for i in range(4)]#walk to right gif
walk_negative = [tk.PhotoImage(file=impath+'walk_negative.gif',format = 'gif -index %i' %(i)) for i in range(4)]#walk to left gif
sitting_headache = [tk.PhotoImage(file=impath+'sitting_headache.gif',format = 'gif -index %i' %(i)) for i in range(6)]
psychic = [tk.PhotoImage(file=impath+'psychic.gif',format = 'gif -index %i' %(i)) for i in range(17)]
sleeping = [tk.PhotoImage(file=impath+'sleeping.gif',format = 'gif -index %i' %(i)) for i in range(12)]
standing_headache = [tk.PhotoImage(file=impath+'standing_headache.gif',format = 'gif -index %i' %(i)) for i in range(10)]
waving = [tk.PhotoImage(file=impath+'waving.gif',format = 'gif -index %i' %(i)) for i in range(7)]

#window configuration
window.config(highlightbackground='green', borderwidth=0)
label = tk.Label(window,bd=0,bg='green')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'green')
label.pack()
#loop the program
window.after(0,update,cycle,check,event_number,x)
window.mainloop()
