"""
https://leetcode.com/problems/graph-valid-tree/

"""

import collections


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not edges:
            return n == 1
                
        
        def create_adj_list():
            
            adj = collections.defaultdict(list)
            
            for node1, node2 in edges:
                adj[node1].append(node2)
                adj[node2].append(node1)
                
            return adj
        
        adj_list = create_adj_list()
        
        
        visited = set()
        
        def dfs(root, prev):
            if root is None:
                return True
            
            visited.add(root)
            
            for neighbour in adj_list[root]:
                if neighbour not in visited:
                    dfs(neighbour, root)
                elif neighbour == prev: ## very important to exclude false positives
                    continue
                else:
                    return False
                
            return True
        
        
        
        
        return  dfs(0, -1) and len(visited) == n