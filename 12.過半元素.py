a2=input("輸入一串序列(以空格隔開):")
list_1=a2.split(" ")
many=max(list_1,key=list_1.count)

if list_1.count(many)>=len(list_1)/2:
    print("過半元素為:",many)
else:
    print("過半元素為:NO")