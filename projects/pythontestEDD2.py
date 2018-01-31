class Video:
	pass

def runVideo():
	vid=Video()
	vid.ext='mkv'
	vid.size='1024'
	print(vid.ext, vid.size)

class Imagen:
	def __init__(self):
		self.ext=''
		self.size=''
		self.data=''

def runImg():
	img=Imagen()
	img.ext='jpeg'
	img.size='8'
	img.data=[255,255,255,200,34,35]
	img.ids=20
	print(img.ext, img.size, img.data, img.ids)

# Tuples (lista imutables)
def tupleEjemplo():
	#a=tuple()
	img=Imagen()
	a=(img, "este es", "un archivo")
	a[0]='nuevo dato'
	print(a)
#doesn't work, tuple no permite asignacion

def calcular_geometria(a,b):
	Features = namedtuple('Geometrical', 'area perimeter mpa mpb')
	area=a*b
	perimeter=2*(a+b)
	mpa=a/2
	mpb=b/2
	#return (area, perimeter, mpa, mpb)
	return Features(area, perimeter, mpa, mpb)
	
def runCalcGeom():
	data=calcular_geometria(20, 10)
	print(data.area)
	print(type(data))
	print("1: {} ".format(data))
	a=data[0]
	print("2: {} ".format(a))
	a, p, mpa, mpb = data
	print("3: {0}, {1}, {2}, {3}".format(a, p, mpa, mpb))
	a, p , mpa ,mpb =calcular_geometria(20, 10)
	print("4: {0}, {1}, {2}, {3}".format(a, p ,mpa, mpb))

#slicing
def sliceIt():
	data=(400,20,1,3,10,11,12,500)
	print(data)
	a=data[1:3]#between 1 and 3
	print("1: {}".format(a))
	a=data[3:]#3 onwards
	print("2: {}".format(a))
	a=data[:5]#all till 5
	print("3: {}".format(a))
	a=data[2::2]#2 onwards, skipping 2
	print("4: {}".format(a))
	a=data[1:6:2]#between 1 and 6, skipping 2
	print("5: {}".format(a))
	a=data[::-1]#inverted
	print("6: {}".format(a))
	
from collections import namedtuple
# definir campos para cada una de las posiciones en que han 
# sido ingresado los datos.
def runNamedTuple():
	Register=namedtuple("Register_type",["RUT", "name", "age"])
	c1=Register("16099080-5","Nicholas", 32)
	c2=Register("4183632-6","Bryan",78)
	print(c1.RUT)
	print(c2.RUT)
	print(type(c2))

# Listas (mutable)
def runLista():
	LE=[]
	LE.append((2018,1,15))
	LE.append((2018,3,6))
	print(LE)
	L=[1, 'string', 20.5, (20,45)]
	print(L)
	print(L[1])

### Agregar individualmente =>append, agregar lista completa => extend
	
def playList():
	canciones=["Addicted to pain", "Ghost love score", "As I am"]
	print(canciones)
	nuevas_canciones=["Elevate", "shine", "cry of Achilles"]
	canciones.extend(nuevas_canciones)
	print(canciones)
	canciones.insert(1, "Sober")
	print("")
	print("Added 1 song to position 1:")
	print(canciones)
	
def runSorting():
	numeros=[6, 7, 2, 4, 10, 20 ,25]
	print(numeros)
	a= numeros.sort()
	print(numeros, a)
	numeros.sort(reverse=True)
	print(numeros)
	
class Pieza:
	pid=0
	def __init__(self, pieza):
		Pieza.pid+=1
		self.pid=Pieza.pid
		self.tipo=pieza
def setgetPiezas():
	piezas=[]
	piezas.append(Pieza("Alfil"))
	piezas.append(Pieza("Peon"))
	piezas.append(Pieza("Rey"))
	piezas.append(Pieza("Reina"))
	for pieza in piezas:
		print("pid: {} - tipo de pieza: {}".format(pieza.pid, pieza.tipo))