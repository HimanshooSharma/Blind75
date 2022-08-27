"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""

class TrieNode:
    def __init__(self):
        self.childern ={}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        curr = self.root
        
        for char in word:
            if char not in curr.childern:
                curr.childern[char] = TrieNode()
            curr = curr.childern[char]
            
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        
        curr = self.root
        
        for char in word:
            if char not in curr.childern:
                return False
            curr = curr.childern[char]
            
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        
        for char in prefix:
            if char not in curr.childern:
                return False
            curr = curr.childern[char]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)