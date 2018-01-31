

	
import numpy as np
	
class Variable:
	def __init__(self,data):
		self.data=np.array(data)
	def representante(self):
		pass
class Ingresos(Variable):
	def representante(self):
		return np.mean(self.data)
class Comuna(Variable):
	def representante(self):
		ind=np.argmax([np.sum(self.data == c) for c in self.data])
		return self.data[ind]
class Puesto(Variable):
	categorias = {'Gerente': 1, 'SubGerente': 2, 'Analista': 3, 'Alumno en Practica': 4} 
	def representante(self):
		return self.data[np.argmin([Puesto.categorias[c] for c in self.data])]
		
def run():
	lista_pesos = Ingresos([50, 80, 90, 150, 45, 65, 78, 89, 59, 77, 90])
	lista_comunas = Comuna(['Providencia', 'Macul' , 'LaReina' ,'Santiago', 'Providencia', 'PuenteAlto', 'Macul', 'Santiago', 'Santiago' ])
	lista_puestos = Puesto(['SubGerente', 'Analista','SubGerente','Analista','Alumno en Practica','Alumno en Practica'])
	print(lista_pesos.representante())
	print(lista_comunas.representante())
	print(lista_puestos.representante())
	
#Representante se sobreescribe para cada clase,
#ingresos tiene promedio, comuna indica max count y puesto ...?

class Carro():
	def __init__(self, lista_productos):
		self.lista_productos=lista_productos
	def __add__(self, otro_carro):
		lista_sumada = self.lista_productos
		for p in otro_carro.lista_productos.keys():
			if p in self.lista_productos.keys():
				lista_sumada.update({p:otro_carro.lista_productos[p] +self.lista_productos[p]})
			else:
				lista_sumada.update({p:otro_carro.lista_productos[p]})
		return Carro(lista_sumada)
	def __repr__(self):
		s=self.__doc__
		return s+"\n"+"\n".join("Producto: {} | Cantidad: {}".format(p, self.lista_productos[p]) for p in self.lista_productos.keys())
	#def __str__(self):
	#	return "\n".join("Producto: {} - Cantidad: {}".format(p, self.lista_productos[p]) for p in self.lista_productos.keys())
#if __str_ is commented, then __repr__ is printed, str>repr
	

def runCarro():
	carro_1 = Carro({'pan' : 3, 'leche' : 2, 'agua' : 6})
	carro_2 = Carro({'leche' : 5, 'bebida' : 2, 'cerveza' : 12})
	carro_3 = carro_1 + carro_2
	print(carro_3.lista_productos)
	print()
	print(carro_3)
	
class Punto():
	def __init__(self, x, y):
		self.x=x
		self.y=y 
	def __lt__(self, otro_punto):
		self_mag = (self.x**2)+(self.y**2)
		otro_punto_mag = (otro_punto.x**2)+(otro_punto.y**2)
		return self_mag<otro_punto_mag

def runPunto():
	p1 = Punto(2,4)
	p2= Punto(8,3)
	print(p1<p2)
	
class Pato:
	def gritar(self):
		print("Quack!")
	def caminar(self):
		print("walking like a duck")
class Persona:
	def gritar(self):
		print("Aaaaaah!")
	def caminar(self):
		print("walking like a dude")

def activar(x):
	x.gritar()
	x.caminar()

def runDucking():	
	donald=Pato()
	john=Persona()
	activar(donald)
	activar(john)
	
# class Base:
	# def func_1(self):
		# raise NotImplementedError()
	# def func_2(self):
		# raise NotImplementedError()
# class SubClase(Base):
	# def func_1(self):
		# print("func_1() called...")
		# return

# def runBase():		
	# b1 = Base()
	# b2 = SubClase()
	# b2.func_1()
	# b2.func_2()
#Base is an example that Python with it's Abstract Base Classes,
# it doesn't allow to have an incomplete subclass	

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
	@abstractmethod
	def func_1(self):
		pass
	@abstractmethod
	def func_2(self):
		pass
class SubClase(Base):
	def func_1(self):
		pass
	def func_2(self):
		pass

c= SubClase()
print("Es subclase: {}".format(issubclass(SubClase, Base)))
print("Es instancia: {}".format(isinstance(SubClase(), Base)))

from abc import abstractproperty

class Baset(metaclass=ABCMeta):
	@abstractproperty
	def value(self):
		return "nunca deberiamos llegar aqui"
class Implementation(Baset):
	@property
	def value(self):
		return "propiedad concreta"
try:
	b=Baset()
	print("Baset.value: {}".fromat(b.value))
except Exception as err:
	print("Error: {}".format(str(err)))
i = Implementation()
print("Implementation.value:  {}".format(i.value))

class Palin():
	def reverse(text):
		return text[::-1] #-1 will return text in reverse
	def is_palindrome(text):
		return text == Palin.reverse(text)

def runPalin():
	something = input("Enter text:")
	if (Palin.is_palindrome(something)):
		print("Es palindrome")
	else:
		print("Not palindrome")

def runPoem():
	poem='''\Roses are red, violets are... fuck it.'''
	f=open('poem.txt', 'w') #"w"riting
	f.write(poem)
	f.close()
	
	f=open("poem.txt") #without specifying, it's only read
	#by default
	while True:
		line = f.readline()
		if len(line)==0:
			break
		print(line, end=" ")
	f.close()
#doesn't work, needs permissions to create poem.txt?


#Persistent storing of object (Pickle)

import pickle
def pickleTime():
	shoplistfile='shoplist.data'
	shoplist=["apple", "mango", "carrot"]
	
	f=open(shoplistfile, 'wb')
	pickle.dump(shoplist, f)
	f.close()
	
	del shoplist #must delete in order not to have memory leak
#doesn't work, needs permissions to create shoplist.data?	

def runExcep():
	try:
		text=input("enter something:")
	except EOFError:
		print("Why did you do an EO on me?")
	except KeyboardInterrupt:
		print("You cancelled the operation")
	else:
		print("you entered {}".format(text))

#creating an exception self, length, atleast		
class ShortInputException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length=length
		self.atleast=atleast
	
def runShInputEx():
	try:	
		text= input("Enter something --> ")
		if len(text)<3:
			raise ShortInputException(len(text), 3)
	except EOFError:
		print("why did you do an EO on me?")
	except ShortInputException as ex:
		print("ShortInputException: the input was {0} digits long, expected at least {1}"\
																				  .format(ex.length, ex.atleast))
	else:
		print("No exception was raised.")

import time		
def tryIt():
	try:
		f=open("poem.txt")
		while True:
			line= f.readLine()
			if len(line)==0:
				break	
			print(line, end=" ")
			time.sleep(2)
	except KeyboardInterrupt:
		print("You canceled the reading from the file")
	finally:
		f.close()
		print("Cleaning up: Closed the file")
#can't make it to work due to poem.txt


			
		
