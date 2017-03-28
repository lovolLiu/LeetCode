"""
Description:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Solution:
The key to the solution is to use a HashMap to map the value and the index of original array.
Iterate the array, look back to check if current element's complement already exists in the table,
If it exists, the result is found and return it.
If not, insert current element into the table.

Time complexity: O(N)
Why?
The time complexity of lookup for keys in HashTable and insert/acquire elements in HashTable are O(1).
"""
class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		result = [0, 0]
		# The internal implementation of python dictionary is actually a HashTable.
		dict = {}
		for i in range(len(nums)):
			if target - nums[i] in dict:
				result[0] = dict[target - nums[i]]
				result[1] = i
			else:
				dict[nums[i]] = i
		return result