import os
import sys
import cv2
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk




class SCD():
    def __init__(self) :
        
        self.root = tk.Tk()  # create root window
        self.root.title("SCD layout")
        self.root.config(bg="white")
        self.root.maxsize(720, 540)
        
        self.main()

    def main(self):
        # frame warna
        
        self.frame_warna =tk.Frame(self.root, width=100, height=70, bg="Blue")
        self.frame_warna.pack(side=tk.LEFT, anchor="nw",fill=tk.X,ipadx=0,padx=20)
        
        self.nama_warna = tk.Frame(self.root,width=50,height=70,bg="White" ).pack(side=tk.LEFT)
        tk.Label(self.nama_warna, text="Hex",bg="White").pack(anchor="w")
        tk.Label(self.nama_warna, text="Blue", bg="White").pack(anchor ="w")

        self.mode= tk.Frame(self.root,width=70,height=70,bg="White").pack( side=tk.RIGHT,anchor="ne")
        tk.Label(self.mode,text="Single Color Detection",justify="left" ).pack(side=tk.RIGHT,anchor="n")
        
        self.root.mainloop()

SCD()