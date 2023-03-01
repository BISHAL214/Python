import matplotlib.pyplot as plt
import random
import numpy as np
class Graph:
    def plot1():
        x_axis = np.random.randint(10,50,10)
        y_axis = np.random.randint(40,60,10)
        z_axis = np.random.randint(30,90,10)
        f = plt.figure()
        f.set_figwidth(10)
        f.set_figheight(4) 
        plt.plot(x_axis, linestyle='dotted',marker="o",mfc="blue")
        plt.plot(y_axis,linestyle='dashed',marker="o",mfc="red")
        plt.plot(z_axis,linestyle='dashdot',marker="o",mfc="green")
        plt.show()
    def plot2():
        x_axis = np.array(['A','B','C','D','E','F','G','H','I','J'])
        y_axis = np.random.randint(40,60,10)
        plt.bar(x_axis,y_axis,color="purple",width=0.5)
        plt.grid(color="red")
        plt.show()
        plt.barh(x_axis,y_axis,color="green")
        plt.grid(color="red")
        plt.show()
    def plot3():
        fruits = np.random.randint(20,50,10)
        explode = np.random.randint(40,90,10)
        labels = np.array(["xyz","zyx","yxz","zxy","yzx","rgf","tfg","eds","hcc","hgc"])
        plt.pie(fruits,labels=labels,shadow=True,explode=explode)
        plt.legend(title="mdsvdscjhz")
        plt.show()
    def plot4():
        x_axis = np.random.randint(10,30,10)
        y_axis = np.random.randint(50,80,10)
        x_axis_A = np.random.randint(90,150,10)
        y_axis_B = np.random.randint(150,300,10)
        print(len(x_axis_A),len(y_axis_B))
        plt.scatter(x_axis,y_axis)
        plt.scatter(x_axis_A,y_axis_B)
        plt.show()
Graph.plot1()
Graph.plot2()
Graph.plot3()
Graph.plot4()