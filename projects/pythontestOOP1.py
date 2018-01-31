def firstTest():
	x = 34-23 #comment
	y = "Hello" #comment 2
	z = 3.45
	if z==3.45 or y=="Hello":
		x = x + 1
		y = y + "world"
	print(x) 
	print(y)

	tulip=(1,2,3)
	list=[1,2,3]

def firstLoopTest():
	a=3
	while a <10:
		if a <7:
			a+=1
			print('a is {0}'.format(a))
			print('still in loop')
			continue
		a=a+2
		print('super add, a is {0}'.format(a))
		if a >= 10:
			break
	print('out of loop')

def runTestLoop():
	b=1
	for b in range(10):
		if b <7:
			b+=1
			print('still in loop, b is {0}'.format(b))
			continue
		b=b+2
		print(' b is {0}'.format(b))
		if b>=8:
			break
	print('out of loop')

def guessIt():
	'''Test'''
	number=23
	guess=0
	while guess!=23:
		guess=int(input('Enter an int: '))	#input into console	
		if guess==number:
			print('Nailed it')
		elif guess<number:
			print("little higher")
		else:
			print("little lower")
	print("Done")


x= 50
def func():
	global x
	
	print ('x is', x)
	x=2
	print('changed x to ',x)
	

def shoping():
	shoplist=["seeds", "pondwater", "humus"]
	print("I have ", len(shoplist), " items in list: ")

	for item in shoplist:
		print(item, end=' ')
		
	shoplist.append("ph tabs")

	print("---now I have these items: ", shoplist)


def dict():
	ab={'Nick':'92390279',
	'Alex':'92997732'}
	print(len(ab))
	if 'Nick' in ab:
		print("hell yeaaaaaah")
	else:
		print("nope")
	#print(ab)

#Sets: used as a list, but where the object itself is more important 
# than position and/or how many times it occurs.
def sets():	
	bri=set(["chile", "argentina", "brazil"])
	ass=set(["chile", "usa", "canada"])
	print(bri.intersection(ass))
#>> "chile" in bri --> returns True
#bri.add("peru")
#bric=bri.copy()
#bric.issuperset(bri) --> return True
#bri.remove("usa") 
###OJO, YOU CAN ONLY EXECUTE LINES WITHIN THE FUNCTION, CAN'T 
###bri.add in console, for example, only within function.


def stringDelim():	
	delim="_*_"
	myList=["chile", "brazil", "argentina"]
	b=myList
	c=myList[:] #this generates a copy, not a reference, like with b
	myList.append("peru")
	print(delim.join(b))
	print(delim.join(c))#being copy and b reference, by changing myList, b gets peru and b doesnt'
#listas son mutables, entonces al tener b=myList y al modificar
#myList, tb cambia b... no se aplica mutabilidad a variables, 
#solo listas y diccionarios (tuples [defined by ( )] aren't]

	
def backUp():	
	import os
	import time

	source = ['"C:\\test"', 'C:\\Backup'] #two folders to save?

	target_dir= 'C:\\Backup'

	target=target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'

	zip_command ="zip -qr {0} {1}".format(target, ' '.join(source))

	if os.system(zip_command) == 0:
		print("backup to ",target)
	else:
		print("failed")

		
class Person:
	def __init__(self, name):
		self.name=name
	def sayHi(self):  #has to have self as an argument so it can be instanced as "itself"
		print("Hello, my name is",
		self.name)
		
def exePerson():		
	p = Person("nicky")
	p.sayHi()

	
### Population belongs to the Robot class and hence is a class variable. 
### The name variable belongs to the object (it is assigned using self)
### and hence is an object variable.	
class Robot:
	pop=0
	def __init__(self, name):
		self.name=name
		print('(Initializing {0})'.format(self.name))
		Robot.pop+=1
	def __del__(self):
		print('{0} is being destroyed'.format(self.name))
		Robot.pop-=1
		if Robot.pop==0:
			print('{0} was the last of his kind... a robot'.format(self.name))
		else:
			print('There are still {0:d} robots working'.format(Robot.pop))
			#test :d
			
