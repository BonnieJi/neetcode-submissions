class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store the complete word at end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word  # Store the word at the end
        
        ROWS, COLS = len(board), len(board[0])
        result = []
        
        # Step 2: DFS on board
        def dfs(r, c, node):
            # If current char not in trie, stop
            if board[r][c] not in node.children:
                return
            
            # Move to next node
            next_node = node.children[board[r][c]]
            
            # Check if we found a word
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicates
            
            # Mark as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 directions
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
            
            # Restore
            board[r][c] = temp
        
        # Step 3: Start DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        
        return result
        