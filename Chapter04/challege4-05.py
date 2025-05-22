def f(x):
    try:
        return float(x)
    except ValueError:
        print("floatに変換できませんでした。")
a=f("12")
print(a)

b=f("abc")
print(b)