# The howMany is actually a method that belongs to the class and not 
# to the object. This means we can define it as either a classmethod 
# or a staticmethod depending on whether we need to know which class
# we are part of. Since we don't need such information, we will
# go for staticmethod.

	@staticmethod
	def howMany():
		print('we have {0:d} robots'.format(Robot.pop))
	
def addRobots():
	robo1= Robot('mazinger')
	robo2 = Robot('vf-10')
	print('robots', robo1, robo2, 'added')

#FOR PRIVATE VARIABLES, USE "__" BEFORE NAME

class Departamento:
	def __init__(self, _id, mts2, valor, num_dorms, num_banos):
		self._id = _id
		self.mts2 =mts2
		self.valor = valor
		self.num_dorms=num_dorms
		self.num_banos=num_banos
		self.vendido=False
	def vender(self):
		if not self.vendido:
			self.vendido=True
		else:
			print("Departamento {} ya se vendio".format(self._id))

#d1= Departamento(_id=1, mts2 = 100, valor = 5000, num_dorms=3, num_banos=2)
#print(d1.vendido)
#d1.vender()
#print(d1.vendido)
#d1.vender()

class PalabraSecreta:
	def __init__(self, palabra_clave, frase_secreta):
		self.__palabra_clave = palabra_clave
		self.__frase_secreta = frase_secreta
	def descriptar(self, frase_secreta):
		'''Solo si la grase es correcta'''
		if frase_secreta == self.__frase_secreta:
			return self.__palabra_clave
		else:
			return ' '

#s= PalabraSecreta("animal", "tiene patas")
#print(s.descriptar("tiene patas"))
#s.__palabra_clave
#s._PalabraSecreta__palabra_clave 
#s.__palabra_clave is private, while s._PalabraSecreta__palabra_clave
#let's there be a public access

import datetime

class PostIt:
	last_id = 0 #static variable for last id generated
	def __init__(self, mensaje, tags=''):
		self.mensaje = mensaje
		self.tags=tags
		self.creation_date =datetime.date.today()
		self._id= PostIt.last_id
		PostIt.last_id+=1
	def match(self, keyword):
		return keyword in self.mensaje or keyword in self.tags

#msg=PostIt("testit1", "t1")

class Panel:
	def __init__(self):
		self.postit_dict={}
	def _buscar_postit_id(self, postit_id):
		for p in self.postit_dict:
			if p._id == postit_id:
				return p
			return None
	def nuevo_postit(self, texto, tags=''):
		p=PostIt(texto, tags)
		self.postit_dict.update({p._id:p})
	def modifica_mensaje(self, postit_id, mensaje_nuevo):
		for p in self.postit_dict:
			if p._id == postit_id:
				self.postit_dict[postit_id].mensaje=mensaje_nuevo
	def modifica_tags(self, postit_id, tags_nuevos):
		self.postit_dict[postit_id].tags = tags_nuevos
	def buscar_postits(self, keyword):
		return [p for p in self.postit_dict.values() if p.match(keyword)]
	def display(self, keyword= None):
		result=[]
		if keyword:
			result=[p for p in self.buscar_postits(keyword)]
		else:
			result = self.postit_dict
		for p in result:
			print("post it {0}: \n Mensaje: {1} \n Tags: {2}".format(p._id, p.mensaje, p.tags))

import sys

