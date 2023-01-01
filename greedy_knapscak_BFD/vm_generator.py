# %%
import random

# %%
random.randint(20,30)

# %%
def overloadInstanceGenerator(num:int, capacity:int):
    # input check
    if num < 2 or capacity <= 0:
        return
    # generate
    while True:
        # instance = weight, value
        weight_list = []
        value_list=[]
        # calculate mean (must be integer)
        weight_mean = capacity//num
        
        for _ in range(0,num):
            weight_list.append(random.randint(weight_mean-15,weight_mean+10))
            value_list.append(random.randint(50,100))
        # check whether the sum of instances is overloaded
        sum_check = sum(weight_list)
        if sum_check < capacity:
            continue
        else:
            return weight_list,value_list
        

# %%
overloadInstanceGenerator(5,100)

# %%
def unoverloadInstanceGenerator(num:int, capacity:int):
    # input check
    if num < 2 or capacity <= 0:
        return
    # generate
    while True:
        # instance = weight, value
        weight_list = []
        value_list=[]
        # calculate mean (must be integer)
        weight_mean = capacity//num

        for _ in range(0,num):
            weight_list.append(random.randint(weight_mean-10,weight_mean+10))
            value_list.append(random.randint(50,100))
        sum_check = sum(weight_list)
        # check whether the sum of instances is unoverloaded
        if sum_check <= capacity-25:
            #print(sum_check)
            return weight_list,value_list
        else:
            continue

# %%
unoverloadInstanceGenerator(5,100)

# %%
def InstanceGenerator(num:int = 5,size:int = 100, capacity:int = 100):
    a = []
    b = []
    for i in range(int(size*0.4)):
        a.append(overloadInstanceGenerator(5,capacity))
        
    for i in range(int(size*0.6)):
        b.append(unoverloadInstanceGenerator(5,capacity))      
    return a,b

# %%
InstanceGenerator(5,100)

# %%



