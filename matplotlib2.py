import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5]
y = [10,20,25,30,40]

#Plot Types 

#Line Graph
plt.plot(x , y)
plt.show()

#Bar Graph
plt.bar(x , y)
plt.show()
plt.barh(x, y)
plt.show()

#Scatter plot
plt.scatter(x , y)
plt.show()

#Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.show()

#Pie
sizes = [30, 25, 20, 15, 10]       # values
labels = ["A", "B", "C", "D", "E"] # category names
colors = ["gold", "skyblue", "lightgreen", "pink", "orange"]

plt.pie(sizes, labels=labels, colors=colors)
plt.show()
