import matplotlib.pyplot as plt # library for plotting graph on axis

#taking coordinates 
x=[2,5]
x1=[3,4,5,7]
y=[4,8]
y1=[8,10,7,9]

#defining x axis as  distance
plt.xlabel("Distance")
#defining y axis as  time
plt.xlabel("Time")

#defining title of the graph
plt.title("cal speed")

#plottting x nd y
plt.plot(x,y,label="road",c='r',m='*',s=200)#label gives the label to the line, c is for color, m is  for marker, s is for size

#plotting in terms of spoting
plt.scatter(x1,y1)

#to show the labels
plt.legend()

#for showing grid
plt.grid(color='g')

#showing x and y
plt.show()
