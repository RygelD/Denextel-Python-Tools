# Denextel Python Graphics Engine Display
# DPGED.PY
# 2018 Denextel, 2018 Rygel Dagenais
# Part of the DenextelPythonScreenKit 

__version__ = '0.2.3'

from tkinter import Tk, Canvas, Frame, BOTH
def shex(number):
    """ Convert numbers from 0 to 255 to 2 digit hexadecimal numbers (for RGB purposes)
Use:
  0 -> 00
255 -> ff
 16 -> 10

Used for converting RGB colours to hex RGB colours (for code purposes)
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
        """ Draw a pixel at (x,y), colour (R,G,B) (with r g and b in decimal values (default colour is black)
"""
        r = round(rgb(0))
        g = round(rgb(1))
        b = round(rgb(2))
        canvas = self.canvas
        canvas.create_rectangle(x,y,x,y,outline='#'+str(shex(r))+str(shex(g))+str(shex(b)))        
        canvas.pack(fill=BOTH, expand=1)


def main(item,length,width,xy=(0,0)): 
    root = Tk()
    ex = item
    root.geometry( str(length)+ "x" +str(width)+ "+"+str(xy[0])+"+" + str(xy[1]))
    root.mainloop()
    
def mkcanvas(name,length,width,xy=(0,0),screenname='DXL'):
    """ Safe method to make a screen, with name being the variable name containing the screen,
length and width being the dimentions of the screen, xy being the x and y coordinates of the top left corner of the canvas (defaulting to (0,0), screenname (defaulting to DXL)
being the name of the canvas"""
    exec(name+' = Screen("p",  screenname )')
    exec('main(' + name + ',' +  str(length) + ', ' + str(width) + ',' + str(xy) + ')')

