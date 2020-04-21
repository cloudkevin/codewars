# You are given a binary tree:

# class Node:
#     def __init__(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
# Your task is to return the list with elements from tree sorted by levels, which means the root element goes first,
# then root children (from left to right) are second and third, and so on.
# Return empty list if root is None.
# Example 1 - following tree:
#                  2
#             8        9
#           1  3     4   5
# Should return following list:
# [2,8,9,1,3,4,5]

from collections import deque

class Node:
	def __init__(self, L, R, n):
		self.left = L
		self.right = R
		self.value = n

def tree_by_levels(node):
	if not node:
		return []
	answer, queue = [], deque([node,])
	while queue:
		n = queue.popleft()
		answer.append(n.value)
		if n.left is not None:
			queue.append(n.left)
		if n.right is not None:
			queue.append(n.right)
	return answer