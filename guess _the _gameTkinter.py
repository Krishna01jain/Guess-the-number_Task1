from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import math
from tkinter import filedialog
import string

global HighScore_
global High_Score_C
global Score
global ScoreC


High_Score_C = 0


HighScore_ = 0
Score = 6
ScoreC = 0
if (Score < ScoreC):
    Score = ScoreC
if (HighScore_ < ScoreC):
    HighScore_ = ScoreC




def Number_Random():
    global number
    number = random.randint(1, 10)
    your_ANSWER.config(text='your\n Answer')
    messagebox.showinfo(
        'Generator', ' I have chosen a \nnumber between 1 - 10,\n can u guess it : ')
    return number



def HighScore1():
    global Score
    global HighScore_
    if HighScore_ < Score:
        HighScore_ = Score
    return HighScore_




def Input():
    global Num
    Number = (INPUT_number.get("1.0", 'end-1c'))
    if Number.isnumeric():
        Num = int(Number)
        if Num <= 0 or Num > 10:
            messagebox.showinfo('invalid Number', "Input out of Range")
        else:
            your_ANSWER.config(text=Num)
    else:
        messagebox.showinfo('Invaid Input!!', 'Invalid Input')

    return Num


def Main_game():
    # Score1()
    Input()

    global Num
    global ScoreC
    global Score
    global HighScore_
    global number
    guess = Num
    while Score >= 0:
        if guess < number:
            Instructions.config(text='Your guess is too low')
            Score = Score - 2
            ScoreC = Score

            if Score < 0:
                Score = 0
            Score_label.config(text=Score)
            break
        elif guess > number:
            Instructions.config(text=' Your guess is too high')
            Score -= 2
            ScoreC = Score
            if Score < 0:
                Score = 0
            Score_label.config(text=Score)
            break
        elif guess == number:
            Instructions.config(text='Congratulations You guessed the number in '
                                + ' tries!')
            # number = Number_Random()
            Score += 2
            ScoreC = Score+2
            HighScore_ = HighScore1()
            Score_label.config(text=Score)
            HighScore.config(text=HighScore_)
            messagebox.showinfo('Congratulations🍕 you win',
                                "Please generate a new Number")
            break
        else:
            Instructions.config(text="YOU GUESS WRONG ")
            Score_label.config(text=Score)
            break



# Tkinter Frame

frame = Tk()
frame.title('Guess The Game')
frame.iconbitmap('numbers.ico')


# Window size and Bg color
frame['background'] = '#7F60FF'
frame.geometry("700x700")

# Tkinter Logo tittle bar
GAME_LOGO = Image.open("1.png")
resize_GAME_LOGO = GAME_LOGO.resize((500, 300))
imgGAME_LOGO = ImageTk.PhotoImage(resize_GAME_LOGO)
GAME_LOGO_Label = Label(bg="#7F60FF", image=imgGAME_LOGO)
GAME_LOGO_Label.pack()
GAME_LOGO_Label.place(relx=0.5, rely=0.25, anchor=CENTER)

# INPUT NUMBER FEILD

INPUT_number = Text(frame,
                    height=3,
                    width=10)
INPUT_number.pack()
INPUT_number.place(relx=0.5, rely=0.6, anchor=CENTER)


# start Button Input button
Enter_Button = Button(frame, text='ENTER', height=3, width=15,
                      fg='white', bg="#6644F0", command=Main_game)

#   command=lambda: [frame.destroy, Start(Start_Button)])

# This is ENTER BUTTON
Enter_Button.pack()
Enter_Button.place(relx=0.5, rely=0.7, x=-60)

# Random Number GENETATOR 
Generator_Button = Button(frame, text='Generator', height=3, width=15,
                          fg='white', bg="#6644F0", command=Number_Random)


Generator_Button.pack()
Generator_Button.place(relx=0.5, rely=0.9, x=-60)

# This is HINT LABEL

Instructions = Label(text="hint", bg="#ffffff", height=3, width=50)
Instructions.pack()
Instructions.place(relx=0.4, rely=0.7, x=-190, y=28, anchor=CENTER)

# this is your Answer

your_ANSWER = Label(text="your\nANSWER", bg="#ffffff", height=2, width=7)
your_ANSWER.pack()
your_ANSWER.place(relx=0.4, rely=0.5, x=-100, y=70, anchor=CENTER)


# this is hightscore label

HighScore = Label(text="HighScore", bg="#ffffff", height=3, width=15)
HighScore.pack()
HighScore.place(relx=0.5, rely=0.8, x=-3, y=50, anchor=CENTER)


# this is score label


Score_label = Label(text="Score", bg="#ffffff", height=3, width=15)
Score_label.pack()
Score_label.place(relx=0.6, rely=0.7, x=98, y=28, anchor=CENTER)
Score_label.config(text=Score)


# Main_game(guess)
frame.mainloop()
