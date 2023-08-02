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

def main():
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=720, height=540, bg="white", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)

    # add some widgets to the canvas
    mycanvas.create_rectangle(0, 0, 720, 67, fill="#D9D9D9", outline="#D9D9D9")
    mycanvas.create_text(360, 30, text="Help",fill="#000000",font='Arial 24', tags="title_tag")
    mycanvas.create_rectangle(26, 122, 293, 354, fill="#D9D9D9", outline="#D9D9D9")
    mycanvas.create_rectangle(428, 122, 694, 354, fill="#D9D9D9", outline="#D9D9D9")
    mycanvas.create_text(160, 370, text="Arahkan kamera ke benda yang dituju,", fill="#000000",font='Arial 12', tags="text_tag")
    mycanvas.create_text(160, 390, text="lalu ambil gambar", fill="#000000",font='Arial 12', tags="text_tag")
    mycanvas.create_text(560, 370, text="tekan tombol “open gallery”, lalu", fill="#000000",font='Arial 12', tags="text_tag")
    mycanvas.create_text(560, 390, text="pilihlah gambar", fill="#000000",font='Arial 12', tags="text_tag")
    mycanvas.create_rectangle(26, 440, 131, 480, fill="#D9D9D9", outline="#D9D9D9")
    mycanvas.create_text(78,460, text="Back", fill="#000000",font='Arial 16', tags="button_tag")
    mycanvas.create_rectangle(0, 494, 720, 540, fill="#D9D9D9", outline="#D9D9D9")
    mycanvas.create_text(365,515, text="Created By ....", fill="#000000",font='Arial 16', tags="button_tag")
    mycanvas.pack()
    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()