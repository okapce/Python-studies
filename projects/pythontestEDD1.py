import sys, warnings
def versionWar():
	if sys.version_info[0]<3:
		warnings.warn("Pyhton version is lese than 3.0", RuntimeWarning)
	else:
		print("Proceed as normal, version is 3.0 or higher")

import platform, os, logging
def logIt():
	if platform.platform().startswith("Windows"):
		logging_file= os.path.join(os.getenv("HOMEDRIVE"), os.getenv("HOMEDRIVE"), "test.log")
	else:
		logging_file=os.path.join(os.getenv("HOME"), "test.log")
	logging.basicConfig(
		level=logging.DEBUG,
		format='%(asctime)s : %(levelname)s : %(message)s',
		filename=logging_file,
		filemode='w',
		)
	logging.debug("Start of Program")
	logging.info("Doing something")
	logging.warning("Dying now")
###Permission denied

#Lambda is used to create a new function and then return them at runtime		
def make_repeater(n):
	return lambda s: s*n
def lambdaTest():	
	twice=make_repeater(2)
	print(twice('word'))
	print(twice(5))
	
#List comprehension -> new list, from existing one given x conditions.
def listTest():
	listone=[2,3,4]
	listtwo=[2*i for i in listone if i>2]
	print(listone, listtwo)
	

class Arbol: 
	def __init__(self, id_nodo, valor=None, id_padre=None):
		self.id_nodo=id_nodo
		self.id_padre=id_padre
		self.valor=valor
		self.hijos={}  # nodos hijos serán guardados en un diccionario.
	def agregar_nodo(self, id_nodo, valor=None, id_padre=None):
# Cada vez que agregamos un nodo verificamos primero si corresponde 
# al nodo padre donde queremos agregar el nuevo nodo. 
# Si no es el nodo, buscamos recursivamente a través de todos 
# los nodos existentes hasta que encontremos el nodo correspondiente.
		if self.id_nodo==id_padre: # Si el nodo es el nodo padre
			self.hijos.update({id_nodo: Arbol(id_nodo, valor, id_padre)})
		else:
# Si no, recursivamente seguimos buscando en el árbol el nodo padre
			for hijo in self.hijos.values():
				hijo.agregar_nodo(id_nodo, valor, id_padre)
	def obtener_nodo(self, id_nodo):
		if self.id_nodo==id_nodo:
			return self
		else:
# recursivamente obtenemos el nodo siempre y cuando exista la posicion.
			for hijo in self.hijos.values():
				nodo=hijo.obtener_nodo(id_nodo)
				if nodo:
					return nodo
	def __repr__(self):
		def recorrer_arbol(raiz):
			for hijo in raiz.hijos.values():
				self.ret+="id_nodo: {} -> id_padre: {} -> valor: {}\n".format(hijo.id_nodo, hijo.id_padre, hijo.valor)
				recorrer_arbol(hijo)
			return self
		self.ret="RAIZ:\nroot-id: {} -> valor: {} \n\nHIJOS:\n".format(self.id_nodo, self.valor)
		recorrer_arbol(self)
		return self.ret
				
def runArbol():
	T = Arbol(0, 10)
	T.agregar_nodo(1, 8, 0)
	T.agregar_nodo(2, 12, 0)
	T.agregar_nodo(3, 4, 1)
	T.agregar_nodo(4, 9, 1)
	T.agregar_nodo(5, 1, 3)
	T.agregar_nodo(6, 18, 2)
	print(T)
	#nodo=T.obtener_nodo(6)
	print("El id del nodo es {}".format(T.obtener_nodo(3).id_nodo))
	print("El nodo tiene {} hijos".format(len(T.obtener_nodo(3).hijos)))

	
#En esta forma de recorrer el árbol nodo raíz se visita primero, 
# y luego su hijos son recorridos recursivamente.	
class ArbolPreOrder(Arbol):
# Se hereda de la clase original Arbol y se hace override del metodo
# recorrer_arbol
	def __repr__(self):
		def recorrer_arbol(raiz):
			self.ret += "nodo_id: {0}, id_padre: {1} -> valor: {2}\n".format(raiz.id_nodo, raiz.id_padre, raiz.valor)
			for hijo in raiz.hijos.values():
				recorrer_arbol(hijo)
			return self
		self.ret=""
		recorrer_arbol(self)
		return self.ret
		
def runArbolPreOrder():
	T=ArbolPreOrder(0,10)
	T.agregar_nodo(1, 8, 0)
	T.agregar_nodo(2, 12, 0)
	T.agregar_nodo(3, 4, 1)
	T.agregar_nodo(4, 4, 1)
	T.agregar_nodo(5, 1, 3)
	T.agregar_nodo(6, 18, 2)
	print(T)
	
# En esta modalidad de recorrido primero se visita recursivamente 
# los sub-arboles generados por los nodos hijos y finalmente 
# el nodo raíz.
class ArbolPostOrder(Arbol):
		def __repr__(self):
			def recorrer_arbol(raiz):
				for hijo in raiz.hijos.values():
					recorrer_arbol(hijo)
				self.ret+="nodo_id {}, id_padre: {} -> valor: {}\n".format(raiz.id_nodo, raiz.id_padre, raiz.valor)
				return self
			self.ret=""
			recorrer_arbol(self)
			return self.ret

