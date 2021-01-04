import os

def split_sum(num):
    s = str(num)
    res = 0
    for i in s:
       res += int(i)*int(i)
    # print(res)

    return res

# split_sum(19)
n = 2
while True:
    tmp = split_sum(n)
    if tmp == 1:
        print("happy!!")
        break
    else:
        n = split_sum(n)
        if n == tmp:
            print("not happy")
            break
        print(tmp)
        pass