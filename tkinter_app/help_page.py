import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Canvas

class About(tk.Tk):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas