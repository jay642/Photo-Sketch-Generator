from PIL import Image as im, ImageFilter
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Image Viewer")

filename = ""
display = Label(image = "")

def browse_file_func():
        global filename
        
        
        filename = filedialog.askopenfilename(initialdir = "/home/Projects/sketch_generator/testing/image/", 
                    title = "Gallery",
                    filetypes = (("jpg files", ".jpg"),("png files",".png"),("jpeg files",".jpeg"), ("all files", ".")))

        display_image()
        
 #THIS FUNCTION IS USED TO CONVERT THE IMAGE INTO GRAY COLOUR IMAGE       
def grey_scale(img, pixel_img):
        width, height = img.size

        for i in range(width):
            for j in range(height):

                r,g,b = img.getpixel((i, j))
                gray_scale = (0.299*r + 0.587*g + 0.114*b)
                pixel_img[i, j] = (int(gray_scale), int(gray_scale), int(gray_scale))


#THIS FUNCTION CONVERT BLACK BACKGROUND TO WHITE AND WHITE EDGES TO BLACK
def invert_image(img):
        width, height = img.size

        for i in range(width):
            for j in range(height):

                r,g,b = img.getpixel((i, j))
                img.putpixel((i, j), (abs(255 - r), abs(255 - g), abs(255 - b)))


#THIS FUNCTION IS USED TO DISPLAY THE SKETCH 
def display_image():
    global display
   
    img = im.open(filename)

    pixel_img = img.load()
    
    grey_scale(img, pixel_img)
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    
    img = img.filter(ImageFilter.FIND_EDGES)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    invert_image(img)

    #img.thumbnail((1500, 900), im.ANTIALIAS)

    img.save("./save/save.jpg")

    display_sketch=ImageTk.PhotoImage(im.open("./save/save.jpg"))

    display.destroy()
    display = Label(image = display_sketch)
    display.grid(row=0,column=0,columnspan=3)

    browse_button = Button(root, text = "Browse Files", command = browse_file_func)
    browse_button.grid(column = 2, row = 2)
    
    #THIS MAINLOOP IS USED TO ALLOW USER TO BROWSE PHOTOS UNTIL THE THE EXIT BUTTON IS NOT CLICKED
    root.mainloop() 

browse_button = Button(root, text = "Browse Files", command = browse_file_func)
exit_button = Button(root, text = "Exit", command = exit)

#GRID IS USED TO ALIGN WIDGETS IN THE ROOT WINDOW
browse_button.grid(column = 2, row = 2)
exit_button.grid(column = 0, row = 2)

root.mainloop()