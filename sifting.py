
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import BOTTOM
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import cv2
import numpy as np





def sift(image):
    covers =    ("808", "College_Dropout", "Graduation", "Jesus_Is_King", "KSG",
                "Late_Registration", "MBDTF", "TLOP", "Watch_The_Throne", "Ye", "Yeezus")
    imgPull = image
    img1=cv2.imread(imgPull, 0)

    percentArray = []

    for i in range(len(covers)):
        img2=cv2.imread("pics/" + covers[i] + ".jpg", 0)

        # Initiate SURF detector
        surf=cv2.SIFT_create()

        # find the keypoints and descriptors with SURF
        kp1, des1 = surf.detectAndCompute(img1,None)
        kp2, des2 = surf.detectAndCompute(img2,None)

        # BFMatcher with default params
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2, k=2)

        amount_Not_Good = 0
        # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < .75*n.distance:
                good.append([m])
            else:
                amount_Not_Good += 1
                
        img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
        percent = len(good) / (len(good) + amount_Not_Good) * 100
        print(percent)

        percentArray.append(percent)

    index = percentArray.index(max(percentArray))

    master = tk.Tk()
    master.geometry("600x600")
    master.columnconfigure(1,weight=1)
    master.rowconfigure(1,weight=1)
    img3 = "pics/" + covers[index] + ".jpg"
    img3 = Image.open(img3)
    img3 = img3.resize((600,600),Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    panel = tk.Label(master, image = img3)
    panel.grid(rowspan =3)

    albumLabel = tk.Label(master,text = "Your album is "+covers[index])
    albumLabel.grid(pady=10)
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            master.destroy()
        master.protocol("WM_DELETE_WINDOW", on_closing)
        SystemExit


    master.mainloop()

