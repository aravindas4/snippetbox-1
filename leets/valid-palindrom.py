class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        rear = len(s) - 1

        while front <= rear:
            if not s[front].lower().isalnum():
                front += 1
                continue

            if not s[rear].lower().isalnum():
                rear -= 1
                continue
                
            if s[front].lower() != s[rear].lower():
                return False
            else:
                front += 1
                rear -= 1

        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))