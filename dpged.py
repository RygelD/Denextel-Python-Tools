# Denextel Python Graphics Engine Display
# DPGED.PY
# 2018 Denextel, 2018 Rygel Dagenais
# Part of the DenextelPythonScreenKit 

__version__ = '0.2.4.4'

from tkinter import Tk, Canvas, Frame, BOTH
def shex(number):
    """ Convert numbers from 0 to 255 to 2 digit hexadecimal numbers (for RGB purposes)
Use:
  0 -> 00
255 -> ff
 16 -> 10
"""
    a = hex(number)
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
  
    def __init__(self,mod='',title='DXL'):
        self.title = title
        if mod != 'p':
            super().__init__()   
         
            self.initG() 
    def initG(self):
        """ Activates the canvas
"""
        super().__init__()
        self.master.title(self.title)        

        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        
    def drawpx(self,xy,rgb=(0,0,0)):
        """ Draws a pixel at (x,y), colour (R,G,B) (with r g and b in decimal values (default colour is black)
"""
        x = xy[0]
        y = xy[1]
        r = round(rgb[0])
        g = round(rgb[1])
        b = round(rgb[2])
        canvas = self.canvas
        canvas.create_rectangle(x,y,x,y,outline='#'+str(shex(r))+str(shex(g))+str(shex(b)))        
        canvas.pack(fill=BOTH, expand=1)
        
    def drawrt(self,xytl,xybr,rgb=(0,0,0)):
        """ Draws a rectangle using the top left coordinates (xytl, in (x,y))and the bottom right (xybr) coordinates. Colour (rgb) defaults to black.
"""
        xr = xybr[0]
        xl = xytl[0]
        yr = xybr[1]
        yl = xytl[1]
        r = round(rgb[0])
        g = round(rgb[1])
        b = round(rgb[2])
        pr = '#'+str(shex(r))+str(shex(g))+str(shex(b))
        canvas = self.canvas
        canvas.create_rectangle(xl,yl,xr,yr,outline=pr,fill=pr)        
        canvas.pack(fill=BOTH, expand=1)
        
    def drawsq(self,xy,size,rgb=(0,0,0)):
        """ Draws a square with the top right coordinates (xy, in (x,y)) with sides size pixels long. Colour (rgb) defaults to black.
"""
        x = xy[0]
        y = xy[1]
        r = round(rgb[0])
        g = round(rgb[1])
        b = round(rgb[2])
        pr = '#'+str(shex(r))+str(shex(g))+str(shex(b))
        canvas = self.canvas
        canvas.create_rectangle(x,y,x+size,y+size,outline=pr,fill=pr)        
        canvas.pack(fill=BOTH, expand=1)


def main(item,length,width,xy=(0,0),opt=False): 
    root = Tk()
    ex = item
    root.geometry( str(length)+ "x" +str(width)+ "+"+str(xy[0])+"+" + str(xy[1]))
    ex.initG()
    if opt:
        root.mainloop()
def control():
    root = Tk()
