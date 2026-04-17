"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # for keep in track of the nodes we already created
        oldToNew = {}

        def dfs(node):
            # check if the node has already been cloned
            if node in oldToNew:
                return oldToNew[node]
            # make deep copy of the node
            copy = Node(node.val)
            # mark the node as created
            oldToNew[node] = copy
            for nei in node.neighbors:
                # dfs all the neighbors to make deep copies
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None

    # O(n) time




