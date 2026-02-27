import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

image = Image.open("image.jpg")
image = image.resize((500, 300))
img = ImageTk.PhotoImage(image)

label = tk.Label(root, image= img)
label.pack()


root.mainloop()