class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def set_tree():

    n1 = TreeNode(15)
    n2 = TreeNode(7)

    n3 = TreeNode(20, n1, n2)
    n4 = TreeNode(9)
    root = TreeNode(3, n4, n3)
    return root

if __name__ == "__main__":

    def pre_order(root):

        pass