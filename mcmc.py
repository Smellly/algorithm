# -*- coding: utf-8 -*-
import random
"""
Spyder Editor

This is a temporary script file.
"""
#由于作业主要是进行MCMC算法的编写，所以这里就不考虑复杂的贝叶斯网络了
#首先我们定义cloud(隐含变量)以及rain（需要计算的变量）的转移概率
#我们假设，当r=flase的时候 pc为真的概率为：
pc_rf=0.3
#我们假设当r=true的时候，cloud为真的概率，
pc_rt=0.4
#同理，我们也需要设置相同情况下r的概率
pr_cf=0.6
pr_ct=0.8
#我们来进行具体的统计
#设置N=1000
N=1000
#初始的时候，设置两个都为真第一个是r，第二个代表c
initial=[1,1]
total=0
total_true=0
for i in range(0,1000):
    #开始进行更新c的操作
    if initial[0]==1:
        total_true+=1
        total+=1
        if random.random() >0.4:
            initial[1]=0
        else:
            initial[1]=1
    elif initial[0]==0:
        total+=1
        if random.random()>0.3:
            initial[1]=0
        else:
            initial[1]=1
    #开始进行r的转移操作：
    if initial[1]==1:
        if random.random()>0.8:
            initial[0]=0
            total+=1
        else:
            initial[0]=1
            total_true+=1
            total+=1
        
    else:
        if random.random()>0.6:
            initial[0]=0
            total+=1
        else:
            initial[0]=1
            total_true+=1
            total+=1
print(float(total_true)/float(total))