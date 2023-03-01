class Array:
    def main_array():
        arr_1 = []
        n = int(input("enter the no. of array elements => "))
        for x in range(0,n):
            xyz = int(input())
            arr_1.append(xyz)
        print("original Array => ",arr_1)
        print(type(arr_1))
        arr_1.sort()
        print("ASCENDING ORDER =>",arr_1)
        arr_1.sort(reverse=True)
        print("DESCENDING ORDER => ",arr_1)
object=Array
object.main_array()


# import numpy as np
# import random
# class Random:
#     def random_array():
#         arr_1 = np.random.randint(10,50,9)
#         print("---------- Array with random Elements -----------")
#         print(arr_1)
# Random.random_array()