class Menu:
	def __init__(self):
		self.panel=Panel()
		self.opciones = { 
						"1": self.display_postits,
						"2": self.buscar_postits,
						"3": self.agregar_postit,
						"4": self.modificar_postit,
						"5": self.salir
						}
	def display_menu(self):
		print("""
			Menu:
				1: Mostar Post-Its
				2: Buscar Post-Its
				3: Agregar nuevo Post-Its
				4: Modificar Post-Its existente
				5: Salir
			""")
	def run(self):
		while True:
			self.display_menu()
			eleccion = input("Ingrese Opcion: ")
			accion = self.opciones.get(eleccion)
			if accion:
				accion()
			else:
				print("{0} no es una opcion valida".format(eleccion))
	def display_postits(self, p_list=None):
		if not p_list:
			p_list= self.panel.postit_dict.values()
		if not p_list:
			print("No hay Post-Its creados...")
		else:
			for p in p_list:
				print("post it {0}: \n Mensaje: {1} \n Tags: {2}".format(p._id, p.mensaje, p.tags))
	
	def buscar_postits(self):
		keyword= input("Ingrese keyword: ")
		postit_list = self.panel.buscar_postits(keyword)
		self.display_postits(postit_list)
	def agregar_postit(self):
		mensaje=input("Ingrese Mensaje: ")
		tag_list = input("Ingrese Tags separados por espacios:")
		tag_list = tag_list.split()
		self.panel.nuevo_postit(mensaje, tag_list)
		print("Nota creada exitosamente")
	def modificar_postit(self):
		_id=input("ingrese el id del Post-It que quiere modificar: ")
		_id=int(_id)
		while _id not in self.panel.postit_dict.keys():
			print("El id no existe en la base de datos...")
			_id= input("ingrese el id del Post-It que quiere modificar")
			_id=int(_id)
		mensaje= input("Ingrese el nuevo mensaje: ")
		tag_list = input("Ingrese los nuevos tags separados por espacios: ")
		if mensaje:
			print(_id)
			self.panel.modifica_mensaje(_id, mensaje)
		if tag_list:
			tag_list = tag_list.split()
			self.panel.modifica_tags(_id, tag_list)
		print("postit modificado existosamente!!")
	def salir(self):
		print("Gracias por usar nuestro Post-It")
		sys.exit(0)
		
class Animal():
	def __init__(self, nombre, patas):
		self.nombre=nombre
		self.patas=patas
		self.estomago=[]
	def __call__(self, comida):
		self.estomago.append(comida)
	def asimilar(self):
		if len(self.estomago)>0:
			return self.estomago.pop(0)
	def __str__(self):
		return ('Animal llamado: {}'.format(self.nombre))

gato=Animal('Cucho', 4)
perro=Animal('Boby', 4)
pajaro=Animal('Tweeety', 2)

#print(gato.nombre)
#gato('pescado')
#print(gato.estomago)
#gato.asimilar()
#print(gato.estomago)

###Obejtos over###

##Inicio Property:
class Email:
	def __init__(self, address):
		self._email = address
	def _set_email(self, value):
		if '@' not in value:
			print("Esto no parece una direccion de correo.")
		else:
			self._email = value
	def _get_email(self):
		return self._email
	def _del_email(self):
		print("Correo eliminado")
		del self._email
	email = property(_get_email, _set_email, _del_email, "Esta propiedad corresponde al correo")

#implementando decorador (shortcut-like to calling explicit statement)	
class Color:
	def __init__(self, rgb_code, nombre):
		self.rgb_code =rgb_code
		self._nombre = nombre
	@property
	def nombre(self):
		print("getting color name")
		return self._nombre
	@nombre.setter
	def nombre(self, valor):
		self._nombre = valor	
	@nombre.deleter
	def nombre(self):
		del self._nombre
	#nombre=property(get_nombre, set_nombre)

class Circulo:
	def __init__(self, radio):
		self._radio = radio
	@property
	def area(self):
		return self._radio**2*3.14
		
from urllib.request import urlopen

class WebPage:
	def __init__(self, url):
		self.url= url
		self._content=None
	@property
	def content(self):
		if not self._content:
			print("Obteniendo Página Web...")
			self._content = urlopen(self.url).read()
		return self._content

def runWebPage():
	import time
	page = WebPage("http://www.puc.cl")
	now = time.time() #Return the time in seconds
	contenido_1 = page.content
	print("Tiempo en obtener la página por primera vez: {}".format(time.time() - now))
	now = time.time()
	contenido_2 = page.content
	print("Tiempo en obtener la página por segunda vez: {}".format(time.time() - now))
	contenido_1 == contenido_2
	
#Herencias
class ContactList(list):
	def buscar(self, nombre):
		matches=[]
		for contacto in self:
			if nombre in contacto.nombre:
				matches.append(contacto)
		return matches

