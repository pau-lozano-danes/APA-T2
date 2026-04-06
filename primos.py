"""
Módulo de manejo de números primos.
Alumno: Pau Lozano Danes

Tests Unitarios:
>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """
    Determina si un número natural mayor que 1 es primo.
    
    Argumentos:
        numero (int): Número a evaluar.
        
    Retorna:
        bool: True si es primo, False en caso contrario.
        
    Excepciones:
        TypeError: Si el argumento no es entero o es menor que 2.
    """
    if not isinstance(numero, int) or numero < 2:
        raise TypeError("El argumento debe ser un número entero mayor que 1.")
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    """
    Devuelve todos los números primos menores que el argumento.
    
    Argumentos:
        numero (int): Límite superior (no incluido) para buscar primos.
        
    Retorna:
        tuple: Tupla con los números primos encontrados.
    """
    return tuple(i for i in range(2, numero) if esPrimo(i))

def descompon(numero):
    """
    Descompone un número en sus factores primos.
    
    Argumentos:
        numero (int): Número a descomponer.
        
    Retorna:
        tuple: Tupla con los factores primos.
    """
    factores = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        else:
            divisor += 1
    return tuple(factores)

def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo de un número arbitrario de argumentos
    usando la descomposición en factores primos.
    
    Argumentos:
        *numeros (int): Números enteros.
        
    Retorna:
        int: El mínimo común múltiplo.
    """
    if not numeros:
        return 1
    
    max_factores = {}
    for num in numeros:
        factores_actuales = descompon(num)
        # Usamos set para iterar por factores únicos
        for factor in set(factores_actuales):
            cantidad = factores_actuales.count(factor)
            if factor not in max_factores or cantidad > max_factores[factor]:
                max_factores[factor] = cantidad
                
    resultado = 1
    for factor, cantidad in max_factores.items():
        resultado *= (factor ** cantidad)
    return resultado

def mcd(*numeros):
    """
    Calcula el máximo común divisor de un número arbitrario de argumentos
    usando la descomposición en factores primos.
    
    Argumentos:
        *numeros (int): Números enteros.
        
    Retorna:
        int: El máximo común divisor.
    """
    if not numeros:
        return 1
    
    # Empezamos asumiendo que los factores comunes son los del primer número
    factores_comunes = list(descompon(numeros[0]))
    
    for num in numeros[1:]:
        factores_actuales = list(descompon(num))
        temp_comunes = []
        for factor in set(factores_comunes):
            # Nos quedamos con la cantidad mínima en la que aparece el factor
            cantidad = min(factores_comunes.count(factor), factores_actuales.count(factor))
            temp_comunes.extend([factor] * cantidad)
        factores_comunes = temp_comunes
        
    resultado = 1
    for factor in factores_comunes:
        resultado *= factor
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()