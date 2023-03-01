import numpy as np

arr = ([[[1,2,3],[4,5,3]],[[6,7,1],[8,9,2]],[[65,72,13],[81,90,21]]])

for x in arr:
    for y in x:
        for z in y:
            print(z,end=" ")
