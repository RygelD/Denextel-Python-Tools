from tkinter import *
#Supported hashtag() colour formats: (255,255,255), #ffffff, <o4colourname>

class Screen:
  def __init__(self,geometry=(300,300),placement=(0,0),title='Screen'):
    master = Tk()
    a = Canvas(master,geometry[0],geometry[1])
    geometry = str(geometry[0])+'x'+str(geometry[1])+'+'+str(placement[0])+'+'+str(placement[1])
    master.title(title)
    master.geometry(geometry)
    self.m = master
    self.type = 'Screen'
    go()
  def go(self):
    x = start_window(self.m)
    self.m.mainloop()
  
class Layer:
  def __init__(self,priority):
    self.priority = priority
    self.type = 'Layer'
    self.items = []
  
  
class Array:
  def __init__(self,colourret=[]):
    self.px = colourret
    self.type = 'a'
class Square:
  def __init__(self,base=100, colour='black'):
    self.px = [base,colour]
    self.type = 's'
#class Rect:
#  def __init__(coordtop
    
#def paste(target,item,position):
 # if target.type == 'Layer'
def getinfo(target):
    return [target.px,target.type]  
def move(target,item,position):
  target.coords(item,position)

def delete(target,item):
  target.delete(item)

def copy(item):
  return item
 
def cut(target,item):
  target.delete(item)
  copy(item)

def clear(target):
  target.delete(ALL)
 
def hashtag(colour):
  colour = str(colour)
  if colour[0] == '(':
    n = 0
    if colour[2] == ',':
      i = colour[1]
      n = 3
    elif colour[3] == ',':
      i = colour[1] + colour[2]
      n = 4
    elif colour[4] == ',':
      i = colour[1] + colour[2] + colour[3]
      n = 5
    if colour[1+n+1] == ',':
      j = colour[n+1]
      n += 2
    elif colour[2+n+1] == ',':
      j = colour[n+1] + colour[1+n+1]
      n += 3
    elif colour[3+n+1] == ',':
      j = colour[n+1] + colour[1+n+1] + colour[2+n+1]
      n += 4
    if colour[1+n+2] == ')':
      k = colour[n+2]
    elif colour[2+n+2] == ')':
      k = colour[n+2] + colour[1+n+2]
    elif colour[3+n+2] == ')':
      k = colour[n+2] + colour[1+n+2] + colour[2+n+2]
    return '#' + colourhex(int(i)) + colourhex(int(j)) + colourhex(int(k))
  elif colour[0] == '#':
    return colour
  else:
    T = False
    tz = ['BLACK','FOREST','GREEN','NAVY','TEAL','OCEAN','BLUE','AQUA','CYAN']
    ty = ['MAHAGONY','OLIVE','LIME','VIOLET','GREY','GRASS','PURPLE','PERIWINKLE','SKY']
    tx = ['RED','ORANGE','YELLOW','PINK','SALMON','SAND','MAGENTA','CARTON','WHITE']
    if colour.upper() in tz:
      r = '00'
      T = True
      y = tz
    elif colour.upper() in ty:
      r = '7f'
      T = True
      y = ty
    elif colour.upper() in tx:
      r = 'ff'
      T = True
      y = tx
    if T:
      d = y.index(colour.upper())
      if d % 3 == 0:
        g = '00'
      elif d % 3 == 1:
        g = '7f'
      else:
        g = 'ff'
      if d // 3 == 0:
        b = '00'
      elif d //3 == 1:
        b = '7f'
      else:
        b = 'ff'
      return '#' + r + g + b
    else:
      w = ['LEATHER','BROWN','DARK','LIGHT']
      if colour.upper() in w:
        a = w.index(colour.upper())
        b = ['#cb6500','#5d2e00','#393939','#cecece']
        return b[a]
    
    
  
def colourhex(number):
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
  
  
  
