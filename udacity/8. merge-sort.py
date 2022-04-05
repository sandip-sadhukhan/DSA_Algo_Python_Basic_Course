"""Merge sort implementation"""

arr: list[int] = [4, 3, 2, 1]
n: int = len(arr)


def merge(arr: list[int], start: int, mid: int, end: int) -> None:
    leftArrLength: int = mid - start + 1
    rightArrLength: int = end - mid

    leftArr: list[int] = []
    rightArr: list[int] = []

    # copy the elements
    for i in range(0, leftArrLength):
        leftArr.append(arr[start + i])
    for j in range(0, rightArrLength):
        rightArr.append(arr[mid + 1 + j])

    i = 0
    j = 0
    k = start

    while i < leftArrLength and j < rightArrLength:
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    while i < leftArrLength:
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < rightArrLength:
        arr[k] = rightArr[j]
        j += 1
        k += 1


def merge_sort(arr: list[int], start: int, end: int) -> None:
    if start < end:
        mid: int = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


merge_sort(arr, 0, n - 1)
print(arr)
