"Binary Search implementation in python"


def binary_search(input_array: list[int], value: int) -> int:

    left: int = 0
    right: int = len(input_array) - 1

    while left <= right:
        mid: int = (left + right) // 2

        if input_array[mid] == value:
            return mid
        elif input_array[mid] > value:
            # go to the left side
            right = mid - 1
        else:
            # go to the right side
            left = mid + 1

    return -1


def binary_search_recursion(
    input_array: list[int], value: int, left: int, right: int
) -> int:
    mid: int = (left + right) // 2

    if left > right:
        return -1
    elif input_array[mid] == value:
        return mid
    elif input_array[mid] > value:
        return binary_search_recursion(input_array, value, left, mid - 1)
    else:
        return binary_search_recursion(input_array, value, mid + 1, right)


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print("----------")

left = 0
right = len(test_list) - 1
print(binary_search_recursion(test_list, test_val1, left, right))
print(binary_search_recursion(test_list, test_val2, left, right))
