import random
x=0
y=100
i=1
while i!='true':
    num=random.randint(x,y)
    print(num)
    javab=input('true or false?')
    if javab=='true':
      print('i win')
      print(i)
      break
      
    elif javab=='bigger':
      x=num+1
      x=num
    elif javab=='lower':
      y=num 
    #i+=1