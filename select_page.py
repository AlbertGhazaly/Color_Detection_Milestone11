import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import * 
from camera_page import access_cam
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
        homeButton = self.canvas.create_text(350, 43, text="Return to Home", font = 'Aerial 18', fill = 'black', tags = 'return-home')
        # Add underline to header buttons
        bboxHome = self.canvas.bbox(homeButton)

        self.canvas.create_rectangle(bboxHome[0], bboxHome[3], bboxHome[2], bboxHome[3] + 2, outline='red', fill = 'red')
        # Add header button fuctionality
        rectHome = self.canvas.tag_bind('return-home', '<Button-1>', self.homeButton)
        self.main()
        
    def homeButton(self, event):
        self.show_page_callback('page1')
        
        
    def main(self):
       # Main Text
        self.canvas.create_text(360,220, text = "MODE 1", fill="blue", font=('Helvetica 15 bold'), tags='start-app')
        self.canvas.create_text(360,270, text = "MODE 2", fill="green", font=('Helvetica 15 bold'), tags='start-app2')
        #tag bind
        self.canvas.tag_bind('start-app', '<Button-1>', self.start_app)
        self.canvas.tag_bind('start-app2', '<Button-1>', self.start_app2)

        self.canvas.create_rectangle(0, 540, 720, 500, fill="#D9D9D9", outline = "#D9D9D9")
        self.canvas.create_text(360,520, text="Created by SPARTANS MS-11", fill = "black", font='Aerial 10', tags="text_tag")
        self.canvas.pack()

    def start_app(self,event):
        access_cam = False
        self.show_page_callback('page3')
        print("access_cam: ", access_cam)
    def start_app2(self,event):
        access_cam = True
        self.show_page_callback('page3')
        print("access cam:", access_cam)


