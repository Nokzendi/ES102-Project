from tkinter import *
import random
import time


# ROOT METHODS
root=Tk()
root.geometry('900x700+300+50')
root.configure(bg='gray70')
root.title('TypeWars')
root.iconbitmap('Typewar.ico')
root.resizable(height=False, width=False)
# ******************************************************

# GETTING THE LIST OF WORDS TO BE USED IN THE GAME
fname=open('words.txt', 'r')
next_word_list=[]
for line in fname:
    newword=line.strip()
    next_word_list.append(newword)
# ******************************************************


# VARIABLES
score, miss, count=0,0,0
time_left=60
updated_title=''
up_next=random.choice(next_word_list)
dis_word=''
number=3
first=True
missed=[]
high_score=[]
# ******************************************************* 


# FUNCTIONS
def title_typer():
    global  count, updated_title
    titlename="Welcome to TypeWars"
    if(count == len(titlename)):
        word_entry.focus()
        return None
    else:
        updated_title+=titlename[count]
        title_label.configure(text=updated_title)
        count+=1
        title_label.after(80, title_typer)


def timer():
    global time_left
    if(time_left<10):
        time_label.configure(fg='red')

    if(time_left>0):
        time_left-=1
        time_label.configure(text=time_left)
        time_label.after(1000, timer)
    else:
        score_label.configure(text=score)
        miss_label.configure(text=miss)
        word_entry.delete(0, END)
        listInsert()
        cur_word_label.configure(text='')
        next_word_label.configure(text='')
        highscore_label.configure(text=max(high_score))
        root.focus_set()


def start(event):
    global score, miss, up_next, time_left, first, missed
    while first==True:
        if(word_entry.get()!=' '):
            return None
        else:
            countdown()
            first=False
    if(time_left == 60):
        timer()
    if(time_left == 0):
        return None
    cur_word_label.configure(fg='black')
    if(word_entry.get().strip()==cur_word_label['text']):
        score+=1
        high_score.append(score)
        cur_word_label.configure(text=up_next)
        up_next=random.choice(next_word_list)
        next_word_label.configure(text=up_next)
    else:
        cur_word_label.configure(fg='red')
        miss+=1
        missed.append(cur_word_label['text'])
    word_entry.delete(0, END)
    perc()


def perc():
    per=0
    global score, miss
    per=(score/(score+miss))*100
    if(per>=90):
        accuracy.configure(fg='green')
    elif(per>=80):
        accuracy.configure(fg='yellow')
    else:
        accuracy.configure(fg='red')
    accuracy.configure(text=str(per)[:5]+'%')
        

def countdown():
    global number
    while(number >0):
        cur_word_label.configure(text=number)
        message_label.configure(text='Press space after every word')
        root.update_idletasks()
        time.sleep(1)
        number-=1
    if(number==0):
        cur_word_label.configure(text='')
        word_entry.configure(text='')
        return None

def listInsert():
    global missed
    missed=set(missed)
    missed=list(missed)
    for i in range(len(missed)):
        miss_list.insert(i+1,' '+str(i+1)+') '+missed[i])


def clear():
    global time_left, score, miss, up_next, number, first, missed
    time_left=60
    score, miss=0, 0
    up_next=random.choice(next_word_list)
    number=3
    first=True
    time_label.configure(fg='black')
    score_label.configure(text='---')
    miss_label.configure(text='---')
    miss_list.delete(0,len(missed))
    missed=[]
    cur_word_label.configure(fg='black')
    next_word_label.configure(text=up_next)
    accuracy.configure(text='---', fg='black')
    message_label.configure(text='Press space to start')
    word_entry.focus()


# *********************************************

            
# LABEL METHODS
title_label=Label(root, text=updated_title, fg='navy', bg='gray70', font=('arial', 30, 'bold'),
                        justify='center', relief='raised', width=18)
title_label.place(x=230, y=15)


highscoreIndicator_label=Label(root, text='High Score', bg='gray70', fg='navy', font=('arial', 25))
highscoreIndicator_label.place(x=20, y=100)

highscore_label=Label(root, text=score, font=('arial', 30), bg='light grey', borderwidth='4', 
                        relief='ridge', justify='center', width='3')
highscore_label.place(x=60, y=150)


timeLeft_label=Label(root, text='Time Left', bg='gray70', font=('arial', 25), fg='navy')
timeLeft_label.place(x=730, y=100)

time_label=Label(root, text=time_left, font=('arial', 30), bg='light grey', borderwidth='4', 
                        relief='ridge', justify='center', width='2')
time_label.place(x=775, y=150)


cur_word_label=Label(root, text=dis_word, font=('arial', 30), bg='light grey', borderwidth=4,
                        relief='sunken', justify='center', width='12')
cur_word_label.place(x=305, y=300)


next_word_label=Label(root, text=up_next, font=('arial', 20), bg='light grey', borderwidth=2, 
                        relief='sunken', justify='center', width='12')
next_word_label.place(x=352, y=250)

nextup_label=Label(root, text='Up next', font=('arial', 20, 'italic'), bg='gray70', fg='navy')
nextup_label.place(x=240, y=250)


message_label=Label(root, text='# Press space to start', font=('arial', 30, 'italic'),
                        bg='gray70', fg='yellow', justify='center', width=27)

message_label.place(x=135, y=450)


accuracy_label=Label(root, text='Accuracy', bg='gray70', fg='navy', font=('arial', 25))
accuracy_label.place(x=380, y=100)

accuracy=Label(root, text='---', font=('arial', 30), bg='light grey', borderwidth='4', 
                        relief='ridge', justify='center', width='6')
accuracy.place(x=376, y=150)


result_score_label=Label(root, text='Score:', bg='gray70', fg='navy', font=('arial', 25))
result_score_label.place(x=20, y=510)

score_label=Label(root, text='---', bg='gray70', fg='navy', font=('arial', 25))
score_label.place(x=200, y=510)


result_miss_label=Label(root, text='Miss:', bg='gray70', fg='navy', font=('arial', 25))
result_miss_label.place(x=20, y=600)

miss_label=Label(root, text='---', bg='gray70', fg='navy', font=('arial', 25))
miss_label.place(x=200, y=600)


missed_words_label=Label(root, text='Missed Words:', bg='gray70', fg='navy', font=('arial', 25) )
missed_words_label.place(x=350, y=510)
# *****************************************************

# ENTRY METHODS
word_entry=Entry(root, bg='light grey', font=('arial', 35), bd='7', justify='center')
word_entry.place(x=180, y=380)

# ******************************************************

#  SCROLL BAR LISTBOX
miss_list=Listbox(root, bg='light grey', font=('arial', 13), width=20, fg='red', height=8)
miss_list.place(x=600, y=510)

scroll=Scrollbar(root)
scroll.pack(side=RIGHT, fill='y')

miss_list.config(yscrollcommand=scroll.set)
scroll.config(command=miss_list.yview)
# *********************************************************

# BUTTON METHODS
retry=Button(root, text='Play Again', command=clear, font='arial', bg='alice blue', fg='green')
retry.place(x=750, y=395)

title_typer() 
root.bind('<space>', start)
root.mainloop()