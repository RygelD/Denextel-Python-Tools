from dpged import *
from screenkitlayers import *
#debug
def test():
    cat = mkcanvas(300,300,(200,200),screenname='FXL')
    for i in range(0,300):
        cat.drawpx((i,i),(255,0,255))
        cat.drawpx((i,300-i),(255,255,0))
        cat.drawpx((300-i,i),(0,255,255))
        cat.drawpx((300-i,300-i),(255,0,0))
        cat.drawpx((150,i),(0,255,0))
        cat.drawpx((i,150),(0,0,255))
        cat.drawpx((150,300-i),(255,255,255))
        cat.drawpx((300-i,150),(0,0,0))
    
	
