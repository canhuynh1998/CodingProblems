"""
Given an int array, move all 0 to the end of the array such 
that all non-zero values are contiguous and in original order.
Input: nums = [7,0,6,0,8] 
Output: nums = [7,6,8,0,0]

- non zero stays in order
- in place no additional structure

- at least 1 element,
- can be all zeros, no zero at well


zero = idx

if not zero: continue

keep track of the index of the last 0 we encounter

# Approach 1: track zero 
Traverse through the input 
  if we see a non-zero:
    swap()

    
  # else:
  #   zero = idx


Input: nums = [7,0,6,0,8,0,0,9] 
 [7,6,8,9,0,0,0,0] 
  7, 0, 6

zero = 0

idx = 0




Input: nums = [7,0,6,0,8] 
    nums = [0, 7, 6]

# Approach 1: track non-zero 
non_zero =
Traverse through the input 
  if we see a zero:
    swap() # swap with the last 0 we encounter
  else:
    zero = idx



Output: nums = [7,6,8,0,0]
nums = [7,0,6,0,8] 

idx = 4
zero = 2

7, 0, 6, 0 ,8

7, 6, 8, 0, 0



"""
# Time complexity: O(N)
# Space complexity: O(1)

def swap_zero(array):
  zero_idx = 0 # O(1)

  # N elements -> O(N)
  for idx, num in enumerate(array):
    if num != 0: # O(1)
      if array[zero_idx] == 0: # O(1)
        array[idx], array[zero_idx] = array[idx], array[zero_idx] # O(1)
      zero_idx += 1 # O(1)

swap_zero([7, 6, 8, 5, 4])