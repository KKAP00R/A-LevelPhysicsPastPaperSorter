import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import Tk
from array import *
import os
import time
import PyPDF2
import tkinter.font as tkfont
from tkinter import ttk
from ttkthemes import themed_tk as theme
from PIL import Image, ImageTk
import fitz

def browsefn():
    global file_name
    file_name = filedialog.askopenfilename(initialdir = "/", title = "SELECT A FILE", filetypes = (("PDF","*.pdf*"), ("ALL FILES", "*.*")))
    print(file_name)
    label1 = Label(window1, text='ENTER 1 for SL and 2 for HL', font = myfont)
    label1.place(height = 20, x = 20, y = 140)
    label2 = Label(window1, text = 'YEAR of this Paper', font = myfont)
    label2.place(height = 20, x = 20, y = 180)
    label3 = Label(window1, text = "NUMBER OF QUESTIONS", font = myfont)
    label3.place(height = 20, x = 20, y = 220)
    label4 = Label(window1, text = "ENTER 1 for May and 2 for Nov. version", font = myfont)
    label4.place(height = 20, x = 20, y = 260)
    label5 = Label(window1, text = "ENTER 1 for Timezone 1 and 2 for Timezone 2", font = myfont)
    label5.place(height = 20, x = 20, y = 300)
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    entry1 = ttk.Entry(window1) 
    entry2 = ttk.Entry(window1)
    entry3 = ttk.Entry(window1)
    entry4 = ttk.Entry(window1)
    entry5 = ttk.Entry(window1)
    entry1.place(height = 20, x = 260, y = 140) 
    entry2.place(height = 20, x = 260, y = 180)
    entry3.place(height = 20, x = 260, y = 220)
    entry4.place(height = 20, x = 260, y = 260)
    entry5.place(height = 20, x = 260, y = 300)
    done = ttk.Button(window1, text = "SAVE", width = 61, command = nextfn)
    done.place(height = 20, x = 15, y = 340)
    labelw = ttk.Label(window1, text = "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", width = 112)
    labelw.place(height = 20, x = 15, y = 360)
def nextfn():
    global s1
    global s2
    global s3
    global s4
    global s5
    s1 = entry1.get()
    s2 = entry2.get()
    s3 = entry3.get()
    s4 = entry4.get()
    s5 = entry5.get()
    print(s1)
    print(s2)
    if s3 == '8':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn8()
    elif s3== '9':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn9()
    elif s3 == '10':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn10()
    elif s3 == '11':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn11()
    elif s3 == '12':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn12()
    else:
        print("ERROR IN PAPER TYPE")

