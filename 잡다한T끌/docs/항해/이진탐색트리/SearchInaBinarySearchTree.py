'''
https://leetcode.com/problems/search-in-a-binary-search-tree/


'''

def solution(root, val):

    def find(node):
        if not node:
            return
        if node.val > val:
            return find(node.left)
        elif node.val < val:
            return find(node.right)
        else:
            return node

    return find(root)


