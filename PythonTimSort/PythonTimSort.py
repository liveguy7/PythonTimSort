import sys
from tkinter import INSERT

def binarySearch(lst,item,start,end):
    if(start == end):
        return start if lst[start] > item else start + 1
    if(start > end):
        return start
    mid = (start + end) // 2
    if(lst[mid] < item):
        return binarySearch(lst,item,mid+1,end)
    elif(lst[mid] > item):
        return binarySearch(lst,item,start,mid-1)

    else:
        return mid

def insertionSort(lst):
    length = len(lst)
    for index in range(1,length):
        value = lst[index]
        pos = binarySearch(lst,value,0,index-1)
        lst = lst[:pos] + [value] + lst[pos:index] + lst[index+1:]

    return lst

def merge(left,right):
    if(not left):
        return right
    if(not right):
        return left
    if(left[0] < right[0]):
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left,right[1:])

def timSort(lst):
    length = len(lst)
    runs,sortedRuns = [], []
    newRun = [lst[0]]
    sortedArray = []
    i = 1
    while(i < length):
        if(lst[i] < lst[i-1]):
            runs.append(newRun)
            newRun = [lst[i]]
        else:
            newRun.append(lst[i])
        i = i + 1
    runs.append(newRun)
    for run in runs:
        sortedRuns.append(insertionSort(run))
    for run in sortedRuns:
        sortedArray = merge(sortedArray, run)

    return sortedArray

lst = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print(lst)
sortedList = timSort(lst)
print(sortedList)





