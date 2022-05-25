km=float(input("請輸入路程公里數"))
s=75
if km>1.5:
    add=(km-1.5)/0.25
    if add>1:
        ad=add//1
        p=s+ad*5
        if (add%0.25)!=0:
            pp=p+5
            print(pp)
        else:
            print(p)
    elif add<1: 
        ad=add//1
        p=s+ad*5
        pp=p+5
        print(pp)
else:
    print(s)
