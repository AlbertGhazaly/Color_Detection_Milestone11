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

def main():
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=720, height=540, bg="white", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)

    # header
    mycanvas.create_rectangle(0, 75, 720, 0, fill="#D9D9D9", outline = "#D9D9D9")
    # middle
    mycanvas.create_rectangle(150, 425, 570, 150, fill="#D9D9D9", outline = "#D9D9D9")
    #footer
    mycanvas.create_rectangle(0, 540, 720, 500, fill="#D9D9D9", outline = "#D9D9D9")

    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()