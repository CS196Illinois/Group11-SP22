from tkinter import * 



'''class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        
        self.test_button = Button(master, text = "Test Zoey", command = self.Zoey)
        self.test_button.pack()

    def greet(self):
        print("Greetings!")
    def Zoey(self):
        print("Hello from Zoey")
        '''

class UserInterface:
    def __init__(self, master):
        self.master = master
        master.title("Curve Meter")

        self.enterGrade_label = Label(master, text = "Enter the Grade",
        foreground = "lime", background= "black", width=20, height=10)
        self.enterGrade_label.pack()

        self.entry = Entry(master, text= "test entry", fg = "lime", bg="black", width=24,)
        self.entry.pack()

      
    


root = Tk()
my_gui = UserInterface(root)
root.mainloop()