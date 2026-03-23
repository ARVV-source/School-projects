class Nodo:
	def __init__(self, valor):
		self.valor = valor
		self.izq = None
		self.der = None


def insertar(raiz, valor):
	if raiz is None:
		return Nodo(valor)

	if valor < raiz.valor:
		raiz.izq = insertar(raiz.izq, valor)
	elif valor > raiz.valor:
		raiz.der = insertar(raiz.der, valor)

	return raiz


def in_order(raiz):
	if raiz is None:
		return []
	return in_order(raiz.izq) + [raiz.valor] + in_order(raiz.der)


def pre_order(raiz):
	if raiz is None:
		return []
	return [raiz.valor] + pre_order(raiz.izq) + pre_order(raiz.der)


def post_order(raiz):
	if raiz is None:
		return []
	return post_order(raiz.izq) + post_order(raiz.der) + [raiz.valor]



apellidos = "arvizu_gonzalez"
raiz = None

for caracter in apellidos:
	raiz = insertar(raiz, caracter)

print(f"apellidos = {apellidos!r}\n")
print("InOrder:  ", ", ".join(in_order(raiz)))
print("PreOrder: ", ", ".join(pre_order(raiz)))
print("PostOrder:", ", ".join(post_order(raiz)))
