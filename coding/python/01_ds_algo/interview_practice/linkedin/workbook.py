"""LinkedIn-style Python interview workbook.

These prompts are paraphrased from the public listing saved in
`EXTRACTED_QUESTIONS.md`. They are rewritten as clean practice prompts rather
than copied problem statements.

Workflow:
1. Pick one exercise.
2. Implement the function or class in place.
3. Add a few assertions or pytest tests.
4. Move finished solutions into a separate solutions file or folder later.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Singly linked list node used by the workbook problems."""

    val: int
    next: Optional["ListNode"] = None


@dataclass
class TreeNode:
    """Binary tree node used by the workbook problems."""

    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    """Helper for local testing."""

    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    """Helper for local testing."""

    out: list[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Question 1: Reverse a singly linked list.

    Given the head of a singly linked list, reverse the list in place and
    return the new head.

    Examples:
    - [1, 2, 3] -> [3, 2, 1]
    - [] -> []
    """

    raise NotImplementedError


def is_sanitized_palindrome(text: str) -> bool:
    """Question 2: Check whether a string is a palindrome after cleanup.

    Ignore case and remove non-alphanumeric characters before checking whether
    the remaining string reads the same forward and backward.

    Examples:
    - "A man, a plan, a canal: Panama" -> True
    - "race a car" -> False
    """

    raise NotImplementedError


def is_perfect_square(n: int) -> bool:
    """Question 3: Determine whether n is a perfect square.

    Solve this with binary search rather than calling a built-in square-root
    helper.

    Examples:
    - 16 -> True
    - 14 -> False
    """

    raise NotImplementedError


def get_intersection_node(
    head_a: Optional[ListNode], head_b: Optional[ListNode]
) -> Optional[ListNode]:
    """Question 4: Find the first shared node of two linked lists.

    Two singly linked lists may merge and share a common tail. Return the first
    shared node object, or None if the lists do not intersect.
    """

    raise NotImplementedError


def kth_largest(nums: list[int], k: int) -> int:
    """Question 5: Return the k-th largest element in an array.

    The result is the element that would appear in position k if the array were
    sorted in descending order.

    Examples:
    - nums=[3, 2, 1, 5, 6, 4], k=2 -> 5
    - nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4 -> 4
    """

    raise NotImplementedError


def count_islands(grid: list[list[str]]) -> int:
    """Question 6: Count connected land regions in a grid.

    The grid contains "1" for land and "0" for water. Cells connect
    horizontally and vertically.

    Example:
    - [["1","1","0"],["0","1","0"],["1","0","1"]] -> 3
    """

    raise NotImplementedError


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    """Question 7: Find the lowest common ancestor of two tree nodes.

    Given the root of a binary tree and two node references p and q, return the
    lowest node in the tree that has both p and q in its subtree.
    """

    raise NotImplementedError


class LRUCache:
    """Question 8: Implement a least-recently-used cache.

    Requirements:
    - `get(key)` returns the stored value or -1 if missing.
    - `put(key, value)` inserts or updates a key.
    - When capacity is exceeded, evict the least recently used entry.

    Target:
    - O(1) average time for both `get` and `put`.
    """

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


def group_words_by_phone_digits(words: list[str]) -> dict[str, list[str]]:
    """Question 9: Group words by phone keypad encoding.

    Use the classic phone keypad mapping:
    - 2: abc
    - 3: def
    - 4: ghi
    - 5: jkl
    - 6: mno
    - 7: pqrs
    - 8: tuv
    - 9: wxyz

    Return a mapping from digit string to all input words that encode to it.

    Example:
    - ["tree", "used"] -> {"8733": ["tree", "used"]}
    """

    raise NotImplementedError


def inverse_depth_weighted_sum(nested: list[object]) -> int:
    """Question 10: Compute an inverse-depth weighted sum.

    The input is a nested Python list containing integers or more nested lists.
    Integers at the deepest level have weight 1. One level above that has
    weight 2, and so on toward the root.

    Example:
    - [1, [4, [6]]] -> 17
      Explanation:
      max depth is 3
      1 has weight 3, 4 has weight 2, 6 has weight 1
      result = 1*3 + 4*2 + 6*1
    """

    raise NotImplementedError


# Suggested local checks once you implement each exercise:
#
# assert linked_list_to_list(reverse_linked_list(build_linked_list([1, 2, 3]))) == [3, 2, 1]
# assert is_sanitized_palindrome("A man, a plan, a canal: Panama") is True
# assert is_perfect_square(16) is True
# assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
# assert count_islands([["1", "1", "0"], ["0", "1", "0"], ["1", "0", "1"]]) == 3
