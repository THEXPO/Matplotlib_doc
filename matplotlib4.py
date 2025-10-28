import matplotlib.pyplot as plt

#plot formatting in matplotlib

x = [1,5,3,7,3,7,5,2,9,6]
y = [10,20,30,40,50,60,70,80,90,100]

#Size and width
plt.plot(x, y,linewidth=2)
plt.plot(x, y,markersize=2)
plt.show()

#Titles & Labels
plt.title("My Plot", fontsize=16, color="blue", loc="center") #Loc can be left,right or center
plt.xlabel("X Axis", fontsize=12)
plt.ylabel("Y Axis", fontsize=12)
plt.plot(x, y)
plt.show()

#Legends
plt.plot(x, y, label="Data 1")
plt.legend(loc="upper left")  # location
plt.plot(x, y)
plt.show()

#Limits
plt.xlim(0,10)
plt.ylim(0,100)