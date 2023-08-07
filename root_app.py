import tkinter as tk
from tkinter import ttk
from tkinter import Canvas

from start_page import Start
from about_page import About
from help_page import Help
from camera_page import App

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Color Detection App")
        self.geometry("720x540")

        self.pages = {}  # Dictionary to hold different page frames
        self.create_pages()
        self.show_page("page1")

    def create_pages(self):
        # Create and store instances of your page frames
        self.pages["page1"] = Start(self, self.show_page)
        self.pages["page2"] = About(self, self.show_page)
        self.pages["page3"] = App(self, self.show_page)
        self.pages["page4"] = Help(self, self.show_page)

    def show_page(self, page_name):
        # Show the selected page and hide others
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()


# class Start(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)

        # mycanvas = ResizingCanvas(self, width=720, height=540, bg="white", highlightthickness=0)
        # mycanvas.pack(fill=BOTH, expand=YES)

        # # header
        # mycanvas.create_rectangle(0, 75, 720, 0, fill="#D9D9D9", outline = "#D9D9D9")
        # mycanvas.create_text(360,30, text="Color Detection APP", fill = "black", font='Aerial 40', tags="title_tag")
        # # middle
        # mycanvas.create_rectangle(150, 425, 570, 150, fill="#D9D9D9", outline = "#D9D9D9")
        # mycanvas.create_text(360,240, text="START", fill = "black", font='Helvetica 40', tags=["title_tag", "start_tag"])
        # mycanvas.create_text(200,390, text="Help", fill = "black", font='Helvetica 20', tags=["help_tag", "button_tag"])
        # mycanvas.create_text(360,390, text="Folder", fill = "black", font='Helvetica 20', tags=["folder_tag", "button_tag"])
        # mycanvas.create_text(520,390, text="Exit", fill = "black", font='Helvetica 20', tags=["exit_tag", "button_tag"])
        # #footer
        # mycanvas.create_rectangle(0, 540, 720, 500, fill="#D9D9D9", outline = "#D9D9D9")
        # mycanvas.create_text(360,520, text="Created By ....", fill = "black", font='Aerial 10', tags="text_tag")
        # mycanvas.pack()

        # button = ttk.Button(self, text="Go to Page 2", command=lambda: parent.show_page("page2"))
        # button.pack()

# class Page2(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)

#         label = tk.Label(self, text="Page 2")
#         label.pack(pady=10)

#         button = ttk.Button(self, text="Go to Page 1", command=lambda: parent.show_page("page1"))
#         button.pack()

#         button = ttk.Button(self, text="Go to Page 3", command=lambda: parent.show_page("page3"))
#         button.pack()

# class Page3(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)

#         label = tk.Label(self, text="Page 3")
#         label.pack(pady=10)

#         button = ttk.Button(self, text="Go to Page 2", command=lambda: parent.show_page("page2"))
#         button.pack()

