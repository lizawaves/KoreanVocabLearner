import tkinter as tk
from tkinter import END
import random

file = open("vocab.txt", "r+", encoding='utf-8')
r = 0
mdv = []
listsize = 0
linestr = ['value', 'value', 'value']
msg = "value"
line = []
read = []
order = 0


def onclick():
    # this will happen once

    if label["text"] == "start":
        global file
        global read
        global mdv
        global r
        global listsize
        global line
        global linestr
        global msg
        global order

        read = file.readlines()

        for line in read:
            if line[-1] == '\n':
                mdv.append(line.strip())

        listsize = len(mdv)
        button["text"] = "submit"
        msg = tk.Message(root, text="started", font=('Arial', 11), width=300, bg="#48C9B0")
        msg.pack(pady=20)

    # get the entry
    x = myentry.get()

    # Korean to english
    if order == 0:
        # test if you got the correct answer
        if x == linestr[2]:
            print("correct! ", linestr[0], "means ", linestr[2])
            msgtmp = ('correct! ' + linestr[0] + ' means ' + linestr[2])
            msg["text"] = msgtmp
            msg["bg"] = "#48C9B0"
        elif linestr[2] == 'value':
            print("started")
        else:
            print("wrong ", linestr[0], " does not mean ", x, " it means ", linestr[2])
            msgtmp = ('wrong! ' + linestr[0] + ' does not mean ' + x + ' it means ' + linestr[2])
            msg["text"] = msgtmp
            msg["bg"] = "#CD6155"

    # English to korean
    if order == 1:
        # test if you got the correct answer
        if x == linestr[0]:
            print("correct! ", linestr[2], "means ", linestr[0])
            msgtmp = ('correct! ' + linestr[2] + ' means ' + linestr[0])
            msg["text"] = msgtmp
            msg["bg"] = "#48C9B0"
        elif linestr[0] == 'value':
            print("started")
        else:
            print("wrong ", linestr[2], " does not mean ", x, " it means ", linestr[0])
            msgtmp = ('wrong! ' + linestr[2] + ' does not mean ' + x + ' it means ' + linestr[0])
            msg["text"] = msgtmp
            msg["bg"] = "#CD6155"

    # randomize a new entry
    r = random.randint(0, (listsize-1))
    order = random.randint(0, 1)
    print(r)

    # create a new entry
    line = mdv[r]
    linestr = line.split()

    # change the labels
    if order == 0:
        label["text"] = linestr[0]
    else:
        label["text"] = linestr[2]

    myentry.delete(0, END)


def onclosing():
    global file
    print("closing")
    file.close()
    root.destroy()


root = tk.Tk()

root.geometry("320x500")
root.title("Kvocab Learner")
root.config(bg="#17202A")
root.protocol("WM_DELETE_WINDOW", onclosing)

label = tk.Label(root, text="start", font=('Arial', 30), width=10, height=2)
label.config(bg="#1B2631", fg="#A1A1A1")
label.pack(pady=80)

myentry = tk.Entry(root, font=('Arial', 20))
myentry.config(bg="#1B2631", fg="#A1A1A1")
myentry.pack()

button = tk.Button(root, text="Start", font=('Arial', 20), command=onclick)
button.config(bg="#1B2631", fg="#A1A1A1")
button.pack(pady=20)

root.mainloop()
