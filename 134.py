class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        required_petrol = 0
        start = 0
        current_petrol = 0
        for i in range(len(gas)):
            current_petrol += gas[i] - cost[i]

            if current_petrol < 0:
                start = i+1
                required_petrol += current_petrol
                current_petrol = 0
        return start if current_petrol + required_petrol >= 0 else -1

        