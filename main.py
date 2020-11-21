'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

a=input()
l=[]
l[:0]=a
l2=[]
for i in range(0,len(l)-1):
    l1=[]
    for j in range(i,len(l)):
        if(l[j] not in l1):
            l1.append(l[j])
        else:
            break
    l2.append(len(l1))
print(max(l2))