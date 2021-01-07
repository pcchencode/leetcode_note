import os
# https://ithelp.ithome.com.tw/articles/10213280


def syn_lst(l):
    if len(l)%2!=0:
        return False
    mid = int((len(l)+1)/2)
    pre = l[0:mid]
    post = l[mid:]
    post.reverse()
    if pre==post:
        return True
    else:
        return False


def split_lst(l):
    res = []
    i = 0
    while i*2+1 <= len(l):
        print(i, i*2+1)
        res.append(l[i:i*2+1])
        i = i*2 + 1
    return res


lst = [1,2,2,3,4,4,3]
sub_lst = split_lst(lst)
result = True
for lsts in sub_lst[1:]:
    if syn_lst(lsts)!=True:
        result = False
        break

print(result)        
    



