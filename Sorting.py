def bubbule_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def selection_sort(nums):
    for i in range(len(nums)-1):
        index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[index]:
                index = j
        if index != i:
            nums[i], nums[index] = nums[index], nums[i]
    return nums

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums

def quick_sort(nums, low, high):
    if low >= high:
        return
    pivot_index = partition(nums, low, high)
    quick_sort(nums, low, pivot_index-1)
    quick_sort(nums, pivot_index+1, high)

def partition(nums, low, high):
    pivot_index = int((low+high)/2)
    nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
    i = low
    for j in range(low, high):
        if nums[j] <= nums[high]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i

def merge_sort(nums):
    if len(nums) == 1:
        return
    middle_index = int(len(nums)/2)
    left = nums[:middle_index]
    right = nums[middle_index:]
    merge_sort(left)
    merge_sort(right)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        nums[k] = right[j]
        k += 1
        j += 1



if __name__ == '__main__':
    a = [1, 5, 3, 2, 4, 8, 7]
    print(bubbule_sort(a))
    print(selection_sort(a))
    print(insertion_sort(a))
    quick_sort(a, 0, len(a)-1)
    print(a)
    b = [1, 5, 3, 2, 4, 8, 7]
    merge_sort(b)
    print(b)
