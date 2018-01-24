'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # "as" lets us use standard abbreviations
import Tkinter
root = Tkinter.Tk()
shade_intvar=Tkinter.IntVar()
shade_intvar.set(50)
'''Read the image data'''
# Get the directory of this python script


directory = os.path.dirname(os.path.abspath(__file__))
print type(directory)
print str(directory)
# Build an absolute file name from directory + filename
filename = os.path.join(directory, 'wolf.jpg')
# Read image data into an array
def shade_intvar(new_interval):
    r=int(new_interval)
radius_slider = Tkinter.Scale(root, from_=0, to=255, variable=shade_intvar,    
                              label='Shade', command=shade_changed)
img = plt.imread(filename)
for row in img:
    for pix in row:
        pix[1]=10+r
'''Show the image data'''

# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 1)
# Show the image data in the first subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()
