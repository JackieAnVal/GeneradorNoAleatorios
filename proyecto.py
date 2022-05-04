import math
import matplotlib.pyplot as plt
from numpy import random


def generaAleatorios(generador, lista_generador, funcion, lista_funcion, n, bars):
    x0 = lista_generador[0]
    a = lista_generador[1]
    xn=x0
    no_aleatorios = []

    if generador == "mixto":
        c = lista_generador[2]
        m = lista_generador[3]
        m_generador=m
    elif generador == 'multiplicativo':
        c = 0
        m = lista_generador[2]
        m_generador=m-1
    else:
        return "Por favor elige entre mixto o multiplicativo"


    #GENERA NUMEROS ALEATORIOS MIXTO O MULTIPLICATIVO
    for i in range(n):
        xn=(a*(xn)+c) % m
        no_aleatorio = xn/m_generador
        no_aleatorios.append(no_aleatorio)
        #print("Xn : "+ str(xn) + "             No. aleatorio: "+ str(no_aleatorio))


    if funcion == 'exponencial':
        new_random_numbers = exponential_distribution(lista_funcion, no_aleatorios)
    elif funcion == 'normal':
        new_random_numbers = normal_distribution(lista_funcion, no_aleatorios)
    elif funcion == 'poisson':
        new_random_numbers = poisson_distribution(lista_funcion,no_aleatorios)
    elif funcion == 'binomial':
        new_random_numbers = binomial_distribution(lista_funcion,no_aleatorios)
    elif funcion== 'uniforme':
        new_random_numbers = uniform_distribution(lista_funcion, no_aleatorios)
    
    plt.hist(x=new_random_numbers, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    plt.show()

def uniform_distribution(function_list, no_aleatorios):
    limite_inferior = function_list[0]
    limite_superior = function_list[1]
    temp = limite_inferior+(limite_superior-limite_inferior)
    new_random_numbers = [no_aleatorio * temp for no_aleatorio in no_aleatorios]
    return new_random_numbers

def exponential_distribution(function_list, no_aleatorios):
    mean = function_list[0]
    new_random_numbers = []
    for number in no_aleatorios:
        distribution = -1/mean * math.log(number)
        new_random_numbers.append(distribution)
    return new_random_numbers

def normal_distribution(function_list, no_aleatorios):
    media = function_list[0]
    variation = function_list[1]
    x = function_list[2]
    exponential = -((x - media) ^ 2) / 2 * variation
    distribution = (1 / math.sqrt(2 * math.pi * variation)) * math.exp(exponential)
    return distribution

def poisson_distribution(function_list, no_aleatorios):
    x = function_list[0]
    mean = function_list[1]
    distribution = ((math.pow(mean, x)) / math.factorial(x)) * math.exp(-mean)
    return distribution

def binomial_distribution(function_list, no_aleatorios):
    x = function_list[0]
    p = function_list[1]
    n = function_list[2]
    distribution = combination(n, x) * math.pow(p, x) * math.pow((1 - p),(n - x))
    return distribution

def combination(n, r):
    c = math.factorial(n) / math.factorial(r) * math.factorial(n - r)
    return c


generador = "mixto"
lista_generador = [[15, 8, 16, 10], [13, 50, 17, 64], [7, 5, 24, 32], [3, 5, 21, 100], [0, 3, 3, 7]]
funcion = "poisson"
lista_funcion = [4, 18]
n = 10
bars = 5

#print(generaAleatorios(generador, lista_generador[4], funcion, lista_funcion, n, bars))

generador_m = "multiplicativo"
lista_generador_m = [[17, 203, 100000], [3, 211, 1000], [7, 5, 64], [1, 6, 13], [2777, 19, 32]]
funcion_m = "exponencial"
lista_funcion_m = [3, 18]
n_m = 10
bars_m = 50

#Multiplicativo x0, a, m 
#Mixto x0, a, c, m
#TODOS ESTOS JALAN BIEN
#generaAleatorios("multiplicativo", [5, 211, 10000], "exponencial", [5], 1000, 5)
#generaAleatorios("mixto", [7,5,24,32], "uniforme", [3,10], 100, 5)
#generaAleatorios("mixto", [5, 211, 16, 10000], "exponencial", [5], 10000, 5)

#print(generaAleatorios(generador_m, lista_generador_m[4], funcion_m, lista_funcion_m, n_m, bars_m))
#plt.hist(x=exponential_distribution([5, 2]), bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
#plt.show()