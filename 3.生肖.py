animal_list=["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]
year=int(input("請輸入西元年"))
a=year%12-4
print(animal_list[a])