# Importación de librerías necesarias
import time
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import random

# ALGORITMOS DE ORDENAMIENTO CON CONTADOR DE PASOS

def merge_sort(arr, pasos=[0]):
    if len(arr) > 1:
        pasos[0] += 1  # Contador de pasos
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, pasos)
        merge_sort(R, pasos)
        i = j = k = 0
        while i < len(L) and j < len(R):
            pasos[0] += 1  # Contador de pasos
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            pasos[0] += 1  # Contador de pasos
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            pasos[0] += 1  # Contador de pasos

def quick_sort(arr, pasos=[0], start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        pivot_index = partition(arr, start, end, pasos)
        quick_sort(arr, pasos, start, pivot_index - 1)
        quick_sort(arr, pasos, pivot_index + 1, end)

def partition(arr, start, end, pasos):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        pasos[0] += 1  # Contador de pasos
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# FUNCIONES PARA GENERAR LISTAS

def generar_lista_aleatoria(tamano):
  return [random.randint(0, tamano) for _ in range(tamano)]

def generar_lista_ascendente(tamano):
  return list(range(1, tamano + 1))

def generar_lista_descendente(tamano):
  return list(range(tamano, 0, -1))

# FUNCIONES DE MEDICIÓN DE TIEMPO Y PASOS

def medir_tiempo(funcion, arr):
    inicio = time.perf_counter()
    funcion(arr.copy())
    fin = time.perf_counter()
    return fin - inicio

def medir_pasos(funcion, arr):
    pasos = [0]
    funcion(arr.copy(), pasos)
    return pasos[0]

# ANÁLISIS DE COMPLEJIDAD

def analizar_complejidad():
    tamano_maximo = int(input("Ingrese el tamaño máximo de la lista: "))
    tamanios_listas = np.array(list(range(10, tamano_maximo + 1, 20)))
    tipos_lista = ['Aleatoria', 'Ascendente', 'Descendente']

    for tipo in tipos_lista:
        tiempos_merge = []
        tiempos_quick = []
        pasos_merge = []
        pasos_quick = []

        for n in tamanios_listas:
            lista = {
                'Aleatoria': generar_lista_aleatoria(n),
                'Ascendente': generar_lista_ascendente(n),
                'Descendente': generar_lista_descendente(n)
            }[tipo]

            tiempo_merge = medir_tiempo(merge_sort, lista)
            tiempos_merge.append(tiempo_merge)
            pasos_merge.append(medir_pasos(merge_sort, lista))

            tiempo_quick = medir_tiempo(quick_sort, lista)
            tiempos_quick.append(tiempo_quick)
            pasos_quick.append(medir_pasos(quick_sort, lista))

        # Ajuste de polinomio y extracción de coeficientes
        coeficientes_merge = Polynomial.fit(tamanios_listas, pasos_merge, 2).convert().coef
        coeficientes_quick = Polynomial.fit(tamanios_listas, pasos_quick, 2).convert().coef

        print(f'Coeficientes del polinomio para Merge Sort ({tipo}): {coeficientes_merge}')
        print(f'Coeficientes del polinomio para Quick Sort ({tipo}): {coeficientes_quick}')

        # Graficar resultados
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        plt.plot(tamanios_listas, tiempos_merge, label='Merge Sort')
        plt.plot(tamanios_listas, tiempos_quick, label='Quick Sort')
        plt.title(f'Tiempos de ejecución - Listas {tipo}')
        plt.xlabel('Tamaño de la lista')
        plt.ylabel('Tiempo de ejecución (s)')
        plt.legend()
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.plot(tamanios_listas, pasos_merge, label='Merge Sort')
        plt.plot(tamanios_listas, pasos_quick, label='Quick Sort')
        plt.title(f'Pasos totales - Listas {tipo}')
        plt.xlabel('Tamaño de la lista')
        plt.ylabel('Pasos totales')
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

# Llama a la función para realizar el análisis
analizar_complejidad()
