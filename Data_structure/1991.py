import sys

input = sys.stdin.readline

class Tree:
    def __init__(self, root):
        self.root = root

    def __insert_node(self, parent, node):
        parent.left = node


    def search_node(self, node, parent, left, right):
        if node is None or node.val == ".":
            return
        if node.val == parent.val:
            if left != ".":
                node.insert_left(left)
            if right != ".":
                node.insert_right(right)
        self.search_node(node.left, parent, left, right)
        self.search_node(node.right, parent, left, right)
    
    def postorder(self, node):
        if node is None or node.val == ".":
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, end="")
    
    def preorder(self, node):
        if node is None or node.val == ".":
            return
        print(node.val, end="")
        self.preorder(node.left)
        self.preorder(node.right)
        
    def inorder(self, node):
        if node is None or node.val == ".":
            return
        self.inorder(node.left)
        print(node.val, end="")
        self.inorder(node.right)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node

def main():
    N = int(input())

    

    for _ in range(N):
        parent, left, right = input().rstrip().split()
        if parent == "A":
            root = Node(parent)
            tree = Tree(root)
            tree.search_node(root, root, Node(left), Node(right))
            continue
        
        tree.search_node(root, Node(parent), Node(left), Node(right))
        
        
    tree.preorder(root)
    print("")
    tree.inorder(root)
    print("")
    tree.postorder(root)
    print("")
if __name__ == "__main__":
    main()