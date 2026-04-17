class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is just like giving an adjacency list
        # then detect a cycle in a graph
        # can do using depth first search

        # create an adjecency list
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        # create a visited set to store all courses
        # along current DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                # cycle detected
                # course visited more than once means cycle
                return False
            if adj[crs] == []:
                # has no prereqs (adj nodes)
                return True

            visitSet.add(crs)
            # loop through all of course's prereqs
            for pre in adj[crs]:
                if not dfs(pre):
                    # if there is a cycle return False
                    return False
            # this needed because multiple courses can have the same prereq
            # no longer visiting
            visitSet.remove(crs)
            # if we have to run dfs on it again we can execute second condition immediately
            adj[crs] = []
            return True
        
        # looping because graph can be unconnected
        for c in range(numCourses):
            # check every course
            if not dfs(c):
                return False
        return True
