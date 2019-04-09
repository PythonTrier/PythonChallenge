def read_succ_from(s, i):
    x = s[i]
    i = i + 1
    y = x

    while i < len(s) and s[i] == x:
        y = y + s[i]
        i = i + 1

    return y, i


def split_str(x):
    i = 0
    xs = []

    while i < len(x):
        y, i = read_succ_from(x, i)
        xs.append(y)

    return xs


def pack_seq(xs):
    s = ""

    for x in xs:
        s = s + str(len(x)) + x[0]

    return s


def next_id(x):
    xs = split_str(x)
    x2 = pack_seq(xs)
    return x2


x = "1"
for i in range(31):
    print(i, x)
    x = next_id(x)