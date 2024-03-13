
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeDepth:
    def max_Depth(self, root: TreeNode):
        if root is None:
            return None
        
        q = deque([root])

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level += 1
        return level

object1 = TreeDepth()  
t1 = TreeNode(15 , None, None)
t2 = TreeNode(7 , None, None)
t3 =  TreeNode(20 , t1, t2)
t4 =  TreeNode(9 ,  None, None)
t5 =  TreeNode(3 , t4, t3)




print(object1.max_Depth(t5))