#print even or odd number


# if number % 2 == 0:
#     print("The number is even")
# else:
   
# #     print("The number is odd")
# def find_largest_num(num1, num2, num3):
#     max_num = num1
    
#     if num2 > max_num:
#         max_num = num2
    
#     if num3 > max_num:
#         max_num = num3
    
#     return max_num
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# largest_num = find_largest_num(num1, num2, num3)
# print("The largest number among", num1, ",", num2, ", and", num3, "is:", largest_num)




      
def d1(A):

    
    def d2(a, b):
       
        return A(a*b)

    return d2
@d1
def d3(c):
   
    return c
d=d1(d3)
print(d(1, 1))






    
    
    

