"""
Funcion que determina si un numero es primo o no (devuelve True o False) 
"""


class PrimeClass(object):
	""" 
	manda a pedir por pantalla numeros
	"""
n=input('ingrese el numero para saber si es prim0   ')
def divisores(n):
	
    """ divisores de  n """
    
    lista_divisores = []
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            lista_divisores.append(divisor)
    return lista_divisores
    
def is_prime(n):

    # Si es primo solo sera divisible entre 1 y si mismo
    return len(divisores(n)) == 2

print is_prime(n)
