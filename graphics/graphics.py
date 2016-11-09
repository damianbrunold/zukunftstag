import math
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    
master = Tk()

w = None
    
fill = "#000"
width = 1
x = 512
y = 512
oben = False

def rot():
    global fill
    fill = "#f00"
    
def gruen():
    global fill
    fill = "#0f0"
    
def blau():
    global fill
    fill = "#00f"

def schwarz():
    global fill
    fill = "#000"

def weiss():
    global fill
    fill = "#fff"

def duenn():
    global width
    width = 1
    
def mittel():
    global width
    width = 3

def dick():
    global width
    width = 5

def hoch():
    global oben
    oben = True
    
def tief():
    global oben
    oben = False
    
def gehezu(x_, y_):
    global x, y
    if not oben:
        w.create_line(x, y, x_, y_, fill = fill, width = width)
    x = x_
    y = y_

def geherichtung(grad, laenge):
    newx = x + int(math.cos(grad * math.pi / 180) * laenge)
    newy = y + int(math.sin(grad * math.pi / 180) * laenge)
    gehezu(newx, newy)
    
def mitte():
    gehezu(500, 500)

def vorbereiten():    
    global w
    w = Canvas(master, width=1000, height=1000)
    w.pack()

def anzeigen():
    mainloop()
