from math import exp
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

def sigmoid(x):
    y=1/(1+exp(-x))
    return y

def step(x):
    if (x<=0):
        return 0
    else:
        return 1
    
def relu(x):
	if (x<=0):
		return 0
	else:
		return x

def modified_sigmoid(c,x):
	y=1/(1+exp(-(c)*x))
	return y
    
#graph sigmoid function
x=np.linspace(-10,10,100)
y=np.array([sigmoid(i) for i in x])
fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_title('Sigmoid Function')

#graphing step function
x=np.linspace(-10,10,100)
y=np.array([step(i) for i in x])
fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_title('Step Function')

#graphing relu function
x=np.linspace(-10,10,100)
y=np.array([relu(i) for i in x])
fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_title('ReLU Function')

#graphing modified sigmoid function
x=np.linspace(-10,10,100)
y=np.array([modified_sigmoid(50,i) for i in x])
fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_title('Modified Sigmoid Function with c=50')

plt.show()