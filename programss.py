# input_string = input("Enter Thde Names of Fruits Separated by bspace => ")
# lst = input_string.split(" ")
# print(lst)
# for x in lst:
#     print(x, end=" ")
#     if x == "t4":
#         break



#----------------------------------------------

# def my_function(fname):
#     print(fname+" " +"SIT")
    
# my_function("emil")
# my_function("Tobias")
# my_function("Linux")

#------------------------------------------------

# def my_function(x):
#     return 5 * x

# print(my_function(3))



#------------------------------------------------

# x = lambda a,b: a + 10
# print(x(5,5))

#---------------------------------

# class test:
#     def main():
#         a = "test1"
#         b = "test2"
#         c = "test3"
#         d = "test4"
#         e = "test5"
#         final_str="{4},{3},{2},{1},{0}"
#         print(final_str.format(a,b,c,d,e))
# test.main()


#---------------------------------------

# class test:
#     def main():
#         a = input("Enter The First Value => ")
#         b = input("Enter The Second Value => ")
#         c = input("Enter The Third Value => ")
#         d = input("Enter The Final Value => ")
#         final_str="{3},{2},{1},{0}"
#         print(final_str.format(a,b,c,d))
# test.main()


#--------------------------------------------

a = int(input("enter the 1st value => "))
b = int(input("enter the 2nd value => "))
c = a + b
d = a * b
print(c)
print(d)
if c > d and c == d :
    raise Exception("Error!")
else:
    raise Exception("No Error!")