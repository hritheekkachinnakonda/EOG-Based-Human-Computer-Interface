from tkinter import *
  
locate = Tk()

## Set Title
locate.title('IBEHS 4F04_buttons')

## Set Panel Size
locate.geometry("600x800")

## Background Panel ON/OFF
locate.overrideredirect(False)

## Local Vriables
count = 0

## Button Color/Count Assignment
rb_pressed = 1
rb_count = 0
def rbPressed():
    global rb_pressed, rb_count
    rb_pressed -= 1
    if rb_pressed ==0:
        rb_pressed = 1
        rb_count = rb_count + 1
        print (rb_count)
        rb_count = 0
        count = rb_count + 1   
    else:
        pass

bb_pressed = 1
bb_count = 1
def bbPressed():
    global bb_pressed, bb_count
    bb_pressed -= 1
    if bb_pressed ==0:
        bb_pressed = 1
        bb_count = bb_count + 1
        print (bb_count)
        bb_count = 1
        count = bb_count + 1
    else:
        pass

gb_pressed = 1
gb_count = 2
def gbPressed():
    global gb_pressed, gb_count
    gb_pressed -= 1
    if gb_pressed ==0:
        gb_pressed = 1
        gb_count = gb_count + 1
        print (gb_count)
        gb_count = 2
        count = gb_count + 1
    else:
        pass

yb_pressed = 1
yb_count = 3
def ybPressed():
    global yb_pressed, yb_count
    yb_pressed -= 1
    if yb_pressed ==0:
        yb_pressed = 1
        yb_count = yb_count + 1
        print (yb_count)
        yb_count = 3
        count = yb_count + 1
    else:
        pass

ob_pressed = 1
ob_count = 4
def obPressed():
    global ob_pressed, ob_count
    ob_pressed -= 1
    if ob_pressed ==0:
        ob_pressed = 1
        ob_count = ob_count + 1
        print (ob_count)
        ob_count = 4
        count = ob_count + 1
    else:
        pass

## Define buttons color, size, location on the panel and button commands
rb = Button(locate, command=rbPressed, activeforeground="red", activebackground="pink", height=2, width=4)
rb.place(x=50 , y=50)
    
bb = Button(locate, command=bbPressed, activeforeground = "blue",activebackground = "blue", height=2, width=4)
bb.place(x=50 , y=700)
  
gb = Button(locate, command=gbPressed, activeforeground = "green",activebackground = "green", height=2, width=4)
gb.place(x=500 , y=700)
  
yb = Button(locate, command=ybPressed, activeforeground = "yellow",activebackground = "yellow", height=2, width=4)
yb.place(x=500 , y=50)

ob = Button(locate, command=obPressed, activeforeground = "orange",activebackground = "orange", height=2, width=4)
ob.place(x=300 , y=400)

## Main
locate.mainloop() 
