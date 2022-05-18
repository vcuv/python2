n=int(input("輸入一個正整數1~1000"))
if n%2==0 and n%11==0 and n%5!=0 and n%7!=0:
    print(str(n)+"為新公倍數?:yes")
else:
    print(str(n)+"為新公倍數?:no")