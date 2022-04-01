word=input("請輸入連續字元")
if str(word)==word[::-1]:
    print("YES")
else:
    print("NO")