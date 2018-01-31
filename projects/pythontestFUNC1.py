from collections import defaultdict
class MyLista(list):
	def __len__(self):
		d=defaultdict(int)
		for i in range(list.__len__(self)):
			d.update({self[i]:d[self[i]]+1})
		return len(d)
		
class MyLista2(list):
	def __len__(self):
		d=defaultdict(int)
		for i in self:
			d.update({i: d[i] + 1})
		return len(d)
		
class MyLista3(list):
	def __len__(self):
		d = set(self)
		return len(d)
		
def runListas():
	L=MyLista([1,2,3,4,5,6,6,7,7,7,7,2,2,3,3,1,1])
	print(len(L))
	L=MyLista2([1,2,3,4,5,6,6,7,7,7,7,2,2,3,3,1,1])
	print(len(L))
	L=MyLista3([1,2,3,4,5,6,6,7,7,7,7,2,2,3,3,1,1])
	print(len(L))

# __getItem__
class MiClase:
	def __init__(self, palabra=None):
		self.palabra= palabra
	def __getitem__(self, i):
		return self.palabra[i]
def runClase():
	p = MiClase("Heeeeey")
	print(p[0])
	[print(c) for c in p]
	(a,b,c,d)=p[0:4]
	print(a,b,c,d)
	print(list(p))
	print(tuple(p))
	
class MiSecuencia:
	def __len__(self):
		return 9
	def __getitem__(self, index):
		return "Item_{0}".format(index)
class MiReversa:
	def __reversed__(self):
		return "Reversing!!"
	
def seqRev():
	lista = [1,2,3,4,5,6]
	for seq in lista, MiSecuencia(), MiReversa():
		print("\n{}: ".format(seq.__class__.__name__),end = "")
		for item in reversed(seq):
			print(item, end=", ")
			
def runEnum():
	lista=["a","b","c","d"]
	for i,j in enumerate(lista):
		print("{}: {}".format(i,j))
	print([par for par in enumerate(lista)])
	print({i:j for i, j in enumerate(lista)})

	
def zipIt():
	variables=["nombre", "apellido", "email"]
	p1=["Juan", "Perez", "jp1@hotmail.com"]
	p2 = ["Gonzalo", 'Aldunate', 'gan@gmail.com']
	p3 = ["Alberto", 'Gomez', 'agomez@yahoo.com']
	contactos=[]
	for p in p1, p2, p3:
		contacto=zip(variables, p)
		contactos.append(dict(contacto))
	for c in contactos:
		print("Nombre: {nombre} {apellido}, email: {email}".format(**c))
#  El doble asterisco es para pasar el diccionario c como "keyworded" argumentos
# es equivalente a .format(nombre = c["nombre"], apellido = c["apellido"], 
# email = c["email"]
	print(list(zip(variables, p1, p2, p3)))
	
def zipIt2():
	A=[1,2,3,4]
	B=["a","b","c","d"]
	zipped=zip(A,B)
	zipped=list(zipped)
	print(zipped)
	unzipped =zip(*zipped)
	unzipped=list(unzipped)
	print(unzipped)
	
def listaXComp():
	lista=['1', '4', '55', '65', '4', '15', '90']
	int_lista=[int(c) for c in lista]
	print(int_lista)
	int_lista_2d=[int(c) for c in lista if len(c) >1]#lista segun condicion
	print(int_lista_2d)
	
from collections import namedtuple
def movies():
	Pelicula= namedtuple("Pelicula", ["titulo", "director", "genero"])
	peliculas=[Pelicula("Into the woods", "Rob Marshall", "Adventura"), Pelicula("American Sniper", "Clint Eastwood", "Accion"), Pelicula("Taken 3", "Olivier Megaton", "Accion")]
	directores_accion= {b.director for b in peliculas if b.genero == 'Accion'}
# ^ set comprehension
	print(directores_accion)
	dict_directores_accion={b.director: b for b in peliculas if b.genero=='Accion'}
# b.director:b does a dictionary with data
	print(dict_directores_accion)
	dict_directores_accion['Olivier Megaton']

# Iterables e Iteradores
def iterable():
	x=[11,32, 43]
	for c in x: print(c)
	print(x.__iter__)
	#next(x) da error, donde list obj is not an iterator
	y=iter(x)
	print(next(y))
	print(next(y))
	print(next(y))
	
class Carta:
	MONOS= {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
	def __init__(self, numero, pinta):
		self.pinta =pinta
		self.numero = numero if numero <=10 else Carta.MONOS[numero]
	def __str__(self):
		return "%s %s" % (self.numero, self.pinta)
class Baraja:
	def __init__(self):
		self.cartas=[Carta(n,p) for p in ['Espada', 'Diamante', 'Corazon', 'Trebol'] for n in range(2, 15)]

def runBaraja():
	for c in Baraja().cartas: print(c)

class Fib:
	def __init__(self):
		self.prev=0
		self.actual=1
	def __iter__(self):
		return self
	def __next__(self):
		valor=self.actual
		self.actual+=self.prev
		self.prev=valor
		return valor

def fibIt():
	f=Fib()
	N=10
	l=[next(f) for i in range(N)]
	print(l)

import itertools
def runitertool():
	letras = ['a', 'b', 'c', 'd', 'e', 'f']
	bools = [1, 0, 1, 0, 0, 1]
	nums = [23, 20, 44, 32, 7, 12]
	decimales = [0.1, 0.7, 0.4, 0.4, 0.5]
	colors=itertools.cycle(letras)
	print(next(colors))
	print(next(colors))
	print(next(colors))
	print(next(colors))
	print(next(colors))
	print(next(colors))
	print(next(colors))
	print(next(colors))
	print(next(colors))
	for i in itertools.chain(letras, bools, decimales): print(i, end=" ")
	print()
	for i in itertools.compress(letras, bools): print(i, end= " ")

from sys import getsizeof	
#Iterar "on the fly", sin ocupar memoria
def runGen():
	a=(b for b in range(10))
	#print(a)
	print(getsizeof(a))
	c = [b for b in range(10)]
	print(getsizeof(c))
	#for b in a: print(b)
	#print(sum(a))
	
def testLog():
	inname, outname= "logs.txt", "logs_out.txt"
	with open(inname) as infile:
		with open(outname, "w") as outfile:
			warnings = (l.replace('WARNING', '') for l in infile if 'WARNING' in l)
			for l in warnings:
				outfile.write(l)
#won't work

def conteo_dec(n):
	print("Contando en forma decreciente desde {}".format(n))
	while n >0:
		yield n 
		n-=1
		
def runConteo():
	x= conteo_dec(10)
	print("{}\n".format(x))
	y=conteo_dec(5)
	print(next(y))
	print(next(y))
	print(next(y))
	print(next(y))
	
