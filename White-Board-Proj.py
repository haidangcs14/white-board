from tkinter import *
# from tkinter.colorchooser import askcolor
from tkinter import ttk, filedialog
import tkinter as tk
import os

class WhiteBoardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("White board")
        self.root.geometry("1050x570+150+50")
        self.root.configure(bg = "#f2f3f5")
        self.root.resizable(False, False)


        self.current_x = 0
        self.current_y = 0
        self.color = "black"
        self.current_val = tk.DoubleVar()
        
        self.create_widgets()
        self.display_pallete()  
        
    def create_widgets(self):
        #icon
        img_icon = PhotoImage(file = "./Images/logo.png")
        self.root.iconphoto(False, img_icon)
        #side bar
        color_box = PhotoImage(file = "./Images/color section.png")
        Label(self.root, image = color_box, bg = "#f2f3f5").place(x = 10, y = 20)

        self.eraser = PhotoImage(file = "./Images/eraser.png")
        Button(self.root, image = self.eraser, bg = "#f2f3f5", command = self.new_canvas).place(x =30, y = 400)

        self.import_img = PhotoImage(file = "./Images/addimage.png")
        Button(self.root, image = self.import_img, bg = "#f2f3f5", command = self.insert_image).place(x =30, y = 450)

        self.display_pallete()
        
        # main screen
        canvas = Canvas(self.root, width = 930, height = 500, background = "white", cursor = "hand2")
        canvas.place(x = 100, y = 10)
        
        canvas.bind('<Button-1>', self.locate_xy)
        canvas.bind('<B1-Motion>', self.addline)

        #slider
        
        slider = ttk.Scale(self.root, from_ = 0 , to_ = 100, orient = "horizontal", command = self.slider_changed, variable = self.current_val)
        slider.place(x = 30, y = 530)

        value_label = ttk.Label(self.root, text = self.get_current_val())
        value_label.place(x = 27, y = 550)

        self.canvas = canvas
        # self.current_val = current_val
        self.value_label = value_label
        
    def locate_xy(self, work):
        # global current_x, current_y
        self.current_x, self.current_y = work.x, work.y
    
    def addline(self, work):
        # global current_x, current_y
        self.canvas.create_line((self.current_x, self.current_y, work.x, work.y), width = self.get_current_val(),
                        fill = self.color, capstyle = ROUND, smooth = True)
        self.current_x, self.current_y = work.x, work.y

    def show_color(self, new_color):
        # global color
        self.color = new_color

    def new_canvas(self):
        self.canvas.delete('all')
        self.display_pallete()

    def insert_image(self):
        # global filename
        # global f_img
        self.filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select image file",
                                            filetypes = (("PNG file", "*.png"), ("Add file", "new.txt")))
        f_img = tk.PhotoImage(file = self.filename)
        my_img = self.canvas.create_image(180, 50, image = f_img)
        self.root.bind("<B3-Motion>", self.my_callback) 

    def my_callback(self, event):
        global f_img
        f_img = tk.PhotoImage(file = self.filename)
        my_img = self.canvas.create_image(event.x, event.y, image = f_img) 

    def display_pallete(self):
        colors = Canvas(self.root, bg = "#fff", width = 37, height = 300, bd = 0)
        colors.place(x = 30, y = 60) 
        id = colors.create_rectangle((10, 10, 30, 30), fill = "black")
        colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('black'))
        id = colors.create_rectangle((10, 40, 30, 60), fill = "brown4")
        colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('brown4'))
        id = colors.create_rectangle((10, 70, 30, 90), fill = "gray")
        colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('gray'))
        id = colors.create_rectangle((10, 100, 30, 120), fill = "red")
        colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('red'))
        id = colors.create_rectangle((10, 130, 30, 150), fill = "orange")
        colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('orange'))
        id = colors.create_rectangle((10, 160, 30, 180), fill = "yellow")
        colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('yellow'))
        id = colors.create_rectangle((10, 190, 30, 210), fill = "green")
        colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('green'))
        id = colors.create_rectangle((10, 220, 30, 240), fill = "blue")
        colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('blue'))
        id = colors.create_rectangle((10, 250, 30, 270), fill = "purple")
        colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('purple'))

    def get_current_val(self):
            return '{: .2f}'.format(self.current_val.get())
        
    def slider_changed(self, event):
        self.value_label.configure(text = self.get_current_val())
    
    def run(self):
        self.root.mainloop()
        

if __name__ == "__main__":
    root = tk.Tk()
    whiteboard_app = WhiteBoardApp(root)
    whiteboard_app.run()