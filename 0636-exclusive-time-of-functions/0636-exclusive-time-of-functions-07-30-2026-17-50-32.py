class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0]*n
        stack = []
        prevTime = 0
        for log in logs:
            id, state, time = log.split(":")
            if state == 'start':
                if (len(stack) != 0):
                    prevId = stack[-1]
                    res[prevId] += int(time) - prevTime
                stack.append(int(id))
                prevTime = int(time) 
            else:
                res[int(id)] += int(time) - prevTime + 1
                stack.pop()
                prevTime = int(time) + 1

        return res