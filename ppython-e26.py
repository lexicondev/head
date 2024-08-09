#What may be perhaps the stupidest way to write this code, but it works. Armored enemy felled by mushroom

win1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]
no = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]
win2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
def w(x,y,z):
    if x == y == z and x != 0:
        print("Player",x,"Wins")
        exit()
    else:
        return False
def cw(lis):
        a = list(lis[0])
        b = list(lis[1])
        c = list(lis[2])
        ta = a[-1]
        ma = a[-2]
        fa = a[-3]
        tb = b[-1]
        mb = b[-2]
        fb = b[-3]
        tc = c[-1]
        mc = c[-2]
        fc = c[-3]
        while True:
            w(ta,ma,fa)
            w(tb,mb,fb)
            w(tc,mc,fc)
            w(ta,tb,tc)
            w(ma,mb,mc)
            w(fa,fb,fc)
            w(ta,mb,fc)
            w(fa,mb,tc)
            print("Draw")
            return False
        
cw(win2)