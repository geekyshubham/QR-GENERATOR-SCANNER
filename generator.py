import qrcode
import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from PIL import Image,ImageTk
from tkinter import filedialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
ROOT.geometry("500x300")
data = simpledialog.askstring(title="QRCode Generator",
                                  prompt="Enter data to feed in QR Code:")

# check it out
img = qrcode.make(data)
"""
qr = qrcode.QRCode(
    version=1, #size_of_box
    error_correction=qrcode.constants.ERROR_CORRECT_H, #
    box_size=10, #pixel_no_for_box
    border=4, #thickness
)

ERROR_CORRECT_L — About 7% or fewer errors can be corrected.
ERROR_CORRECT_M — About 15% or fewer errors can be corrected. This is the default value.
ERROR_CORRECT_Q — About 25% or fewer errors can be corrected.
ERROR_CORRECT_H — About 30% or fewer errors can be corrected.
"""
def logo(img):
    logo_display = Image.open('logo.png')
    logo_display.thumbnail((60, 60))

    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
    img.paste(logo_display, logo_pos)


 #save as image
file_path = filedialog.asksaveasfilename(defaultextension='.png')
img.save(file_path)

ROOT.quit()

print("Your image has been saved ")


#img.show()

root = Toplevel()
root.title("Generated QR CODE")
canvas = Canvas(root,width=300,height=300)
canvas.pack()

image = ImageTk.PhotoImage(img)
imagesprite = canvas.create_image(150, 150,image=image)
root.mainloop()
