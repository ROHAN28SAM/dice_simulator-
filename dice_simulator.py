import random
from tkinter import *
# Using TKinter 
base = Tk()
base.geometry("400x300")
base.title("Dice Simulator")

l1 = Label(base,text='', font=('times',200))
l2 = Label(base,text='Standard Dice')
l3 = Label(base,text='Advance Dice')


def roll():
    number_dice1 = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number_dice1)}')
    l1.pack()

def roll2():
    number_dice2 = ['\u2685','\u2681','\u2682','\u2683','\u2685','\u2685']
    l1.config(text=f'{random.choice(number_dice2)}')
    l1.pack()

b1 = Button(base, text="Let's Roll", command = roll)
b1.place(x= 110, y=0)
l2.place(x=100,y=30)

b2 = Button(base, text="Let's Rock & Roll", command = roll2)
b2.place(x= 230, y=0)
l3.place(x=235,y=30)
base.mainloop()


#using terminal
# again = True

# while again:
#     print(random.randint(1,6))
#     roll_again = input("You want to roll again (y/n): ")
#     if roll_again.lower() == 'y':
#         continue
        
#     else:
#         break


