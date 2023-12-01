class Stack:
    def __init__(self):
        self.stack = []
        self.tos = -1

    def push(self, x):
        self.tos += 1
        self.stack.append(x)

    def pop(self):
        if self.tos == -1:
            return False

        self.tos -= 1
        self.stack.pop()
        return True

    def top(self):
        if self.tos == -1:
            return

        return self.stack[self.tos]

    def is_empty(self):
        return self.tos == -1


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        for char in A:
            if s.top() == char:
                s.pop()
            else:
                s.push(char)
        ans = ""
        while s.top():
            ans += s.top()
            s.pop()

        return ans
