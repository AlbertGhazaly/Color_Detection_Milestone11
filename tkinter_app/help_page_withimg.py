from tkinter import *
from PIL import Image, ImageTk

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
        
        # Resize images based on the new canvas size
        for img_item in self.img_items:
            original_img = self.img_items[img_item]
            resized_img = original_img.resize((event.width, event.height), Image.ANTIALIAS)
            self.photo_items[img_item] = ImageTk.PhotoImage(resized_img)
            self.itemconfig(img_item, image=self.photo_items[img_item])

def on_back_click(event):
    print("Back button clicked!") # Replace this function with the desired action when the "Back" button is clicked
    
def on_back_enter(event):
    # Change the mouse cursor to the hand icon when hovering over the "Back" button
    mycanvas.config(cursor="hand2")

def on_back_leave(event):
    # Change the mouse cursor back to the default arrow when leaving the "Back" button
    mycanvas.config(cursor="arrow")

def main():
    global mycanvas
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe, width=720, height=540, bg="white", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)
    
    # add some widgets to the canvas
    mycanvas.create_rectangle(0, 0, 720, 67, fill="#D9D9D9", outline="#D9D9D9")
    mycanvas.create_text(360, 30, text="Help", fill="#000000", font='Arial 24', tags="title_tag")
    
    # Load images and create image items with specific dimensions
    img1 = Image.open("C:/Users/louis/Downloads/Screenshot 2023-08-02 164127.png")
    img2 = Image.open("C:/Users/louis/Downloads/Screenshot 2023-08-02 164127.png")
    img1 = img1.resize((268, 232), Image.ANTIALIAS)
    img2 = img2.resize((266, 232), Image.ANTIALIAS)
    img1_photo = ImageTk.PhotoImage(img1)
    img2_photo = ImageTk.PhotoImage(img2)
    img1_item = mycanvas.create_image(160, 238, image=img1_photo, tags="img_tag")
    img2_item = mycanvas.create_image(560, 238, image=img2_photo, tags="img_tag")
    
    mycanvas.img_items = {img1_item: img1, img2_item: img2}
    mycanvas.photo_items = {img1_item: img1_photo, img2_item: img2_photo}

    mycanvas.create_text(160, 370, text="Arahkan kamera ke benda yang dituju,", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.create_text(160, 390, text="lalu ambil gambar", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.create_text(560, 370, text="tekan tombol “open gallery”, lalu", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.create_text(560, 390, text="pilihlah gambar", fill="#000000", font='Arial 12', tags="text_tag")
    
    mycanvas.create_rectangle(26, 440, 131, 480, fill="#D9D9D9", outline="#D9D9D9", tags=["back_button"])
    mycanvas.create_text(78, 460, text="Back", fill="#000000", font='Arial 16', tags=["button_tag", "back_button"])
    mycanvas.create_rectangle(0, 494, 720, 540, fill="#D9D9D9", outline="#D9D9D9")
    mycanvas.create_text(365, 515, text="Created By ....", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.pack()
    # tag all of the drawn widgets
    mycanvas.addtag_all("all")

    # Bind the back button to the on_back_click function
    mycanvas.tag_bind("back_button", "<Button-1>", on_back_click)
    mycanvas.tag_bind("back_button", "<Enter>", on_back_enter)
    mycanvas.tag_bind("back_button", "<Leave>", on_back_leave)

    root.mainloop()

if __name__ == "__main__":
    main()



