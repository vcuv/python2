
ans=list(input('enter'))
res=list(input("輸入你的答案"))
a=0
b=0
for i in range(len(ans)):
    if ans[i]==res[i]:
        a+=1
    elif res[i] in ans:
        b+=1
ans1="".join(ans)

if a==len(ans):
    print("%dA%dB" %(a,b) + '全對')
else:
    print("%dA%dB" %(a,b) + '加油')
