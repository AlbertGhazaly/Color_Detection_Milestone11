import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Canvas

class Start(tk.Tk):
    def __init__(self):
        super().__init__()

        # tambahin text didalam sini
        self.canvas = Canvas(width = 1200, height = 900, bg = "white")
        self.canvas.create_rectangle(0,0,1200,112, fill ='#D9D9D9', outline='#D9D9D9')
        self.canvas.create_rectangle(200,150,1000,450, fill ='#D9D9D9', outline='#D9D9D9')
        self.canvas.create_rectangle(0,587,1200, 500, fill ='#D9D9D9', outline='#D9D9D9')
        self.canvas.create_rectangle(0,700,1200,590, fill ='#D9D9D9', outline='#D9D9D9')
        self.canvas.pack()

        self.geometry("1200x900")
        self.title ("Color Detection App")
        # tombol
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    # bisa juga bikin fungsi baru.
    def button_clicked(self):
        showinfo(title="information", message="hello")

app = Start()
app.mainloop()
