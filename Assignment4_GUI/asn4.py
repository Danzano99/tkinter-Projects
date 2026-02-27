import tkinter as tk
from PIL import Image, ImageTk

class FoodViewer:
    def __init__(self):

        # Main window
        self.root = tk.Tk()
        self.root.title("Food Viewer")
        self.root.geometry("400x350")

        # Frames
        self.img_frame = tk.Frame(self.root)
        self.rbdBtn_frame = tk.Frame(self.root)

        self.img_frame.pack()
        self.rbdBtn_frame.pack()

        # ~ The Images ~
        # Chicken(Chicken Scallopini is my favorite meal)
        self.img1 = Image.open("chicken.jpg")
        self.img1 = self.img1.resize((400, 300))
        self.imgOne = ImageTk.PhotoImage(self.img1)

        # Pie(Apple is the best!)
        self.img2 = Image.open("pie.jpg")
        self.img2 = self.img2.resize((400, 300))
        self.imgTwo = ImageTk.PhotoImage(self.img2)

        #Pizza
        self.img3 = Image.open("pizza.jpg")
        self.img3 = self.img3.resize((350, 300))
        self.imgThree = ImageTk.PhotoImage(self.img3)

        # Steak(medium rare of course)
        self.img4 = Image.open("steak.jpg")
        self.img4 = self.img4.resize((300, 300))
        self.imgFour = ImageTk.PhotoImage(self.img4)

        # Label (starting with the chicken)
        self.lbl = tk.Label(self.img_frame, image=self.imgOne)
        self.lbl.pack()

        # IntVar (initialize to 1 = Chicken)
        self.var = tk.IntVar()
        self.var.set(1)

        #Radiobutton Loop
        food_options = [
            ("Chicken", 1),
            ("Pie", 2),
            ("Pizza", 3),
            ("Steak", 4)
        ]

        for text, value in food_options:
            (tk.Radiobutton(
                self.rbdBtn_frame,
                text=text,
                variable=self.var,
                value=value,
                command=self.on_radio_select
            ).pack(side="left", padx=10))

        self.root.mainloop()

    def on_radio_select(self):
        choice = self.var.get()
        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)


if __name__ == "__main__":
    app = FoodViewer()