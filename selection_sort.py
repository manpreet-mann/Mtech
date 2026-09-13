def selection_sort(arr):
    for i in range(len(arr)):
        shortestIdx = i
        for j in range(i+1, len(arr)):
            if( arr[j]<arr[shortestIdx]):
                shortestIdx = j
        arr[i], arr[shortestIdx] = arr[shortestIdx], arr[i]
def printArray(arr):
    for i in range (len(arr)):
        print(arr[i], end= " ")
    print()
if __name__ == '__main__':
    # arr = [7,5,4,2]
    arr = list(map(int, input().split()))
    selection_sort(arr)
    printArray(arr)
