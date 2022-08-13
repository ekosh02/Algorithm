def binatySearch(arr, item):
    low = 0
    high = len(arr) - 1
    mid = 0

    count = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < item:
            count += 1
            low = mid + 1
        elif arr[mid] > item:
            count += 1
            high = mid - 1
        else:
            count += 1
            return mid, count
    return -1


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22]

item = 4

print('lenght -', len(arr))

result = binatySearch(arr, item)

print('item, count -', result)
