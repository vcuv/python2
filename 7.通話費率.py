a=int(input("請輸入所選方案(186,386,586,986)"))
b=int(input("請輸入通話時間(秒)"))
if a==186:
    if (b*0.09)<186:
        print("通話費為:186")
    elif (b*0.09)>186:
        if (b*0.09)>186*2:
            print("通話費為:"+str(round(b*0.09*0.8)))
        else:
            print("通話費為:"+str(round(b*0.09*0.9)))
elif a==386:
    if (b*0.08)<386:
        print("通話費為:386")
    elif (b*0.08)>386:
        if (b*0.08)>386*2:
            print("通話費為:"+str(round(b*0.08*0.7)))
        elif (b*0.08)<386*2:
            print("通話費為:"+str(round(b*0.08*0.8)))
elif a==586:
    if (b*0.07)<386:
        print("通話費為:586")
    elif (b*0.07)>586:
        if (b*0.07)>586*2:
            print("通話費為:"+str(round(b*0.07*0.6)))
        else:
            print("通話費為:"+str(round(b*0.07*0.7)))
elif a==986:
    if (b*0.06)<986:
        print("通話費為:986")
    elif (b*0.06)>986:
        if (b*0.06)>986*2:
            print("通話費為:"+str(round(b*0.06*0.5)))
        else:
            print("通話費為:"+str(round(b*0.06*0.6)))