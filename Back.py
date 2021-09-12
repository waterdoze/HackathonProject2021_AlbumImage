import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PIL import Image
import sys
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
import os
import PIL
import random as rand
import time
from pygame import mixer

m = ''
mixer.pre_init(44100, -16, 1, 512)
mixer.init()
choice = 0
unordereddic = {}
base_file = ""
master = tk.Tk()

master.geometry("400x400")
master['background'] = '#856ff8'


def fix(size1, size2):
    directory = 'Album_Covers'
    for data_filename in os.listdir(directory):
        if data_filename.endswith(".jpg") or data_filename.endswith(".png"):
            data_image = cv2.imread(directory + "\\" + data_filename)
            data_image = cv2.resize(data_image, (size1, size2))
            base_image = cv2.imread(base_file)
            print(data_filename)
            unordereddic, m, s = compare(base_image, data_image, data_filename)
            m = "MSE = " + m
            album_difference_calculator = np.concatenate((base_image, data_image), axis=1)
            cv2.imshow('Album Difference Calculator MSE = {}'.format(m), album_difference_calculator)
            cv2.waitKey(1000)
            time.sleep(.5)
            cv2.destroyAllWindows()
        else:
            continue
        sorteddict = dict(sorted(unordereddic.items(), key=lambda kv: kv[1], reverse=False))
    musical_image = list(sorteddict.keys())[0]
    return musical_image


def find_image():
    global base_file
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    base_file = filename  # filename.split("/")[-1]
    image = Image.open(base_file)
    portion = image.size
    portion = str(portion)
    size1, size2 = portion.split(" ")
    size1 = size1.replace("(", "")
    size1 = size1.replace(",", "")
    size2 = size2.replace(")", "")
    size1 = int(size1)
    size2 = int(size2)
    print(size1)
    print(size2)
    final = fix(size1, size2)
    image2ppm(final)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        master.destroy()


def mse(base_image, data_base_image):
    error = np.sum((base_image.astype("float") - data_base_image.astype("float")) ** 2)
    error /= float(base_image.shape[0] * base_image.shape[1])
    print(error)
    return error


def compare(base_image, data_base_image, data_filename):
    m = mse(base_image, data_base_image)
    s = ssim(base_image, data_base_image, multichannel=True)
    unordereddic[data_filename] = m
    determine_contrast(m, s)
    m = "{:.2f}".format(m)
    print(f"has an MSE of {m} and SSIM  of {s}")
    return unordereddic, m, s


def determine_contrast(measuredse, structdif):
    measuredse = float(measuredse)
    structdif = float(structdif)
    if measuredse == 0.0 and structdif == 1.0:
        print("It's a perfect match! wow")


def image2ppm(data_image):
    directory = 'Album_Covers'
    an_image = PIL.Image.open(directory + "\\" + data_image)
    image_sequence = an_image.getdata()
    image_array = np.array(image_sequence)
    colorchoice(image_array)


def colorchoice(image_array):
    choice = 0
    finalvalues = []
    for i in image_array:
        if i[0] > i[1] and i[0] > i[2]:
            # red dominant
            if i[1] > i[2]:
                # red-green - brown
                choice = 1
            elif i[1] < [2]:
                # red-blue - purple
                choice = 2
            elif i[1] == 0 and i[2] == 0:
                # red
                choice = 3
        elif i[1] > i[2] and i[1] > i[0]:
            # green dominant
            if i[0] > i[2]:
                # green-red - brown
                choice = 4
            elif i[0] < i[2]:
                # green-blue
                choice = 5
        elif i[0] == 0 and i[2] == 0:
            # green
            choice = 6
        elif i[2] > i[0] and i[2] > i[1]:
            if i[0] > i[1]:
                # blue-red
                choice = 7
            elif i[0] < i[1]:
                # blue-green
                choice = 8
        elif i[0] == 0 and i[1] == 0:
            # blue
            choice = 9
        elif i[0] == 255 and i[1] == 255 and i[2] == 255:
            choice = 10
            # white
        elif i[0] == 0 and i[1] == 0 and i[2] == 0:
            # black
            choice = 11
        elif i[0] == 127 and i[1] == 127 and i[2] == 127:
            # grey
            choice = 12
        finalvalues.append(choice)
    playingm(finalvalues)


def playingm(finalvalue):
    directory = 'music'
    count = 1
    finalvalue = finalvalue[rand.randint(200, 400):rand.randint(401, 560)]
    for i in finalvalue:
        pathing = (directory + "\\" + str(i + 1) + ".mp3")
        mixer.music.load(pathing)
        mixer.music.play()
        count += 1
        time.sleep(rand.uniform(.25, 1))


directory = 'HackathonProject2021_AlbumImage'
photo = tk.PhotoImage(directory + "\\" + "background.jpg")
labelTextInstructions = Label(master, text='\nInput an Album Cover to Find a Match \nand\n Create a Funky Tune!',
                              bg='#856ff8').pack()
imagepullerButton = Button(master, text="open file explorer", command=find_image).pack(side=BOTTOM, pady=3)
master.protocol("WM_DELETE_WINDOW", on_closing)

master.mainloop()

sys.exit()
