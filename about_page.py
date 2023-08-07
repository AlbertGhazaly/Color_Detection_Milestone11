import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

class About(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page_callback = show_page_callback
        
        # Canvas
        # Create header, content box, and footer
        self.canvas = Canvas(self, width = 720, height=540, bg="white")
        self.canvas.create_rectangle(0, 0, 720, 75, outline = "light grey", fill="light grey")
        self.canvas.create_rectangle(30, 90, 690, 470, outline = "light grey", fill="light grey")
        
        # Create header buttons
        homeButton = self.canvas.create_text(205, 43, text="Return to Home", font = 'Aerial 18', fill = 'black', tags = 'return-home')
        startAppButton = self.canvas.create_text(500, 43, text="Start App", font = 'Aerial 18', fill = 'black', tags = 'start-app')
        
        # Add underline to header buttons
        bboxHome = self.canvas.bbox(homeButton)
        bboxStart = self.canvas.bbox(startAppButton)
        
        self.canvas.create_rectangle(bboxHome[0], bboxHome[3], bboxHome[2], bboxHome[3] + 2, outline='red', fill = 'red')
        self.canvas.create_rectangle(bboxStart[0], bboxStart[3], bboxStart[2], bboxStart[3] + 2, outline='blue', fill = 'blue')
        
        # Add header button fuctionality
        rectHome = self.canvas.tag_bind('return-home', '<Button-1>', self.homeButton)
        rectStart = self.canvas.tag_bind('start-app', '<Button-1>', self.startApp)
        
        # Add button hover logic
        def buttonEnter(event, button):
            self.canvas.itemconfig(button, fill='#FFA500')
            
            self.canvas.config(cursor='cross')
            self.canvas.update()
            
        def buttonLeave(event):
            self.canvas.itemconfig('return-home', fill='black')
            self.canvas.itemconfig('start-app', fill='black')
            
            self.canvas.config(cursor='')
            self.canvas.update()
        
        self.canvas.tag_bind('return-home', '<Enter>', lambda event: buttonEnter(event, 'return-home'))
        self.canvas.tag_bind('start-app', '<Enter>', lambda event: buttonEnter(event, 'start-app'))
        
        self.canvas.tag_bind('return-home', '<Leave>', buttonLeave)
        self.canvas.tag_bind('start-app', '<Leave>', buttonLeave)
        
        # Main function
        self.main()
        
    def homeButton(self, event):
        self.show_page_callback('page1')
        
    def startApp(self, event):
        self.show_page_callback('page5')
        
    def main(self):
       # Main Text
        self.canvas.create_text(360,115, text = "Kenalan yuk!!!", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(360,145, text = "Aplikasi ini dibuat oleh: Milestone 11 SPARTA HMIF 22", fill="black", font=('Helvetica 15'))
        
        self.names = [
            '19622011 Muhamad Rifki Virziadeili',
            '19622034 Abdullah Mubarak',
            '19622066 Vanson Kurnialim',
            '19622070 Erwan Poltak Halomoan',
            '19622071 Edbert Eddyson Gunawan',
            '19622091 Dinda Thalia Fahira',
            '19622093 Micky Valentino',
            '19622194 Theo Livius Natael',
            '19622223 Louis Ferdyo Gunawan',
            '19622224 Kayla Dyara',
            '19622230 Muhammad Rasheed Qais Tandjung',
            '19622293 Albert Ghazaly',
            '19622311 Jimly Nur Arif']
        
        translate = 0; counter = 0
        for name in self.names:
            if counter <= 6:
                self.canvas.create_text(100, 190 + translate, text = name, fill="black", font=('Helvetica 10'), anchor="w", justify="left")
            else:
                if counter == 7:
                    translate = 0
                self.canvas.create_text(400, 190 + translate, text = name, fill="black", font=('Helvetica 10'), anchor="w", justify="left")

            translate += 20
            counter += 1
        
        base = 340
        self.canvas.create_text(360,base + 0, text = "Definisi", fill="black", font=('Helvetica 12 bold'))
        self.canvas.create_text(360,base + 20, text = "Color Detection App merupakan suatu aplikasi yang membantu ", fill="black", font=('Helvetica 9'))
        self.canvas.create_text(360,base + 40, text = "penderita colour vision deficiency (CVD) atau buta warna untuk mengenali warna disekitarnya. ", fill="black", font=('Helvetica 9'))
        self.canvas.create_text(360,base + 70, text = "Fungsi", fill="black", font=('Helvetica 12 bold'))
        self.canvas.create_text(360,base + 90, text = "Color Detection App akan memindai warna suatu objek dan memberikan hasil warna dari objek yang terdeteksi.  ", fill="black", font=('Helvetica 9'))
        self.canvas.create_text(360,base + 110, text = "memberikan hasil warna dari objek yang terdeteksi. ", fill="black", font=('Helvetica 9'))
        
        self.canvas.create_rectangle(0, 540, 720, 500, fill="#D9D9D9", outline = "#D9D9D9")
        self.canvas.create_text(360,520, text="Created by SPARTANS MS-11", fill = "black", font='Aerial 10', tags="text_tag")
        
        self.canvas.pack()
