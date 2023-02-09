from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Rock Paper Scissor")
window.configure(background ="Light blue")

#Functions
def msg_updation(a):
    final_mess ["text"]=a 

def computer_update():
    final = int(computer_score["text"])
    final += 1
    computer_score["text"] = str(final)
    
def player_update():
    final = int(player_score["text"])
    final += 1
    player_score["text"] = str(final)

def winner_check(p,c):
    if p == c:
        msg_updation("It's a tie")
    elif p == "rock":
        if c == "paper":
            msg_updation("Computer wins")
            computer_update()
        else:
            msg_updation("Player wins")
            player_update()
    elif p == "paper":
        if c == "scissor":
            msg_updation("Computer Wins")
            computer_update()
        else:
            msg_updation("Player Wins")
            player_update()
    elif p == "scissor":
        if c == "rock":
            msg_updation("Computer Wins")
            computer_update()
        else:
            msg_updation("Player Wins")
            player_update()
    else:
        pass

to_select =["rock", "paper", "scissor"]

def choice_update(a):
    choice_computer = to_select[randint(0,2)]
    if choice_computer == "rock":
        Label_computer.configure(image=image_rock1)
    elif choice_computer == "paper":
        Label_computer.configure(image=image_paper1)
    elif choice_computer == "Scissor":
        Label_computer.configure(image_scissor1)
        
    if a == "rock":
        Label_player.configure(image=image_rock2)
    elif a == "paper":
        Label_player.configure(image=image_paper2)
    elif a == "scissor":
        Label_player.configure(image=image_scissor2)
    
    winner_check(a,choice_computer)
#Images
image_rock1 = ImageTk.PhotoImage(Image.open("Rock.jpg"))
image_paper1 = ImageTk.PhotoImage(Image.open("Paper.jpg"))
image_scissor1 = ImageTk.PhotoImage(Image.open("Scissor.jpg"))


image_rock2 = ImageTk.PhotoImage(Image.open("Rock - Copy.jpg"))
image_paper2 = ImageTk.PhotoImage(Image.open("Paper - Copy.jpg"))
image_scissor2 = ImageTk.PhotoImage(Image.open("Scissor - Copy.jpg"))
#Label
Label_computer = Label(window, image=image_scissor1)
Label_player = Label(window, image=image_scissor2)
Label_computer.grid(row=2, column=0)
Label_player.grid(row=2,column=4)

Computer_rep = Label(window, text="Computer",font=("Calibri",30,"bold"))
Player_rep = Label(window, text="Player",font=("Calibri",30,"bold"))
Computer_rep.grid(row=1,column=1)
Player_rep.grid(row=1,column=3) 

computer_score = Label(window, text=0,font=("Calibri",20,"bold"))
player_score = Label(window, text=0,font=("Calibri",20,"bold") )
computer_score.grid(row=2,column=1)
player_score.grid(row=2,column=3) 

final_mess= Label(window,font=("Calibri",20,"bold"))
final_mess.grid(row=4,column=2) 
#Button
button_rock = Button(window, width=16, height=3, text="Rock", font=("Calibri",16,"bold"), command=lambda: choice_update("rock")).grid(row=3,column=1)
button_paper = Button(window, width=16, height=3, text="Paper", font=("Calibri",16,"bold"), command=lambda: choice_update("paper")).grid(row=3,column=2)
button_scissor = Button(window, width=16, height=3, text="Scissor", font=("Calibri",16,"bold"), command=lambda: choice_update("rock")).grid(row=3,column=3)

window.mainloop()
