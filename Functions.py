import math
import random

def calcular_costo(x):
    """Función objetivo: x^2 + 15*sin(x)"""
    return x**2 + 15 * math.sin(x)

def generar_vecindad(actual, radio=2, cantidad=8):
    """Crea una lista de vecinos aleatorios alrededor del estado actual."""
    return [actual + random.uniform(-radio, radio) for _ in range(cantidad)]

def es_movimiento_tabu(vecino, lista_tabu, tolerancia=0.2):
    """Verifica si el vecino está en la memoria tabú con una tolerancia dada."""
    for tabu in lista_tabu:
        if abs(vecino - tabu) < tolerancia:
            return True
    return False