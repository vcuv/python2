ch=int(input("國文"))
en=int(input("英文"))
ma=int(input("微積分"))
pe=int(input("體育"))
co=int(input("程設"))
avg=(ch+en+ma+pe+co)/5
print('平均分數:%.2f'%avg)

total=[ch,en,ma,pe,co]
rand=sorted(total)

print("科目最高分:"+str(rand[4]))
print("科目最低分:"+str(rand[0]))
# total=dict([('國文',ch),('英文',en),('微積分',ma),('體育',pe),('程設',co)])

# rand=sorted(dict.keys())
# rand=sorted(total)
# print(rand)