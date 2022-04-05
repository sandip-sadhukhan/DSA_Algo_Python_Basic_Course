"""
Implementation of bubble sort.
"""

arr = [4, 3, 2, 1]
n = len(arr)

print("Original Array: ", arr)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # swap
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

    print(f"After {i+1} iteration: {arr}")
