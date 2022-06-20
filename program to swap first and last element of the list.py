'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
n=int(input("enter no of elements:"))
list1=[]
for i in range(1,n+1):
    e=int(input("enter the element"))
    list1.append(e)
   
y=len(list1)-1 
z=list1[0]
list1[0]=list1[y]
list1[y]=z
    
print(list1)
