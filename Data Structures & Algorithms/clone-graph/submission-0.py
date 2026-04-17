"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        # clone all neighbors recursively
        # neigghbors creating then adding to neighbor list of node
        def dfs(node):
            # if the node already cloned then return existing clone
            if node in oldToNew:
                return oldToNew[node]

            # clone node
            copy = Node(node.val)
            # put new node at the old node in map
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                # add the copies of the neighbor nodes to neighbor list
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None 


