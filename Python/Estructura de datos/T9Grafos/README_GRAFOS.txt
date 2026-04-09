"""
README - GRAFOS EN PYTHON
Documentación y guía de uso

Autor: Generado con asistencia de IA
Fecha: 2026
Asignatura: Estructura de Datos (DSA)
Basado en: W3Schools DSA - Graphs
"""

===============================================================================
                           DESCRIPCIÓN DEL PROYECTO
===============================================================================

Este proyecto implementa una estructura de datos GRAFO en Python tanto dirigida
como no dirigida, con múltiples algoritmos y visualizaciones.

CARACTERÍSTICAS PRINCIPALES:
✓ Grafos Dirigidos y No Dirigidos
✓ Soporta pesos en aristas (weighted graphs)
✓ Algoritmos de recorrido: DFS y BFS
✓ Algoritmo de Dijkstra para camino más corto
✓ Detección de componentes conexas
✓ Visualización con Matplotlib
✓ Visualización con Graphviz
✓ Ejemplos con números, letras y nombres


===============================================================================
                           ESTRUCTURA DEL PROYECTO
===============================================================================

ARCHIVO 1: T9Grafos.py (BACKEND - CLASES Y ALGORITMOS)
─────────────────────────────────────────────────────

Clase Nodo:
  - Representa un vértice en el grafo
  - Atributos: valor, adyacentes (dict con pesos), visitado
  - Métodos: agregar_vecino(), obtener_vecinos(), obtener_peso()

Clase Grafo (Base):
  - Clase padre para grafos dirigidos y no dirigidos
  - Constructor: Grafo(dirigido: bool)
  
  MÉTODOS DE OPERACIONES BÁSICAS:
    • agregar_vertice(valor)         - Agrega un nodo al grafo
    • eliminar_vertice(valor)        - Elimina un nodo del grafo
    • agregar_arista(v1, v2, peso)   - Agrega una arista entre dos nodos
    • eliminar_arista(v1, v2)        - Elimina una arista
    
  MÉTODOS DE CONSULTA:
    • obtener_vertices()             - Retorna lista de vértices
    • obtener_aristas()              - Retorna lista de aristas (tuplas)
    • es_conexo()                    - Verifica si el grafo es conexo
    
  MÉTODOS DE RECORRIDO:
    • dfs(inicio)                    - Recorrido profundo (Depth-First Search)
    • bfs(inicio)                    - Recorrido por amplitud (Breadth-First Search)
    
  MÉTODOS DE RUTAS:
    • dijkstra(inicio)               - Calcula distancias mínimas desde un nodo
    • obtener_camino(inicio, fin)    - Obtiene el camino más corto entre dos nodos
    
  MÉTODOS AVANZADOS:
    • componentes_conexas()          - Encuentra componentes desconectadas
    • limpiar_visitas()              - Reinicia el estado visitado
    • mostrar_grafo()                - Imprime información del grafo en consola

Clase GrafoDirigido(Grafo):
  - Hereda de Grafo con dirigido = True
  - Las aristas tienen dirección

Clase GrafoNoDirigido(Grafo):
  - Hereda de Grafo con dirigido = False
  - Las aristas son bidireccionales


ARCHIVO 2: T9main.py (FRONTEND - EJEMPLOS Y VISUALIZACIONES)
───────────────────────────────────────────────────────────

Contiene:
  ✓ Función de visualización con Matplotlib
  ✓ Función de visualización con Graphviz
  ✓ 5 Demostraciones completas:
    1. Grafo no dirigido con números
    2. Grafo dirigido con letras
    3. Grafo con ciudades (red de transporte)
    4. Grafo desconexo (múltiples componentes)
    5. Operaciones básicas paso a paso
  ✓ Menú interactivo para seleccionar demostraciones


===============================================================================
                           REQUISITOS E INSTALACIÓN
===============================================================================

REQUISITOS:
  - Python 3.7+
  - Librerías: matplotlib, graphviz

