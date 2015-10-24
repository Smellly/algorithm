#-*-coding:utf8-*-
__author__ = 'sherwood'
import pprint
#检测符合情况
def check(input_array,state_array):
    if input_array[0]==0 and input_array[1]<3:
        return 1
    elif input_array[0]<input_array[1] or input_array[0]<0 or input_array[1]<0 or input_array[0]>3 or input_array[1]>3:
        return 0
    elif input_array[0]<3 and not(input_array[0]==input_array[1]):
        return 0
    elif input_array in state_array:
        return 0
    else:
        return 1
#定义从左边到右边的规则
def l_rules(input_list,rule_number):
    if rule_number==1:
        input_list[0]=input_list[0]-1
        input_list[2]=0
    if rule_number==2:
        input_list[1]=input_list[1]-1
        input_list[2]=0
    if rule_number==3:
        input_list[0]=input_list[0]-2
        input_list[2]=0
    if rule_number==4:
        input_list[1]=input_list[1]-2
        input_list[2]=0
    if rule_number==5:
        input_list[0]=input_list[0]-1
        input_list[1]=input_list[1]-1
        input_list[2]=0
#定义从右边到左边的规则
def r_rules(input_list,rule_number):
    if rule_number==1:
        input_list[0]=input_list[0]+1
        input_list[2]=1
    if rule_number==2:
        input_list[1]=input_list[1]+1
        input_list[2]=1
    if rule_number==3:
        input_list[0]=input_list[0]+2
        input_list[2]=1
    if rule_number==4:
        input_list[1]=input_list[1]+2
        input_list[2]=1
    if rule_number==5:
        input_list[0]=input_list[0]+1
        input_list[1]=input_list[1]+1
        input_list[2]=1
def dfs_search(input_list,state_array):
    #判定搜索条件
    if input_list[0]==0 and input_list[1]==0 and input_list[2]==0:
        print "sucess"
        pprint.pprint(input_list)
        return
    elif input_list in state_array:
        return
    elif not(input_list in state_array):
        state_array.append(input_list)
    else:
        return
    #开始进行搜索
    if input_list[2]==1:
        for i in range(1,6):
            temp_list = input_list[:]
            l_rules(temp_list,i)
            if check(temp_list,state_array)==1:
                input_list = temp_list
                dfs_search(input_list,state_array)
    elif input_list[2]==0:
        for i in range(1,6):
            temp_list = input_list[:]
            r_rules(temp_list,i)
            if check(temp_list,state_array)==1:
                input_list=temp_list
                dfs_search(input_list,state_array)
    return
if __name__ == '__main__':
    input_list=[3,3,1]
    state_array=[]
    dfs_search(input_list,state_array)
    pprint.pprint(state_array)