a1=int(input("輸入第一行正整數為:"))

a2=input("第二行中數列中的數字為(以空格隔開):")
list_1=a2.split(" ")
set1=set(list_1)
many=max(list_1,key=list_1.count)

if a1==len(list_1):
    if len(list_1)==len(set1):
        print("每個數字剛好只出現一次")
    else:
        print("最大出現次數的數字為:" ,many)
        print("出現次數為:",list_1.count(many)) 
        # 好難

