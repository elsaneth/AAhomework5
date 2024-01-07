def create_node(data):
    return {"data": data, "left": None, "right": None}

def insert_node(root, data):
    if root is None:
        return create_node(data)
    else:
        if data < root["data"]:
            root["left"] = insert_node(root["left"], data)
        else:
            root["right"] = insert_node(root["right"], data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root["left"])
        print(root["data"], end=" ")
        inorder_traversal(root["right"])

if __name__ == "__main__":
    numbers = [5, 3, 8, 2, 4, 7, 9]

    # Construct the binary tree
    root = None
    for num in numbers:
        root = insert_node(root, num)

    print("Inorder Traversal:")
    inorder_traversal(root)
