import random
f=1
while f==1:
    janken_list=["グー","チョキ","パー"]
    Pl=input("グー,チョキ,パーのいずれかを入力:")
    npc=random.randint(0,2)
    npc_list=janken_list[npc]

    if Pl == "グー":
        if npc == 0:
            print("あなたの手:{} 相手の手:{}".format(Pl,npc_list))
            print("あいこ")
        elif npc == 1:
            print("あなたの手:{} 相手の手:{}".format(Pl,npc_list))
            print("勝ち")
        else:
            print("あなたの手:{} 相手の手:{}".format(Pl,npc_list))
            print("負け")

    if Pl == "チョキ":
        if npc == 1:
            print("あなたの手:{} 相手の手:{}".format(Pl,npc_list))
            print("あいこ")
        elif npc == 2:
            print("あなたの手:{} 相手の手:{}".format(Pl,npc_list))
            print("勝ち")
        else:
            print("あなたの手:{} 相手の手:{}".format(Pl,npc_list))
            print("負け")

    if Pl == "パー":
        if npc == 2:
            print("あなたの手:{} 相手の手:{}".format(Pl,npc_list))
            print("あいこ")
        elif npc == 0:
            print("あなたの手:{} 相手の手:{}".format(Pl,npc_list))
            print("勝ち")
        else:
            print("あなたの手:{} 相手の手:{}".format(Pl,npc_list))
            print("負け")
    if Pl == "0":
        print("じゃんけんを終了します")
        break

