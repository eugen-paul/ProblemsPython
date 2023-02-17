# Pass through tree
def pass_throughtree(self, root: Optional[TreeNode]):
    buffer = []
    last_node = None
    while buffer or root:
        while root:
            buffer.append(root)
            root = root.left
        root = buffer.pop()
        # do something. compere current node with last node ...

        last_node = root
        root = root.right
