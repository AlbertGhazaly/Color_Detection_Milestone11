import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

def main():
    app = About()
    app.mainloop()


class About(tk.Tk):
    def __init__(self):
        super().__init__()
        # tambahin text didalam sini
        canvas = Canvas(self, width = 1200, height=900, bg="white")
        canvas.create_rectangle(0, 0, 1200, 112, outline = "light grey", fill="light grey")
        canvas.create_rectangle(88, 167, 1100, 600, outline = "light grey", fill="light grey")

        # tombol
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

        back = ttk.Button(self, text = "Back")
        back.place(x = 40, y = 70)

        # Header Text
        canvas.create_text(600,60, text = "About Us", fill="black", font=('Helvetica 30 bold'))


        canvas.create_rectangle(0, 824, 1200, 700, outline = "light grey", fill="light grey")
        canvas.pack()

        # Footer Text
        canvas.create_text(600,730, text = "Created by...", fill="black", font=('Helvetica 15 bold'))

    # bisa juga bikin fungsi baru.
    def button_clicked(self):
        showinfo(title="information", message="hello")


if __name__ == "__main__":
    main()
