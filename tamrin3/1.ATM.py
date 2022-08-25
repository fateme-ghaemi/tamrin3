ramz_obor=1381
i=0
for i in range(3):
    ramz_obor=int(input('please enter your number:'))
    if ramz_obor==1381:
        
        print('open:)')
        
        break
    elif ramz_obor==1831:
        #call police
        print('!we calld the police!')
        break  
    elif ramz_obor!=1381:
        print('ramz_obor is rong')
        i+=1
    else:
        continue
if i<=3:
    print('locked')
    
         
  