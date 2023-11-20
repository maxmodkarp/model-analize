class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def pre_order_traversal(node):
        nonlocal serialized_str
        if not node:
            serialized_str.append("null")
        else:
            serialized_str.append(str(node.val))
            pre_order_traversal(node.left)
            pre_order_traversal(node.right)

    serialized_str = []
    pre_order_traversal(root)
    return ','.join(serialized_str)

def deserialize(data):
    def build_tree(nodes):
        val = nodes.pop(0)
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = build_tree(nodes)
        node.right = build_tree(nodes)
        return node

    values = data.split(',')
    return build_tree(values)


root1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized_tree1 = serialize(root1)
print(serialized_tree1)  

deserialized_tree1 = deserialize(serialized_tree1)

print(deserialized_tree1.val, deserialized_tree1.left.val, deserialized_tree1.right.val,
      deserialized_tree1.right.left.val, deserialized_tree1.right.right.val)

root2 = None
serialized_tree2 = serialize(root2)
print(serialized_tree2)  

deserialized_tree2 = deserialize(serialized_tree2)

print(deserialized_tree2)
