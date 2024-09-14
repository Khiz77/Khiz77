import random

class MyArray:

    def __init__(self, size):
        self.array = [random.random() for _ in range(size)]
        self.logical_length = size
        self.physical_length = size * 2

    def __setitem__(self, index, value):
        if 0 <= index < self.logical_length:
            self.array[index] = value
        else:
            raise IndexError("Index is out of range.")

    def __getitem__(self, index):
        if 0 <= index < self.logical_length:
            return self.array[index]
        else:
            raise IndexError("Index is out of range.")

    def __len__(self):
        return self.logical_length
    
    def __str__(self):
        return str(self.array[:self.logical_length])
    

def test_array():
    test = MyArray(5)  # Creating an object of MyArray named test with size 5
    length = len(test)
    for i in range(length):
        value = random.randint(0, 99)
        test[i] = value
    print(f"Contents of test array are: {test}")
    return test, length

def test1_array(test):
    input("Press any key to continue")
    test1 = MyArray(10)  # Creating an object of MyArray named test1 with size 10
    length1 = len(test1)

    for i in range(length1):
        if i < len(test):
            test1[i] = test[i]
        else:
            test1[i] = random.randint(0, 99)

    print(f"Contents of test1 array are: {test1}")
    return test1, length1

def selection_sort(arr):
    i_range = len(arr)
    print(f"test1 = {arr}")
    for i in range(i_range):
        min_index = i
        print(f"We assume test1[{i}] = {arr[i]} as the minimum value and compare it with every other value on the right-hand side.")
        for j in range(i+1, i_range):
            print(f"j = {j}")
            if arr[j] < arr[min_index]:
                min_index = j
            
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"test1 = {arr}")
