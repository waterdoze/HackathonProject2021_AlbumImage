import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image
import sys
import os

master = tk.Tk()

master.geometry("400x400")


def find_image():
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    try:
        im = Image.open(files)
    except IOError:
        messagebox.showerror("not an image")


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        master.destroy()


labelTextInstructions = Label(master, text="this is main window \n select an image from file explorer").pack(pady=10)

imagepullerButton = Button(master, text="open file explorer", command=find_image).pack(pady=10)

master.protocol("WM_DELETE_WINDOW", on_closing)

master.mainloop()

sys.exit()
