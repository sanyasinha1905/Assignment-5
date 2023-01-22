x=float(input("Enter the lenght of the side(in cm):  "))
y=float(input("Enter the lenght of the side(in cm):  "))
z=float(input("Enter the lenght of the side(in cm):  "))
 ####################################
def check(a,b,c):
    if (a+b)>c and (a+c)>b and(b+c)>a:
        x=1
        s=((a+b+c)/2)
        area= (s*(s-a)*(s-b)*(s-c))**0.5
        print('Area of the given triangle is : ',area,'sq.cm')
    else:
        x=0
        print('triangle cannot be formed by the  given dimentions')
#####################################
check(x,y,z)
