#function
def my_function():
  print("Glen Arua")
my_function()


#Argument
def sum (x,y):
  a=x+y
  print("The sum is",a)
sum(10,20)
sum(501,958)

def sum (x,y):
  a=x+y
  return a

print(sum(10,20))

#Number of Arguments
def courses(*args):
   for subject in args:
      print(subject)
courses("Big Data", "CCNA", "OOP2")

def courses(*args):
   for subject in args:
      return subject
print(courses("Big Data", "CCNA", "OOP2"))

#Arbitrary keyword arguments.

def courses(**kwargs):
   for key,value in kwargs.items():
     print("{}:{}" .format(key,value))
courses(first="Big Data",second="CCNA",third="OOP2")

#default parameter value
def kenya(county ="Kisumu"):
  print("I am from " + county)

kenya()
kenya("Nairobi")
kenya("Siaya")
kenya("Kisumu")

#passing a list as an arguments
def my_function(food):
  for x in food:
    print(x)

#The pass statement
def my_function():
pass()
	
	
	
fruits = ["Apple", "Banana", "Mango"]
my_function(fruits)

def my_function(student):
   for y in student:
     print(y)
student = {"Glen Arua", "Bscit-05-0075/2019", "glenarua@gmail.com"}
my_function(student)


#Create Area of a circle
def Area_of_a_circle (r):
  a=(22*r*r)/7
  return a

print(Area_of_a_circle(14))

#volume of a cylinder
def Volume_of_a_cylinder (r,h):
  a=(22*r*r*h)/7
  return a

print(Volume_of_a_cylinder(7,10))