def fn12():
    j = 12
    i = 1
    k = 360
    while i<=j:
        k+=40
        labelz = ttk.Label(window1, text = "ENTER TOPIC OF Q" + str(i)) 
        labelz.place(x = 20, y = +k)
        labely = ttk.Label(window1, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION")
        labely.place(x = 280, y = +k)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global e12
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global p11
    global p12
    e1 = ttk.Entry(window1)
    e1.place(x = 150, y = 400)
    e2 = ttk.Entry(window1)
    e2.place(x = 150, y = 440)
    e3 = ttk.Entry(window1)
    e3.place(x = 150, y = 480)
    e4 = ttk.Entry(window1)
    e4.place(x = 150, y = 520)
    e5 = ttk.Entry(window1)
    e5.place(x = 150, y = 560)
    e6 = ttk.Entry(window1)
    e6.place(x = 150, y = 600)
    e7 = ttk.Entry(window1)
    e7.place(x = 150, y = 640)
    e8 = ttk.Entry(window1)
    e8.place(x = 150, y = 680)
    e9 = ttk.Entry(window1)
    e9.place(x = 150, y = 720)
    e10 = ttk.Entry(window1)
    e10.place(x = 150, y = 760)
    e11 = ttk.Entry(window1)
    e11.place(x = 150, y = 800)
    e12 = ttk.Entry(window1)
    e12.place(x = 150, y = 840)
    p1 = ttk.Entry(window1)
    p1.place(x = 570, y = 400)
    p2 = ttk.Entry(window1)
    p2.place(x = 570, y = 440)
    p3 = ttk.Entry(window1)
    p3.place(x = 570, y = 480)
    p4 = ttk.Entry(window1)
    p4.place(x = 570, y = 520)
    p5 = ttk.Entry(window1)
    p5.place(x = 570, y = 560)
    p6 = ttk.Entry(window1)
    p6.place(x = 570, y = 600)
    p7 = ttk.Entry(window1)
    p7.place(x = 570, y = 640)
    p8 = ttk.Entry(window1)
    p8.place(x = 570, y = 680)
    p9 = ttk.Entry(window1)
    p9.place(x = 570, y = 720)
    p10 = ttk.Entry(window1)
    p10.place(x = 570, y = 760)
    p11 = ttk.Entry(window1)
    p11.place(x = 570, y = 800)
    p12 = ttk.Entry(window1)
    p12.place(x = 570, y = 840)
    save = ttk.Button(window1, text = "SAVE", width = 112, command = savedata12)  
    save.place(height = 20, x = 15, y = 880)
    elektra1 = Label(window1, text = "When entering multiple topics, seperate both with a double space | Subtract 1 from the page no. at the top in beginning page", fg = "Red")
    elektra1.place(height = 20, x = 15, y = 900) 
#FN12 CHECKED - STATUS OK
def fn11():
    j = 11
    i = 1
    k = 360
    while i<=j:
        k+=40
        labelz = ttk.Label(window1, text = "ENTER TOPIC OF Q" + str(i)) 
        labelz.place(x = 20, y = +k)
        labely = ttk.Label(window1, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION")
        labely.place(x = 280, y = +k)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global p11
    e1 = ttk.Entry(window1)
    e1.place(x = 150, y = 400)
    e2 = ttk.Entry(window1)
    e2.place(x = 150, y = 440)
    e3 = ttk.Entry(window1)
    e3.place(x = 150, y = 480)
    e4 = ttk.Entry(window1)
    e4.place(x = 150, y = 520)
    e5 = ttk.Entry(window1)
    e5.place(x = 150, y = 560)
    e6 = ttk.Entry(window1)
    e6.place(x = 150, y = 600)
    e7 = ttk.Entry(window1)
    e7.place(x = 150, y = 640)
    e8 = ttk.Entry(window1)
    e8.place(x = 150, y = 680)
    e9 = ttk.Entry(window1)
    e9.place(x = 150, y = 720)
    e10 = ttk.Entry(window1)
    e10.place(x = 150, y = 760)
    e11 = ttk.Entry(window1)
    e11.place(x = 150, y = 800)
    p1 = ttk.Entry(window1)
    p1.place(x = 570, y = 400)
    p2 = ttk.Entry(window1)
    p2.place(x = 570, y = 440)
    p3 = ttk.Entry(window1)
    p3.place(x = 570, y = 480)
    p4 = ttk.Entry(window1)
    p4.place(x = 570, y = 520)
    p5 = ttk.Entry(window1)
    p5.place(x = 570, y = 560)
    p6 = ttk.Entry(window1)
    p6.place(x = 570, y = 600)
    p7 = ttk.Entry(window1)
    p7.place(x = 570, y = 640)
    p8 = ttk.Entry(window1)
    p8.place(x = 570, y = 680)
    p9 = ttk.Entry(window1)
    p9.place(x = 570, y = 720)
    p10 = ttk.Entry(window1)
    p10.place(x = 570, y = 760)
    p11 = ttk.Entry(window1)
    p11.place(x = 570, y = 800)
    save = ttk.Button(window1, text = "SAVE", width = 112, command = savedata12)  
    save.place(height = 20, x = 15, y = 880)
    elektra1 = Label(window1, text = "When entering multiple topics, seperate both with a double space | Subtract 1 from the page no. at the top in beginning page", fg = "Red")
    elektra1.place(height = 20, x = 15, y = 900) 
#FN11 CHECKED - STATUS OK
def fn10():
    j = 10
    i = 1
    k = 360
    while i<=j:
        k+=40
        labelz = ttk.Label(window1, text = "ENTER TOPIC OF Q" + str(i)) 
        labelz.place(x = 20, y = +k)
        labely = ttk.Label(window1, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION")
        labely.place(x = 280, y = +k)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    e1 = ttk.Entry(window1)
    e1.place(x = 150, y = 400)
    e2 = ttk.Entry(window1)
    e2.place(x = 150, y = 440)
    e3 = ttk.Entry(window1)
    e3.place(x = 150, y = 480)
    e4 = ttk.Entry(window1)
    e4.place(x = 150, y = 520)
    e5 = ttk.Entry(window1)
    e5.place(x = 150, y = 560)
    e6 = ttk.Entry(window1)
    e6.place(x = 150, y = 600)
    e7 = ttk.Entry(window1)
    e7.place(x = 150, y = 640)
    e8 = ttk.Entry(window1)
    e8.place(x = 150, y = 680)
    e9 = ttk.Entry(window1)
    e9.place(x = 150, y = 720)
    e10 = ttk.Entry(window1)
    e10.place(x = 150, y = 760)
    p1 = ttk.Entry(window1)
    p1.place(x = 570, y = 400)
    p2 = ttk.Entry(window1)
    p2.place(x = 570, y = 440)
    p3 = ttk.Entry(window1)
    p3.place(x = 570, y = 480)
    p4 = ttk.Entry(window1)
    p4.place(x = 570, y = 520)
    p5 = ttk.Entry(window1)
    p5.place(x = 570, y = 560)
    p6 = ttk.Entry(window1)
    p6.place(x = 570, y = 600)
    p7 = ttk.Entry(window1)
    p7.place(x = 570, y = 640)
    p8 = ttk.Entry(window1)
    p8.place(x = 570, y = 680)
    p9 = ttk.Entry(window1)
    p9.place(x = 570, y = 720)
    p10 = ttk.Entry(window1)
    p10.place(x = 570, y = 760)
    save = ttk.Button(window1, text = "SAVE", width = 112, command = savedata12)  
    save.place(height = 20, x = 15, y = 880)
    elektra1 = Label(window1, text = "When entering multiple topics, seperate both with a double space | Subtract 1 from the page no. at the top in beginning page", fg = "Red")
    elektra1.place(height = 20, x = 15, y = 900) 
#FN10 CHECKED - STATUS OK
def fn9():
    j = 9
    i = 1
    k = 360
    while i<=j:
        k+=40
        labelz = ttk.Label(window1, text = "ENTER TOPIC OF Q" + str(i)) 
        labelz.place(x = 20, y = +k)
        labely = ttk.Label(window1, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION")
        labely.place(x = 280, y = +k)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    e1 = ttk.Entry(window1)
    e1.place(x = 150, y = 400)
    e2 = ttk.Entry(window1)
    e2.place(x = 150, y = 440)
    e3 = ttk.Entry(window1)
    e3.place(x = 150, y = 480)
    e4 = ttk.Entry(window1)
    e4.place(x = 150, y = 520)
    e5 = ttk.Entry(window1)
    e5.place(x = 150, y = 560)
    e6 = ttk.Entry(window1)
    e6.place(x = 150, y = 600)
    e7 = ttk.Entry(window1)
    e7.place(x = 150, y = 640)
    e8 = ttk.Entry(window1)
    e8.place(x = 150, y = 680)
    e9 = ttk.Entry(window1)
    e9.place(x = 150, y = 720)
    p1 = ttk.Entry(window1)
    p1.place(x = 570, y = 400)
    p2 = ttk.Entry(window1)
    p2.place(x = 570, y = 440)
    p3 = ttk.Entry(window1)
    p3.place(x = 570, y = 480)
    p4 = ttk.Entry(window1)
    p4.place(x = 570, y = 520)
    p5 = ttk.Entry(window1)
    p5.place(x = 570, y = 560)
    p6 = ttk.Entry(window1)
    p6.place(x = 570, y = 600)
    p7 = ttk.Entry(window1)
    p7.place(x = 570, y = 640)
    p8 = ttk.Entry(window1)
    p8.place(x = 570, y = 680)
    p9 = ttk.Entry(window1)
    p9.place(x = 570, y = 720)
    save = ttk.Button(window1, text = "SAVE", width = 112, command = savedata9)  
    save.place(height = 20, x = 15, y = 880)
    elektra1 = Label(window1, text = "When entering multiple topics, seperate both with a double space | Subtract 1 from the page no. at the top in beginning page", fg = "Red")
    elektra1.place(height = 20, x = 15, y = 9000) 
#FN9 CHECKED - STATUS OK
def fn8():
    j = 8
    i = 1
    k = 360
    while i<=j:
        k+=40
        labelz = ttk.Label(window1, text = "ENTER TOPIC OF Q" + str(i)) 
        labelz.place(x = 20, y = +k)
        labely = ttk.Label(window1, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION")
        labely.place(x = 280, y = +k)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    e1 = ttk.Entry(window1)
    e1.place(x = 150, y = 400)
    e2 = ttk.Entry(window1)
    e2.place(x = 150, y = 440)
    e3 = ttk.Entry(window1)
    e3.place(x = 150, y = 480)
    e4 = ttk.Entry(window1)
    e4.place(x = 150, y = 520)
    e5 = ttk.Entry(window1)
    e5.place(x = 150, y = 560)
    e6 = ttk.Entry(window1)
    e6.place(x = 150, y = 600)
    e7 = ttk.Entry(window1)
    e7.place(x = 150, y = 640)
    e8 = ttk.Entry(window1)
    e8.place(x = 150, y = 680)
    p1 = ttk.Entry(window1)
    p1.place(x = 570, y = 400)
    p2 = ttk.Entry(window1)
    p2.place(x = 570, y = 440)
    p3 = ttk.Entry(window1)
    p3.place(x = 570, y = 480)
    p4 = ttk.Entry(window1)
    p4.place(x = 570, y = 520)
    p5 = ttk.Entry(window1)
    p5.place(x = 570, y = 560)
    p6 = ttk.Entry(window1)
    p6.place(x = 570, y = 600)
    p7 = ttk.Entry(window1)
    p7.place(x = 570, y = 640)
    p8 = ttk.Entry(window1)
    p8.place(x = 570, y = 680)
    save = ttk.Button(window1, text = "SAVE", width = 112, command = savedata8)  
    save.place(height = 20, x = 15, y = 880)
    elektra1 = Label(window1, text = "When entering multiple topics, seperate both with a double space | Subtract 1 from the page no. at the top in beginning page", fg = "Red")
    elektra1.place(height = 20, x = 15, y = 900) 
#FN8 CHECKED - STATUS OK
def savedata11():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    string9 = e9.get()
    string10 = e10.get()
    string11 = e11.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    if string9 == '1':
        string9 = '1 '
    if string10 == '1':
        string10 = '1 '
    if string11 == '1':
        string11 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    page9 = p9.get()
    page10 = p10.get()
    page11 = p11.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("9.  " + string9 + "\n")
    f.write(" 9P. " + page9 + "\n")
    f.write("10.  " + string10 + "\n")
    f.write(" 10P. " + page10 + "\n")
    f.write("11.  " + string11 + "\n")
    f.write(" 11P. " + page11 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
#CHECKED - SAVEDATA11 HAS NO ISSUES
def savedata8():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
#CHECKED - SAVEDATA8 HAS NO ISSUES
def savedata12():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    string9 = e9.get()
    string10 = e10.get()
    string11 = e11.get()
    string12 = e12.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    if string9 == '1':
        string9 = '1 '
    if string10 == '1':
        string10 = '1 '
    if string11 == '1':
        string11 = '1 '
    if string12 == '1':
        string12 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    page9 = p9.get()
    page10 = p10.get()
    page11 = p11.get()
    page12 = p12.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("9.  " + string9 + "\n")
    f.write(" 9P. " + page9 + "\n")
    f.write("10.  " + string10 + "\n")
    f.write(" 10P. " + page10 + "\n")
    f.write("11.  " + string11 + "\n")
    f.write(" 11P. " + page11 + "\n")
    f.write("12.  " + string12 + "\n")
    f.write(" 12P. " + page12 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
def savedata10():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    string9 = e9.get()
    string10 = e10.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    if string9 == '1':
        string9 = '1 '
    if string10 == '1':
        string10 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    page9 = p9.get()
    page10 = p10.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("9.  " + string9 + "\n")
    f.write(" 9P. " + page9 + "\n")
    f.write("10.  " + string10 + "\n")
    f.write(" 10P. " + page10 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
#CHECKED SAVEDATA10 HAS NO ISSUES
def savedata9():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    string9 = e9.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    if string9 == '1':
        string9 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    page9 = p9.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("9.  " + string9 + "\n")
    f.write(" 9P. " + page9 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
#CHECKED SAVEDATA9 HAS NO ISSUES 
window1 = theme.ThemedTk()
window1.get_themes()
window1.set_theme("plastik")
myfont = tkfont.Font(family = "Century Gothic", size = 8, weight = "bold")
my = tkfont.Font(family = "Century Gothic", size = 8, weight = "bold")
window1.geometry("2200x950")
window1.title("PROGRAM WINDOW")
load = ttk.Button(window1, text = "LOAD NEW PAPER", width = 30, command = browsefn)
load.place(height = 20, x = 20, y = 20)
load = ttk.Button(window1, text = "ACCESS LOADED PAPERS", width = 30, command = window1.destroy)
load.place(height = 20, x = 20, y = 60)
load = ttk.Button(window1, text = "EXIT", width = 30, command = window1.destroy)
load.place(height = 20, x = 20, y = 100)
labelx = ttk.Label(window1, text = "------------------------------------------------------------------------------------", width = 61)
labelx.place(height = 20, x = 20, y = 120)
window1.mainloop()
