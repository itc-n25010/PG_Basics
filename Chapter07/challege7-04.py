num=[11,22,33,44,55]
while True:
    ans=input("数字を当てよう!:")
    if ans=="q":
        break
    try:
        ans=int(ans)
    except ValueError:
        print("数字を入力するか、qで終了します")
    if ans in num:
        print("正解!")
    else:
        print("不正解")
