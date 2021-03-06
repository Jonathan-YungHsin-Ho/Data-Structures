from dll_stack import Stack
from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            return self.right.contains(target) if self.right else False
        else:
            return self.left.contains(target) if self.left else False

    # Return the maximum value found in the tree
    def get_max(self):
        # return self.right.get_max() if self.right else self.value
        return self.value if not self.right else self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)
        self.left and self.left.for_each(cb)
        self.right and self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.left and self.in_order_print(node.left)
        print(node.value)
        node.right and self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        to_print = Queue()
        to_print.enqueue(node)
        while to_print.len() > 0:
            dequeued_node = to_print.dequeue()
            print(dequeued_node.value)
            dequeued_node.left and to_print.enqueue(dequeued_node.left)
            dequeued_node.right and to_print.enqueue(dequeued_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        to_print = Stack()
        to_print.push(node)
        while to_print.len() > 0:
            popped_node = to_print.pop()
            print(popped_node.value)
            popped_node.right and to_print.push(popped_node.right)
            popped_node.left and to_print.push(popped_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        node.left and self.pre_order_dft(node.left)
        node.right and self.pre_order_dft(node.right)

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        node.left and self.post_order_dft(node.left)
        node.right and self.post_order_dft(node.right)
        print(node.value)
