class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        
        def helper(node):
            # print(node)
            nonlocal out
            if node not in g:
                return 
            if g[node]['color'] == 'g':
                return 
            
            g[node]['color'] = 'g'
            # out = 0
            fromchildren = g[node]['from']
            n = len(fromchildren)
            for i in range(n):
                v = fromchildren[i]
                helper(v)
            
            tochildren = g[node]['to']
            n = len(tochildren)
            for i in range(n):
                v = tochildren[i]
                if g[v]['color'] == 'r':
                    helper(v)
                    out += 1
            return 
        
        g = {}
        out = 0
        for source, target in connections:
            if source not in g:
                g[source] = {'to': [], 'from': [], 'color' : 'r'}
                
            if target not in g:
                g[target] = {'to': [], 'from': [],'color' : 'r'}
            
            # print((source, target))
            g[source]['to'].append(target)
            g[target]['from'].append(source)
            # print(g)
        # print(g)
        helper(0)
        return out
            
        
        