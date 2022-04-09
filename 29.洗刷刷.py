l1=input("甲方的數字")
l2=input("乙方的數字")
l1_=l1.split(" ")
l2_=l2.split(" ")
for i in range(len(l1_)):

    if l1_[i]==l2_[i]:
        print("和")
    elif l1_[i]>l2_[i]:
        print("贏")
    else:
        print("輸")

