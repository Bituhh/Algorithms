from random import randint
from typing import Optional, List, Union


class Tree(object):
    """
    Description:
        A Binary Tree. Sort & Remove duplicates.
    Attributes:
        root: Branch
        values: List[int]

    Methods:
        build(array: List) -> Tree
        add_value(val: int) -> Tree
        pick_branch(val: int) -> Optional[Branch]
        pick_value(val: int) -> Optional[int]

    """

    def __init__(self):
        """ Constructor for Tree """
        self.root: Optional['Branch'] = None

    def build(self, array: List) -> 'Tree':
        for val in array:
            self.add_value(val)
        return self

    def add_value(self, val: int) -> 'Tree':
        node = Branch(val)
        if self.root is None:
            self.root = node
        else:
            self.root.add_node(node)
        return self

    def pick_branch(self, val: int) -> Optional['Branch']:
        if self.root is None:
            return None
        else:
            return self.root.find(val, True)

    def pick_value(self, val: int) -> Optional[int]:
        if self.root is None:
            return None
        else:
            return self.root.find(val, False)

    @property
    def values(self) -> List[int]:
        if self.root is None:
            return []
        else:
            return self.root.get_values()

    def __str__(self):
        return str(self.__dict__)


class Branch(object):
    """
    Description:

    Attributes:
        value: int
        left: _Node
        right: _Node

    Methods:
        add_node(self, node: '_Node') -> None
        get_values(array: Optional[List] = None) ->  -> List
        find(val: int, branch: bool) -> Union['_Node', int, None]
    """

    def __init__(self, val: int):
        """ Constructor for _Node """
        self.value = val
        self.left: Optional['Branch'] = None
        self.right: Optional['Branch'] = None

    def add_node(self, node: 'Branch') -> None:
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add_node(node)
        elif node.value > self.value:
            if self.right is None:
                self.right = node
            else:
                self.right.add_node(node)

    def get_values(self, array: Optional[List] = None) -> List:
        if array is None:
            array = []
        if self.left is not None:
            self.left.get_values(array)
        array.append(self.value)
        if self.right is not None:
            self.right.get_values(array)
        return array

    def find(self, val: int, branch: bool) -> Union['Branch', int, None]:
        if self.value == val:
            if branch:
                return self
            else:
                return self.value
        elif val < self.value and self.left is not None:
            return self.left.find(val, branch)
        elif val > self.value and self.right is not None:
            return self.right.find(val, branch)
        return None

    def __repr__(self):
        return str({'value': self.value, 'left': self.left, 'right': self.right})


if __name__ == '__main__':
    arr = [2, 5.5, 8, 6, 9.0, 34, 4, 1.01, 1]
    tree = Tree()
    tree.build(arr)
    tree.add_value(5)
    pick = tree.pick_branch(5)
    print(pick)
    print(tree.values)
    print(tree)
