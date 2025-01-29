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

# SETUP GEOLOCATION
geolocator = Nominatim(user_agent="my_weather_app_v1")

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

# Clock
clock = Label(root, font=("Helvetica", 30, "bold"), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# Timezone
timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

#first cell
first_frame = Frame(root, width=230, height=132, bg="#282829")
first_frame.place(x=35, y=315)
day_1 = Label(first_frame, font="arial 20", bg="#282829", fg="#fff")
day_1.place(x=100, y=5)
firstimage = Label(first_frame, bg="#282829")
firstimage.place(x=1, y=15)
day1temp = Label(first_frame, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=100, y=50)

#second cell
second_frame = Frame(root, width=70, height=115, bg="#282829")
second_frame.place(x=305, y=325)
day_1 = Label(second_frame, bg="#282829", fg="#fff")
day_1.place(x=10, y=5)
firstimage = Label(second_frame, bg="#282829")
firstimage.place(x=7, y=20)
day1temp = Label(second_frame, bg="#282829", fg="#fff")
day1temp.place(x=10, y=70)

#third cell
third_frame = Frame(root, width=70, height=115, bg="#282829")
third_frame.place(x=405, y=325)
day_2 = Label(third_frame, bg="#282829", fg="#fff")
day_2.place(x=10, y=5)
secondimage = Label(third_frame, bg="#282829")
secondimage.place(x=7, y=20)
day2temp = Label(third_frame, bg="#282829", fg="#fff")
day2temp.place(x=10, y=70)

#fourth cell
fourth_frame = Frame(root, width=70, height=115, bg="#282829")
fourth_frame.place(x=505, y=325)
day_3 = Label(fourth_frame, bg="#282829", fg="#fff")
day_3.place(x=10, y=5)
thirdimage = Label(fourth_frame, bg="#282829")
thirdimage.place(x=7, y=20)
day3temp = Label(fourth_frame, bg="#282829", fg="#fff")
day3temp.place(x=10, y=70)