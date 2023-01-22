rows = int(input("Enter no.of rows: "))
alphabet = 65
i = 0
while(i< rows):
    j=0
    while(j<= i):
        print('%c'%alphabet, end ='' )
        if alphabet==90:
            alphabet=65
        else:
            alphabet+= 1
        j+=1
    print()
    i+=1
    
