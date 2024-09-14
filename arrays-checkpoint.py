""" def selection_sort(arr):
    i_range = len(arr)
    for i in range(i_range):
        j_range = i_range - 1
        for j in range(i+1, j_range):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr """

def bubble_sort(arr):
	i_range = len(arr)
	for i in range(i_range):
		j_range = i_range-i-1
		for j in range(j_range):
			if arr[j]>arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr





test = [29, 28, 12, 21, 3]

test1 = test + [4, 5, 6, 2, 8]

length_test1 = len(test1)

print(f"The contents of test1 array are {test1}")
print(f"The length of test1 array is {length_test1}")

bblsrt = bubble_sort(test1)
print(bblsrt)
""" sltsrt = selection_sort(test1)
print(sltsrt)
 """
