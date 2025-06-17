import csv

mov=[
        ["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]]

with open("movie.csv","w")as f:
    w=csv.writer(f,delimiter=",")
    for movie in mov:
        w.writerow(movie)
