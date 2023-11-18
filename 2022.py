# 2022. Convert 1D Array Into 2D Array

def convert_1D_to_2D(arr,m,n):
    return [arr[i:i+n] for i in range(0,len(arr),n)] if len(arr) == m*n else []


arr = [1,2,3,4,5,6]
m,n = 2,3
print(convert_1D_to_2D(arr,m,n))

