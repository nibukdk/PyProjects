import matplotlib.pyplot as plt

fig= plt.figure()

rect=fig.patch
rect.set_facecolor('green')
graph1=fig.add_subplot(2,1,1,facecolor='brown')

x=[1,2,4,5]
y=[10,15,23,0]
x2=[3,6,6,9]
y2=[11,20,27,30]
x3=[1.2,6.5,9.8,11.5]
y3=[2,5,8,10]

graph1.plot(x,y,'white',linewidth=4.0)
graph1.plot(x2,y2,'blue',linewidth=3.0)
graph1.plot(x3,y3,'yellow',linewidth=2.0)

graph1.tick_params('x',color='white')
graph1.tick_params('y',color='white')

graph1.spines['top'].set_color('w')
graph1.spines['bottom'].set_color('w')
graph1.spines['left'].set_color('w')
graph1.spines['right'].set_color('w')

graph1.set_title('Random Plots',color='w')
graph1.set_xlabel('This is x axis',color='b')
graph1.set_ylabel('This is y axis',color='b')

#Second Graph Plot
graph2=fig.add_subplot(2,1,2,facecolor='black')

graph2.plot(x,y,'white',linewidth=4.0)
graph2.plot(x2,y2,'blue',linewidth=3.0)
graph2.plot(x3,y3,'yellow',linewidth=2.0)

graph2.tick_params('x',color='white')
graph2.tick_params('y',color='white')

graph2.spines['top'].set_color('w')
graph2.spines['bottom'].set_color('w')
graph2.spines['left'].set_color('w')
graph2.spines['right'].set_color('w')

graph2.set_title('Random Plots Number 2',color='w')
graph2.set_xlabel('This is x axis',color='b')
graph2.set_ylabel('This is y axis',color='b')


plt.show()
