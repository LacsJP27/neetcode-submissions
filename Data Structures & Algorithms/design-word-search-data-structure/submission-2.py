class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word) -> None:
        node = self.root
        for c in word:
            # check if the first letter in the children
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEndOfWord = True



    def search(self, word) -> bool:
        # j is the index of the current character
        def dfs(j, root):
            node = root

            for i in range(j, len(word)):
                c = word[i]
                # recursive only if there is a dot
                if c == ".":
                    # go down all possible paths
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                # not recursive when no dot
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.isEndOfWord

        return dfs(0, self.root)
                    
                


