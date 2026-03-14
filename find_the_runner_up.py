# find the runner up score

import bisect

n = 5
arr = [2, 3, 6, 6, 5]

arr = list(arr)
arr.sort()
maximum = max(arr)
print(arr[bisect.bisect_left(arr, maximum)-1])