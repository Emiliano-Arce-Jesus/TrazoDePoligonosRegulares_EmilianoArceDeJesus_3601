import matplotlib.pyplot as plt

def PBRESEN():

    #plt.plot(round(x),round(y), marker="s", color="black")
    #print(x,' , ',y)

    #SUPERIOR IZQUIERDO
    x1=-4
    y1=1
    x2= 0
    y2= 5
    # DATOS SUPERIOR IZQUIERDO
    dx= abs(x2 - x1)
    dy =abs(y2 -y1)
    p= (2 * dy) -dx


    #SUPERIOR DERECHO 
    xa= 4 #4
    ya= y1 #0
    xa1= x2 #0
    ya1= y2#4
    #DATOS SUPERIOR DERECHO
    dxa= abs(xa1 - xa)
    dya =abs(ya1 -ya)
    pa= (2 * dya) -dxa


    #COSTADO DERECHO INFERIOR
    xb= 2#x2#1
    yb= -3#y1 -(y1*2)#-2
    xb1= 10#xa#2
    yb1= 0#1
    #DATOS DERECHA INFERIOR
    dxb= abs(xb1 - xb)
    dyb = abs(yb1 -yb)
    pb= (2 * dyb) -dxb


    #INFERIOR
    xc= -2
    yc= -3
    xc1= 2
    yc1= -3
    #DATOS  INFERIOR
    dxc= abs(xc1 - xc)
    dyc = abs(yc1 -yc)
    pc= (2 * dyc) -dxc

    
    #IZQUIERDO INFERIOR
    xd= -2
    yd= -3
    xd1= -10#x1#-4
    yd1= 0#-2
    #DATOS IZQUIERDA INFERIOR
    dxd= abs(xd1 - xd)
    dyd = abs(yd1 -yd)
    pd= (2 * dyd) -dxd
    

    

    
    

    #IZQUIERDO SUPERIOR
    print(' IZQUIERDO SUPERIOR')
    while x1 <= x2:
        plt.plot(round(x1),round(y1), marker="s", color="black")
        x1= x1 + 1
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            y1= y1 + 1
        print(x1,' , ',y1)

    
    
    #DERECHO SUPERIOR
    print('DERECHO SUPERIOR')
    while ya <= ya1:
        plt.plot(round(xa),round(ya), marker="s", color="black")
        ya= ya +1
        if pa < 0:
            pa= pa + (2 * dya)
        else:
            pa= pa + (2 * dya) - (2 * dxa)
            xa= xa - 1
        print(xa,' , ',ya)



    
    #DERECHA INFERIOR
    print('DERECHA INFERIOR')
    while yb <= yb1:
        plt.plot(round(xb),round(yb), marker="s", color="black")
        yb= yb +1
        if pb < 0:
            pb= pb + (2 * dyb)
        else:
            pb= pb + (2 * dyb) - (2 * dxb)
            xb= xb + 1
        print(xb,' , ',yb)

    
    #INFERIOR
    print('INFERIOR')
    while xc <= xc1:
        plt.plot(round(xc),round(yc), marker="s", color="black")
        xc= xc +1
        if pc < 0:
            pc= pc + (2 * dyc)
        else:
            pc= pc + (2 * dyc) - (2 * dxc)
            yc= yc + 1
        print(xc,' , ',yc)


    #IZQUIERDO INFERIOR
    #xd= -2
    #yd= -3
    #xd1= x1#-4
    #yd1= y1#1
    #DATOS IZQUIERDA INFERIOR
    #dxd= abs(xd1 - xd)
    #dyd = abs(yd1 -yd)
    #pd= (2 * dyd) -dxd

    #IZQUIERDO INFERIOR
    print('IZQUIERDO INFERIOR')
    while yd <= yd1:
        plt.plot(round(xd),round(yd), marker="s", color="black")
        yd= yd +1
        if pd < 0:
            pd= pd + (2 * dyd)
        else:
            pd= pd + (2 * dyd) - (2 * dxd)
            xd= xd - 1
        print(xd,' , ',yd)
    

    plt.show()
if __name__=='__PBRESEN__':
    PBRESEN()
