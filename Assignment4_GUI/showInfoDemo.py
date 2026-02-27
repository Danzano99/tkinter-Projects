# Show Info Program

import tkinter

class ShowInfoGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Show Info")
        self.main_window.minsize(300,200)

        # Create two frames
        self.top_frame = tkinter.Frame(self.main_window,bg="pink", height= 400, width=400)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create a blank label in the top frame
        #this variable gets assigned a value in the showInfo method
        self.value = tkinter.StringVar()   
        self.address_label = tkinter.Label(self.top_frame,
                    textvariable= self.value)
                       
        # Create the two buttons in the bottom frame
        self.address_button = tkinter.Button(self.bottom_frame,
                text = 'Show Info', command = self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame,
                text = 'Quit', command = self.main_window.destroy)

        # Pack the label
        self.address_label.pack()
        #Pack the buttons
        self.address_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def show_info(self):
        #assigning a value to the String variable that was created earlier
        self.value.set('Aflac\n1932 Wynnton Road\n'
                       'Columbus, GA 31999')

# Create an instance of ShowInfoGUI
if __name__ == '__main__':
    show_info = ShowInfoGUI()