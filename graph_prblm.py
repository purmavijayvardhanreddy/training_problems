# n=int(input())
# m=[]
# for i in range(n):
#     t=[]
#     for j in range(n):
#         t.append(int(input()))
#     m.append(t)
def  fun(mat,i,j,x,y):
    print(i,j)
    if i==x and j==y:
        return True
    
    if j<len(mat) and mat[i][j+1]==1:
        fun(mat,i,j+1,x,y)
    else:
        return 
    if i<len(mat) and mat[i+1][j]==1:
        fun(mat,i+1,j,x,y)
    else:
        return

        

m=[[1,1,0,1],[1,1,0,0],[0,1,0,1],[0,1,1,1]]
x,y=map(int,input().split())
gp={}
for  i in m:
    print(*i)
for i in range(len(m)):
    gp[i]=[]
    for j in range(len(m[i])):
        if m[i][j]==1:
            gp[i].append(j)
print(gp)
fun(gp,0,0,x,y)
    