class Contacto:
	contactos_list=ContactList()
	def __init__(self, nombre, email):
		self.nombre=nombre
		self.email=email
		Contacto.contactos_list.append(self)
		
class Familiar(Contacto):
	def __init__(self, nombre, email, relacion):
		super().__init__(nombre, email) #herencia
		self.relacion=relacion

def runContactList():
	p1=Familiar("juan", "jc@gmail.com", "padre")
	p2=Contacto("jorge", "jg@hotmail.com")
	p3 = Familiar("pablo", "pab@yahoo.com", "primo")
	p4=Contacto("jorge T", "noemail@gmail.com")

	L=[c.nombre for c in p1.contactos_list.buscar("jorge")]
	print('[', end='')
	print(*L, sep=', ',end='')
	print(']')

class SchoolMember:
		def __init__(self, name, age):
			self.name=name
			self.age=age
			print("Initialized SchoolMember: {}".format(self.name))
		def tell(self):
			print('Name: "{0}" Age: "{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary=salary
		print("Initialized Teacher: {}".format(self.name))
	def tell(self):
		SchoolMember.tell(self)
		print('Salary: "{0:d}"'.format(self.salary))
		
class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks=marks
		print("Initialized Student: {}".format(self.name))
		
	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{0:d}"'.format(self.marks)) 
		
def runSchool():
	t=Teacher("Mr.Powers", 40, 30000)
	s=Student("Nicholas", 32, 62)
	members=[t,s]
	for member in members:
		member.tell()

class Investigador():
	def __init__(self, area):
		self.area=area
class Docente():
	def __init__(self, Departamento):
		self.departamento=Departamento
class Academico(Docente, Investigador):
	def __init__(self, nombre, area_investigacion, departamento):
		Investigador.__init__(self, area_investigacion)
		Docente.__init__(self, departamento)
		self.nombre = nombre

def runAcademico():
	p1 = Academico("Juan Perez", "Inteligencia de Máquina", "Ciencia De La Computación")
	print(p1.nombre)
	print(p1.area)
	print(p1.departamento)
	
###Falta ver herencia mejor, *args and *kwargs

class ClaseB:
	num_llamadas_B=0
	def llamar(self):
		print("Llamando método en clase B")
		self.num_llamadas_B+=1
		
class SubClaseIzq(ClaseB):
	num_llamadas_izq=0
	def llamar(self):
		super().llamar()
		print("Llamando método en SubClase Izq")
		self.num_llamadas_izq+=1

class SubClaseDer(ClaseB):
	num_llamadas_der=0
	def llamar(self):
		super().llamar()
		print("Llamando método en SubClase Der")
		self.num_llamadas_der+=1

class SubClaseA(SubClaseIzq, SubClaseDer):
	num_llamadas_subA=0
	def llamar(self):
		super().llamar()
		#SubClaseDer.llamar(self)
		print("Llamando método en SubClaseA")
		self.num_llamadas_subA+=1
		
def runHerenClases():
	s = SubClaseA()
	s.llamar()
	print(s.num_llamadas_subA, s.num_llamadas_izq, s.num_llamadas_der, s.num_llamadas_B)

class AddressHolder:
	def __init__(self, calle='', ciudad='', numero='', comuna='',**kwargs):
		super().__init__(**kwargs)
		self.calle = calle
		self.ciudad = ciudad
		self.comuna = comuna
		self.numero = numero

class Contacto:
	contactos_list=[]
	def __init__(self, nombre='', email='', **kwargs):
		super().__init__(**kwargs)
		self.nombre=nombre
		self.email=email
		Contacto.contactos_list.append(self)
		
class Cliente(Contacto, AddressHolder):
	def __init__(self, telefono='', **kwargs):
		super().__init__(**kwargs)
		self.telefono=telefono

def runClienteContacto():
	c = Cliente(nombre = 'Juan Perez', email = 'jp@gmail.com',
	telefono = '23542331', calle = 'Pedro de Valdivia', numero = '231', 
	comuna = 'Providencia', ciudad = 'Santiago')
	print("{}, {}, {}, {}".format(c.nombre, c.email, c.calle, c.comuna))

