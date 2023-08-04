import tkinter as tk
from tkinter import ttk

import root_app 

class App2(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("750x540")
        self.title("page2")
        self.main()
    
    def main(self):
        # back button
        self.back = ttk.Button(self, text="Back", command=self.go_page1)
        self.back.grid(row=2,column=0)

        # next button
        self.next = ttk.Button(self, text="next")
        self.next.grid(row=2,column=1)
    
    def go_page1(self):
        win = Toplevel()
        root_app.App()
        self.withdraw()
        win.deiconify()