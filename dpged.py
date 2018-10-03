#
#
#
#
from tkinter import Tk, Canvas, Frame, BOTH
def shex(n):
    a = hex(n)
    a = str(a)
    b = list(a)
    b.pop(1)
    b.pop(0)
    if len(b) < 2:
        c = '0' + b[0]
    else:
        c = b[0] + b[1]
    return c

class Example(Frame):
  
    def __init__(self,mod=''):
        if mod != 'p':
            super().__init__()   
         
            self.initG()
            self.drawpx(5,5)
        
        
    def initG(self):
      
        self.master.title("Lines")        
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
    def drawpx(self,x,y):
        canvas = self.canvas
        r = 255
        g = 000
        b = 000
        canvas.create_rectangle(x,y,x,y,outline='#'+str(shex(r))+str(shex(g))+str(shex(b)))

        
        canvas.pack(fill=BOTH, expand=1)


def main(item,l,w):
  
    root = Tk()
    ex = item
    root.geometry("400x250+"+str(l)+"+"+str(w))
    root.mainloop()
def mkcanvas(name,l,w):
    exec(name+' = Example("p")')
    exec('main(' + name + ', '+  str(l) + ', ' + str(w) + ')')
#ex = Example()
#main(Tk,ex)
#ex.drawpx(15,15)
