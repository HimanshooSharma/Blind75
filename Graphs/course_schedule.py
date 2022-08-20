class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = { i:[] for i in range(numCourses)}

        visted = set()

        for course, pre in prerequisites:
            preMap[course].append(pre)

        def dfs(course) :
            if course in visted:
                return False

            if preMap[course] == 0:
                return True

            visted.add(course)

            for crs in preMap[course]:
                if not dfs(crs):
                    return False

            visted.remove(course)
            preMap[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True



