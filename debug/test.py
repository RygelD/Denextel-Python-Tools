from tkinter import *
import random
window = Tk()
window.geometry("600x400")
window.title("Test")
window.sx = random.randint(1,10) * random.choice([-1,1])
window.sy = random.randint(1,10) * random.choice([-1,1])
window.x = window.sx
window.y = window.sy

def test(event):
    print("Hi")
def up(event):
    window.y += 1
def down(event):
    window.y -= 1
def left(event):
    window.x -= 1
def right(event):
    window.x += 1
def enter(event):
    print('\nx='+str(window.x)+'\ny='+str(window.y))
    if window.x ==0 and window.y == 0:
        print('Victory!')
window.bind("a", test)
window.bind('<Up>',up)
window.bind('<Down>',down)
window.bind('<Left>',left)
window.bind('<Right>',right)
window.bind('<Return>',enter)
#window.mainloop()
