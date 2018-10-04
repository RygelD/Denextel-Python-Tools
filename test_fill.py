from dpged import *
__version__ = '0.1.0-alpha'
def fill(item,xytocolour):
  #Fill: Item = canvas name, xycolour is [ ((x,y),(r,g,b)) , ((),())]
  fn = xytocolour
  for i in fn:
    j = i[1]
    item.drawpx(i[0],j)
sets = []
class Layer:
    def __init__(self,priority,xytocolour):
      self.p = priority
      self.i = item
      self.s = xytocolour
      sets.append(self)
    def setpx(self,xy,rgb):
      comp = []
      for i in self.s:
        comp.append([self.s[0],i])
      for j in list(reversed(comp)):
        if j[0] == xy:
          self.s.remove(j[1])
      self.s.append([xy,rgb])
      
def ptop(item):
  fights = []
  for i in sets:
    pixels = i.s
    
    comp = ()
    
