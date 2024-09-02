def insertionsort_alg(array):
    for i in range(1, len(array)):
        k = array[i]
        j = i - 1
        while j >= 0 and k < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = k
        
array = [12, 11, 13, 5, 6]
print("The original array is:", array)
insertionsort_alg(array)
print("The sorted array is:", array)