import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image  
import sys
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
#create canvas
master = tk.Tk()

master.geometry("400x400")

def findMSE(ImageA, ImageB):
    mse = np.sum(ImageA.astype("float") - ImageB.astype("float")) ** 2
    mse /= float(ImageA.shape[0] * ImageA.shape[1])
    
    return mse;


#image recoginition
def start(ImageB):
    print("asd")
    #print(findMSE())

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
        ButtonDecline = Button(master, text = "wrong image", command = findImage).pack(side = BOTTOM)
        ButtonConfirm = Button(master, text = "correct image", command = start(imgPrint)).pack(side = BOTTOM)
        
    #catch error if file selected is not an image
    except IOError:
        messagebox.showerror("error","not an image")
    
        
#instruction text
labelTextInstructions = Label(master,text = " select an image from file explorer").pack(pady =10)
#button to show file explorer
imagepullerButton = Button(master, text = "open file explorer" , command = findImage).pack(pady = 10)

#exit
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        master.destroy()
master.protocol("WM_DELETE_WINDOW", on_closing)

master.mainloop()



sys.exit()










    


    
