# 344. Reverse String
# Write a function that takes a string as input and returns the string reversed.
# Example:
# Given s = "hello", return "olleh".
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]



# 345. Reverse Vowels of a String
# Write a function that takes a string as input and reverse only the vowels of a string.
# Example 1:
# Given s = "hello", return "holle".
# Example 2:
# Given s = "leetcode", return "leotcede".
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_s = []
        vowels_pos = []
        s_list = list(s)
        for i, char in enumerate(s_list):
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels_pos.append(i)
                vowels_s.append(char)
                
        for x in vowels_pos:
            s_list[x] = vowels_s.pop()
        
        return ''.join(s_list)



# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
            
        n = min([len(str) for str in strs])
        start = 0
        while start < n:
            curr_chr = strs[0][start]
            if all([curr_chr == strs[x][start] for x in range(1, len(strs))]):
                start += 1
            else:
                break
            
        return strs[0][:start]
# Built-in function: os.path.commonprefix(list)



# 104. Maximum Depth of Binary Tree
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2
    
    def getHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))



# 100. Same Tree
# Given two binary trees, write a function to check if they are equal or not.
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p == q



#226. Invert Binary Tree        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            
        return root



# 235. Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else: # root.val equals to one of p.val and q.val or root.val is in the middle of the two
                return root



# 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
        return root if left and right else left or right



# 101. Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # recursively
        if not root: return True
        return self.isMirror(root.left, root.right)
        
    
    def isMirror(self, node1, node2):
        if not node1 and not node2: return True
        elif not node1 or not node2: return False
        
        return node1.val == node2.val and self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)