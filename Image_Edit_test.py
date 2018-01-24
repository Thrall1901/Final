


#####
# radius_changer.py
# 
# Creates a Scale and a Canvas. Updates a circle based on the Scale.
# (c) 2013 PLTW
# version 11/1/2013
####

import Tkinter
import os.path #often people import Tkinter as *

#####
# Create root window 
####
root = Tkinter.Tk()
#root is the window

#####
# Create Model
######
radius_intvar = Tkinter.IntVar()
radius_intvar.set(100)
directory = os.path.dirname(os.path.abspath(__file__)) #initialize radius
# center of circle
x = 200 
y = 100

######
# Create Controller
#######
# Event handler for slider
def radius_changed(new_intval):
    # Get data from model
    # Could do this: r = int(new_intval)
    r = radius_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x-r, y-r, x+r, y+r)
#x-r and y-r is top left while x+r and y+r is bottom left
# Instantiate and place slider
radius_slider = Tkinter.Scale(root, from_=1, to=175, variable=radius_intvar,    
                              label='Diameter', command=radius_changed)
#root= box; from= smallest unit; to= biggest unit
radius_slider.grid(row=1, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

######
# Create View
#######
# Create and place a canvas
canvas = Tkinter.Canvas(root, width=300, height=300, Tkinter.PhotoImage(os.path.join(directory, 'wolf.jpg')))
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
r = radius_intvar.get()
circle_item = Tkinter.PhotoImage(os.path.join(directory, 'wolf.jpg'))
#######
# Event Loop
#######
root.mainloop()