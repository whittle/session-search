from typing import Dict, TypeVar
from .context import rose_tree

T = TypeVar('T')

def mkTree(children: Dict[T, rose_tree.RoseTree[T]] = {}) -> rose_tree.RoseTree[T]:
    return rose_tree.RoseTree(children)

def test_add_child_simple() -> None:
    tree: rose_tree.RoseTree[int] = mkTree({1: mkTree(), 17: mkTree()})
    subtree: rose_tree.RoseTree[int] = mkTree({5: mkTree(), 10: mkTree()})
    tree.add_child(24, subtree)
    assert len(tree.children) == 3
    assert tree.children[24] == subtree

def test_add_child_merge() -> None:
    tree: rose_tree.RoseTree[int] = mkTree({61: mkTree(), 81: mkTree({3: mkTree(), 7: mkTree()})})
    subtree_children: Dict[int, rose_tree.RoseTree[int]] = {10: mkTree()}
    subtree: rose_tree.RoseTree[int] = mkTree(subtree_children)
    tree.add_child(61, subtree)
    assert len(tree.children) == 2
    assert tree.children[61].children == subtree_children
