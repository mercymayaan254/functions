def product(x,y):
  a=x*y;
  print("The product is ",a)
product(24,4)

def substraction(q,p):
  c=q-p;
  print("The substraction is ",c)
substraction(80,10)

def division(a,b):
  d=a/b;
  print("The division is ",d)
division(24,4)

def courses(*sub):
  for courses in sub:
    print(courses)
courses("OOPII","OOSAD","WEB DEV","ETHICS")

#number of arguments
def names(fname,lname):
  print(fname+ " " +lname)
names("Tony", "Matara")

#arbitrary arguments
def courses(**sub):
  for key,value in sub.items():
    print("{}:{}".format(key,value))
courses(first="Big data", second="CCNA", third="OOPII")

#defaul parameter value
def kenya(county ="mombasa"):
  print("I am from " + county)
kenya()
kenya("kiambu")
kenya("nairobi")
kenya("kisumu")

#passing a dictionary as an arguement
def my_function(food):
  for x in food:
    print (x)
student = {"Name: " "Austin "
    "Regno: " "BBAM-01-5454/2015 "
    "Email: " "austin@gmail.com"}
my_function(student)