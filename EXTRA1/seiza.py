mon=input("月を入力してください:")
mon=int(mon)

day=input("日を入力してください:")
day=int(day)

seiza_list=["", "山羊", "水瓶", "魚", "牡羊", "牡牛", "双子",
              "蟹", "獅子", "乙女", "天秤", "蠍", "射手"]

seiza=seiza_list[mon]

if mon == 2:
    if day >= 19:
        seiza=seiza_list[mon +1]
if mon == 1 or 4:
    if day >= 20:
        seiza=seiza_list[mon +1]
if mon == 3:
   if day >= 21:
        seiza=seiza_list[mon +1]
if mon == 6 or 12:
    if day >= 22:
        seiza=seiza_list[mon +1]
if mon == 7 or 8 or 11:
    if day >= 23:
        seiza=seiza_list[mon +1]
if mon == 10:
    if day >= 24:
        seiza=seiza_list[mon +1]

print("あなたの星座は{}座です。".format(seiza))
