import matplotlib.pyplot as plt
import numpy as np
class DataPlot:
    def Plot1():
        x_axis = np.array([10,16,34,76,87,85,90,56,32,45,57,78,84,91,63,23])
        y_axis = np.array([11,24,52,48,94,64,76,78,69,78,50,40,39,50,60,32])
        z_axis = np.array([13,46,73,49,76,43,90,95,84,76,67,43,54,86,90,42])
        f = plt.figure()
        f.set_figwidth(10)
        f.set_figheight(4) 
        plt.plot(x_axis, linestyle='dotted',marker="o",mfc="blue")
        plt.plot(y_axis,linestyle='dashed',marker="o",mfc="red")
        plt.plot(z_axis,linestyle='dashdot',marker="o",mfc="green")
        plt.show()
    def Plot2():
        x_axis = np.array([48,81,78,69,21,78,20,19,79,19,37,60])
        y_axis = np.array([71,61,47,18,82,24,79,78,77,68,80,57])
        x_axis_A = np.array([10,16,37,85,12,15,86,70,69,41,81,47])
        y_axis_B = np.array([36,31,14,86,53,16,10,87,60,88,81,88])
        print(len(x_axis_A),len(y_axis_B))
        plt.scatter(x_axis,y_axis)
        plt.scatter(x_axis_A,y_axis_B)
        plt.show()
    def Plot3():
        x_axis = np.array(['A','B','C','D','E','F','G','H','I','J'])
        y_axis = np.array([48,81,78,69,71,28,19,79,19,20])
        plt.bar(x_axis,y_axis,color="purple",width=0.5)
        plt.grid(color="red")
        plt.show()
        plt.barh(x_axis,y_axis,color="green")
        plt.grid(color="red")
        plt.show()
    def Plot4():
        students = np.array([15,20,25,30,50,9,75,1])
        explode = np.array([0.6,0.6,0,0,0,0,0,0.6])
        labels = np.array(["xyz","zyx","yxz","zxy","yzx","rgf","tfg","eds"])
        plt.pie(students,labels=labels,shadow=True,explode=explode)
        plt.legend(title="Annual Result")
        plt.show()
DataPlot.Plot1()
DataPlot.Plot2()
DataPlot.Plot3()
DataPlot.Plot4()
