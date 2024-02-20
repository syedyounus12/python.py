#input() and eval() using with control statment
#if, else, elif, match
# #task1
# a = 10
# b = 20
# if a < b:
    
#     print("True")
    
# else:                             #True
    
#     print("false")
    
# if a > b:
    
#     print("True")
    
# else:                              #False
    
#     print("False")

#task2 
# Username = input("Enter Username:")
# Password = input("Enter Password:")

# if Username == "admin" and Password == "admin":
 
#   print("login successfull")
  
# else:
    
#     print("login unsuccesfull")


#task3

# a = 10
# b = 20
# c = 10

# if a == b and c == b:      
#                      #when we use 'and' operator the must both condition are satisfy
#     print("both are staisfied")
# else:                              #both are not staisfied
    
#     print("both are not staisfied")
    
# if a == b or c == a:
#                       #when we use 'or' operator the one condition are satisfy. one condition will satisfy it will print 'if' logic.
#     print("if condition")

# else:                       #if condition
    
#     print("else condition")
    
    
# #task4
# emp_salary = int(input("Enter your salary: "))

# if emp_salary <= 30000:
#     print("no tax deduction")
# elif emp_salary <= 40000:
#     print("tax deduction")
# elif emp_salary <= 50000:
#     print("tax deduction")
# elif emp_salary <= 60000:
#     print("tax deduction")
# elif emp_salary <= 70000:
#     print("tax deduction")
# else:
#     print("invalid")
    
    
    # task5
    
emp_salary = float(input("Enter your salary: "))
match emp_salary: 
        
    case 30000: print("NO Tax Deduction")   
    
    case 40000: print(" Tax Deduction")  
     
    case 50000: print(" Tax Deduction")  
      
    case 60000: print(" Tax Deduction")
    
    case _ : print("invalied")  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    