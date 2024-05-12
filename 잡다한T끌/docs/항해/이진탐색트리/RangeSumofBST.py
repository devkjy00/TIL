'''
https://leetcode.com/problems/range-sum-of-bst/

트리의 값 탐색, 범위 내의 값 더하기

:param root: [10, 5, 15, 3, 7, null, 18]
:param low: 7
:parma high: 15
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root, low, high):
    result = [low + high]

    def dfs(node):
        if node:
            if low < node.val < high:
                result[0] += node.val

            dfs(node.left)
            dfs(node.right)


    dfs(root)

    print(result[0])






solution(TreeNode(10,
                  TreeNode(5,
                           TreeNode(3),
                           TreeNode(7)),
                  TreeNode(15,
                            TreeNode(None),
                            TreeNode(18))), 7, 15)