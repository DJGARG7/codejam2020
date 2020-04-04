T=int(input())
for t in range(T):
    entries=[]
    newl=[]
    temp=[]
    rc=0
    cc=0
    sum=0
    for i in range(N):
        entries.append(list(map(int, input().split())))
        sum=sum+entries[i][i]
        z=list(set(entries[i]))
        if len(z) != len(entries[i]):
            rc=rc+1
    for i in range(N):
        temp=[]
        for j in range(N):
            temp.append(entries[j][i])
        newl.append(temp)
        z=list(set(newl[i]))
        if len(z) != len(newl[i]):
            cc=cc+1
    print('Case #{}: {} {} {}'.format(t+1,sum,rc,cc))