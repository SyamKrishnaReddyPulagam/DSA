"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        dict1={None:None}
        curr=head
        while curr:
            node=Node(curr.val)
            dict1[curr]=node
            curr=curr.next
        curr=head
        while curr:
            node1=dict1[curr]
            node1.next=dict1[curr.next] if curr.next else None
            node1.random=dict1[curr.random] if curr.random else None
            curr=curr.next
        return dict1[head]