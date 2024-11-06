from tkinter import *
import math

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
COUNT = 5
reps = 0
temporizador = None

# TIMER RESET MECHANISM


def reset_timer():
    window.after_cancel(temporiz)
    global reps
    reps = 0
    canvas.itemconfig(timer, text="00:00")
    timer_txt.config(text="Timer")
    check_mark.config(text="")


# TIMER MECHANISM


def call():
    global reps
    reps += 1
    work_min_s = WORK_MIN * 60
    short_break_s = SHORT_BREAK_MIN * 60
    long_break_s = LONG_BREAK_MIN * 60

    if reps % 3 == 0:
        check_mark.config(text="✓")
    else:
        check_mark.config(text="")

    if reps % 8 == 0:
        count_down(long_break_s)
        timer_txt.config(text="Long break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_s)
        timer_txt.config(text="Short break", fg=RED)
    else:
        count_down(work_min_s)
        timer_txt.config(text="Work time!", fg=GREEN)

# COUNT DOWN MECHANISM


def count_down(number):
    # global reps
    min = math.floor(number/60)
    sec = number % 60
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer, text=f"{min} : {sec}")

    if number > 0:
        global temporiz
        temporiz = window.after(1000, count_down, number - 1)
    else:
        call()

# UI SETUP


window = Tk()


window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


startb = Button(text="Start", command=call)
startb.grid(row=2, column=0)
reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

timer_txt = Label(text="Timer", fg=GREEN, font=("Times New Roman", 35, "bold"), bg=YELLOW)
timer_txt.grid(row=0, column=1)
check_mark = Label(fg=GREEN,  bg=YELLOW,  font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=3, column=1)

window.mainloop()
