import csv
import os
from datetime import date


class Nodo:
    """Nodo para el árbol AVL"""
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class ArbolAVL:
    """Árbol AVL balanceado"""
    
    def __init__(self):
        self.raiz = None
    
    def obtener_altura(self, nodo):
        """Obtiene la altura de un nodo"""
        if nodo is None:
            return 0
        return nodo.altura
    
    def obtener_balance(self, nodo):
        """Obtiene el factor de balance de un nodo"""
        if nodo is None:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)
    
    def actualizar_altura(self, nodo):
        """Actualiza la altura de un nodo"""
        if nodo is not None:
            nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda),
                                  self.obtener_altura(nodo.derecha))
    
    def rotacion_derecha(self, nodo):
        """Rotación a la derecha"""
        izq = nodo.izquierda
        nodo.izquierda = izq.derecha
        izq.derecha = nodo
        self.actualizar_altura(nodo)
        self.actualizar_altura(izq)
        return izq
    
    def rotacion_izquierda(self, nodo):
        """Rotación a la izquierda"""
        der = nodo.derecha
        nodo.derecha = der.izquierda
        der.izquierda = nodo
        self.actualizar_altura(nodo)
        self.actualizar_altura(der)
        return der
    
    def insertar(self, valor):
        """Inserta un valor en el árbol manteniendo balance"""
        self.raiz = self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        """Inserción recursiva con balanceo"""
        if nodo is None:
            return Nodo(valor)
        
        if valor < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)
        else:
            return nodo
        
        self.actualizar_altura(nodo)
        
        # Obtener factor de balance
        balance = self.obtener_balance(nodo)
        
        # Caso Izquierda-Izquierda
        if balance > 1 and valor < nodo.izquierda.valor:
            return self.rotacion_derecha(nodo)
        
        # Caso Derecha-Derecha
        if balance < -1 and valor > nodo.derecha.valor:
            return self.rotacion_izquierda(nodo)
        
        # Caso Izquierda-Derecha
        if balance > 1 and valor > nodo.izquierda.valor:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)
        
        # Caso Derecha-Izquierda
        if balance < -1 and valor < nodo.derecha.valor:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)
        
        return nodo
    
    def recorrido_inorden(self):
        """Recorrido en orden del árbol"""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        """Recorrido inorden recursivo"""
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, resultado)
    
    def mostrar_arbol(self):
        """Muestra el árbol de forma visual"""
        self._mostrar_recursivo(self.raiz, "", True)
    
    def _mostrar_recursivo(self, nodo, prefijo, es_ultimo):
        """Muestra el árbol de forma recursiva"""
        if nodo is not None:
            print(prefijo + ("└── " if es_ultimo else "├── ") + str(nodo.valor))
            hijos = []
            if nodo.izquierda is not None:
                hijos.append((nodo.izquierda, False))
            if nodo.derecha is not None:
                hijos.append((nodo.derecha, True))
            
            for i, (hijo, es_ultimo_hijo) in enumerate(hijos):
                es_ultimo_actual = i == len(hijos) - 1
                extension = "    " if es_ultimo else "│   "
                self._mostrar_recursivo(hijo, prefijo + extension, es_ultimo_actual)

