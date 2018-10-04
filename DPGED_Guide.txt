Denextel-Python-Tools
Graphics tools for Python 3
2018 Denextel


HOW TO USE DPGED - DENEXTEL'S PYTHON GRAPHICS ENGINE DISPLAY (v0.2.4):

To make a screen, use mkcanvas(name,length,width,xy=(0,0),screenname='DXL'), assigning an activated canvas at xy with sides width and height pixels long with a name of screenname to item.

To draw something there, use item.drawpx(xy,rgb=(0,0,0)) with item being the variable you assigned your canvas to, xy being the (x,y) coordinates of the pixel you wanted to place, and rgb being the colour you want to set it to in rgb (default is black).

class Screen:
  Class for windows (tkinter windows) with canas properties
  
  Modifiers: 
    mod = 'p', stops screen from imediatly being built
    title = '', changes screen title from 'DXL' to whatever string you want
  
  Functions:
    initG(): start letting the canvas change
    drawpx(xy,rgb=(0,0,0)): Draw a pixel at (x,y), colour (R,G,B) (with r g and b in decimal values (default colour is black))
    
Functions:
  main(item,length,width,xy=(0,0)): Draws the canvas item completly, at xy (default is (0,0)), with sides of length pixels and width pixels
  
  mkcanvas(name,length,width,xy=(0,0),screenname='DXL'): Safe method to make a screen, with name being the variable name containing the screen,length and width being the dimentions of the screen, xy being the x and y coordinates of the top left corner of the canvas (defaulting to (0,0), screenname (defaulting to DXL) being the name of the canvas"""
  
  shex(number): Converts number, a number from 0 to 255 to 2 digit hexadecimal numbers (for RGB purposes)
