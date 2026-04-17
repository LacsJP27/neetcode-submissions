class PrefixNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        cur = self.root

        # go char by char to build tree and place in HashMap
        for c in word:
            if c not in cur.children:
                # Character as key value
                # Trienode() as value
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
        # marks the last node
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord


    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True
        