# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(self, nums, target):
    # Create a dictionary to store the values and their indices
    dict = {}
    # Loop through the list of numbers
    for i in range(len(nums)):
        # Calculate the difference between the target and the current number
        diff = target - nums[i]
        # If the difference is in the dictionary
        if diff in dict:
            # Return the indices of the difference and the current number
            return [dict[diff], i]
        # Add the current number and its index to the dictionary
        dict[nums[i]] = i
    # If no solution is found, return an empty list
    return []

nums = [3,3,8]
target = 6
print(twoSum(twoSum, nums, target))
