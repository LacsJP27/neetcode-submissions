class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        g = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            g[prereq].append(course)
        
        for i in range(numCourses):
            for to in g[i]:
                in_degree[to] += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        index = 0
        order = []

        while queue:
            curr = queue.popleft()
            order.append(curr)
            for node in g[curr]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    queue.append(node)
        if len(order) != numCourses:
            return []
        return order





        
        