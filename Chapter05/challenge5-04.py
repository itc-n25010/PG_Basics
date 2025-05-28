fav={
        "ブルアカ":"陸八魔アル",
        "学マス":"篠澤広",
}

ans=input("ブルアカor学マス:")
if ans in fav:
    res=fav[ans]
    print(res)
else:
    print("わかりません")
