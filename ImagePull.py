import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
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
    mse = np.sum((ImageA.astype("float") - ImageB.astype("float")) ** 2)
    mse /= float(ImageA.shape[0] * ImageA.shape[1])
    
    return mse;

#image recoginition
def start(ImageStr):
      
    tempWin = Toplevel(master)
    tempWin.geometry("400x400")
    imgTemp = Image.open("C:/Users/Kevin Dai/Downloads/CLB2.jpeg")
    imgTemp = imgTemp.resize((300,300),Image.ANTIALIAS)
    imgTempP = ImageTk.PhotoImage(imgTemp)
    labelTemp = tk.Label(tempWin,image = imgTempP)
    labelTemp.image = imgTempP
    labelTemp.place(x=50,y=0)
    
    ImageA = cv2.imread("C:/Users/Kevin Dai/Downloads/CLB2.jpeg")
    ImageB = cv2.imread(ImageStr)
    ImageB = cv2.cvtColor(ImageB, cv2.COLOR_BGR2GRAY)
    ImageA = cv2.cvtColor(ImageA, cv2.COLOR_BGR2GRAY)
    ImageA = cv2.resize(ImageA, (480,480),interpolation = cv2.INTER_AREA)
    ImageB = cv2.resize(ImageB, (480,480),interpolation = cv2.INTER_AREA)
    
    imagea = Image.fromarray(ImageA)
    imagea = ImageTk.PhotoImage(imagea)
    labelTemp = tk.Label(tempWin, image = imagea)
    labelTemp.image = imageas
    
    print(findMSE(ImageA, ImageB))
    print(ssim(ImageA, ImageB))

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
        label1 = tk.Label(image = imgPrint)
        label1.image = imgPrint
        label1.place(x=50,y=0)
        
        ButtonDecline = tk.Button(master, text = "wrong image", command = findImage).pack(side = BOTTOM)
        ButtonConfirm = tk.Button(master, text = "correct image", command = lambda: start(files[0])).pack(side = BOTTOM)
        
    #catch error if file selected is not an image
    except IOError:
        messagebox.showerror("error","not an image")
    
        
#instruction text
labelTextInstructions = tk.Label(master,text = " select an image from file explorer").pack(pady =10)
#button to show file explorer
imagepullerButton = tk.Button(master, text = "open file explorer" , command = findImage).pack(pady = 10)

#exit
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        master.destroy()
master.protocol("WM_DELETE_WINDOW", on_closing)

master.mainloop()

sys.exit()











    
