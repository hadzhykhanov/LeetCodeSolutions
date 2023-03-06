from queue import Queue


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """1. recursive using levels"""
        res = []

        def dfs(node, level):
            if not node:
                return None

            if len(res) - 1 < level:
                res.append([])

            res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """2. recursive with queue"""
        def dfs(que, ans):
            current_ans = []
            next_nodes = []

            for node in que.get():
                if node.left:
                    next_nodes.append(node.left)
                    current_ans.append(node.left.val)
                if node.right:
                    next_nodes.append(node.right)
                    current_ans.append(node.right.val)

            if len(next_nodes) == 0:
                return None

            que.put(next_nodes)
            ans.append(current_ans)
            dfs(que, ans)

        if not root:
            return []

        ans = [[root.val]]
        que = Queue()
        que.put([root])

        dfs(que, ans)
        return ans

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """3. iterative with queue"""
            if not root:
                return []

            que = Queue()
            que.put([root])
            ans = [[root.val]]

            while True:
                current_nodes = que.get()
                current_ans = []
                next_nodes = []

                for node in current_nodes:
                    if node.left:
                        next_nodes.append(node.left)
                        current_ans.append(node.left.val)
                    if node.right:
                        next_nodes.append(node.right)
                        current_ans.append(node.right.val)

                if len(next_nodes) == 0:
                    break

                ans.append(current_ans)
                que.put(next_nodes)

            return ans

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """4. recursive without queue"""
        def dfs(ans):
            new_lst = []
            for node in ans[-1]:
                if node.left:
                    new_lst.append(node.left)
                if node.right:
                    new_lst.append(node.right)

            if len(new_lst) == 0:
                return None

            ans.append(new_lst)
            dfs(ans)

        if not root:
            return []

        ans = [[root]]
        dfs(ans)

        for lst in ans:
            for i in range(len(lst)):
                lst[i] = lst[i].val

        return ans

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """5. iterative with queue"""
        if not root:
            return []

        new_lst = [root]
        ans = [new_lst]

        while len(new_lst) != 0:
            new_lst = []
            for node in ans[-1]:
                if node.left:
                    new_lst.append(node.left)
                if node.right:
                    new_lst.append(node.right)

            ans.append(new_lst)
        else:
            ans.pop()

        for lst in ans:
            for i in range(len(lst)):
                lst[i] = lst[i].val

        return ans
