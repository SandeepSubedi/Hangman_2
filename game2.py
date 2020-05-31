import random
from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase
root = Tk()
root.title("HANGMAN")
word = ['education', 'computer',  'sky', 'culture','cricket']
photos= [PhotoImage(file="hang3.png"),PhotoImage(file="hang4.png"),PhotoImage(file="hang5.png"),PhotoImage(file="hang6.png"),PhotoImage(file="hang7.png"),PhotoImage(file="hang8.png"),PhotoImage(file="hang9.png")
         ,PhotoImage(file="hang10.png"),PhotoImage(file="hang11.png")]
def game():
    global wrd
    global chances
    chances= 0
    #img.config(image=photos[0])
    picked = random.choice(word)
    wrd=" ".join(picked)
    lblword.set(" ".join("_"*len(picked)))
def guess(letter):
    global chances
    if chances<8:
        txt = list(wrd)
        guessed = list(lblword.get())
        if wrd.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lblword.set("".join(guessed))
                if lblword.get()==wrd:
                    messagebox.showinfo("Hangman","You guessed it")
        else:
            chances += 1
            img.config(image=photos[chances])
            if chances==8:
                messagebox.showwarning("Hangman","Game Over")


img= Label(root)
img.grid(row=0,column=0,columnspan=3,padx=10,pady=40)
img.config(image = photos[0])
lblword = StringVar()
Label(root,textvariable=lblword,font=("Console 24 bold")).grid(row=0,column=4,columnspan=6,padx=10)
game()
n =  0
for c in ascii_lowercase:
    button =Button(root, text=c ,command =lambda c=c: guess(c)  , font={"Helvetica 18"}, width = 4)
    button.grid(row = 1 + n//9,column = n%9)
    n +=1
Button(root,text="New\nGame",command=lambda:game()).grid(row=3,column=8)

root.mainloop()