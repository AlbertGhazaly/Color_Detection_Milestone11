import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)
    
        # Calculate the new font sizes based on the window height
        title_font_size = int(24 * (event.height / 540))  # 540 is the initial canvas height
        text_font_size = int(12 * (event.height / 540))  # 540 is the initial canvas height
        button_font_size = int(16 * (event.height / 540))  # 540 is the initial canvas height

        # Set the new font sizes for the text elements in the canvas
        self.itemconfig("title_tag", font=("Arial", title_font_size))
        self.itemconfig("text_tag", font=("Arial", text_font_size))
        self.itemconfig("button_tag", font=("Arial", button_font_size))

class About(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # self.show_page_callback = show_page_callback

        # self.pack(fill=BOTH, expand=YES)
        # mycanvas = ResizingCanvas(self, width=720, height=540, bg="white", highlightthickness=0)
        # mycanvas.pack(fill=BOTH, expand=YES)
        
        # Canvas
        self.canvas = Canvas(self, width = 720, height=540, bg="white")
        self.canvas.create_rectangle(0, 0, 720, 75, outline = "light grey", fill="light grey")
        self.canvas.create_rectangle(30, 90, 690, 470, outline = "light grey", fill="light grey")

        back = ttk.Button(self, text = "Back", command=lambda: parent.show_page("page1"))
        back.place(x = 40, y = 30)

        next = ttk.Button(self, text = "Next", command=lambda: parent.show_page("page3"))
        next.place(x = 134, y = 30)

        self.main()

    def main(self):
        # self.canvas.create_rectangle(0, 0, 20, 112, outline = "light grey", fill="red")
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
        self.canvas.create_text(360,520, text="Created by MS-11", fill = "black", font='Aerial 10', tags="text_tag")
        
        self.canvas.pack()
