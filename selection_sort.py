# 선택정렬
def findSmallListIndex(arr): 
    smallest = arr[0] # 가장 작은 정수를 저장
    smallest_index = 0 # 가장 작은 정수의 인덱스를 저장
    
    for j in range(1, len(arr)):
        if arr[j] < smallest:
            smallest = arr[j]
            smallest_index = j

    return smallest_index

def selectionSort(arr):
    new_array = []
    for i in range(len(arr)):
        smallest = findSmallListIndex(arr)
        new_array.append(arr.pop(smallest))
        
    return new_array

print (selectionSort([5, 3, 6, 2, 10]))