INSTALACIÓN:
  pip install matplotlib graphviz

NOTA: Para Graphviz también necesitas el software Graphviz instalado en tu sistema:
  - Windows: Descargar desde https://graphviz.org/download/
  - Mac: brew install graphviz
  - Linux: sudo apt-get install graphviz


===============================================================================
                           CÓMO USAR EL CÓDIGO
===============================================================================

OPCIÓN 1: EJECUTAR EL MENÚ INTERACTIVO
──────────────────────────────────────

python T9main.py

Esto abre un menú interactivo donde puedes seleccionar qué demostración ejecutar.


OPCIÓN 2: USAR LAS CLASES DIRECTAMENTE
──────────────────────────────────────

from T9Grafos import GrafoNoDirigido, GrafoDirigido

# Crear un grafo no dirigido
g = GrafoNoDirigido()

# Agregar aristas (crea automáticamente los vértices)
g.agregar_arista('A', 'B', peso=5)
g.agregar_arista('B', 'C', peso=3)
g.agregar_arista('A', 'C', peso=10)

# Recorridos
print(g.dfs('A'))        # ['A', 'B', 'C']
print(g.bfs('A'))        # ['A', 'B', 'C']

# Camino más corto
print(g.obtener_camino('A', 'C'))  # ['A', 'B', 'C']

# Información
g.mostrar_grafo()


===============================================================================
                           ALGORITMOS EXPLICADOS
===============================================================================

1. DFS (DEPTH-FIRST SEARCH)
──────────────────────────
Estrategia: Explora tan profundo como sea posible antes de retroceder
Complejidad: O(V + E)
Ejemplo de uso: Detectar ciclos, encontrar componentes conexas

    Algoritmo:
    1. Comenzar desde un nodo inicial
    2. Marcar como visitado
    3. Explorar recursivamente cada vecino no visitado
    4. Retroceder cuando no hay más vecinos


2. BFS (BREADTH-FIRST SEARCH)
────────────────────────────
Estrategia: Explora todos los vecinos antes de ir más profundo
Complejidad: O(V + E)
Ejemplo de uso: Camino más corto en grafos sin pesos

    Algoritmo:
    1. Comenzar desde un nodo inicial
    2. Marcar como visitado y agregar a cola
    3. Para cada nodo en cola:
       - Explorar todos sus vecinos
       - Si no fueron visitados, marcar y agregar a cola


3. DIJKSTRA (CAMINO MÁS CORTO)
──────────────────────────────
Estrategia: Encuentra las distancias mínimas desde un nodo a todos los otros
Complejidad: O((V + E) log V)
Requisito: No puede haber pesos negativos
Ejemplo de uso: GPS, redes de telecomunicaciones

    Algoritmo:
    1. Inicializar distancias en infinito, excepto el inicio en 0
    2. Usar cola de prioridad para explorar nodos por distancia menor
    3. Para cada nodo:
       - Actualizar distancias de vecinos si encontramos camino más corto
       - Registrar el predecesor


4. COMPONENTES CONEXAS
─────────────────────
Estrategia: Encontrar grupos desconectados en el grafo
Complejidad: O(V + E)
Ejemplo de uso: Redes sociales, análisis de conectividad

    Algoritmo:
    1. Para cada nodo no visitado:
       - Hacer DFS/BFS desde ese nodo
       - Todos los nodos alcanzados forman una componente


===============================================================================
                           EJEMPLOS PRÁCTICOS
===============================================================================

EJEMPLO 1: Red Social Simple
────────────────────────────

from T9Grafos import GrafoNoDirigido

red_social = GrafoNoDirigido()

# Agregar amistades (aristas sin peso)
amigos = [('Carlos', 'María'), ('Carlos', 'Juan'), ('María', 'Juan'),
          ('Juan', 'Ana'), ('Ana', 'Pedro')]

for persona1, persona2 in amigos:
    red_social.agregar_arista(persona1, persona2)

