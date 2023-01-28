class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {")": "(", "}": "{", "]": "["}
        
        for elem in s:
            if elem in maps.values():
                stack.append(elem)
                continue
            if not stack or stack[-1] != maps[elem]:
                return False 
            stack.pop()
        return len(stack) == 0

s = Solution()
print(s.isValid("{[])"))