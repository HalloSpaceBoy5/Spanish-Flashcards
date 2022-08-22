import csv
import tkinter as tk
from tkinter import *
from random import randint, seed


#make sure that theres the spanish word first in the csv file





file = open('words.csv')
type(file)
csvreader = csv.reader(file)
rows = []
for row in csvreader:
        rows.append(row)
max = 0
for row in rows:
    max=max+1
max=max-1

def getNewRow():
    newrow = randint(0, max)
    trow = rows[newrow]
    return trow

def refresh():
    global root
    global cw
    global check_button
    canvas.delete('all')
    canvas.create_text(x, y-25, text=cw[0], fill="White", font=('Arial 30'))
    check_button.configure(command=next)

def next():
    global root
    global cw
    global check_button
    canvas.delete('all')
    canvas.create_text(x, y-25, text=cw[1], fill="White", font=('Arial 30'))
    check_button.configure(command=refresh)

def newword():
    global cw
    save=cw
    cw=getNewRow()
    while save==cw:
        cw=getNewRow()
    canvas.delete('all')
    canvas.create_text(x, y-25, text=cw[0], fill="White", font=('Arial 30'))
    check_button.configure(command=next)

root=tk.Tk()
global cw
cw=getNewRow()
global canvas
global check_button
root.resizable(False, False)
root.attributes('-topmost', 'false')
root.configure(bg="Navy")
root.title("Flashcards")
width = 600
height = 500
next_button = Button(root, text="Next",font="Arial 15 bold", command=newword, width=round(width/2), bg="#3EB489", activebackground="#3EB489")
next_button.pack(pady=5, side=BOTTOM)
check_button = Button(root, text="Flip",font="Arial 15 bold", command=refresh, width=round(width/2), bg="#3EB489", activebackground="#3EB489")
check_button.pack(pady=5, side=BOTTOM)
canvas= Canvas(root, width= width, height= height, bg="Navy",highlightthickness=0)
screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight() 
posX = round((screen_width/2) - (width/2))
posY = round((screen_height/2) - (height/2))
x=round(width/2)
y=round(height/2)
newword()
canvas.pack()
root.geometry(f'{width}x{height}+{posX}+{posY}')
root.mainloop()
