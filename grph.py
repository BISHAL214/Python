import numpy as np
import matplotlib.pyplot as plt
class Graph:
    def plot1():
        x_axis = np.array([32,45,63,71,75,94])
        y_axis = np.array([12,34,56,73,68,84])
        z_axis = np.array([23,34,56,76,87,90])
        f = plt.figure()
        f.set_figwidth(10)
        f.set_figheight(4) 
        plt.plot(x_axis, linestyle='dotted',marker="o",mfc="blue")
        plt.plot(y_axis,linestyle='dashed',marker="o",mfc="red")
        plt.plot(z_axis,linestyle='dashdot',marker="o",mfc="green")
        plt.show()
Graph.plot1