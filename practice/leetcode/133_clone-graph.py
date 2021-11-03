"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new_graph = [None for _ in range(101)]
        def clone_node(cur_node):
            if new_graph[cur_node.val] is None:
                cloned_node = Node(val = cur_node.val)
                new_graph[cur_node.val] = cloned_node
                for neighbor in cur_node.neighbors:
                    clone_node(neighbor)
                    cloned_node.neighbors.append(new_graph[neighbor.val])
                return cloned_node
            else:
                return new_graph[node.val]
        if node is not None:
            return clone_node(node)
