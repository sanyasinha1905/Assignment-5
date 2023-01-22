a=int(input('Enter the number: '))
Prime=True
if  a==1:
    print('1 is not a Prime number')
elif a>1:
    for i in range(2,a):
        if a%i==0:
            Prime=False
if Prime==True:
    print (a,'is a Prime number')
else:
    print(a,'is not a Prime number')



        
        
