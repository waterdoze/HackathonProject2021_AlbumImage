import tkinter as tk
<<<<<<< HEAD
from tkinter import *
from tkinter import messagebox
=======
>>>>>>> 150a24cad51e9087110c5905255dd0d0329e3fd6
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image
import sys
<<<<<<< HEAD
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sifting

#create canvas
=======
import os

>>>>>>> 150a24cad51e9087110c5905255dd0d0329e3fd6
master = tk.Tk()

master.geometry("400x400")

<<<<<<< HEAD
#image recoginition
def start(ImageB):
    master.destroy()
    sifting.sift(ImageB)
    exit()

#choosing image from file explorer
def findImage():
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    #shows image and confirms correct
    try: 
        img=Image.open(files[0])
        img = img.resize((300, 300), Image.ANTIALIAS) 
        imgPrint =ImageTk.PhotoImage(img)
        label1 = Label(image = imgPrint)
        label1.image = imgPrint
        label1.place(x=50,y=0)
        ButtonDecline = Button(master, text = "wrong image", command = lambda: findImage()).pack(side = BOTTOM)
        ButtonConfirm = Button(master, text = "correct image", command = lambda:start(files[0])).pack(side = BOTTOM)
        
    #catch error if file selected is not an image
    except IOError:
        messagebox.showerror("error","not an image")
    
#instruction text
labelTextInstructions = Label(master,text = " select an image from file explorer").pack(pady =10)

#button to show file explorer
imagepullerButton = Button(master, text = "open file explorer" , command = findImage).pack(pady = 10)
=======

def find_image():
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    try:
        im = Image.open(files)
    except IOError:
        messagebox.showerror("not an image")

>>>>>>> 150a24cad51e9087110c5905255dd0d0329e3fd6

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        master.destroy()

<<<<<<< HEAD
master.mainloop()

sys.exit()
=======
>>>>>>> 150a24cad51e9087110c5905255dd0d0329e3fd6

labelTextInstructions = Label(master, text="this is main window \n select an image from file explorer").pack(pady=10)

imagepullerButton = Button(master, text="open file explorer", command=find_image).pack(pady=10)

master.protocol("WM_DELETE_WINDOW", on_closing)

master.mainloop()

<<<<<<< HEAD


    


    
=======
sys.exit()
>>>>>>> 150a24cad51e9087110c5905255dd0d0329e3fd6
