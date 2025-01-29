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

# IMAGE RESIZING FUNCTION
def resize_image_aspect(image_path, max_width, max_height):
    try:
        img = Image.open(image_path)
        width, height = img.size
        aspect_ratio = width / height

        if width > max_width:
            new_width = max_width
            new_height = int(new_width / aspect_ratio)
        elif height > max_height:
            new_height = max_height
            new_width = int(new_height * aspect_ratio)
        else:
            new_width, new_height = width, height

        resized_img = img.resize((new_width, new_height))
        return ImageTk.PhotoImage(resized_img)
    except FileNotFoundError:
        print(f"Image file not found: {image_path}")
        return None
    except Exception as error_message:
        print(f"Error processing image: {error_message}")
        return None

# WEATHER ICON RETRIEVAL FUNCTION
def get_weather_icon(condition, is_night):
    icon_map = {
        "clear": "01n@2x" if is_night else "01d@2x",
        "partly cloudy": "02n@2x" if is_night else "02d@2x",
        "cloudy": "03n@2x" if is_night else "03d@2x",
        "overcast": "04n@2x" if is_night else "04d@2x",
        "light rain": "09n@2x" if is_night else "09d@2x",
        "rain": "10n@2x" if is_night else "10d@2x",
        "thunderstorm": "11n@2x" if is_night else "11d@2x",
        "snow": "13n@2x" if is_night else "13d@2x",
        "mist": "50n@2x" if is_night else "50d@2x",
    }
    for key, icon in icon_map.items():
        if key in condition:
            return icon
    return "01d@2x"  # Default to clear (day)

# WEATHER DATA RETRIEVAL FUNCTION
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error_message:
        return {"error": f"Error fetching weather data: {error_message}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {error_message}"}

# MAIN WEATHER UPDATE FUNCTION
def getWeather():
    city = textfield.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return
    try:
        location = geolocator.geocode(city)
        if not location:
            messagebox.showerror("Error", "City not found!")
            return

        map_view.set_position(location.latitude, location.longitude, marker=True)
        map_view.set_zoom(10)

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        
        weather_data = get_weather(city)

        if "error" in weather_data:
            messagebox.showerror("Error", weather_data["error"])
            return

# Update current weather information
        try:
            condition_text = weather_data['current_condition'][0]['weatherDesc'][0]['value'].lower()
            condition.config(text=condition_text.capitalize())
            temperature.config(text=weather_data['current_condition'][0]['temp_C'] + " °C")
            wind.config(text=weather_data['current_condition'][0]['windspeedKmph'] + " km/h")
            pressure.config(text=weather_data['current_condition'][0]['pressure'] + " mb")
            visibility.config(text=weather_data['current_condition'][0]['visibility'] + " km")
        except (IndexError, KeyError) as error_message:
            messagebox.showerror("Error", f"Error processing current weather data: {error_message}")
            return

# Update current weather icon
        try:
            is_night = "pm" in current_time.lower()
            icon_file = get_weather_icon(condition_text, is_night)
            icon_path = f"C:/Users/emmad/OneDrive/Desktop/images/{icon_file}.png"
            photo1 = resize_image_aspect(icon_path, 100, 100)
            if photo1:
                firstimage.config(image=photo1)
                firstimage.image = photo1
        except (IndexError, KeyError, FileNotFoundError) as error_message:
            messagebox.showerror("Error", f"Error loading current weather icon: {error_message}")
            print(f"Error loading icon: {error_message}, path: {icon_path}")
            return

# Update weekly forecast information and icons
        if 'weather' in weather_data:
            num_forecast_days = len(weather_data['weather'])
            today = date.today()
            print(f"Weather data received: {weather_data}")
            for days_index in range(3):  # Loop over the first 3 days
                future_date = today + timedelta(days=days_index)
                day_name = future_date.strftime("%A")
                try:
                    day_labels[days_index].config(text=day_name)

                    
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

# Weather current
long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

condition = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
condition.place(x=100, y=120)

temperature = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
temperature.place(x=130, y=140)

wind = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
wind.place(x=130, y=160)

pressure = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
pressure.place(x=130, y=180)

visibility = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
visibility.place(x=130, y=200)

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