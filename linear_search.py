def liner_search(arr, x):
    n = len(arr)
    for i in range(0, n):
        if(arr[i]==x):
            return i
    return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5,9]
    x= 3
    result= liner_search(arr, x)
    if(result == -1):
        print("Element not present")
    else:
        print("Element is present. its index is: ", result)