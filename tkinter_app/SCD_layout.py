import os
import sys
import cv2
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk




class frame :
    def __init__(self) :
      
        self.root = tk.Tk()  # create root window
        self.root.title("SCD layout")
        self.root.config(bg="white")
        self.root.maxsize(1200, 900)


# frame warna
        
        self.frame_warna =tk.Frame(self.root, width=70, height=70, bg="Blue")
        self.frame_warna.grid(row=0, column=0, padx=50, pady=10)
        self.nama_warna = tk.Frame(self.root,width=50,height=70,bg="White" ).grid(row=0,column=1,padx=0,pady=0)
        tk.Label(self.nama_warna, text="Hex",bg="White").grid(row=0,column=1,padx=0,pady=10,sticky="SW")
        tk.Label(self.nama_warna, text="Blue", bg="White").grid(row=0,column=1,padx=0,pady=10,sticky="NW")
        self.mode= tk.Frame(self.root,width=70,height=70,bg="White").grid(row = 0,column= 2,padx=600,pady=10,sticky="NE")
        tk.Label(self.mode,text="Single Color Detection" ).grid(row = 0,column= 2,padx=5,pady=10)
        
        
        
        self.root.mainloop()
        
        
        
    
        
    

        
        
frame()