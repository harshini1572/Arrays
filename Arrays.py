#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1. Given an array, check if it contains any duplicates or not.

def contains_duplicates(arr):
    return len(arr) != len(set(arr))

# Example usage:
arr = [1, 2, 4, 2, 5, 9]
print(contains_duplicates(arr))


# In[2]:


#Q2. Given an array and an integer k, rotate the array to the right by k steps.

def rotate_array(arr, k):
    k = k % len(arr)  # In case k is larger than the array length
    return arr[-k:] + arr[:-k]

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(arr, k)) 


# In[3]:


#Q3. Reverse the given array in-place, means without using any extra data structure.

def reverse_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Example usage:
arr = [2, 4, 5, 7, 9, 12]
print(reverse_array(arr)) 


# In[4]:


#Q4. Given an array of integers, find the maximum element in the array.
def find_max_element(arr):
    return max(arr)

# Example usage:
arr = [10, 5, 20, 8, 15]
print(find_max_element(arr))


# In[5]:


#Q5. Given a sorted array, remove the duplicate elements without using any extra data structure.

def remove_duplicates(arr):
    index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]
    return arr[:index+1]

# Example usage:
arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5]


# In[ ]:




