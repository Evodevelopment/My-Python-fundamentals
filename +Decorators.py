def hello():
  print("Helllooooooo")

greet = hello
#del hello - deletes the name function but in Python memory stays the function itseld
print(greet(()

def hello_1(func):
    func ()

def greet():
  print("still here!")

a = hello(greet)

print (a)
