class TrieNode:
    def __init__(self, val=""):
        self.val = val
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEndOfWord = True
            
    def search(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isEndOfWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        wordTrie = PrefixTree()
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        res  = set()

        for word in words:
            wordTrie.insert(word)

        def dfs(r, c, node, curWord):
            if node.isEndOfWord:
                res.add(curWord)
                if not node.children:
                    return

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS  or visited[r][c]):
                return

            if board[r][c] in node.children:
                visited[r][c] = True
                targetChild = node.children[board[r][c]]
                curWord += (board[r][c])
                dfs(r + 1, c, targetChild, curWord)
                dfs(r - 1, c, targetChild, curWord)
                dfs(r, c + 1, targetChild, curWord)
                dfs(r, c - 1, targetChild, curWord)
                visited[r][c] = False
                    

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, wordTrie.root, "")
        return list(res)



        