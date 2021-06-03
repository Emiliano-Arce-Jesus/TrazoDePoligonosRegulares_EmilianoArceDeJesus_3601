import matplotlib.pyplot as plt

def HBRESEN():
    #ORIGEN
    x=0
    y=0
    #plt.plot(round(x),round(y), marker="s", color="black")
    print(x,' , ',y)

    #SUPERIOR
    x1=-1
    y1=2
    x2= 1
    y2= 2
    #DATOS BASE
    dx= abs(x2 - x1)
    dy =abs(y2 -y1)
    p= (2 * dy) -dx


    #COSTADO DERECHO SUPERIOR
    xa= y1 #2
    ya= y1-y1 #0
    xa1= x2 #1
    ya1= y2 #2
    #DATOS DERECHA SUPERIOR
    dxa= abs(xa1 - xa)
    dya =abs(ya1 -ya)
    pa= (2 * dya) -dxa


    #COSTADO DERECHO INFERIOR
    xb= x2#1
    yb= y1 -(y1*2)#-2
    xb1= xa#2
    yb1= ya#0
    #DATOS DERECHA INFERIOR
    dxb= abs(xb1 - xb)
    dyb = abs(yb1 -yb)
    pb= (2 * dyb) -dxb


    #INFERIOR
    xc= xb#1
    yc= y1 -(y1*2)#-2
    xc1= x1#-1
    yc1= y2-(y2*2)#-2
    #DATOS DERECHA INFERIOR
    dxc= abs(xc1 - xc)
    dyc = abs(yc1 -yc)
    pc= (2 * dyc) -dxc

    
    #IZQUIERDO INFERIOR
    xd= x1#1
    yd= y1 -(y1*2)#-2
    xd1= x2-(x2*2)#-1
    yd1= y2-y2#-2
    #DATOS DERECHA INFERIOR
    dxd= abs(xd1 - xd)
    dyd = abs(yd1 -yd)
    pd= (2 * dyd) -dxd
    

    

    
    

    #SUPERIOR
    print('BASE')
    while x1 <= x2:
        plt.plot(round(x1),round(y1), marker="s", color="black")
        x1= x1 + 2
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            y1= y1 + 1
        print(x1,' , ',y1)

    
    
    #DERECHO SUPERIOR
    print('DERECHA')
    while ya <= ya1:
        plt.plot(round(xa),round(ya), marker="s", color="black")
        ya= ya +2
        if pa < 0:
            pa= pa + (2 * dya)
        else:
            pa= pa + (2 * dya) - (2 * dxa)
            xa= xa - 1
        print(xa,' , ',ya)



    
    #DERECHA INFERIOR
    print('DERECHA')
    while xb <= xb1:
        plt.plot(round(xb),round(yb), marker="s", color="black")
        xb= xb +1
        if pb < 0:
            pb= pb + (2 * dyb)
        else:
            pb= pb + (2 * dyb) - (2 * dxb)
            yb= yb + 2
        print(xb,' , ',yb)

    
    #INFERIOR
    print('DERECHA')
    while xc >= xc1:
        plt.plot(round(xc),round(yc), marker="s", color="black")
        xc= xc -2
        if pc < 0:
            pc= pc + (2 * dyc)
        else:
            pc= pc + (2 * dyc) - (2 * dxc)
            yc= yc - 1
        print(xc,' , ',yc)

    #IZQUIERDOINFERIOR
    print('DERECHA')
    while yd <= yd1:
        plt.plot(round(xd),round(yd), marker="s", color="black")
        yd= yd +2
        if pd < 0:
            pd= pd + (2 * dyd)
        else:
            pd= pd + (2 * dyd) - (2 * dxd)
            xd= xd - 1
        print(xd,' , ',yd)

    

    plt.show()
if __name__=='__HBRESEN__':
    HBRESEN()
