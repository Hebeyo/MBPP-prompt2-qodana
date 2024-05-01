def shell_sort(my_list):
    n = len(my_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = my_list[i]
            j = i
            while j >= gap and my_list[j - gap] > temp:
                my_list[j] = my_list[j - gap]
                j -= gap
            my_list[j] = temp
        gap //= 2
    return my_list
