import time
from Functions import calcular_costo, generar_vecindad, es_movimiento_tabu

def algoritmo_lista_tabu(estado_inicial, max_iter, tam_tenencia):
    inicio_reloj = time.perf_counter()

    actual = estado_inicial
    mejor_global = actual
    costo_mejor_global = calcular_costo(actual)
    lista_tabu = []

    print("-" * 60)
    print(f"ESTADO INICIAL: {actual:.4f} | COSTO: {costo_mejor_global:.4f}")
    print("-" * 60)

    for i in range(max_iter):
        vecinos = generar_vecindad(actual)
        mejor_candidato = None
        costo_mejor_candidato = float('inf')
        rechazados_tabu = 0

        for vecino in vecinos:
            costo_vecino = calcular_costo(vecino)
            es_tabu = es_movimiento_tabu(vecino, lista_tabu)

            # Criterio de Aspiración
            if not es_tabu or costo_vecino < costo_mejor_global:
                if costo_vecino < costo_mejor_candidato:
                    mejor_candidato = vecino
                    costo_mejor_candidato = costo_vecino
            else:
                rechazados_tabu += 1

        if mejor_candidato is not None:
            lista_tabu.append(actual) # Memoria a corto plazo
            actual = mejor_candidato

            if len(lista_tabu) > tam_tenencia:
                lista_tabu.pop(0)

            if costo_mejor_candidato < costo_mejor_global:
                mejor_global = mejor_candidato
                costo_mejor_global = costo_mejor_candidato

        if i % 10 == 0:
            print(f"ITERACIÓN {i} | Mejor Costo: {costo_mejor_global:.4f} | Tabús: {rechazados_tabu}")

    fin_reloj = time.perf_counter()
    return mejor_global, costo_mejor_global, (fin_reloj - inicio_reloj)

if __name__ == "__main__":
    solucion, costo, tiempo = algoritmo_lista_tabu(20.0, 100, 5)
    
    print("\n" + "=" * 60)
    print(f"RESULTADO FINAL: x = {solucion:.4f}")
    print(f"COSTO MÍNIMO: {costo:.4f}")
    print(f"TIEMPO DE EJECUCIÓN: {tiempo:.6f} segundos")
    print("=" * 60)