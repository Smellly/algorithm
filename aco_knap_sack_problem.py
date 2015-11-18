#-*-coding:utf8-*-
#author sherwood
#在背包问题当中使用蚁群算法
import random
import pprint
#输入主要为，重量List，价格list，背包的容量，输出一个最优解,蚂蚁的数量,迭代次数
def aco_knap_sack(weight,price,package_capacity,ants_number,iter_num,rho):
    #首先对输入进行判断
    if not len(weight)==len(price):
        print("the input isn't right!")
        exit()
    else:
        length = len(weight)
    #定义初始化的概率每一条路径行走的概率
    route_proba=[]
    for i in range(length):
        route_proba.append(1./float(length))
    #下面来进行具体蚂蚁的行走
    best_route=[]
    best_price=0
    #外循环定义迭代次数
    for i in range(iter_num):
        #内循环定义每一只蚂蚁
        for j in range(ants_number):
            #初始化每一个蚂蚁的选择
            ant_pass_route=[]
            #背包当中的重量
            ant_weight=0
            #价格
            ant_price=0
            ant_chose_flag=True
            while ant_weight<package_capacity:
                while ant_chose_flag:
                    #随机的选择一个
                    ant_chose_index = random.randint(0,length-1)
                    if ant_chose_index not in ant_pass_route and route_proba[ant_chose_index]>random.random():
                        ant_chose_flag=False
                ant_price+=price[ant_chose_index]
                ant_weight+=weight[ant_chose_index]
                ant_pass_route.append(ant_chose_index)
                ant_chose_flag=True
            #循环结束，进行一定的迭代处理，由于循环到最后，又加上了一个不必要的值，所以我们来进行具体的操作
            last_ant_route_index = len(ant_pass_route)-1
            ant_price-=price[ant_pass_route[last_ant_route_index]]
            ant_weight-=weight[ant_pass_route[last_ant_route_index]]
            del ant_pass_route[last_ant_route_index]
            #来进行具体的比较
            if best_price<ant_price:
                best_price=ant_price
                best_route=ant_pass_route[:]
        #现在开始对选择概率进行更新
        for k in range(length):
            if k in best_route:
                route_proba[k]=float(route_proba[k])*rho+rho/float(len(best_route))
            else:
                route_proba[k]=float(route_proba[k])*rho
        pprint.pprint(best_route)
        pprint.pprint(best_price)
        pprint.pprint(route_proba)
        pprint.pprint(i)
if __name__ == '__main__':
    #进行具体的定义
    weight=[]
    price=[]
    for i in range(10):
        weight.append(random.randint(1, 10))
        price.append(random.randint(1, 10))
    package_capacity = 20
    aco_knap_sack(weight,price,package_capacity,10,50,0.5)
    print ("done")
