# // Time Complexity :O(n) for traversal
# // Space Complexity : O(n/2) for size of last level order
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :No

#Using Siblings logic
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: return False                                                   # empty tree
        #BFS    
        q = deque()
        q.append(root)
        x_found, y_found = False, False
   
        while q:
            size = len(q)                                                           # queue size will change for every level order
            for i in range(size):
                curr = q.popleft()

                if curr.val == x:                                                   # x found
                    x_found = True

                if curr.val == y:                                                   # y found
                    y_found = True

                if  curr.left != None and curr.right != None:                       # if they are siblings: False
                    if (curr.left.val == x and curr.right.val == y) : return False 
                    if (curr.left.val == y and curr.right.val == x) : return False
                    
                if curr.left != None:                                               # add next stage left to queue
                    q.append(curr.left)

                if curr.right:                                                      # add next stage right to queue
                    q.append(curr.right)
           
            if x_found and y_found :                                                # both x and y are found in the same level order? True   
                return True
            
            if x_found or y_found:                                                  # either x or y found on the same level? False
                return False
        #no Final return required

#using Parents
# from collections import deque
# class Solution:
#     def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
#         if not root: return False
            
#         q = deque()
#         parentQ = deque() 

#         q.append(root)
#         parentQ.append(None)
        
#         x_found, y_found = False, False
#         x_parent, y_parent = None, None                                             # can be avoided if instead of parents only siblings are checked
        
#         while q:
#             size = len(q)
#             for i in range(size):
#                 curr = q.popleft()
#                 parent = parentQ.popleft()                                          # extra space (h)

#                 if curr.val == x:
#                     x_found = True
#                     x_parent = parent

#                 if curr.val == y:
#                     y_found = True
#                     y_parent = parent

#                 if curr.left != None:
#                     q.append(curr.left)
#                     parentQ.append(curr)

#                 if curr.right:
#                     q.append(curr.right)
#                     parentQ.append(curr)   
              

#             if x_found and y_found :                                                                   
#                 return x_parent != y_parent
            
#             if x_found or y_found:
#                 return False
#         return True                                                                   # true required? misses one condition 