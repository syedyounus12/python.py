# x =10
# def d1():
#     y = 20
#     print("local variable:", y) #global variable: 10  #local variable: 20
# d1()
# print("global variable:", x) #global variable: 10
# print(y) #we can call local variable outside funtion its error
# print(x)  #10
 
# x = 10
# def d1():
#      y = 20
#      print("local variable:", y) #local variable: 20
#      print("Global variable:", globals()["x"]) #Global variable: 10
# d1()


# def d1():
#     x=10
#     print("local variable:",x)
#     print("local varible:", locals() ["x"])
#     locals() ["x"] = 30 #error
# d1()
# locals() ["x"] = 30
# print("local varible:", locals() ["x"]) #local varible: 30
# print("local variable:",x)
# print(x)
# print("Global variable:", globals()["x"]) 

# x, y, z = 10, 20 ,30 
# def g():
#     return globals()
# def l():
#     a, b, c = 40, 50, 60 
#     return locals()
# print(g()) #{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000227C8B5BC20>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\syedy\\Desktop\\python.py\\funtions\\golbal-local.py', '__cached__': None, 'x': 10, 'y': 20, 'z': 30, 'g': <function g at 0x00000227C8B4A2A0>, 'l': <function l at 0x00000227C8E09080>}
# print(l()) #{'a': 40, 'b': 50, 'c': 60}

# x = 40
# def d1():
#     y = 20
#     print(y) #20
#     print(x) #40
# d1()
# print(x) #40
# print(y) #error


# x = 40
# def d1():
#     global y
#     y = 20
#     print(y) #20
#     print(x) #40
# d1()
# print(x) #40
# print(y) #20


# def d1(a, b):
#     print(a+b) #10
# c=d1
# # c(4, 6)

# def d2(a, b):
#     print(a-b)
# c=d2
# c(6, 4) #2

# inner funtion
# def d1(a):
#     print(a) #6
#     def d2(b):
#         print(b) #4
#         print(a+b) #10
#     d2(4)
    
# d1(6)

def login():
    
    
    def sales():
        print("sales")
        sales()
    def support():
        print("support")
        support()
    def developer():
        print("developer")
        developer()
        
        
login()
