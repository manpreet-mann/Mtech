def quick_sort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)

        quick_sort(arr, low, pivotIndex - 1)
        quick_sort(arr, pivotIndex + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr) - 1)

    printArray(arr)