class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        brace_map = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        open_braces = brace_map.keys()
        closed_braces = brace_map.values()

        queue = []

        for i, char in enumerate(s):
            if char in open_braces:
                queue.append(char)

            if not queue:
                return False
            
            if char in closed_braces and char != brace_map[queue.pop(-1)]:
                return False

        if len(queue) > 0:
            return False

        return True
