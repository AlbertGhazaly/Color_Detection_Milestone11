import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Canvas

class About(tk.Tk):
    def __init__(self):
        super().__init__()

        # tambahin text didalam sini
        self.geometry("720x540")
        self.title("tes")
        self.canvas = Canvas(width=720, height=540, bg="white")
        self.canvas.create_rectangle(0, 0, 1200, 112, fill="green", outline="green")
        self.canvas.create_rectangle(44, 203, 488, 590, fill="green", outline="green")
        self.canvas.create_rectangle(713, 203, 1157, 590, fill="green", outline="green")
        self.canvas.create_rectangle(0, 723, 1200, 900, fill="green", outline="green")
        self.canvas.create_rectangle(26, 649, 219, 712, fill="green", outline="green")
        self.canvas.pack()
         # tombol
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    # bisa juga bikin fungsi baru.
    def button_clicked(self):
        showinfo(title="information", message="hello")

app = About()
app.mainloop()
