a=int(input('Enter the nuber to divide with'))
b=int(input('Enter the starting of the range'))
c=int(input('Enter the ending of  the range'))+1
for i in range(b,c):
    if i%a==0:
        print(i)
    
