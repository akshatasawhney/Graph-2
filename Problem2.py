"""
// Time Complexity : o(n^2)
// Space Complexity : o(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
"""
class Solution(object):
    def dfs(self, node, graph, c): #dfs to find color groups
        if self.colors[node] != -1:
            return
        #logic
        self.colors[node] = c
        for i in range(self.n):
            if graph[node][i] == 1:
                self.dfs(i, graph, c)
                
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        self.n = len(graph)
        
        self.colors = [-1] * self.n
        c = 0
        
        for i in range(len(graph)):
            self.dfs(i, graph, c)
            c += 1
        
        grps = [0] * len(self.colors) # number of nodes in each grp
        malware = [0] * len(self.colors) #number of malwares in each grp
        #print(self.colors)
        
        for g in self.colors:
            grps[g] += 1
        
        
        for ini in initial:
            malware[self.colors[ini]] += 1
        
        
        res = sys.maxint
        
        for i in initial:
            clr = self.colors[i]
            
            if malware[clr] == 1: #only if theres 1 infected node in that network grp
                if res == sys.maxint: # no node has been found yet
                    res = i
                elif grps[self.colors[res]] < grps[self.colors[i]]: #else compare the number of nodes that can be saved from the prev node and the current node
                    res = i
                elif grps[self.colors[res]] == grps[self.colors[i]] and i < res: #if no. of nodes saved are equal but index value for current node is smaller
                    res = i
                    
                    
        if res == sys.maxint: #if none of the network groups can be saved due to the presence of more than 1 infected node in each grp, the node with samllest index value has to be removed
            res = min(initial)
        return res
                    
                    
                    