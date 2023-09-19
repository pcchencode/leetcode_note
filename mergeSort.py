def find_mid(array):
    L, R = 0, len(array)-1
    return (L+R)//2

def merge(left, right):
    result = []
    i, j = 0, 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    # print(i,j)
    if i==len(left):
        result += right[j:]
    if j==len(right):
        result += left[i:]
    return result

def mergeSort(array):
    
    def helper(array):
        #Base Case
        if len(array)<=1:
            return array

        mid = find_mid(array)
        left = helper(array[0:mid+1]) #包含mid
        right = helper(array[mid+1:])
        return merge(left, right)

    return helper(array)

print(mergeSort([]))
# print(merge([1], [5]))