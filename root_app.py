import tkinter as tk
from tkinter import ttk, Toplevel

import root_app2 

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("750x540")
        self.title("camera")
        self.main()
    
    def main(self):
        # back button
        self.back = ttk.Button(self, text="Back")
        self.back.grid(row=2,column=0)

        # next button
        self.next = ttk.Button(self, text="next", command=self.go_page2)
        self.next.grid(row=2,column=1)
    
    def go_page2(self):
        win = Toplevel()
        # root_app2.MyApp()
        self.withdraw()
        win.deiconify()

app = App()
app.mainloop()