# Encontrar todos los amigos de Carlos
print("Amigos conectados a Carlos:")
print(red_social.bfs('Carlos'))

# Componentes conexas
print("Grupos de amigos:")
print(red_social.componentes_conexas())


EJEMPLO 2: Red de Transportes
──────────────────────────────

from T9Grafos import GrafoNoDirigido

rutas = GrafoNoDirigido()

# Agregar ciudades con distancias en km
ciudades = [('Madrid', 'Barcelona', 620),
            ('Madrid', 'Valencia', 360),
            ('Barcelona', 'Valencia', 480),
            ('Valencia', 'Sevilla', 700)]

for ciudad1, ciudad2, distancia in ciudades:
    rutas.agregar_arista(ciudad1, ciudad2, distancia)

# Encontrar ruta más corta
print(rutas.obtener_camino('Madrid', 'Sevilla'))

# Distancias desde Madrid
dijkstra = rutas.dijkstra('Madrid')
for ciudad, (distancia, _) in dijkstra.items():
    print(f"Madrid -> {ciudad}: {distancia} km")


EJEMPLO 3: Dependencias de Tareas
──────────────────────────────────

from T9Grafos import GrafoDirigido

tareas = GrafoDirigido()

# Agregar dependencias (A debe completarse antes que B)
dependencias = [('Diseño', 'Desarrollo'), ('Desarrollo', 'Testing'),
                ('Desarrollo', 'Documentación'), ('Testing', 'Deploy')]

for tarea_prev, tarea_actual in dependencias:
    tareas.agregar_arista(tarea_prev, tarea_actual)

# Orden de ejecución
print("Orden de tareas (BFS):")
print(tareas.bfs('Diseño'))


===============================================================================
                           TIPS Y MEJORES PRÁCTICAS
===============================================================================

1. ELEGIR ENTRE DIRIGIDO Y NO DIRIGIDO:
   - Dirigido: Para relaciones de una sola dirección (seguidores, dependencias)
   - No Dirigido: Para relaciones mutuas (amistad, carreteras)

2. USAR PESOS CUANDO SEA NECESARIO:
   - Con pesos: Usar Dijkstra para rutas óptimas
   - Sin pesos: BFS es más simple y eficiente

3. VALIDACIÓN DE ENTRADA:
   Los métodos devuelven False o [] si hay errores. Siempre verifica:
   - Si un vértice existe antes de usarlo
   - Si una arista existe antes de eliminarla

4. COMPLEJIDAD DE TIEMPO:
   - Agregar/eliminar: O(1)
   - Recorridos (DFS/BFS): O(V + E)
   - Dijkstra: O((V + E) log V)

5. VISUALIZACIÓN:
   - Matplotlib: Mejor para análisis rápido, personalización
   - Graphviz: Mejor para grafos grandes y documentación


===============================================================================
                           PREGUNTAS FRECUENTES
===============================================================================

P: ¿Puedo tener bucles (self-loops)?
R: Sí, agrega una arista de un nodo a sí mismo: g.agregar_arista(1, 1)

P: ¿Qué pasa si agrego una arista a vértices inexistentes?
R: Los vértices se crean automáticamente, no hay errors.

P: ¿Puedo modificar pesos después de crear una arista?
R: Elimina y re-agrega la arista con el nuevo peso.

P: ¿Funciona con grafos muy grandes (10,000+ nodos)?
R: Sí, pero la visualización será lenta. Los algoritmos mantendrán O(V + E).

P: ¿Cómo detectar ciclos?
R: Usar DFS y tracker nodos visitados en la ruta actual.


===============================================================================
                           RECURSOS ADICIONALES
===============================================================================

W3Schools DSA - Graphs:
https://www.w3schools.com/dsa/dsa_graphs.php

Visualizadores Graph Online:
https://dreampuf.github.io/GraphvizOnline/

NetworkX (librería para análisis de grafos):
https://networkx.org/

===============================================================================
"""
