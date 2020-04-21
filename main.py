# Complexity
# O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)

# Amortized Runtime
# N inserts to a resizable array require O(N) inserts. O(1) amortized runtime.

# log n Runtimes
# When the number of elements in the problem space gets halved each time, it has a O(log n) runtime.

# Recursive Runtimes
# n = branches of recursion tree, m = depth of recursion tree
# time: O(n^m)
# space: O(m)

# 2 Pointer Technique
# one slow pointer and one fast pointer (useful in linked list or array questions)

# Tree Traversal
# in-order: left -> current -> right
# pre-order: current -> left -> right
# post-order: left -> right -> current

# Heaps
# insert: O(log n)
# remove: O(log n)

# Stack
stack = []
stack.append('a')       # push 'a'
stack.append('b')       # push 'b'
stack.pop()             # pop 'b'
stack.pop()             # pop 'a'

# Queue
queue = []
queue.append('a')       # enqueue 'a'
queue.append('b')       # enqueue 'b'
queue.pop(0)            # dequeue 'a'
queue.pop(0)            # dequeue 'b'

# Dequeue
import collections
deque = collections.deque()
deque.appendleft('a')   # enqueue left 'a'
deque.append('b')       # enqueue right 'b'
deque.pop()             # dequeue right 'b'
deque.popleft()         # dequeue left 'a'

# Binary Search
def binarySearch(arr, x):
    l, r = 0, len(arr)
    while l <= r:
        mid = l + (r - l) // 2;
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

from typing import List, Set, Dict

# Graphs (Adjacency List)
class Graph:
    def __init__(self):
        self.nodes: List[Node] = []

class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.children: List[Node] = []

# Graphs (Adjacency Matrix)
n: int = 10 # number of nodes/vertices in the graph
matrix: List[List[int]] = [[0]*n]*n

# DFS
visited: Set[Node] = set()

def dfs(root: Node):
    if not root:
        return;
    visited.add(root)
    for n in root.children:
        if n not in visited:
            search(n)

# BFS
def bfs(root: Node):
    if not root:
        return;
    queue: List[Node] = []
    queue.append(root)
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.add(n)
            for child in n.children:
                queue.append(child)
