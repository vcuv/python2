def prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

num=input(int("請輸入一正整數"))
a=[]

for i in range(len(num)):
    for j in range(i,len(num)):
        key=int(num[i:j+1])
        prime(key)
        if prime(key): 
            a.append(key)
print(f"最大的子字串是{max(a)}" 
        if len(a) > 0 else "No prime found")   