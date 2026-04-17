class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        # j is the index of the current character
        def dfs(j, root):

            cur = root
            # since starting at j, j doesn't have to at beginning so adjust range
            for i in range(j, len(word)):
                c = word[i]

                # recursive when you have a dot
                if c == ".":
                    # go down all possible paths
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                # not recursive when there's no dot
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEndOfWord
        
        return dfs(0, self.root)

