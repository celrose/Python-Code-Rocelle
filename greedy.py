#CMSC 142 - MP#1
#Cadavos, Rocelle Anne

#----------------# KNIGHT'S TOUR #----------------#
print("Knight's Tour")
#Change board size here
m = 8
n = 8

#Change starting point
start_x = 0
start_y = 0

steps = 1
#Generating board
matrix = [[0 for i in range(m)] for j in range(n)]
matrix[start_x][start_y] = steps #Starting Point

s = ''
for i in range(0, m):
    for j in range(0, n):
       s = s + str(matrix[i][j])
    s = s + "\n"

print s #print board initial


def generate_moves():
    
    possible_pos = []
    legal_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    #get curr pos
    #check for neighbors
    return 0

def smallest_possible_moves():
    #check all possible moves' next moves
    #choose the smallest then move there, steps += 1
    return 0

def start_tour():
    return 0
    #generate moves
    #check neighbor
    #return true/false if there is a possible path

#Time complexity: Knight's Tour is linear or O(n)
#----------------# SET COVER PROBLEM #----------------#
print("Set Cover Problem")

#Change universal set here
universal_arr = [1, 2, 3, 4, 5, 6, 7, 8]
#change set of sets here
arr_of_arr = [[1, 2], [7, 8], [2, 3, 4, 5, 6, 7], [1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 7]]
#print uni_set
#print set_of_sets
arr_set = []
temp = 0
for i in range(0, len(arr_of_arr)):
    arr_set.append(len(arr_of_arr[i]))

temp = arr_set.index(max(arr_set))
copy = universal_arr

temp_arr = []
temp_arr.append(arr_of_arr[temp])

print temp_arr, "\n"

#iterate thru set
#find items from universal_arr that is not yet in temp_arr
#append those items

#----------------# COIN CHANGE PROBLEM #----------------#
print("Coin Change Problem")


#Change money here
money = 357
#Change set of coins here
set_of_coins = [1, 2, 5, 10, 50, 100, 500]


print "Money: ", money
print "Set of coins: ", set_of_coins

set_of_coins.reverse()

remaining = money;
set_of = 0;
count_set = [];
holder = 0;

while remaining > 0:
	
	while remaining < set_of_coins[holder]:
		holder = holder + 1
	
	set_of = remaining // set_of_coins[holder]
	remaining = remaining % set_of_coins[holder]

	count_set.append(str(set_of_coins[holder]) + " x " + str(set_of))

print count_set, "\n"

#Time complexity: Coin Change is also linear: O(n) 
#(also depends on how much set of coins we have)

#----------------# SORT ARRAY #----------------#
print("Sorting an Array ")
#Change array here
set_of_numbers = [32, 12, 31, 22, 16, 86, 44, 75, 4, 3, 11, 99, 75, 49]
copy_array = set_of_numbers

sorted_array = []
num_value = copy_array[0]
i = 0

while len(copy_array) > 0:
    if  copy_array[i] < num_value:
        num_value = copy_array[i]
    i = i + 1
    if i == len(copy_array):
        sorted_array.append(num_value)
        copy_array.remove(num_value)
        if copy_array:
          num_value = copy_array[0]
        i = 0

print(sorted_array)

#Time Complenxity: Selection Sort is O(n^2)
