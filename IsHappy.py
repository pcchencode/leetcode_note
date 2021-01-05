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
            print(tmp)
            print("happy!!")
            return True
            break
        else:
            split_result.append(tmp)
            n = split_sum(n)
            next2_split = split_sum(n)
            if next2_split in split_result:
                print("not happy")
                return False
                break
            print(tmp)
            pass

print(isHappy(2))
print(isHappy(19))