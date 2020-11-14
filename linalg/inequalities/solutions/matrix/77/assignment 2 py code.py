def NbyNMul(A,B):
    lst=[]
    str1=0
    str2=0
    newlst=[]
    
    for x in range(len(B[0])):
        for i in A:
            j=0
            for z in B:
                str1=i[j]*z[x]
                j+=1
                str2=str2+str1
            lst.append(str2)
            str2=0
    tstcount=0
    while tstcount<len(B):
        col=[]
        for i in range(0,len(lst),len(B)):
            col.append(lst[tstcount+i])
        newlst.append(col)
        tstcount+=1
    return newlst	
	
def constmul(a,const):
    for i in range(len(a)):
        for j in range(len(a)):
            a[i][j]*=const
    return a
	
	
def addmat(a,b):
    for i in range(len(b)):
        for j in range(len(b)):
            a[i][j]=a[i][j]+b[i][j]
    return a
	
def submat(a,b):
    for i in range(len(b)):
        for j in range(len(b)):
            a[i][j]=a[i][j]-b[i][j]
    return a
	
#Main program starts from here
I=[[1,0],[0,1]]
A=[[3,-6],[1,-2]]
Result=[]
templst=[]
templst=addmat(I,A)
templst=NbyNMul(NbyNMul(templst,templst),templst)
Result=submat(templst,constmul(A,7))
print(Result)