f=int(input('1.hour/second,2.second/hour:'))
if f==1:
    t=float(input('enter time:'))
    second=t*3600
    print(second,'s')
elif f==2:
    s=int(input('enter second:'))
    hour=s/3600
    print(hour,'hr')
