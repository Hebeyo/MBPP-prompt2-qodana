def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1]*n
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n):
        maximum = max(maximum , lis[i])
    return maximum
