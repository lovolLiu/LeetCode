"""
Description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Solution:
The solution is just like adding two numbers on paper. The pseudo codes are:
1. Initialize the current node to dummy head of the returning list.
2. Initialize carry to 0.
3. Initialize p and q to head of l1 and l2 respectively.
4. Loop through lists l1 and l2 until reach both ends.
  Set x to node p's value. If p has reached the end of l1, set to 0.
  Set y to node q's value. If q has reached the end of l2, set to 1.
  Set sum = x + y + carry.
  Update carry = sum / 10
  Create a new node with the digit value of (sum % 10) and set it to current node's next, advance current node to next.
  Advance both p and q.
5. Check if carry = 1, if so, append a new node with digit 1 to the returning list.
6. Return dummy head's next node.

Time complexity: O(N)
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    We can write codes below simply according to the pseudo codes above.
    """

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        currentnode = dummy
        carry = 0
        while l1 or l2:
            x = 0
            y = 0
            if l1:
                x = l1.val
            if l2:
                y = l2.val
            sum = x + y + carry
            carry = sum / 10
            newnode = ListNode(sum % 10)
            currentnode.next = newnode
            currentnode = newnode
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry == 1:
            newnode = ListNode(1)
            currentnode.next = newnode
        return dummy.next

    """
    Some of the if conditions on the above codes are the same and can be merged into one block.
    """

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = current_node = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            x = y = 0
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next
            summary = x + y + carry
            carry = summary / 10
            new_node = ListNode(summary % 10)
            current_node.next = new_node
            current_node = new_node
        return dummy.next
