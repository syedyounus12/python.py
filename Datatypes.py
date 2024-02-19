i = 10
print(i, type(i)) # 10 <class 'int'>

j = 14.3
print(j, type(j))      #14.3 <class 'float'>
 
b = True
print(b, type(b)) 
# True <class 'bool'>

c = 20j
print(c, type(c))
# 20j <class 'complex'>

s = "name"
print(s, type(s))
# name <class 'str'>

l1= []
print(l1, type(l1))
# [] <class 'list'>
##
tuple1= []
print(tuple1, type(tuple1))

r1 = range(0)
print(r1, type(r1))
# range(0, 0) <class 'range'>

d1 = {}
print(d1, type(d1))
# {} <class 'dict'>

s1 = {12}
print(s1, type(s1))
# {12} <class 'set'>

b1 = bytes()
print(b1, type(b1))
# b'' <class 'bytes'>
b2 = bytearray()
print(b2, type(b2))
# bytearray(b'') <class 'bytearray'>

f1 = frozenset()
print(f1, type(f1))
# frozenset() <class 'frozenset'>

default_values = (int, float, str, range, frozenset, set, list, complex, bool, dict, bytes, bytearray, None)
print(default_values)

# bytearray(b'') <class 'bytearray'>
# frozenset() <class 'frozenset'>
# (<class 'int'>, <class 'float'>, <class 'str'>, <class 'range'>, <class 'frozenset'>, <class 'set'>, <class 'list'>, <class 'complex'>, <class 'bool'>, <class 'dict'>, <class 'bytes'>, <class 'bytearray'>, None) 

d_objects = [int(), float(), str(), range(0), frozenset(), set(), list(), complex(), bool(), dict(), bytes(), bytearray()]
print(d_objects)
# [0, 0.0, '', range(0, 0), frozenset(), set(), [], 0j, False, {}, b'', bytearray(b'')]
