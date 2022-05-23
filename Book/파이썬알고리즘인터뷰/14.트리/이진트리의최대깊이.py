'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/

이진 트리의 최대 깊이를 구하라
'''
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    '''
    모든 노드를 끝까지 가야 높이를 알수 있다, BFS로 탐색하자
    '''

    result = 0
    tree = collections.deque()
    tree.append(root)
    while tree:
        if node := tree.popleft():
            result += 1
            tree.append(node.left)
            tree.append(node.right)

    print(result//2)



tree = TreeNode(3,
                TreeNode(9,
                         TreeNode(None),
                         TreeNode(None)),
                TreeNode(20,
                         TreeNode(15),
                         TreeNode(7)))
solution(tree)

