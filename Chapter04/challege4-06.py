def f(x):
    """
受け取った整数を2倍にします。
    """
    return x**2


def p(x):
    """
受け取った文字列を出力します。
    """
   print(x)


def f(a,b,c,x=10,y=5):
    """
５つの整数を足します。
最低３つの整数が必要です。
    """
    return a+b+c+x+y


def i(x):
    """
受け取った整数を2で割ります。
受け取っ整数に4をかけます。
    """
    return x/2

def j(x):
    return x*4


def f(x):
    """
受け取った文字列を整数に変換します。
    """
    try:
        return float(x)
    except ValueError:
        print("floatに変換できませんでした。")

