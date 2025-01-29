# INSTALL AND IMPORT REQUIRED LIBRARIES
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage, Button, Frame
from geopy.geocoders import Nominatim
from tkinter import messagebox
from datetime import *
import requests
import re 
import time
import os
import pytz
from PIL import Image, ImageTk
from timezonefinder import TimezoneFinder
from tkintermapview import TkinterMapView

# INITIALIZE THE MAIN APP WINDOW
root = Tk()
root.title("WeatherMap Explorer")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

# Labels for each field
label1 = Label(root, text="Condition:", font=('Helvetica', 10), fg="white", bg="#203243")
label1.place(x=35, y=120)
label2 = Label(root, text="Temperature:", font=('Helvetica', 10), fg="white", bg="#203243")
label2.place(x=35, y=140)
label3 = Label(root, text="Wind Speed:", font=('Helvetica', 10), fg="white", bg="#203243")
label3.place(x=35, y=160)
label4 = Label(root, text="Pressure:", font=('Helvetica', 10), fg="white", bg="#203243")
label4.place(x=35, y=180)
label5 = Label(root, text="Visibility:", font=('Helvetica', 10), fg="white", bg="#203243")
label5.place(x=35, y=200)

# Search Box
search_path = os.path.join("C:/Users/emmad/OneDrive/Desktop/images", "Rounded Rectangle 3.png") #Replace with your actual path
try:
    search_image = PhotoImage(file=search_path)
    my_image = Label(image=search_image, bg="#57adff")
    my_image.place(x=270, y=120)
except FileNotFoundError:
    print("Warning: Search box image not found.")

weat_path = os.path.join("C:/Users/emmad/OneDrive/Desktop/images", "Layer 7.png") #Replace with your actual path
try:
    weat_image = PhotoImage(file=weat_path)
    weather_image = Label(root, image=weat_image, bg="#203243")
    weather_image.place(x=290, y=127)
except FileNotFoundError:
    print("Warning: Weather icon image not found.")

textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

search_icon = os.path.join("C:/Users/emmad/OneDrive/Desktop/images", "Layer 6.png")
search_photo = PhotoImage(file=search_icon)
my_image_icon = Button(image=search_photo, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
my_image_icon.place(x=645, y=125)

# Bottom box
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# Bottom boxes
firstpath = os.path.join("C:/Users/emmad/OneDrive/Desktop/images", "Rounded Rectangle 2.png")
firstbox = PhotoImage(file=firstpath)
secondpath = os.path.join("C:/Users/emmad/OneDrive/Desktop/images", "Rounded Rectangle 2 copy.png")
secondbox = PhotoImage(file=secondpath)

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)