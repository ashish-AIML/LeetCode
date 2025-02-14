# count = 0
# nums = [1,2,3,4,5,1]

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         print('i', nums[i])
#         print('j', nums[j])
#         if nums[i] == nums[j]:
#             count += 1

# print(count)

class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {}   # count maps each element with its own unique and increments 
        good_pairs = 0 # counting pairs

        for each_element in nums: # increments each element in list
            if each_element in count: # increments each element from the count dict
                good_pairs = good_pairs + count[each_element]  # adds all previous occurances 
                count[each_element] += 1
            else:
                count[each_element] = 1
        return good_pairs

# Example usage:
nums = [1,2,3,1,1,3]
solution = Solution()  # Create an instance of the class
print(solution.numIdenticalPairs(nums))  # Output: 2
