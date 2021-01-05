import os

def split_sum(num):
    s = str(num)
    res = 0
    for i in s:
       res += int(i)*int(i)
    # print(res)
    return res

def isHappy(n):
    # split_sum(19)
    # n = 2
    split_result = []
    while True:
        tmp = split_sum(n)
        if tmp == 1:
            print("happy!!")
            return True
            break
        else:
            split_result.append(tmp)
            n = split_sum(n)
            n2 = split_sum(n)
            if n2 in split_result:
                print("not happy")
                return False
                break
            # if n == init:
            #     print("not happy")
            #     break
            print(tmp)
            pass

print(isHappy(2))