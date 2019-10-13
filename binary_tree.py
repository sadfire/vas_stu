from copy import copy


def binary_tree_tree(tree: list, nodes: list) -> list:
    cash = []
    first_index_remove = 0
    for index, node in enumerate(tree):
        if cash:
            first_index_remove = cash[0]
        if node in nodes:
            cash.append(index)

        if first_index_remove and ((first_index_remove+1)*2 - 1) == index:
            tree[first_index_remove] = node
            del cash[0]
            cash.append(index)

    for index in cash:
        tree[index] = 0

    return tree


if __name__ == '__main__':
    tree = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    nodes = [2, 9]
    print(f"{binary_tree_tree(copy(tree), nodes)} \n{tree}")
