# Denextel Python Graphics Engine Display
# DPGED.PY
# 2018 Denextel, 2018 Rygel Dagenais
# Part of the DenextelPythonScreenKit 
# version = 0.1

__version__ = 0.1
from tkinter import Tk, Canvas, Frame, BOTH
def shex(number):
    """ Convert numbers from 0 to 255 to 2 digit hexadecimal numbers (for RGB purposes)
Use:
  0 -> 00
255 -> ff
 16 -> 10

Used for converting RGB colours to hex
"""
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

class Screen(Frame):
  
    def __init__(self,title='DXL',mod=''):
        if mod != 'p':
            super().__init__()   
         
            self.initG() 
        self.title = title
    def initG(self):
        """ Activates the canvas
"""
        self.master.title(title)        
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        
    def drawpx(self,xy,rgb=(0,0,0)):
        """ Draw a pixel at (x,y), colour (R,G,B) (default colour is black)
"""
        r = rgb(0)
        g = rgb(1)
        b = rgb(2)
        canvas = self.canvas
        canvas.create_rectangle(x,y,x,y,outline='#'+str(shex(r))+str(shex(g))+str(shex(b)))        
        canvas.pack(fill=BOTH, expand=1)


def main(item,length,width): 
    root = Tk()
    ex = item
    root.geometry("0x0+"+str(length)+"+"+str(width))
    root.mainloop()
    
def mkcanvas(name,length,width)
    """ Safe method to make a screen """
    exec(name+' = Screen("p")')
    exec('main(' + name + ', '+  str(length) + ', ' + str(width) + ')')

