from tkinter import *
import time
import random
from tkinter import messagebox

score = 2
sec = 60
l = list(range(1, 5))
random.shuffle(l)

def changeTextAll():
    btn['text'] = ''
    btn2['text'] = ''
    btn3['text'] = ''
    btn4['text'] = ''

def changeText1():
    btn['text'] = f'{l[0]}'
    for i in l:
        if l[0]>i:
            messagebox.showinfo("You lose", "You lose")
            exit()

    l[0] =5


def changeText2():
    btn2['text'] = f'{l[1]}'
    for i in l:
        if l[1]>i:
            messagebox.showinfo("You lose", "You lose")
            exit()

    l[1] = 5


def changeText3():
    btn3['text'] = f'{l[2]}'
    for i in l:
        if l[2]>i:
            messagebox.showinfo("You lose", "You lose")
            exit()
    if l[2] == i:
        l[2] = 5

def changeText4():
    btn4['text'] = f'{l[3]}'
    for i in l:
        if l[3]>i:
            messagebox.showinfo("You lose", "You lose")
            exit()
    l[3] = 5



def click_button():
    global score
    score+=1

def countdown(sec):
    while sec:
        m, s = divmod(sec, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        sec -= 1

    sec = 60


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
lbl = Label(window, text="Уровень:"+ "1", font=("Arial Bold", 24), width=8)
lbl.grid(column=1, row=0)
lbl2 = Label(window, text="time", font=("Arial Bold", 24), width=8)
lbl2.grid(column=2, row=0)
lbl3 = Label(window, text="Очки:" + f'{score}', font=("Arial Bold", 24), width=8)
lbl3.grid(column=3, row=0)
btn = Button(window, width=11, command=changeText1, text=f'{l[0]}')
btn2 = Button(window, width=11, command=changeText2, text=f'{l[1]}')
btn3 = Button(window,  width=11, command=changeText3, text=f'{l[2]}')
btn4 = Button(window,  width=11, command=changeText4, text=f'{l[3]}')
btn5 = Button(window,  width=11, command=changeTextAll, text='Запомнил')


btn.grid(column=1, row=1)
btn2.grid(column=2, row=1)
btn3.grid(column=3, row=1)
btn4.grid(column=4, row=1)
btn5.grid(columnspan=4, row=2)




window.mainloop()