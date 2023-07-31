from __future__ import annotations
from typing import Dict, Generic, TypeVar

"""The type of the labels in the rose tree."""
T = TypeVar('T')

class RoseTree(Generic[T]):
    """Implementation of a rose tree. The type of the tree is
    parameterized over the type of the edge labels.
    """

    def __init__(self, children: Dict[T, RoseTree[T]] = {}) -> None:
        self.children: Dict[T, RoseTree[T]] = children

    def add_child(self, label: T, subtree: RoseTree[T]) -> None:
        if label in self.children:
            self.children[label].merge_tree(subtree)
        else:
            self.children[label] = subtree

    def merge_tree(self, tree: RoseTree[T]) -> None:
        for label, subtree in tree.children.items():
            self.add_child(label, subtree)
