def bs(sort_nums, target):
    m_idx = 0; M_idx = len(sort_nums)
    # print(m_idx, M_idx); os._exit(0)
    while len(sort_nums)>1:
        print(sort_nums)
        if len(sort_nums)%2 == 0:
            middle_idx = int(len(sort_nums)/2)
        else:
            middle_idx = int(len(sort_nums)/2 + 1)
        left = sort_nums[0:middle_idx]
        right = sort_nums[middle_idx:]
        print(left, right)
        if len(left) == 1 and left[-1] == target:
            # M_idx -= 1
            M_idx = M_idx - len(right)
            print("find!!")

            break
        if len(right) == 1 and right[-1] == target:
            # m_idx += 1
            m_idx += len(left)
            print("find!")
            break

        if left[0] <= target and left[-1] >= target:
            M_idx = M_idx - len(right)
            sort_nums = left
            
        elif right[0] <= target and right[-1] >= target:
            m_idx += len(left)
            sort_nums = right 
        else:
            print("not find")
            # print(-1)
            return -1
        # print(m_idx, M_idx)
    # print(sort_nums)
    # print(m_idx, M_idx)
    sort_idx = int((m_idx+M_idx)/2)
    print("sort_idx: ", sort_idx)
    return sort_idx

def binary_search(data, key):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = int((low + high) / 2)
        if key == data[mid]:
            return mid
        elif key > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# bs([0,1,2,3,4,5,6], target=4)
# bs([1,3], target=2)

print(binary_search([0,1,2,3,4,5,6], key=87))