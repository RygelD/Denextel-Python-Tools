def filter(colour,xycolour):#,method='scale'):
  if colour in ['r','g','b','rg','rb','gb','c','m','y','bk','black','k','rgb','w']
    def r(xycolouro):
      cz = []
      for i in xycolouro:
        j = i[1]
        j[1] = 0
        j[2] = 0
        cz.append(i[0],j)
      return cz
    def g(xycolouro):
      cz = []
      for i in xycolouro:
        j = i[1]
        j[0] = 0
        j[2] = 0
        cz.append(i[0],j)
      return cz
    def b(xycolouro):
      cz = []
      for i in xycolouro:
        j = i[1]
        j[1] = 0
        j[0] = 0
        cz.append(i[0],j)
      return cz
    def combine(xytocolourone,xytocolourtwo,xytocolourthree=None):
      a = xytocolourone
      b = xytocolourtwo
      c = xytocolourthree
      pa = 2
      if c != None:
        pa = 3
      retl = []
      for i in a:
        rgb = ()
        j = b[a.index(i)]
        if c != None:
          k = c[a.index(i)]
        q = i[1]
        w = j[1]
        R = q[0] + w[0]
        G = q[1] + w[1]
        B = q[2] + w[2]
        if pa == 3:
          e = k[1]
          R += e[0]
          G += e[1]
          B += e[2]
        rR = R / pa
        gG = G / pa
        bB = B / pa
        rgb = (rR,gG,bB)
        xy = i[0]
        retl.append(xy,rgb)
      return retl
    
    if colour == 'r':
        return r(xycolour)
        
    elif colour == 'g':
      return g(xycolour)
      
    elif colour == 'b':
      return b(xycolour)
      
    elif colour == 'y' or colour == 'rg':
      return combine(r(xycolour),g(xycolour)) 
      
    elif colour == 'm' or colour == 'rb':
      return combine(r(xycolour),b(xycolour)) 
      
    elif colour == 'c' or colour == 'gb':
      return combine(g(xycolour),b(xycolour)) 
      
    elif colour in['bk','black','rgb','k','w']:
      return combine(r(xycolour),g(xycolour),b(xycolour)) 
        
  else:
    print('NOTICE - FILTER NOT FOUND')
    
    
    
 
 
 
