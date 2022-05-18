n=int(input("請輸入有幾筆測試資料1~20"))

for j in range(n):   
    n4=[]  
    for i in range(4):
        n1=int(input('請輸入已知數列前四端'))
        n4.append(n1)
    if n4[3]-n4[2]==n4[2]-n4[1]==n4[1]-n4[0]:
        l=n4[3]+(n4[3]-n4[2])
        n4.append(l)
        print(n4)
        print("此為等差數列")
    elif n4[3]/n4[2]==n4[2]/n4[1]==n4[1]/n4[0]:
        ll=int(n4[3]*(n4[3]/n4[2]))
        n4.append(ll)
        print(n4)
        print("此為等比數列")











