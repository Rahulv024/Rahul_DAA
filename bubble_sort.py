def bubblesort_alg(array):
    n = len(array)
    for i in range(1, n):
        swapped = False
        for j in range(n - 1, i - 1, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swapped = True
        if not swapped:
            break
    return array

array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubblesort_alg(array)
print("Sorted array is:", sorted_array)
