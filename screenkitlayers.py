# Denextel Python Layers Screen Kit for Graphic Displays
# SCREENKITLAYERS.PY
# 2018 Denextel, 2018 Rygel Dagenais
# Part of the DenextelPythonScreenKit

from dpged import *
__version__ = '0.2.1'
def fill(item,xytocolour):
  """ Fill pixels in xycolour on the canvas named item in a colour in xycolour
  XYCOLOUR: [ ((x position, y position),(r value, g value, b value)) ]
  """
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
      
def ptop():
  """ Returns layer consisting of pixels based on position in priority (top layer)
  """
  sets = sorted(sets,key=lambda x: x.p )
  final = {}
  retlist = []
  items = []
  for i in sets:
    pl = i.s
    for j in pl:
      final[j[0]] = j[1]
  for i in final:
    retlist.append([i,final[i]])
  return retlist

def update_canvas_layer(item):
  """ Updates canvas to top layer 
"""
  fill(item,ptop())
 
def sizeprint(item,xy,size,rgb=(0,0,0)):
  xy[0] = xy[0] * size
  xy[1] = xy[1] * size
  item.drawsq(xy,size,rgb)
    
