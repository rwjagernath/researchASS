# https://pythongeeks.org/classes-in-python/

'Creating a class'
class vehicle:
	pass # Cuz empty classes raise an error
print(vehicle)

'Creating an object'
car = vehicle() 
'''
object_name = ClassName(*args)

1. Identity is the name of the object.

Example: car

2. In Python, every object has its unique state. We give each object its unique state by creating attributes in the __init__method of the class.

Example: Number of doors and seats in a car.

3. Behaviour of an object is what the object does with its attributes. We implement behavior by creating methods in the class.

Example: Accelerating and breaking in a car.

'''
print(car)


'Dot Operator'
class vehicle2:
    wheels = 4
car2 = vehicle2()
car2.wheels = 10
print(car2.wheels) # To access variables and functions inside the class


'Attributes'
class vehicle3:
	wheels = 4 # Wheels is a class attribute, value shard by all objects of the class

car3 = vehicle3()
van3 = vehicle3()

print(car3.wheels)
print(van3.wheels)
print(vehicle3.wheels) # Also works

vehicle3.wheels = 10 # changing value of a class atribute using the class name changes value in all objects of the class
print(car3.wheels)
print(van3.wheels)
print(vehicle3.wheels) 


'__init__() method'
class vehicle4:
	wheels = 4

	def __init__(self,doors): # Executed as soon as you create an object
		print(f'Object created with doors = {doors}')

car4 = vehicle4(2) 
van4 = vehicle4(6)

'Self parameter'
class vehicle5:
	def __init__(self, name): # Self refers to current object of the class 
		self.name = name # Can change it as long as it's the first parameter of the method

vehicle5a = vehicle5('car')
vehicle5b = vehicle5('van')

print(vehicle5a.name)
print(vehicle5b.name)

'Instance attributes'
class vehicle6:
	wheels = 4

	def __init__(self, name, doors, seats):
		self.name = name
		self.doors = doors
		self.seats = seats

car6 = vehicle6('car', 2, 2)
van6 = vehicle6('van', 6, 12)

print(car6.name, car6.doors, car6.seats)
print(van6.name, van6.doors, van6.seats)

'Methods'
class vehicle7:
	wheels = 4

	def __init__(self, name, doors, seats):
		self.name = name
		self.doors = doors
		self.seats = seats

	def accelerate(self,distance): # Behavior
		return f"{self.name} has travelled {distance} km"

car7 = vehicle7('car', 2, 2)
print(car7.accelerate(10))

'Polymorphism'
class Charles:

	def __init__(self) -> None:
		self.name = 'Charles'
		self.age = 20
	
	def get_name(self):
		print(f'sup, me name {self.name}')
	
	def get_age(self):
		print(f'me age {self.age}')
class Solomon:

	def __init__(self) -> None:
		self.name = 'Solomon'
		self.age = 50
	
	def get_name(self):
		print(f'sup, me name {self.name}')
	
	def get_age(self):
		print(f'me age {self.age}')

person1 = Charles()
person2 = Solomon()

for person in (person1, person2):
    person.get_name()
    person.get_age()


def number(x) -> int: # Doesn't enforce int (x can also be float etc.)
	return x

print(type(number(3.23)))