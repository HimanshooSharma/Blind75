"""
https://leetcode.com/problems/alien-dictionary/
"""
# Topological sort problem

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adj_list = {c:set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            
            minLength  = min (len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]: # edge case
                return ""
            
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
                    
            
        visited = {} # map to False if visited and True if in current path
        
        res = []
        
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            
            for neighbour in adj_list[c]:
                if dfs(neighbour):
                    return True
                
            visited[c] = False
            res.append(c)
            
            
        for c in adj_list.keys():
            if dfs(c):
                return ""
            
        res.reverse()
        
        return "".join(res)
            