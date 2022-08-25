import random 
list1=[]
list2=[]
for i in range(20):
    lst=random.randint(0,1000)
    list1.append(lst)
    tavan=lst**2
    list2.append(tavan)
print(list1)
print(list2)
