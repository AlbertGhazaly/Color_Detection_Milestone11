import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import * 

class Select(tk.Frame):
    def __init__(self,parent,show_page_callback):
        super().__init__(parent)
        self.show_page_callback = show_page_callback
       # Canvas
        # Create header, content box, and footer
        self.canvas = Canvas(self, width = 720, height=540, bg="white")
        self.canvas.create_rectangle(0, 0, 720, 75, outline = "light grey", fill="light grey")
        self.canvas.create_rectangle(30, 90, 690, 470, outline = "light grey", fill="light grey")

