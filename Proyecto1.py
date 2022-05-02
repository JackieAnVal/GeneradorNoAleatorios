import math

def generaAleatorios(generador, lista_generador, funcion, lista_funcion, n, m):
    x0=lista_generador[0]
    a=lista_generador[1]

    if(generador=="mixto"):
        c=lista_generador[2]
        m=lista_generador[3]
        m_generador=m
    else:
        c = 0
        m = lista_generador[2]
        m_generador=m-1

    #print("C: "+str(c)+" M: "+str(m))

    xn=x0
    no_aleatorios = []

    no_aleatorio = 0
    periodo=0
    found = False
    for i in range(n):
        xn=(a*(xn)+c) % m
        no_aleatorio = xn/m_generador
        
        if no_aleatorio in no_aleatorios and found!=True:
            periodo = i - no_aleatorios.index(no_aleatorio)
            found = True
            '''#SIRVE PARA DETERMINAR EL PERIODO
            print("\nSe repitió: " + str(no_aleatorio) + "  En ciclo: "+str(i)+"    First occurrence at: "+ str(no_aleatorios.index(no_aleatorio))+"  Periodo: "+ str(periodo) +"\n")
            print(no_aleatorios)
            break
            '''
        
        no_aleatorios.append(no_aleatorio)
        print("Xn : "+ str(xn) + "             No. aleatorio: "+ str(no_aleatorio))

    if(funcion=="uniforme"):
        limite_inferior = lista_funcion[0]
        limite_superior = lista_funcion[1]
        temp = limite_inferior+(limite_superior-limite_inferior)
        print(temp)
        no_aleatorios_uniformes = [no_aleatorio * temp for no_aleatorio in no_aleatorios]
        
    print(no_aleatorios)
    print(no_aleatorios_uniformes)


generador="mixto"
lista_generador= [[15,8,16,10],[13,50,17,64],[7,5,24,32],[3,5,21,100]]
funcion = "uniforme"
lista_funcion = [3,10]
n = 10
m = 5

generaAleatorios(generador, lista_generador[2], funcion, lista_funcion, n, m)    
#generaAleatorios(generador, lista_generador[1], funcion, lista_funcion, n, m) 
#generaAleatorios(generador, lista_generador[2], funcion, lista_funcion, n, m)
#generaAleatorios(generador, lista_generador[3], funcion, lista_funcion, n, m)

'''
generador="multiplicativo"
#x0, a, c, m
lista_generador= [[17, 203, 100000],[3,211, 1000],[7,5,64], [1,6,13], [2777,19,32]]
funcion = "uniforme"
lista_funcion = [0,18]
n = 10
m = 5

#generaAleatorios(generador, lista_generador[0], funcion, lista_funcion, n, m)
#generaAleatorios(generador, lista_generador[2], funcion, lista_funcion, n, m)
#generaAleatorios(generador, lista_generador[1], funcion, lista_funcion, n, m)
generaAleatorios(generador, lista_generador[4], funcion, lista_funcion, n, m)
'''