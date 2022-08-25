"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        
        rank  = [1 for _ in range(n)]
        
        def find(node):
            
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]] # Path compression - optimization
                res = parent[res]
                
            return res
                
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parent1 == parent2:
                return 0
                
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
                
            else:
                parent[parent1] = parent2
                rank[parent2] += 1
                
            return 1
                
        
        
        res = n
        
        for node1, node2 in edges:
            res -= union(node1,node2)
            
        return res
        