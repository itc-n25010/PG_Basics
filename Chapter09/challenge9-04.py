import csv

mov=[
        ["トップガン","危険な情事","マイノリティ・リポート"],
        ["タイタニック","レヴェナント: 蘇えりし者","インセプション"],
        ["トレーニング・デイ","マン・オン・ファイア","フライト"]]

with open("movie.csv","w",encoding="utf-8")as f:
    w=csv.writer(f,delimiter=",")
    for movie in mov:
        w.writerow(movie)
