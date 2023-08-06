import tkinter as tk
from about_page import *
from help_page import *
from tkinter import *

# from root_app import App


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

class Start(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)

        self.show_page_callback = show_page_callback

        self.pack(fill=BOTH, expand=YES)
        # sel.pack(fill=BOTH, expand=YES)
        mycanvas = ResizingCanvas(self, width=720, height=540, bg="white", highlightthickness=0)
        mycanvas.pack(fill=BOTH, expand=YES)

        # header
        mycanvas.create_rectangle(0, 75, 720, 0, fill="#D9D9D9", outline = "#D9D9D9")
        mycanvas.create_text(360, 40, text="MS-11 Color Detector", fill = "black", font='Aerial 40', tags="title_tag")
        # middle
        mycanvas.create_rectangle(150, 425, 570, 150, fill="#D9D9D9", outline = "#D9D9D9")
        
        mycanvas.create_text(360, 260, text="[START]", fill = "black", font='Helvetica 40', tags=["title_tag", "start_tag"])
        
        mycanvas.create_text(200,390, text="[Help]", fill = "black", font='Helvetica 20', tags=["help_tag", "button_tag"])
        mycanvas.create_text(360,390, text="[Folder]", fill = "black", font='Helvetica 20', tags=["folder_tag", "button_tag"])
        mycanvas.create_text(520,390, text="[Exit]", fill = "black", font='Helvetica 20', tags=["exit_tag", "button_tag"])
        #footer
        
        mycanvas.create_rectangle(0, 540, 720, 500, fill="#D9D9D9", outline = "#D9D9D9")
        mycanvas.create_text(360,520, text="Created by MS-11", fill = "black", font='Aerial 10', tags="text_tag")

        mycanvas.tag_bind("title_tag", "<Button-1>", self.nextButton)
        mycanvas.tag_bind("help_tag", "<Button-1>", self.helpButton)
        mycanvas.pack()
        # tag all of the drawn widgets
        mycanvas.addtag_all("all")
        # root.mainloop()

    def nextButton(self, event):
        print("ho")
        self.show_page_callback("page2")

    def helpButton(self, event):
        print("ho")
        self.show_page_callback("page4")
