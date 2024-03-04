
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeDepth:
    def max_Depth_dfs(self, root: TreeNode):
        ## base 
        if root is None:
            return 0
        
        return (max(1 + self.max_Depth_dfs(root.left), (1 + self.max_Depth_dfs(root.right))))
        
      

object1 = TreeDepth()  
t1 = TreeNode(15 , None, None)
t2 = TreeNode(7 , None, None)
t3 =  TreeNode(20 , t1, t2)
t4 =  TreeNode(9 ,  None, None)
t5 =  TreeNode(3 , t4, t3)




print(object1.max_Depth_dfs(t5))