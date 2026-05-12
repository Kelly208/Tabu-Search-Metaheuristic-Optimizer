# Lista Tabú

Un proyecto de optimización que ataca un problema clásico: cómo salir de los óptimos locales sin perder eficiencia. La Búsqueda Tabú no se conforma con la primera solución aceptable; explora, recuerda y corrige el rumbo para acercarse a una solución global mejor.

## Resumen

Este repositorio implementa una versión clara y funcional de Búsqueda Tabú sobre una función objetivo continua. El resultado es un ejemplo práctico de cómo una estrategia de memoria puede mejorar la exploración en problemas de optimización.

## Lo que hace distinto a este proyecto

- Evita ciclos con una memoria de corto plazo que bloquea movimientos recientes.
- Explora con mayor amplitud gracias a la diversificación de vecinos.
- Rompe sus propias reglas cuando una solución tabú es demasiado buena para descartarla.
- Mide rendimiento real para mostrar mejora de costo y tiempo de ejecución.

## Base técnica

La función objetivo trabajada es:

$$f(x) = x^2 + 15\sin(x)$$

La lógica del algoritmo sigue esta secuencia:

1. Parte desde un estado inicial.
2. Genera una vecindad aleatoria alrededor del punto actual.
3. Filtra movimientos tabú, excepto cuando aplican criterios de aspiración.
4. Mantiene una lista tabú de tamaño limitado para evitar repetir rutas recientes.
5. Conserva la mejor solución global encontrada durante toda la ejecución.

## Benchmark

Una corrida típica muestra el contraste entre el estado inicial y la solución encontrada:

- **Costo inicial**: `413.6942`
- **Costo mínimo encontrado**: `-12.8189`
- **Tiempo de ejecución**: `0.000804 s`

Los valores exactos pueden variar entre ejecuciones por la aleatoriedad de la vecindad, pero el patrón se mantiene: mejora rápida del costo y muy bajo tiempo de ejecución.

## Arquitectura

La solución está dividida en dos módulos para mantener una estructura limpia y fácil de leer:

- [`Functions.py`](Functions.py) concentra la lógica matemática: costo, vecindad y validación tabú.
- [`Main.py`](Main.py) contiene el flujo del algoritmo, la iteración principal y la salida por consola.

Esa separación hace que el proyecto se vea y se mantenga como software bien organizado, no como un script monolítico.

## Aplicaciones reales

La Búsqueda Tabú es útil en escenarios donde no basta con encontrar una respuesta rápida, sino una mejor:

- Optimización de rutas de entrega en logística.
- Diseño de horarios y problemas de scheduling.
- Configuración de redes de telecomunicaciones.

## Ejecución

```bash
python3 Main.py
```

No requiere dependencias externas; solo Python 3.

## Estructura

```text
.
├── Functions.py
├── Main.py
└── README.md
```
