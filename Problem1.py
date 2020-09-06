"""
// Time Complexity : o(v+e)
// Space Complexity : o(v)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
"""

class Solution(object):
    def build_graph(self, cons): #building adjecenecy list from the list of connected edges
        
        for c in cons:
            fir = c[0]
            sec = c[1]
            self.graph[fir].append(sec) #creating neighbors list for each node
            self.graph[sec].append(fir)
            
    def dfs(self, parent, node):
        
        if self.discovery[node] != -1: #if node visited already, terminate
            return 
        self.discovery[node] = self.d_time #discovery time fr current node
        self.lower[node] = self.d_time
        self.d_time += 1
        
        for n in self.graph[node]: #for all neighbors for the current node
            if n == parent: 
                continue
            self.dfs(node, n) #if the neighbor is not the parent, call dfs on it
            
            if self.lower[n] > self.discovery[node]: # for current node and its current neighbor, if the lowest node reached by the neighbor is greater than the discovery time of the node, then it is a critical edge -> add too result list
                self.res.append([node,n])
            self.lower[node] = min(self.lower[node], self.lower[n]) #update the lower value for the current node
            
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        self.graph = [[] for i in range(n)]
        self.build_graph(connections)
        
        self.discovery = [-1] * n #initialize discovery times for each node to be -1 and lower to 0
        self.lower = [0] * n

        self.d_time = 0 #incremented at each dfs call
    
        self.res = []
        self.dfs(0,0) 
        return self.res