import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

class About(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # tambahin text didalam sini
        self.canvas = Canvas(self, width = 720, height=540, bg="white")
        self.canvas.create_rectangle(0, 0, 720, 112, outline = "light grey", fill="light grey")
        self.canvas.create_rectangle(88, 167, 720, 600, outline = "light grey", fill="light grey")

        back = ttk.Button(self, text = "Back", command=lambda: parent.show_page("page1"))
        back.place(x = 40, y = 70)

        next = ttk.Button(self, text = "Next", command=lambda: parent.show_page("page3"))
        next.place(x = 80, y = 70)

        self.main()

    def main(self):
       # Main Text
        self.canvas.create_text(600,200, text = "Kenalan yuk!!!", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(600,230, text = "Milestone 11 SPARTA HMIF ITB 2022", fill="black", font=('Helvetica 15'))
        self.canvas.create_text(300,280, text = "19622066 Vanson Kurnialim", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(700,280, text = "19622093 Micky Valentino", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(300,300, text = "19622071 Edbert Eddyson Gunawan ", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(700,300, text = "19622194 Theo Livius Natael ", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(300,320, text = "19622293 Albert Ghazaly", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(700,320, text = "19622011 Muhamad Rifki Virziadeili", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(300,340, text = "19622091 Dinda Thalia Fahira", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(700,340, text = "19622230 Muhammad Rasheed Qais Tandjung", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(300,360, text = "19622223 Louis Ferdyo Gunawan", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(700,360, text = "19622070 Erwan Poltak Halomoan", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(300,380, text = "19622034 Abdullah Mubarak", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(700,380, text = "19622224 Kayla Dyara", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(300,400, text = "19622311 Jimly Nur Arif", fill="black", font=('Helvetica 10'), anchor="w", justify="left")
        self.canvas.create_text(600,430, text = "Definisi", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(600,460, text = "Color Detection App merupakan suatu aplikasi yang membantu ", fill="black", font=('Helvetica 12'))
        self.canvas.create_text(600,490, text = "penderita colour vision deficiency (CVD) atau buta warna untuk mengenali warna disekitarnya. ", fill="black", font=('Helvetica 12'))
        self.canvas.create_text(600,520, text = "Fungsi", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(600,550, text = "Color Detection App akan memindai warna suatu objek dan memberikan hasil warna dari objek yang terdeteksi.  ", fill="black", font=('Helvetica 12'))
        self.canvas.create_text(600,580, text = "memberikan hasil warna dari objek yang terdeteksi. ", fill="black", font=('Helvetica 12'))
        self.canvas.pack()
