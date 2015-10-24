#-*-coding:utf8-*-
__author__ = 'sherwood'
import pprint
import random
import math
#模拟退火算法解决旅行商问题
#首先要解决的是初始化的问题n为城市的数量，i为初始序列，dis为城市之间的距离
def initial(n,route,dis):
    #初始化序列
    for i in range(0,n):
        route.append(i)
    random.shuffle(route)
    for i in range(0,n):
        for j in range(0,n):
            dis[i].append(random.uniform(1,100))
def caculate_dis(route,dis_array,dis=0):
    length = len(dis_array)
    for i in range(0,length):
        if i==(length-1):
            if route[0]>route[(length-1)]:
                dis+=dis_array[route[(length-1)]][route[0]]
                return dis
            else:
                dis+=dis_array[route[0]][route[(length-1)]]
                return dis
        if route[i+1]>route[i]:
            dis+=dis_array[route[i]][route[i+1]]
        else:
            dis+=dis_array[route[i+1]][route[i]]
def generate(route):
    length = len(route)
    start = random.randint(0,(length-2))
    end = random.randint(start+1,length-1)
    i=start
    j=end
    while not(i>j):
        temp = route[i]
        route[i]=route[j]
        route[j]=temp
        i+=1
        j-=1
def sa(route,dis_array,t,l):
    unchange=0
    for i in range(0,l):
        pri_dis = caculate_dis(route,dis_array)
        #随机的改变一些序列
        last_route = route[:]
        generate(last_route)
        last_dis = caculate_dis(last_route,dis_array)
        if last_dis >pri_dis:
            df = last_dis-pri_dis
            pro = math.exp(-df)
            #如果达到概率，那么我们就进行操作
            if random.uniform(0,1)<pro:
                route = last_route
                unchange=0
            else:
                unchange+=1
        else:
            unchange=0
            route = last_route
        if unchange>2:
            return
        pprint.pprint(route)
        pprint.pprint(caculate_dis(route,dis_array))


        t=t*.9




if __name__=='__main__':
    n=10
    route=[]
    dis_array = [[] for i in range(n)]
    initial(n,route,dis_array)
    t=100
    l=20000
    dis=0


    sa(route,dis_array,100,l)