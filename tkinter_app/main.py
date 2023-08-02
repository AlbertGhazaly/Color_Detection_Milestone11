import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # tambahin text didalam sini
        
        # tombol
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    # bisa juga bikin fungsi baru.
    def button_clicked(self):
        showinfo(title="information", message="hello")

app = App()
app.mainloop()
