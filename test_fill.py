from dpged import *
def fill(item,xytocolour):
  #Fill: Item = canvas name, xycolour is {(x,y):(r,g,b)}
  fn = xytocolour
  for i in fn:
    j = fn[i]
    item.drawpx(i,j)
