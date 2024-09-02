def selectionsort_alg(Array):
    for i in range(len(Array) - 1):  
        min = i              
        for j in range(i + 1, len(Array)):  
            if Array[j] < Array[min]:  
                min = j
        
        Array[i], Array[min] = Array[min], Array[i]


Array = [64, 25, 12, 22, 11]
print("Original array:", Array)
selectionsort_alg(Array)
print("Sorted array:", Array)
