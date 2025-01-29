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

