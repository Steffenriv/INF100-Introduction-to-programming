import numpy as np
arr = np.arange(42,59)

arr[arr % 2 ==1] = 1

print(arr)