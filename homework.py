import numpy as np  
import matplotlib.pyplot as plt  
import random  

   
X = np.random.uniform(size=2000)  #随机生成二维的点
Y = np.random.uniform(size=2000)
x = X-0.5
y = Y-0.5

 # 迭代阀值，当两次迭代损失函数之差小于该阀值时停止迭代   
epsilon = 0.00001
#学习率 
alpha = 0.001    
error1 = 0.5 
error0 = 0.5
flag = 0  
   
  
# 初始化参数  原始点
thetax = 0.5
thetay = 0.5

while True:  
    flag += 1  
    for i in range(len(x)):  
    #i = random.randint(0,len(x)-1)
        thetax -= alpha*(thetax-x[i])
        thetay -= alpha*(thetay-y[i])   
    error1 = 0  
    for lp in range(len(x)):  
        error1 += (thetax-x[lp])**2/2 +(thetay-y[lp])**2/2
    if abs(error1-error0) < epsilon:  
        break  
    else:  
        error0 = error1  
  
    print ('thetax : %f,  thetay : %f' % (thetax,  thetay)  )
print ('  thetax : %f, thetay : %f' % ( thetax, thetay)  )