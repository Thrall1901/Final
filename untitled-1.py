import Tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

path = "Wolf.jpg"

img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(window, image = img)

panel.pack(side = "bottom", fill = "both", expand = "yes")

window.mainloop()