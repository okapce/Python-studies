from math import *

def excercise1():
	width=17
	height=12
	delimiter='.'
	
	print("width/2 = {}".format(width/2))
	print("width/2.0 = {}".format(width/2.0))
	print("height/3 = {}".format(height/3))
	print("1+2*5= {} ".format(1+2*5))
	print("delimiter*5={}".format(delimiter*5))

#print(pi) --> will give error
#from math import pi
#print(pi) --> will work since it was imported

def countdown(n):
	if n<=0:
		print("Blastoff!!")
	else:
		print(n)
		countdown(n-1) #recursive
		
def testInput():
	a=input("ingrese algo: \n")
	print("today we have "+a)

#composition (functions calling other functions)
def area(radius):
	temp= pi * radius**2
	return temp
	
def distance(x1, x2, y1, y2):
	dx=x2-x1
	dy=y2-y1
	dsquared=dx**2 +dy**2
	result=sqrt(dsquared)
	return result
	
def circle_area(xc, yc, xp, yp):
	radius= distance(xc, yc, xp, yp)
	result= area(radius)
	return result
	
def is_divisible(x, y):
	if x % y == 0:
		print("{} is divisible by {}".format(x,y))
		return True
	else:
		print("{} is NOT divisible by {}".format(x, y))
		return False
		
def is_between(x, y, z):
	if x<=y and y<=z:
		return True
	else:
		return False

def argsTest(var1, *argv):
	print("1st variable: {}".format(var1))
	for arg in argv:
		print("other variables through argv : {}".format(arg))

def multiply(*args):
	z=1
	for num in args:
		z*=num
	print(z)

def kwargTest( **kwargs):
	print(kwargs)
	for key, value in kwargs.items():
		print("The value of {} is {}".format(key, value))

def travLoopWh():
	index=0
	fruit="banana"
	while index<len(fruit):
		letter=fruit[index]
		print(letter)
		index+=1
		
def travLoopFor():
	index=0
	fruit="banana"
	for chars in fruit:
		print(chars)
			
def inBoth(w1, w2):
	#letter="wuuuuut"
	for letter in w1:
		if letter in w2:
			print(letter)
			
def histogram(s):
	d= dict() #creates empty dictionary
	for c in s: #checking letter in word "s"
		if c not in d: #if letter of word "c" not in dictionary, d[letter]=1
			d[c]=1
		else: #if letter of word c in dictionary, it just adds
			d[c]+=1
	return d
	
def print_hist(h):
	for c in h:
		print(c, h[c])