from matplotlib.pyplot import close, contour
from C_DDA_EmilianoArceDeJesus_3601 import CDDA
from C_Bresenhams_EmilianoArceDeJesus_3601 import CBRESEN
from T_DDA_EmilianoArceDeJesus_3601 import TDDA
from T_Bresenhams_EmilianoArceDeJesus_3601 import TBRESEN
from H_Bresenhams_EmilianoArceDeJesus_3601 import HBRESEN
from P_Bresenhams_EmilianoArceDeJesus_3601 import PBRESEN
def main():
    continuar= True
    while continuar==True:
        n=int(input('INGRESA EL NUMERO DE LADOS DEL POLÍGONO REGULAR A DIBUJAR: '))
        if n < 3:
            print('\n¡ERROR! NO SE PUEDE DIBUJAR UNA FIGURA MENOR A 3 LADOS\n')
            #main()
            continuar=False
        #TRIANGULO
        elif n==3:
            algoritmo=False
            while algoritmo== False:
                metodo= int(input('¿CON QUÉ ALGORITMO DESEAS DIBUJAR EL POLÍGONO?\n1= DDA   2= BRESENHAMS \n'))
                if metodo==1:
                    algoritmo=True
                    TDDA()
                elif metodo==2:
                    algoritmo=True
                    TBRESEN()
                elif metodo > 2 or metodo < 1:
                    print('OPCION NO RECONOCIDA INTENTALO DE NUEVO')
                    algoritmo= False
        #CUADRADO
        elif n==4:
            algoritmo=False
            while algoritmo== False:
                metodo= int(input('¿CON QUÉ ALGORITMO DESEAS DIBUJAR EL POLÍGONO?\n1= DDA   2= BRESENHAMS \n'))
                if metodo==1:
                    algoritmo=True
                    CDDA()
                elif metodo==2:
                    algoritmo=True
                    CBRESEN()
                elif metodo > 2 or metodo < 1:
                    print('OPCION NO RECONOCIDA INTENTALO DE NUEVO')
                    algoritmo= False
        
        #PENTAGONO
        elif n==5:
            algoritmo=False
            while algoritmo== False:
                metodo= int(input('¿CON QUÉ ALGORITMO DESEAS DIBUJAR EL POLÍGONO?\n1= DDA   2= BRESENHAMS \n'))
                if metodo==1:
                    algoritmo=True
                    print('\n¡LO SENTIMOS, EL ALGORITMO DDA SE ENCUENTRA EN DESARROLLO!')
                    algoritmo=False
                    #CDDA()
                elif metodo==2:
                    algoritmo=True
                    PBRESEN()
                elif metodo > 2 or metodo < 1:
                    print('OPCION NO RECONOCIDA INTENTALO DE NUEVO')
                    algoritmo= False

        #HEXAGONO
        elif n==6:
            algoritmo=False
            while algoritmo== False:
                metodo= int(input('¿CON QUÉ ALGORITMO DESEAS DIBUJAR EL POLÍGONO?\n1= DDA   2= BRESENHAMS \n'))
                if metodo==1:
                    algoritmo=True
                    print('\n¡LO SENTIMOS, EL ALGORITMO DDA SE ENCUENTRA EN DESARROLLO!')
                    algoritmo=False
                    #CDDA()
                elif metodo==2:
                    algoritmo=True
                    HBRESEN()
                elif metodo > 2 or metodo < 1:
                    print('OPCION NO RECONOCIDA INTENTALO DE NUEVO')
                    algoritmo= False

        elif n>6:
            print('\n¡LO SENTIMOS, EL PROGRAMA NO PUEDE DIBUJAR FIGURAS CON MAS DE 6 LADOS!')
            continuar=False
        ##¿CONTINUAR?
        continuar= int(input('\n¿DESEAS CONTINUAR DIBUJANDO POLIGONOS?\n1= SI 2= NO\n'))
        if continuar ==2:
            exit
            print('HASTA LUEGO\n')
            
        elif continuar ==1:
            continuar= True
   
if __name__== "__main__":
    main()