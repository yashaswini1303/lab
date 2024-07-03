from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry("600x420+100+75")
window.title("Tic Tac Toe")


one = StringVar()
two = StringVar()
three = StringVar()
four = StringVar()
five = StringVar()
six = StringVar()
seven = StringVar()
eight = StringVar()
nine = StringVar()

lst = [""] * 9
user = "X"


def change_user():
    global user
    user = "O" if user == "X" else "X"


def check_winner():
    winning_combinations =[
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]]
    
    for combo in winning_combinations:
        if lst[combo[0]] == lst[combo[1]] == lst[combo[2]] and lst[combo[0]] != "":
            messagebox.showinfo("Tic Tac Toe", f"Player {lst[combo[0]]} wins!")
            reset_game()
            return

    if all(lst):
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        reset_game()


def play(n, var):
    if lst[n] == "":
        lst[n] = user
        var.set(user)
        check_winner()
        change_user()
    print(lst)


def reset_game():
    global lst, user
    lst = [""] * 9
    user = "X"
    one.set("")
    two.set("")
    three.set("")
    four.set("")
    five.set("")
    six.set("")
    seven.set("")
    eight.set("")
    nine.set("")

Button(window, textvariable=one, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(0, one)).place(x=0, y=0)
Button(window, textvariable=two, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(1, two)).place(x=200, y=0)
Button(window, textvariable=three, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(2, three)).place(x=400, y=0)
Button(window, textvariable=four, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(3, four)).place(x=0, y=140)
Button(window, textvariable=five, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(4, five)).place(x=200, y=140)
Button(window, textvariable=six, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(5, six)).place(x=400, y=140)
Button(window, textvariable=seven, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(6, seven)).place(x=0, y=280)
Button(window, textvariable=eight, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(7, eight)).place(x=200, y=280)
Button(window, textvariable=nine, bg="#303F9F", fg="#FFFFFF", font=("arial", 24, "bold"), width=10, height=3, command=lambda: play(8, nine)).place(x=400, y=280)

window.mainloop()

