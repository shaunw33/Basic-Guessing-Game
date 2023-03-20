#Shaun Wilkerson, CIS 345, 12pm, PE9
from tkinter import *
from tkinter import ttk
import random

window = Tk()
window.title('Guess Game')
window.geometry("250x195")
window.iconbitmap('pic.ico')

def reset_game():
    global answer, count, feedback, guess, counter
    answer = random.randint(1, 10)
    feedback.set('Enter guess 1')
    count = 0
    counter.set(f'Guess {count}/3')
    submit_button['state'] = NORMAL
    progress['value'] = 0

def check_answer():
    global answer, count, feedback, guess, counter
    count += 1
    counter.set(f'Guess {count}/3')
    progress.step(100)
    try:
        g = int(guess.get())
    except:
        guess.set('')
        g = 0
    if g == answer:
        feedback.set('You Win!')
        submit_button.config(state=DISABLED)
    else:
        if g > answer:
            feedback.set(f'{g} was too high')
        else:
            feedback.set(f'{g} was too low')
        guess.set('')
        guess_textBox.focus_set()
        if count == 3:
            feedback.set('You Lose!')
            submit_button.config(state=DISABLED)

answer = random.randint(1, 10)
count = 0
feedback = StringVar()
guess = StringVar()
counter = StringVar()

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Reset', command=reset_game)
file_menu.add_command(label='Exit', command=window.quit)

feedback_label = Label(window, textvariable=feedback, justify=LEFT)
feedback_label.grid(row=0, column=0, columnspan=2, sticky=W)
guess_textBox = Entry(window, textvariable=guess, justify=RIGHT)
guess_textBox.grid(row=1, column=0, columnspan=2, sticky=W)
progress = ttk.Progressbar(window, orient='horizontal', length=250, maximum=301, mode='determinate')
progress.grid(row=2, column=0, columnspan=2, sticky=W)
counter_label = Label(window, textvariable=counter, justify=CENTER)
counter_label.grid(row=3, column=0, columnspan=2, sticky=W)
submit_button = Button(window, text='Submit', command=check_answer)
submit_button.grid(row=4, column=0, columnspan=2, sticky=W)

reset_game()
window.mainloop()