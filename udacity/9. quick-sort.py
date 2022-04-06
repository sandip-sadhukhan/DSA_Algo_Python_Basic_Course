"""
Implement Quick sort
"""

array: list[int] = [4, 3, 2, 1]
n: int = len(array)


def partition(arr: list[int], start: int, end: int) -> int:
    pivot: int = arr[end]

    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            # swap
            arr[i], arr[j] = arr[j], arr[i]

    # swap
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quicksort(arr: list[int], start: int, end: int) -> None:

    if start < end:
        pi: int = partition(arr, start, end)

        quicksort(arr, start, pi - 1)
        quicksort(arr, pi + 1, end)


quicksort(array, 0, n - 1)
print(array)
