import matplotlib.pyplot as plt
import numpy as np


pos= np.arange(6)+0.5
names=['Nibesh', 'Prakash','Cj', 'Amit', 'Kaka', 'Kamal']

plt.bar(pos,(4,9,15,18,28,39),align="center",color='blue')

plt.tick_params('x',color='white')
plt.tick_params('y',color='white')

plt.title('Random Plots',color='w')
plt.xlabel('Friends',color='b')
plt.ylabel('Friends ',color='b')

plt.xticks(pos,names)


plt.show()
