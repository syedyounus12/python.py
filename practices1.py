# # t1=()
# # print(t1, type(t1)) #() <class 'tuple'>
# # t1=(10, 20, 30, 40, 50, 60, 10, 20, 30)
# # print(t1.count(20))
# # print(t1)
# # t2 = (10, 20, 30, 50, 70, 80)
# # print(t2.index(70))
# # print(t2)
# # print(len(t1))
# # print(len(t2))
# # print(t1)
# # print(len(t2))
# # print(dir(tuple))
# # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__',
# #  '__eq__', '__format__', '__ge__', 
# #  '__getattribute__', '__getitem__', '__getnewargs__', 
# #  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# #  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
# #  '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', 
# #  '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
# # t3 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# # print(t3[2:7])
# # print(t3[2:])
# # print(t3[ :8])
# # print(t3[::1])
# # print(t3[::-1])
# # a= (10)
# # print(a)
# # b=(2); c= (50)
# # print(b)
# # print(c)
# # print(d)
# s1 = set()
# print(s1)
# s2 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# print(s2)
# s2.add("element")
# print(s2)
# s2.add(140)
# print(s2)
# s2.remove(50)
# print(s2)
# s2.discard(100)
# print(s2)
# s2.update(["younus", 1, 2, 3, 4, 5])
# # print(s2)
# # t4 = tuple(s2)
# # print(t4)
# # l3 = list(t4)
# # print(l3)
# # l3.sort()
# # print(l3)
s1 = {10, 20, 30, 40, 50, 60,}
print(s1)
l1 = list(s1)
print(l1)
l1.sort()
print(l1)
s1 = set(l1)
print(s1)
s1.clear()
print(s1)
s1.add(30)
print(s1)
s1.add(40)
s1.add(50)
s1.add(20)
print(s1)
s1.copy()
print(s1)
f1 = frozenset(s1)
print(f1)
f1.union({"younus"})
print(f1)    