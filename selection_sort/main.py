def selectionSort(array, size):
    for i in range(size-1):
        min_value = array[i]
        min_index = i

        for j in range(i + 1, size):
            if min_value > array[j]:
                min_value = array[j]
                min_index = j

        if min_index != i:
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp


array = [3, 4, 5, 6, 76, 45, 3, 3, 5, 7, 7, 9, 0, 76, 5, 3]
size = len(array)
selectionSort(array, size)
print(array)
