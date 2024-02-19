#dict
# using dict we can store key value pairs
# in dict key can be either string or integer
#print(dir(dict))
print(dir(dict))
#'clear',
# 'copy',
# 'items',
# 'keys',
# 'pop',
# 'update',
# 'values'
d1 = {1: 10, 2: 20, 3: 30 }
print(d1)
print(d1.keys()) #dict_keys([1, 2, 3])
print(d1.values())         # dict_values([10, 20, 30])
print(d1.items())           #dict_items([(1, 10), (2, 20), (3, 30)])

d2 = {1: 10, 2: 20, 3: 30}
d2[4] = 40
print(d2)
# {1: 10, 2: 20, 3: 30, 4: 40}

d3 = {}
d3[1] = 10
d3[2] = 20
print(d3)
# {1: 10, 2: 20}
d1 = {"nameone": "Krishna", "nametwo": "rama"}
print(d1)
d1["nametwo"] = "Rahim"
print(d1)
# {'nameone': 'Krishna', 'nametwo': 'Rahim'}
d1 = {1: 10, 2: 20, 3: 30}
d2 = {"nameone": "Uama", "nametwo": "Mahesh"}
d1.update(d2)
print(d1)
# {1: 10, 2: 20, 3: 30, 'nameone': 'Uama', 'nametwo': 'Mahesh'}
d1.update({1: "Younus"})
print(d1)
# {1: 'Younus', 2: 20, 3: 30, 'nameone': 'Uama', 'nametwo': 'Mahesh'}
d1 = {1: 10, 2: 20, 3:30, 4: 40}
d1["nameone"] = d1.pop(1)
print(d1)
# {2: 20, 3: 30, 4: 40, 'nameone': 10}
d1["nameone"] = d1.pop(2)
print(d1)
d1["nameone"] = d1.pop(3)
print(d1)
# {4: 40, 'nameone': 30}
employees = {
                "employeesName": {"Nameone": "Ram", "Nametwo": "Ramu"},
                "employeeSalary": 20000,
                "employeePosition": ["Developer", "Designer", "Devops"]    
}
print(employees["employeesName"])                    #{'Nameone': 'Ram', 'Nametwo': 'Ramu'}
print(employees["employeesName"]["Nametwo"])          #Ramu
print(employees["employeeSalary"])                     #20000
print(employees["employeePosition"][1])                  #Designer


r1 = range(0,10)
print(r1)
l1 = []
l1.extend(r1)
print(l1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(id(l1))