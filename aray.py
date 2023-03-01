# import numpy as np
# arr_1 = np.array([[1,2,3],[4,5,6]])
# print(arr_1.ndim)
# xyz = arr_1[0,2] + arr_1[1,0]
# print(xyz)

#------------------------------------------------

# arr_2 = ["google", "microswoft", "tcs", "wipro"]
# print(arr_2)

# arr_2[1] = "Bishal"
# print(arr_2)

# arr_2.insert(2, "Mondal")
# print(arr_2)

# arr_2.append("SIT")
# print(arr_2)

# final_array = arr_2
# print(final_array)
# print(final_array[2:4])

# arr_4 = ("test1", "test2", "test3", "test4", "test5", "test6", "test7")
# print(type(arr_4),len(arr_4))


#---------------------------------------------------------

# arr_1 = {1,2,3}
# arr_2 = [1,2,3]
# arr_3 = (1,2,3)
# arr_4 = {
#     "Name" : "test1",
#     "age" : "test_age",
#     "blood_group" : "tesrgroup",
# }

# print(type(arr_1))
# print(type(arr_2))
# print(type(arr_3))
# print(type(arr_4))


#-----------------------------------------

import numpy as np

arr = ([[[1,2,3],[4,5,3]],[[6,7,1],[8,9,2]],[[65,72,13],[81,90,21]]])

for x in arr:
    for y in x:
        for z in y:
            print(z,end=" ")



#-------------------------------------------


# import numpy as np

# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=1)

# print(arr1)
# print("\n")
# print(arr2)

# print("\n")
# print(arr)


#----------------------------------------

# import numpy as np

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2), axis=1)

# print(arr)


#--------------------------------------------

# import numpy as np

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))

# print(arr)

#---------------------------------------------

# import numpy as np

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.vstack((arr1, arr2))

# print(arr)

#-------------------------------

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(x)

#-----------------------


# import numpy as np
# class arraysearch:
#     def ArrSearch():
#         arr=[]
#         n = int(input("Enter The No. Of Array Elements => "))
#         for x in range(n):
#             arr.append(int(input()))
#         arr = np.array(arr)
#         print("Original Array => ",arr)
#         print("\n")
#         z = int(input("Enter A Number To Search In Array => "))
#         x = np.where(arr == z)
#         print("Indexes Found => ",x)
# arraysearch.ArrSearch()


#-------------------------------


