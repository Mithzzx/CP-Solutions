class TreeNode:
    def __init__(self, val=None, children=None, parent=None):
        self.parent = parent
        self.children = children
        self.value = val


class Tree:
    def __init__(self, root=None):
        self.root = root

    def addChildren(self, node, children):
        for child in children:
            node.children.append(child)

    def print(self, root):
        while root:
            print(root.value)
            if root.children:
                for child in root.children:
                    self.print(child)
            else:
                return None


t = TreeNode("boss",[TreeNode("Allakai1"),TreeNode("AllaKai2")])
tt = Tree()
tt.print(t)
