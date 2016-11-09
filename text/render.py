import math
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    
master = Tk()

w = None

def to_pixel(x):
    return int(x * 1000.0 / 29.7)
    
def text(x, y, s):
    w.create_text(to_pixel(x), to_pixel(y), text = s, anchor = NW)

def linie(x, y, x2, y2):
    w.create_line(to_pixel(x),
                  to_pixel(y),
                  to_pixel(x2),
                  to_pixel(y2))

def vorbereiten():    
    global w
    w = Canvas(master, width=int(1000*21/29.7), height=1000)
    w.pack()

def anzeigen():
    mainloop()