def runArbolPostOrder():
	T = ArbolPostOrder(0, 10)
	T.agregar_nodo(1, 8, 0)
	T.agregar_nodo(2, 12, 0)
	T.agregar_nodo(3, 4, 1)
	T.agregar_nodo(4, 4, 1)
	T.agregar_nodo(5, 1, 3)
	T.agregar_nodo(6, 18, 2)
	print(T)

#Bread-First-Search (BFS), search without iteration, just making list with colas
from collections import deque
class ArbolBFS(Arbol):
	def __repr__(self):
		def recorrer_arbol(raiz):
			Q=deque()
			Q.append(raiz)#cola para almacenar nodos por visitar
			visitados = []#lista para registrar nodos visitados
			while len(Q)>0:
				p=Q.popleft()
				if p.id_nodo not in visitados:
					visitados.append(p.id_nodo)
					self.ret+="nodo_id: {}, id_padre: {} -> valor: {}\n".format(p.id_nodo, p.id_padre, p.valor)
					for hijo in p.hijos.values():
						Q.append(hijo)
			return self
		self.ret=""
		recorrer_arbol(self)
		return self.ret

def runArbolBFS():
	T = ArbolBFS(0, 10)
	T.agregar_nodo(1, 8, 0)
	T.agregar_nodo(2, 12, 0)
	T.agregar_nodo(3, 4, 1)
	T.agregar_nodo(4, 4, 1)
	T.agregar_nodo(5, 1, 3)
	T.agregar_nodo(6, 18, 2)

	print(T)

# Depth First Search consiste en recorrer el árbol por profundidad, siendo primero visitados todos los nodos 
# de más arriba en la jerarquía del árbol.
class ArbolDFS(Arbol):
	def __repr__(self):
		def recorrer_arbol(raiz):
			Q=deque()
			Q.append(raiz)
			visitados=[]
			while len(Q)>0:
				p=Q.pop()
				if p.id_nodo not in visitados:
					visitados.append(p.id_nodo)
					self.ret+="nodo_id: {}, id_padre: {} -> valor: {}\n".format(p.id_nodo, p.id_padre, p.valor)
					for hijo in p.hijos.values():
						Q.append(hijo)
			return self
		self.ret=""
		recorrer_arbol(self)
		return self.ret

def runArbolDFS():
	T = ArbolDFS(0, 10)
	T.agregar_nodo(1, 8, 0)
	T.agregar_nodo(2, 12, 0)
	T.agregar_nodo(3, 4, 1)
	T.agregar_nodo(4, 4, 1)
	T.agregar_nodo(5, 1, 3)
	T.agregar_nodo(6, 18, 2)

	print(T)

# Arbol Binario
class NodoB:
	def __init__(self, valor, padre = None):
		self.valor =valor
		self.padre=padre
		self.hijo_izq=None
		self.hijo_der =None
	def __repr__(self):
		return "padre: {}, valor: {}".format(self.padre, self.valor)

class ArbolBinario:
	def __init__(self, nodo_raiz=None):
		self.nodo_raiz=nodo_raiz
	def agregar_nodo(self, valor):
		if self.nodo_raiz==None:
			self.nodo_raiz=NodoB(valor)
		else:
			temp= self.nodo_raiz
			agregado=False
			while not agregado:
				if valor <=temp.valor:
					if temp.hijo_izq==None:
						temp.hijo_izq=NodoB(valor, temp.valor)
						agregado=True
					else:
						temp=temp.hijo_izq
				else:
					if temp.hijo_der==None:
						temp.hijo_der=NodoB(valor, temp.valor)
						agregado=True
					else:
						temp=temp.hijo_der
	def __repr__(self):
		def recorrer(nodo, lado="r"):
			ret=''
			if nodo !=None:
				ret+='{} -> {}\n'.format(nodo, lado)
				ret+=recorrer(nodo.hijo_izq, "i")
				ret+=recorrer(nodo.hijo_der, "d")
			return ret
		ret = recorrer(self.nodo_raiz)
		return ret
		
def runArbolBinario():
	T = ArbolBinario()
	T.agregar_nodo(4)
	T.agregar_nodo(1)
	T.agregar_nodo(5)
	T.agregar_nodo(3)
	T.agregar_nodo(20)
	print(T)

#Lista Enlazada/Ligada
class Nodo:
	def __init__(self, valor=None):
		self.siguiente = None
		self.valor = valor
		
class ListaLigada:
	def __init__(self):
		self.cola=None
		self.cabeza=None
	def agregar_nodo(self, valor):
		if not self.cabeza:
			self.cabeza = Nodo(valor)
			self.cola =self.cabeza
		else:
			self.cola.siguiente=Nodo(valor)
			self.cola =self.cola.siguiente
	def obtener(self, posicion):
		nodo = self.cabeza
		for i in range(posicion):
			if nodo:
				nodo = nodo.siguiente
		if not nodo:
			return "posicion no encontrada"
		else:
			return nodo.valor
	def __repr__(self):
		rep=''
		nodo_actual= self.cabeza
		while nodo_actual:
			rep+='{} -> '.format(nodo_actual.valor)
			nodo_actual=nodo_actual.siguiente
		return rep

def runListaLig():
	l = ListaLigada()
	l.agregar_nodo(2)
	l.agregar_nodo(4)
	l.agregar_nodo(7)

	print(l.obtener(2))
	print(l.obtener(1))

	print(l)
