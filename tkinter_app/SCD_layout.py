from tkinter import *


class frame :
    def __init__(self):
        self.root = Tk()  # create root window
        self.root.title("SCD layout")
        self.root.config(bg="white")
        self.root.maxsize(1200, 900)


# frame warna
        
        self.frame_warna =Frame(self.root, width=70, height=70, bg="Blue")
        self.frame_warna.grid(row=0, column=0, padx=50, pady=10)
        self.nama_warna = Frame(self.root,width=50,height=70,bg="White" ).grid(row=0,column=1,padx=0,pady=0)
        Label(self.nama_warna, text="Hex",bg="White").grid(row=0,column=1,padx=0,pady=10,sticky="SW")
        Label(self.nama_warna, text="Blue", bg="White").grid(row=0,column=1,padx=0,pady=10,sticky="NW")
        self.mode= Frame(self.root,width=70,height=70,bg="White").grid(row = 0,column= 2,padx=600,pady=10,sticky="NE")
        Label(self.mode,text="Single Color Detection" ).grid(row = 0,column= 2,padx=5,pady=10)
        
        
        self.root.mainloop()
        
        
        
    
        
    

        
        
frame()