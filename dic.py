# d={'hyd':'blr','blr': 'delhi','blr':"che","che":'goi','goi':'mub'}
d={}
s='hyd'
des='delhi'
f=0
while(s in d):
    if s==des:
        f=1
        print('yes')
        break

    s=d[s]
    # print(s)
if f==0:
    if s==des:
        print('Yes')
    else:
        print('no')