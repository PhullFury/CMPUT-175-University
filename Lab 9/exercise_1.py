import random
import time

#---------------------------------------#      
# Implement Recursive selection sort here. 

# n: size of array - index is index of starting element
def recursive_selection_sort(data, data_len, index = 0): 
    if (index < data_len - 1):  # "loops" until reaches the end of the list
        temp = data[index]
        big_index = find_biggest_index(data, data_len, index, index)
        data[index] = data[big_index]
        data[big_index] = temp
        index += 1
        recursive_selection_sort(data, data_len, index)

def find_biggest_index(data, data_len, index, big_index):
    if (index < data_len):  # loops until the end of the list
        if (data[index] > data[big_index]):  # if the current index is bigger than the previous changes them
            big_index = index
        index += 1
        return find_biggest_index(data, data_len, index, big_index)
    else:
        return big_index

#---------------------------------------#
#Implement the Recursive merge sort here
  
def recursive_merge_sort(data): 
    if (len(data) <= 1):  # if the list is empty or has 1 one elements returns it as is
        return data
    middle = len(data)//2  # find the middle index
    left = recursive_merge_sort(data[:middle])
    right = recursive_merge_sort(data[middle:])
    return merge(left, right, 0, 0, [])

def merge(left, right, i, j, result):
    if (i < len(left) and j < len(right)):  # "loops" until one of the indexes gets bigger than the final index
        if (left[i] >= right[j]):  # if the left index is bigger appends it to the result list
            result.append(left[i])
            i += 1
            return merge(left, right, i, j, result)
        else:  # else appends the right index to the result list
            result.append(right[j])
            j += 1
            return merge(left, right, i, j, result)
    else:
        # "dumps" all the remaining elements into the result list
        result += left[i:]
        result += right[j:]
        return result

#---------------------------------------#
if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))