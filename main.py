import customtkinter
from tkinter import filedialog
from classifier import classifierFunction
from PIL import ImageTk, Image
import pyglet

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry('700x500')

pyglet.font.add_file('C:/Users/MSI/PycharmProjects/breedClassifier/FontRoboto/Roboto-Regular.ttf')

titleFont = customtkinter.CTkFont(family="Roboto-Regular",
              size=35, weight='bold')

buttonFont = customtkinter.CTkFont(family="Roboto-Regular",
              size=30)

resultFont = customtkinter.CTkFont(family="Roboto-Regular",
              size=20)

def upload_photo(label, display_image):
    root.update()
    file = filedialog.askopenfilename()
    label.configure(text=classifierFunction.cat_color(file))
    new_image = customtkinter.CTkImage(Image.open(file), size=(300, 250))
    display_image.configure(image=new_image)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=60, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame, text="Cat?", font=titleFont)
title.pack(pady=5, padx=5)

button = customtkinter.CTkButton(master=frame, text="Upload Cat",
                                 command=lambda: upload_photo(color, display), font=buttonFont)
button.pack(pady=5, padx=10)

display = customtkinter.CTkLabel(master=frame, text="")
display.pack(pady=0, padx=0)

color = customtkinter.CTkLabel(master=frame, text="", font=resultFont)
color.pack(pady=5, padx=10)

root.mainloop()
