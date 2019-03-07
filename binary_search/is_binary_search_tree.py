from typing import Tuple

import unittest


def check_tree_ret_min_max(node) -> Tuple[bool, int, int]:
    '''
    Checks the validitiy of the given subtree and returns the min and the max of the tree
    Note: This is not meant to be called on None!
    '''
    if (node is None):
        return False, 0, 0  # dummy values
    # Since we have not seen children set min and max to the value of the node.
    tree_min = node.value
    tree_max = node.value
    if node.left is not None:
        left_valid, left_min, left_max = check_tree_ret_min_max(node.left)
        if not left_valid:
            return (False, tree_min, tree_max)
        if (left_max > node.value):
            # The maximum element of the left subtree should be less than the root.
            # Otherwise send False and in that case don't bother to much about correctness of
            # min and max
            return (False, tree_min, tree_max)
        tree_min = left_min
    if node.right is not None:
        right_valid, right_min, right_max = check_tree_ret_min_max(node.right)
        if not right_valid:
            return (False, tree_min, tree_max)
        if (right_min < node.value):
            # The minimum element of the right subtree should be less than the root's value
            return (False, tree_min, tree_max)
        tree_max = right_max
    return (True, tree_min, tree_max)


def is_binary_search_tree(root):
    '''Determine if the tree is a valid binary search tree
    '''
    if root is None:
        return True
    if root.left is not None:
        left_valid, _, left_max = check_tree_ret_min_max(root.left)
        if not left_valid:
            return False
        if (left_max > root.value):
            # The maximum element of the left subtree should be less than the root.
            return False
    if root.right is not None:
        right_valid, right_min, _ = check_tree_ret_min_max(root.right)
        if not right_valid:
            return False
        if (right_min < root.value):
            # The minimum element of the right subtree should be less than the root's value
            return False
    return True


# Tests


class Test(unittest.TestCase):
    class BinaryTreeNode(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)