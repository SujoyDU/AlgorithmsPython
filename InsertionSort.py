def insertionSort(Arr):
    n = len(Arr)
    print("Lenth of the Array is: {:d}".format(n))
    print("Content of the array: {}".format(Arr))

    for i in range(1,n):
        j=i
        for j in range(j,0,-1):
            if(Arr[j] < Arr[j-1]):
                low = Arr[j]
                Arr[j] = Arr[j-1]
                Arr[j-1] = low

    print("Content of the sorted array: {}".format(Arr))



if __name__ == "__main__":
    arr = [5,3,1,9,8,10,2,6]
    insertionSort(arr)
    print(arr)


"""
Insertion Sort Algorithm:

Array Size = N

i=2

for i to N:
    j=i
    for j lower to 1:
        if(A[j] < A[j-1]):
            low = A[j]
            A[j] = A[j-1]
            A[j-1] = low
    

"""


