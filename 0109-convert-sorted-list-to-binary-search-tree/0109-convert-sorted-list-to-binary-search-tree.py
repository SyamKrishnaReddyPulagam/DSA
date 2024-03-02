# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        def insert(root,nums):
            if not nums:
                return root
            if not root:
                root=TreeNode(nums[len(nums)//2])
                root.left=insert(root.left,nums[:len(nums)//2])
                root.right=insert(root.right,nums[(len(nums)//2)+1:])
            else:
                if min(nums)<root.val and max(nums)<root.val:
                    root.left=insert(root.left,nums)
                else:
                    root.right=insert(root.right,nums)
            return root
        return insert(None,nums)