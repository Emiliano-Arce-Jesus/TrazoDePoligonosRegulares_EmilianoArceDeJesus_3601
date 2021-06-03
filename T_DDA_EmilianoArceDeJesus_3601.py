import matplotlib.pyplot as plt

def TDDA():
    
    x=0

    #BASE
    x1= -2
    y1= 0
    x2= 3
    y2= 0

    #IZQUIERDA
    xa= x1
    ya=y1
    xa1=0
    ya1=5

    #DERECHA
    xb1=0
    yb1=5
    xb= 2
    yb=0

   
    #BASE
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    if dx > dy:
        steps= dx
    else:
        steps= dy
    incx= dx/steps
    incy= dy/steps

    for i in range (x, steps):
        plt.plot(round(x1), round(y1), marker="s", color="black")
        x1= x1+incx
        y1= y1+incy
        print (x1, ',', y1)


    #IZQUIERDA
    dx= abs(xa1-xa)
    dy= abs(ya1-ya)
    if dx > dy:
        steps= dx
    else:
        steps= dy
    incx= dx/steps
    incy= dy/steps

    for i in range (x, steps):
        plt.plot(round(xa), round(ya), marker="s", color="black")
        xa= xa+incx
        ya= ya+incy
        print (xa, ',', ya)

    #DERECHA
    dx= abs(xb1-xb)
    dy= abs(yb1-yb)
    if dx > dy:
        steps= dx
    else:
        steps= dy
    incx= dx/steps
    incy= dy/steps

    for i in range (x, steps):
        plt.plot(round(xb), round(yb), marker="s", color="black")
        xb= xb-incx
        yb= yb+incy
        print (xb, ',', yb)

    
    
    plt.show()
if __name__== '__TDDA__':
    TDDA()