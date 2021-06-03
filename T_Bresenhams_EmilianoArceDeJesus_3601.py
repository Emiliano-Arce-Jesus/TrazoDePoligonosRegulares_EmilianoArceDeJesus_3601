import matplotlib.pyplot as plt

def TBRESEN():
    #BASE
    x1=0
    y1=0
    x2= x1+2
    y2= y1

    #COSTADO IZQUIERDO
    xa= x1
    ya= y1
    xa1= x1+1
    ya1= x2

    #COSTADO DEECHO
    xb= x1+4
    yb= y1
    xb1= x2
    yb1= y1 +2

    #DATOS BASE
    dx= abs(x2 - x1)
    dy =abs(y2 -y1)
    p= (2 * dy) -dx

    #DATOS IZQUIERDA
    dxa= abs(xa1 - xa)
    dya =abs(ya1 -ya)
    pa= (2 * dya) -dxa

    #DATOS DERECHA
    dxb= abs(xb1 - xb)
    dyb = abs(yb1 -yb)
    pb= (2 * dyb) -dxb

    

    #BASE
    print('BASE')
    while x1 <= (x2+2):
        plt.plot(round(x1),round(y1), marker="s", color="black")
        x1= x1 + 2
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            y1= y1 + 1
        print(x1,' , ',y1)

    #BIZQUIERDA
    print('IZQUIERDA')
    while ya <= ya1:
        plt.plot(round(xa),round(ya), marker="s", color="black")
        ya= ya +1
        if pa < 0:
            pa= pa + (2 * dya)
        else:
            pa= pa + (2 * dya) - (2 * dxa)
            xa= xa + 1
        print(xa,' , ',ya)


    #DERECHA
    print('DERECHA')
    while xb >= xb1:
        plt.plot(round(xb),round(yb), marker="s", color="black")
        xb= xb -1
        if pb < 0:
            pb= pb + (2 * dyb)
        else:
            pb= pb + (2 * dyb) - (2 * dxb)
            yb= yb + 1
        print(xb,' , ',yb)

    

    plt.show()
if __name__=='__TBRESEN__':
    TBRESEN()
