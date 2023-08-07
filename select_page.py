import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import * 

class Select(tk.Frame):
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
        self.main()
        
    def homeButton(self, event):
        self.show_page_callback('page1')
        
    def startApp(self, event):
        self.show_page_callback('page3')
        
    def main(self):
       # Main Text
        self.canvas.create_text(360,220, text = "MODE 1", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(360,270, text = "MODE 2", fill="black", font=('Helvetica 15'))
       
        self.canvas.create_rectangle(0, 540, 720, 500, fill="#D9D9D9", outline = "#D9D9D9")
        self.canvas.create_text(360,520, text="Created by SPARTANS MS-11", fill = "black", font='Aerial 10', tags="text_tag")
        
        self.canvas.pack()


