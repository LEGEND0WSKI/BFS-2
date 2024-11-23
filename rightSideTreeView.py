# // Time Complexity :O(n) for traversal
# // Space Complexity :O(n/2) for queue and O(h) for stack
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        #bfs uses queue
        result = []
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if i == 0:                              #for right to left, use the first element "0" in the level order to get rightmost;
                    result.append(curr.val)             #otherwise i == size-1 for left to right

                if curr.right:                          # right first
                    q.append(curr.right)

                if curr.left:                           # left next
                    q.append(curr.left)

        return result
    


    
# with DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #DFS uses stack
        self.result  = []
        self.helper(root,0)
        return self.result

    def helper(self,root,depth):
        if not root: return

        if depth == len(self.result):               # if depth for level order seen 1st time : add value for index(depth)
            self.result.append(root.val)            
        else:                                       # if already seen for current depth: update index(depth) 
            self.result[depth] = root.val
        
        self.helper(root.left,depth+1)              # recursion 
        self.helper(root.right,depth+1)