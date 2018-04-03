"""
https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/

Given a binary tree in which each node element contains a number.
Find the maximum possible sum from one leaf node to another.
The maximum sum path may or may not go through root.
"""

def maximum_sum_path(root):
    """
    Time: O(n)
    Space: O(1)
    """
    result = [float("-inf")]
    maximum_sum_path_util(root, result)
    return result[0]

def maximum_sum_path_util(node, result):
    # base case
    if node is None:
        return 0
    # base case: a leaf node
    if node.left is None and node.right is None:
        return root.value
    # find the max sum in left and right subtree
    left_sum = maximum_sum_path_util(node.left, result)
    right_sum = maximum_sum_path_util(node.right, result)

    if node.left is not None and node.right is not None:
        # update result if bigger value found
        result[0] = max(result[0], left_sum + right_sum + node.value)
        # return max possible value for root being on one side
        return max(left_sum, right_sum) + node.value

    # if any of the children is empty, return the node sum for node being on one side
    if node.left is None:
        return right_sum + node.value
    else:
        return left_sum + node.value


if __name__ == '__main__':
    pass