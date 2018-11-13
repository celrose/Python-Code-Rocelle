import string
import random
import numpy

#CMSC 142 - MP#2
#Cadavos, Rocelle Anne


#function to randomize items in array
def arr_randomizer(arr, s):
	for i in range(0, s):
		arr.append(random.randint(1, 100))
	return arr

#---------------- BINARY SEARCH ----------------#
#Time complexity: O(log n)

def binary_search(arr, find):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr) // 2
        #remove print if you do not want to see iteration
    	print "Currently at: %d" %arr[midpoint]
        if arr[midpoint] == find:
        	return True
        else:
        	if find < arr[midpoint]:
        		return binary_search(arr[:midpoint], find)
        	else:
        		return binary_search(arr[midpoint + 1:], find)


#edit s = size of array
s = 10
arr = []
find = random.randint(1,100)

arr_randomizer(arr, s)

arr.sort()
print "BINARY SEARCH"
print "Is %d in: " %find
print arr
print (binary_search(arr, find))


#---------------- MERGE SORT ----------------#
#Time complexity: Θ(n log n)

def merge_sort(arr2):
    
    if len(arr2) > 1:
        mid = len(arr2) // 2
        lefthalf = arr2[:mid]
        righthalf = arr2[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr2[k] = lefthalf[i]
                i = i + 1
            else:
                arr2[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            arr2[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            arr2[k]=righthalf[j]
            j = j + 1
            k = k + 1
    

arr2 = []
arr_randomizer(arr2, s)
print "\nMERGE SORT"
print "Before Merge Sort: ", arr2

merge_sort(arr2)
print "After Merge Sort: ", arr2


#---------------- MATRIX MULTIPLICATION ----------------#
#Time complexity: O(n^2)

def matrix_mult(matrix):
	#divide matrix by smaller cells
	#N/2 x N/2
	return matrix



#creating Matrix
row, col = 8, 8
matrix = [[0] * row for i in range(col)]

for a in range(0, row):
	for b in range(0, col):
		matrix[a][b] = random.randint(0, 10)


print "\nMATRIX MULTIPLICATION"
print "Given: \n", matrix		

#print matrix_mult(matrix)


