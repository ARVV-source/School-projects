"""
Estructura de Datos: Grafos
Implementación de grafos dirigidos y no dirigidos con operaciones comunes
"""

from typing import List, Dict, Set, Tuple, Optional
from collections import deque
import heapq


class Nodo:
    """Representa un nodo/vértice en el grafo"""
    
    def __init__(self, valor):
        """
        Inicializa un nodo
        
        Args:
            valor: Identificador del nodo (número, letra o string)
        """
        self.valor = valor
        self.adyacentes: Dict = {}  # {nodo_destino: peso}
        self.visitado = False
    
    def agregar_vecino(self, nodo: 'Nodo', peso: int = 1):
        """Agrega un nodo vecino con su peso"""
        self.adyacentes[nodo] = peso
    
    def obtener_vecinos(self) -> List['Nodo']:
        """Retorna lista de nodos adyacentes"""
        return list(self.adyacentes.keys())
    
    def obtener_peso(self, nodo: 'Nodo') -> int:
        """Retorna el peso de la arista hacia un nodo"""
        return self.adyacentes.get(nodo, float('inf'))
    
    def __repr__(self):
        return f"Nodo({self.valor})"
    
    def __hash__(self):
        return hash(self.valor)
    
    def __eq__(self, other):
        if isinstance(other, Nodo):
            return self.valor == other.valor
        return False


