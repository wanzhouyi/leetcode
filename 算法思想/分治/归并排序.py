def merge_sort(nums: list):
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    m, n = len(left), len(right)
    i, j = 0, 0
    ans = []
    while i < m and j < n:
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    if i < m:
        ans.extend(left[i:])
    if j < n:
        ans.extend(right[j:])
    return ans


if __name__ == '__main__':
    print(merge_sort([10, 15, 9, 7, 22, 36]))
