#-*-coding:utf8-*-
import pprint
__author__ = 'sherwood'
#检测是否符合要求
def check(input_list):
    if input_list[0]>10 or input_list[1]>7 or input_list[2]>3 or input_list[0]<0 or input_list[1]<0 or input_list[2]<0:
        return 0
    else:
        return 1
#所有的规则
def rules(input_list,rule_number):
    if rule_number==1:
        dif = 7-input_list[1]
        if dif >= input_list[0]:
            input_list[1]+=input_list[0]
            input_list[0]=0
        else:
            input_list[0]-=dif
            input_list[1]+=dif
    if rule_number==2:
        dif = 3-input_list[2]
        if dif >input_list[0]:
            input_list[2]+=input_list[0]
            input_list[0] = 0
        else:
            input_list[0]-=dif
            input_list[1]+=dif
    if rule_number==3:
        dif = 10 - input_list[0]
        if dif>input_list[1]:
            input_list[0]+=input_list[1]
            input_list[1]=0
        else:
            input_list[1]-=dif
            input_list[0]+=dif
    if rule_number==4:
        dif = 3 - input_list[2]
        if dif>input_list[1]:
            input_list[2]+=input_list[1]
            input_list[1]=0
        else:
            input_list[1]-=dif
            input_list[2]+=dif
    if rule_number==5:
        dif = 10 - input_list[0]
        if dif>input_list[2]:
            input_list[0]+=input_list[2]
            input_list[2]=0
        else:
            input_list[2]-=dif
            input_list[0]+=dif
    if rule_number == 6:
        dif = 7 - input_list[1]
        if dif>input_list[2]:
            input_list[1] += input_list[2]
            input_list[2] = 0
        else:
            input_list[2] -= dif
            input_list[1] += dif
def check_state_array(input_list, state_array):
    for i in state_array:
        if i[0]==input_list[0] and i[1]==input_list[1] and i[2]==input_list[2]:
            if i[3]==1:
                return 2
            else:
                return 1
    temp_list = input_list[:]
    temp_list.append(0)
    state_array.append(temp_list)
    return 0
#input_list指的是输入的数组，state_array保存曾经访问过的list，背后会跟着一个flag表示是否被访问过
def bfs_search(input_list,state_array):
    check_state_array(input_list, state_array)
    for i in range(1,7):
        temp_list = input_list[:]
        rules(temp_list,i)
        if temp_list[0]==5 and temp_list[1]+temp_list[2]==5:
            return temp_list
        if temp_list!=input_list:
            #check通过
            if check(temp_list)==1:
                #检测是否在数组当中并且进行操作
                check_state_array(temp_list, state_array)
    #所有的子节点都遍历结束，所以我们标注为１
    for index , i in enumerate(state_array):
        if i[0]==input_list[0] and i[1]==input_list[1] and i[2]==input_list[2] and i[3]==0:
            state_array[index][3]=1
    pprint.pprint(state_array)
    #所有的节点都访问过，并且没有正确答案，我们返回没有结果
    count=0
    for index,i in enumerate(state_array):
        if i[3] == 0:
           break
        count+=1
    if count == len(state_array):
        print('no right answer!')
        return 0
    #递归调用
    input_list[0] = state_array[count][0]
    input_list[1] = state_array[count][1]
    input_list[2] = state_array[count][2]
    bfs_search(input_list,state_array)
if __name__ == '__main__':
    input_list=[10,0,0]
    state_array=[]
    a=bfs_search(input_list,state_array)


