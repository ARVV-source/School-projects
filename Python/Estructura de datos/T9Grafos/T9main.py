"""
Archivo principal - Demostración de Grafos
Incluye ejemplos con números, letras, ciudades y visualizaciones
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import graphviz
import os
import sys
from T9Grafos import GrafoDirigido, GrafoNoDirigido


# ============================================================================
# FUNCIONES DE VISUALIZACIÓN CON MATPLOTLIB
# ============================================================================

def calcular_posiciones_circulares(vertices: list, radio: float = 1.0) -> dict:
    """Calcula posiciones circulares para los vértices"""
    import math
    posiciones = {}
    n = len(vertices)
    
    for i, vertice in enumerate(vertices):
        angulo = (2 * math.pi * i) / n
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        posiciones[vertice] = (x, y)
    
    return posiciones


def visualizar_grafo_matplotlib(grafo, titulo: str = "Grafo", filename: str = None):
    """
    Visualiza un grafo usando Matplotlib
    
    Args:
        grafo: Objeto Grafo a visualizar
        titulo: Título de la visualización
        filename: Nombre del archivo para guardar (sin extension)
    """
    vertices = grafo.obtener_vertices()
    aristas = grafo.obtener_aristas()
    
    if not vertices:
        print("El grafo está vacío")
        return
    
    # Crear figura
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # Calcular posiciones
    posiciones = calcular_posiciones_circulares(vertices)
    
    # Dibujar aristas
    for v1, v2, peso in aristas:
        x1, y1 = posiciones[v1]
        x2, y2 = posiciones[v2]
        
        if grafo.dirigido:
            # Dibujar flecha para grafo dirigido
            dx = x2 - x1
            dy = y2 - y1
            
            # Ajustar el inicio y final de la flecha para que no toque los círculos
            radio_nodo = 0.15
            distancia = (dx**2 + dy**2)**0.5
            
            if distancia > 0:
                dx_norm = dx / distancia
                dy_norm = dy / distancia
                
                x1_adj = x1 + dx_norm * radio_nodo
                y1_adj = y1 + dy_norm * radio_nodo
                x2_adj = x2 - dx_norm * radio_nodo
                y2_adj = y2 - dy_norm * radio_nodo
            else:
                x1_adj, y1_adj, x2_adj, y2_adj = x1, y1, x2, y2
            
            arrow = FancyArrowPatch(
                (x1_adj, y1_adj), (x2_adj, y2_adj),
                arrowstyle='->', mutation_scale=20, 
                linewidth=2, color='#2E7D32', zorder=2
            )
            ax.add_patch(arrow)
        else:
            # Dibujar línea para grafo no dirigido
            ax.plot([x1, x2], [y1, y2], 'b-', linewidth=2, zorder=1)
        
        # Dibujar el peso en la mitad de la línea
        if peso != 1:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mx, my, str(peso), fontsize=10, ha='center', 
                   bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    # Dibujar vértices
    for vertice, (x, y) in posiciones.items():
        circle = plt.Circle((x, y), 0.15, color='#1976D2', zorder=3, ec='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, str(vertice), ha='center', va='center', 
               fontsize=12, fontweight='bold', color='white', zorder=4)
    
    # Configurar ejes
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Título
    tipo = "Dirigido" if grafo.dirigido else "No Dirigido"
    ax.set_title(f"{titulo}\n({tipo})", fontsize=14, fontweight='bold', pad=20)
    
    # Información del grafo
    info_text = f"Vértices: {len(vertices)} | Aristas: {len(aristas)} | Conexo: {grafo.es_conexo()}"
    ax.text(0, -1.35, info_text, ha='center', fontsize=10, 
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))
    
    plt.tight_layout()
    
    # Guardar y mostrar
    if filename:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, f'{filename}.png')
        plt.savefig(filepath, dpi=150, bbox_inches='tight')
        print(f"✓ Visualización guardada en: {filename}.png")
    
    plt.show()


def visualizar_grafo_graphviz(grafo, titulo: str = "Grafo", filename: str = None):
    """
    Visualiza un grafo usando Graphviz
    
    Args:
        grafo: Objeto Grafo a visualizar
        titulo: Título de la visualización
        filename: Nombre del archivo para guardar
    """
    vertices = grafo.obtener_vertices()
    aristas = grafo.obtener_aristas()
    
    if not vertices:
        print("El grafo está vacío")
        return
    
    # Crear gráfico Graphviz
    if grafo.dirigido:
        g = graphviz.Digraph(comment=titulo, format='png')
    else:
        g = graphviz.Graph(comment=titulo, format='png')
    
    # Configurar atributos
    g.attr(rankdir='LR', size='8,6')
    g.attr('node', shape='circle', style='filled', fillcolor='#1976D2', 
           fontcolor='white', fontsize='12', fontname='Arial', width='0.8', height='0.8')
    
    # Agregar nodos
    for vertice in vertices:
        g.node(str(vertice), str(vertice))
    
    # Agregar aristas
    for v1, v2, peso in aristas:
        if peso != 1:
            label = str(peso)
        else:
            label = ''
        
        if grafo.dirigido:
            g.edge(str(v1), str(v2), label=label, color='#2E7D32')
        else:
            g.edge(str(v1), str(v2), label=label, color='#2E7D32')
    
    # Guardar y mostrar
    if filename:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, filename)
        g.render(filepath, cleanup=True)
        print(f"✓ Visualización Graphviz guardada en: {filename}.png")
    else:
        g.render('temp_graph', view=True, cleanup=True)


# ============================================================================
# FUNCIONES DE DEMOSTRACIÓN
# ============================================================================

def demo_grafo_numeros():
    """Demuestra un grafo con números"""
    print("\n" + "="*70)
    print("DEMO 1: GRAFO NO DIRIGIDO CON NÚMEROS")
    print("="*70)
    
    grafo = GrafoNoDirigido()
    
    # Agregar vértices y aristas
    aristas = [
        (1, 2, 4), (1, 3, 2), (2, 3, 1), (2, 4, 5),
        (3, 4, 8), (3, 5, 10), (4, 5, 2), (4, 6, 3)
    ]
    
    for v1, v2, peso in aristas:
        grafo.agregar_arista(v1, v2, peso)
    
    grafo.mostrar_grafo()
    
    # Operaciones
    print("DFS desde 1:", grafo.dfs('1'))
    print("BFS desde 1:", grafo.bfs('1'))
    print("Camino más corto de 1 a 6:", grafo.obtener_camino('1', '6'))
    print("Componentes conexas:", grafo.componentes_conexas())
    
    # Visualizar
    visualizar_grafo_matplotlib(grafo, "Grafo No Dirigido con Números", 
                               "grafo_numeros_matplotlib")
    visualizar_grafo_graphviz(grafo, "Grafo No Dirigido con Números", 
                             "grafo_numeros_graphviz")


def demo_grafo_letras():
    """Demuestra un grafo con letras"""
    print("\n" + "="*70)
    print("DEMO 2: GRAFO DIRIGIDO CON LETRAS")
    print("="*70)
    
    grafo = GrafoDirigido()
    
    # Construir un grafo tipo red social
    aristas = [
        ('A', 'B', 1), ('A', 'C', 1), ('B', 'D', 1),
        ('C', 'D', 1), ('D', 'E', 1), ('C', 'E', 1),
        ('E', 'F', 1), ('F', 'G', 1), ('D', 'G', 1)
    ]
    
    for v1, v2, peso in aristas:
        grafo.agregar_arista(v1, v2, peso)
    
    grafo.mostrar_grafo()
    
    # Operaciones
    print("DFS desde A:", grafo.dfs('A'))
    print("BFS desde A:", grafo.bfs('A'))
    print("Dijkstra desde A:", grafo.dijkstra('A'))
    print("Camino más corto de A a G:", grafo.obtener_camino('A', 'G'))
    
    # Visualizar
    visualizar_grafo_matplotlib(grafo, "Grafo Dirigido con Letras", 
                               "grafo_letras_matplotlib")
    visualizar_grafo_graphviz(grafo, "Grafo Dirigido con Letras", 
                             "grafo_letras_graphviz")


def demo_grafo_ciudades():
    """Demuestra un grafo con ciudades (nombres)"""
    print("\n" + "="*70)
    print("DEMO 3: GRAFO CON CIUDADES (RED DE TRANSPORTE)")
    print("="*70)
    
    grafo = GrafoNoDirigido()
    
    # Red de ciudades con distancias
    ciudades_aristas = [
        ("Madrid", "Barcelona", 620),
        ("Madrid", "Valencia", 360),
        ("Madrid", "Sevilla", 540),
        ("Barcelona", "Valencia", 480),
        ("Valencia", "Sevilla", 700),
        ("Sevilla", "Málaga", 250),
        ("Madrid", "Bilbao", 400),
        ("Bilbao", "Barcelona", 650),
    ]
    
    for ciudad1, ciudad2, distancia in ciudades_aristas:
        grafo.agregar_arista(ciudad1, ciudad2, distancia)
    
    grafo.mostrar_grafo()
    
    # Operaciones
    print("BFS desde Madrid:", grafo.bfs("Madrid"))
    print("Camino más corto Madrid -> Málaga:", grafo.obtener_camino("Madrid", "Málaga"))
    
    # Dijkstra
    dijkstra_result = grafo.dijkstra("Madrid")
    print("\nDistancias desde Madrid:")
    for ciudad, (distancia, _) in sorted(dijkstra_result.items()):
        if distancia != float('inf'):
            print(f"  → {ciudad}: {distancia} km")
    
    # Visualizar
    visualizar_grafo_matplotlib(grafo, "Red de Transporte - Ciudades", 
                               "grafo_ciudades_matplotlib")
    visualizar_grafo_graphviz(grafo, "Red de Transporte - Ciudades", 
                             "grafo_ciudades_graphviz")


def demo_grafo_desconexo():
    """Demuestra un grafo no conexo"""
    print("\n" + "="*70)
    print("DEMO 4: GRAFO NO CONEXO (MÚLTIPLES COMPONENTES)")
    print("="*70)
    
    grafo = GrafoNoDirigido()
    
    # Componente 1
    aristas_c1 = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    for v1, v2 in aristas_c1:
        grafo.agregar_arista(v1, v2)
    
    # Componente 2
    aristas_c2 = [('D', 'E'), ('E', 'F'), ('F', 'D')]
    for v1, v2 in aristas_c2:
        grafo.agregar_arista(v1, v2)
    
    # Componente aislada
    grafo.agregar_vertice('G')
    
    grafo.mostrar_grafo()
    
    # Operaciones
    print("DFS desde A:", grafo.dfs('A'))
    print("DFS desde D:", grafo.dfs('D'))
    print("Componentes conexas:", grafo.componentes_conexas())
    
    # Visualizar
    visualizar_grafo_matplotlib(grafo, "Grafo No Conexo (Componentes Desconectadas)", 
                               "grafo_desconexo_matplotlib")
    visualizar_grafo_graphviz(grafo, "Grafo No Conexo", 
                             "grafo_desconexo_graphviz")


def demo_operaciones_basicas():
    """Demuestra operaciones básicas con un grafo"""
    print("\n" + "="*70)
    print("DEMO 5: OPERACIONES BÁSICAS")
    print("="*70)
    
    grafo = GrafoDirigido()
    
    print("\n1. Agregar vértices y aristas:")
    for i in range(1, 5):
        grafo.agregar_vertice(i)
        print(f"   ✓ Vértice {i} agregado")
    
    aristas = [(1, 2), (2, 3), (3, 4), (1, 4), (2, 4)]
    for v1, v2 in aristas:
        grafo.agregar_arista(v1, v2)
        print(f"   ✓ Arista {v1} → {v2} agregada")
    
    grafo.mostrar_grafo()
    
    print("\n2. Eliminar una arista:")
    print(f"   Eliminando arista 1 → 4")
    grafo.eliminar_arista(1, 4)
    grafo.mostrar_grafo()
    
    print("\n3. Eliminar un vértice:")
    print(f"   Eliminando vértice 3")
    grafo.eliminar_vertice(3)
    grafo.mostrar_grafo()
    
    print("   Recorridos:")
    print(f"   DFS desde 1: {grafo.dfs(1)}")
    print(f"   BFS desde 1: {grafo.bfs(1)}")


# ============================================================================
# MENÚ PRINCIPAL
# ============================================================================

def menu_principal():
    """Menú interactivo principal"""
    while True:
        print("\n" + "="*70)
        print("ANÁLISIS DE ESTRUCTURAS DE DATOS: GRAFOS")
        print("="*70)
        print("\n1. Grafo No Dirigido con Números")
        print("2. Grafo Dirigido con Letras")
        print("3. Grafo con Ciudades (Red de Transporte)")
        print("4. Grafo No Conexo (Múltiples Componentes)")
        print("5. Operaciones Básicas")
        print("6. Ejecutar Todas las Demostraciones")
        print("0. Salir")
        
        opcion = input("\nSelecciona una opción (0-6): ").strip()
        
        if opcion == '1':
            demo_grafo_numeros()
        elif opcion == '2':
            demo_grafo_letras()
        elif opcion == '3':
            demo_grafo_ciudades()
        elif opcion == '4':
            demo_grafo_desconexo()
        elif opcion == '5':
            demo_operaciones_basicas()
        elif opcion == '6':
            print("\nEjecutando todas las demostraciones...\n")
            demo_grafo_numeros()
            input("\nPresiona Enter para continuar...")
            demo_grafo_letras()
            input("\nPresiona Enter para continuar...")
            demo_grafo_ciudades()
            input("\nPresiona Enter para continuar...")
            demo_grafo_desconexo()
            input("\nPresiona Enter para continuar...")
            demo_operaciones_basicas()
        elif opcion == '0':
            print("\n¡Hasta luego!")
            break
        else:
            print("\n❌ Opción inválida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    # Ejecutar menú
    menu_principal()
