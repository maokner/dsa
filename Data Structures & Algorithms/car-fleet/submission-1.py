class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(map(list, zip(position, speed)), key=lambda pair: pair[0])
        stack = []
        for car in cars:
            if not stack:
                stack.append(car)
            else:
                time_to_target = (target - car[0]) / car[1]
                while stack and (target - stack[-1][0]) / stack[-1][1] <=time_to_target:
                    stack.pop()
                stack.append(car)
        return len(stack)
        