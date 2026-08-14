def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)

# Main Program
arr = list(map(int, input("Enter numbers: ").split()))

print("Before Sorting:", arr)
print("After Sorting:", quick_sort(arr)) 

