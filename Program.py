# class Test:
#     def main():
#         a = str(input("Enter The First Name =>"))
#         b = str(input("Enter The Second Name =>"))
#         c = a + " " + b
#         print("Your Name =>", c)
#     def main_2():
#         a = str(input("Enter your School Name =>"))
#         b = str(input("Enter The First Name =>"))
#         c = str(input("Enter The Last Name =>"))
#         d = str(input("Enter Your Class =>"))
#         final_str= "My Name is {1} {2}. I study {0} school. I am in {3}"
#         print(final_str.format(a,b,c,d))
# Test.main()
# print("\n")
# Test.main_2()



class Test:
    def even():
        print("---------- E V E N  N U M B E R S ----------")
        a = int(input("Enter Starting Range => "))
        b = int(input("Enter Ending Range => "))
        for x in range(a,b):
            if x%2==0:
                print(x,end=" ")
    def odd():
        print("---------- O D D  N U M B E R S ----------")
        a = int(input("Enter Starting Range => "))
        b = int(input("Enter Ending Range => "))
        for x in range(a,b):
            if x%2!=0:
                print(x,end=" ")
object_loop = Test
object_loop.even()
print("\n")
object_loop.odd()



import random
a = int(input("Enter a Number => "))
b = int(input("Enter second Number => "))
abc = random.randint(10,20)
print(abc)