class Grafo:
    """Clase base para representar un grafo"""
    
    def __init__(self, dirigido: bool = False):
        """
        Inicializa un grafo
        
        Args:
            dirigido: Si True, es grafo dirigido; si False, no dirigido
        """
        self.nodos: Dict = {}  # {valor: Nodo}
        self.dirigido = dirigido
    
    def agregar_vertice(self, valor):
        """Agrega un vértice (nodo) al grafo"""
        if valor not in self.nodos:
            self.nodos[valor] = Nodo(valor)
            return True
        return False
    
    def eliminar_vertice(self, valor):
        """Elimina un vértice del grafo"""
        if valor not in self.nodos:
            return False
        
        nodo = self.nodos[valor]
        
        # Eliminar aristas asociadas
        for otro in self.nodos.values():
            if nodo in otro.adyacentes:
                del otro.adyacentes[nodo]
            if not self.dirigido and otro.valor != valor and otro in nodo.adyacentes:
                del nodo.adyacentes[otro]
        
        del self.nodos[valor]
        return True
    
    def agregar_arista(self, valor1, valor2, peso: int = 1):
        """
        Agrega una arista entre dos vértices
        
        Args:
            valor1: Valor del primer vértice
            valor2: Valor del segundo vértice
            peso: Peso de la arista (por defecto 1)
        """
        # Crear vértices si no existen
        self.agregar_vertice(valor1)
        self.agregar_vertice(valor2)
        
        nodo1 = self.nodos[valor1]
        nodo2 = self.nodos[valor2]
        
        # Agregar arista
        nodo1.agregar_vecino(nodo2, peso)
        
        # Si no es dirigido, agregar también la inversa
        if not self.dirigido:
            nodo2.agregar_vecino(nodo1, peso)
    
    def eliminar_arista(self, valor1, valor2):
        """Elimina una arista entre dos vértices"""
        if valor1 not in self.nodos or valor2 not in self.nodos:
            return False
        
        nodo1 = self.nodos[valor1]
        nodo2 = self.nodos[valor2]
        
        if nodo2 not in nodo1.adyacentes:
            return False
        
        del nodo1.adyacentes[nodo2]
        
        if not self.dirigido and nodo1 in nodo2.adyacentes:
            del nodo2.adyacentes[nodo1]
        
        return True
    
    def limpiar_visitas(self):
        """Limpia el estado visitado de todos los nodos"""
        for nodo in self.nodos.values():
            nodo.visitado = False
    
    def obtener_vertices(self) -> List:
        """Retorna lista de valores de vértices"""
        return list(self.nodos.keys())
    
    def obtener_aristas(self) -> List[Tuple]:
        """Retorna lista de aristas (tuplas)"""
        aristas = []
        visitadas = set()
        
        for valor, nodo in self.nodos.items():
            for vecino, peso in nodo.adyacentes.items():
                if self.dirigido:
                    aristas.append((valor, vecino.valor, peso))
                else:
                    # Evitar duplicados en grafos no dirigidos
                    arista = (min(valor, vecino.valor), max(valor, vecino.valor), peso)
                    if arista not in visitadas:
                        aristas.append((valor, vecino.valor, peso))
                        visitadas.add(arista)
        
        return aristas
    
    def dfs(self, inicio: str, visitados: Set = None) -> List:
        """
        Recorrido Depth-First Search (DFS)
        
        Args:
            inicio: Valor del nodo inicial
            
        Returns:
            Lista de valores en orden DFS
        """
        if visitados is None:
            visitados = set()
            self.limpiar_visitas()
        
        if inicio not in self.nodos:
            return []
        
        resultado = [inicio]
        visitados.add(inicio)
        nodo = self.nodos[inicio]
        
        for vecino in nodo.obtener_vecinos():
            if vecino.valor not in visitados:
                resultado.extend(self.dfs(vecino.valor, visitados))
        
        return resultado
    
    def bfs(self, inicio: str) -> List:
        """
        Recorrido Breadth-First Search (BFS)
        
        Args:
            inicio: Valor del nodo inicial
            
        Returns:
            Lista de valores en orden BFS
        """
        if inicio not in self.nodos:
            return []
        
        self.limpiar_visitas()
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)
        resultado = []
        
        while cola:
            nodo_actual = cola.popleft()
            resultado.append(nodo_actual)
            
            for vecino in self.nodos[nodo_actual].obtener_vecinos():
                if vecino.valor not in visitados:
                    visitados.add(vecino.valor)
                    cola.append(vecino.valor)
        
        return resultado
    
    def dijkstra(self, inicio: str) -> Dict[str, Tuple[int, Optional[str]]]:
        """
        Algoritmo de Dijkstra para encontrar camino más corto
        
        Args:
            inicio: Valor del nodo inicial
            
        Returns:
            Diccionario {destino: (distancia, predecesor)}
        """
        if inicio not in self.nodos:
            return {}
        
        distancias = {valor: float('inf') for valor in self.nodos}
        distancias[inicio] = 0
        predecesores = {valor: None for valor in self.nodos}
        
        # Cola de prioridad (distancia, valor)
        cola = [(0, inicio)]
        visitados = set()
        
        while cola:
            dist_actual, nodo_actual = heapq.heappop(cola)
            
            if nodo_actual in visitados:
                continue
            
            visitados.add(nodo_actual)
            
            if dist_actual > distancias[nodo_actual]:
                continue
            
            nodo = self.nodos[nodo_actual]
            for vecino in nodo.obtener_vecinos():
                peso = nodo.obtener_peso(vecino)
                nueva_dist = dist_actual + peso
                
                if nueva_dist < distancias[vecino.valor]:
                    distancias[vecino.valor] = nueva_dist
                    predecesores[vecino.valor] = nodo_actual
                    heapq.heappush(cola, (nueva_dist, vecino.valor))
        
        # Retornar resultado en el formato (distancia, predecesor)
        return {destino: (distancias[destino], predecesores[destino]) 
                for destino in self.nodos}
    
    def obtener_camino(self, inicio: str, fin: str) -> List[str]:
        """
        Obtiene el camino más corto entre dos nodos usando Dijkstra
        
        Args:
            inicio: Nodo inicial
            fin: Nodo destino
            
        Returns:
            Lista representando el camino
        """
        if inicio not in self.nodos or fin not in self.nodos:
            return []
        
        resultado_dijkstra = self.dijkstra(inicio)
        camino = []
        nodo_actual = fin
        
        while nodo_actual is not None:
            camino.append(nodo_actual)
            nodo_actual = resultado_dijkstra[nodo_actual][1]
        
        camino.reverse()
        
        # Verificar si hay camino válido
        if camino[0] == inicio:
            return camino
        return []
    
    def componentes_conexas(self) -> List[Set]:
        """
        Encuentra todas las componentes conexas del grafo
        
        Returns:
            Lista de sets, cada one contiene los valores de una componente conexa
        """
        self.limpiar_visitas()
        componentes = []
        visitados = set()
        
        for valor in self.nodos:
            if valor not in visitados:
                componente = set(self.dfs(valor))
                componentes.append(componente)
                visitados.update(componente)
        
        return componentes
    
    def es_conexo(self) -> bool:
        """Verifica si el grafo es conexo"""
        if not self.nodos:
            return True
        
        componentes = self.componentes_conexas()
        return len(componentes) == 1
    
    def mostrar_grafo(self):
        """Muestra la representación del grafo en consola"""
        print(f"\n{'='*50}")
        print(f"GRAFO {'DIRIGIDO' if self.dirigido else 'NO DIRIGIDO'}")
        print(f"{'='*50}")
        print(f"Vértices: {self.obtener_vertices()}")
        print(f"Total de vértices: {len(self.nodos)}")
        print(f"\nAristas:")
        for v1, v2, peso in self.obtener_aristas():
            if self.dirigido:
                print(f"  {v1} → {v2} (peso: {peso})")
            else:
                print(f"  {v1} -- {v2} (peso: {peso})")
        print(f"Total de aristas: {len(self.obtener_aristas())}")
        print(f"¿Es conexo?: {self.es_conexo()}")
        print(f"{'='*50}\n")


class GrafoDirigido(Grafo):
    """Grafo dirigido (aristas con dirección)"""
    
    def __init__(self):
        """Inicializa un grafo dirigido"""
        super().__init__(dirigido=True)


class GrafoNoDirigido(Grafo):
    """Grafo no dirigido (aristas bidireccionales)"""
    
    def __init__(self):
        """Inicializa un grafo no dirigido"""
        super().__init__(dirigido=False)
