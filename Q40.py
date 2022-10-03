class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answers = []
        strings = []
        total = sum(candidates)
        if total < target:
            return []
        def backtrack(total, array, index):
            if total == 0:
                string = ''
                for each in array:
                    string += "_" + str(each)  # Separate the values
                if string not in strings:
                    answers.append(array)
                    strings.append(string)
                    return
            if index >= len(candidates) or total < 0:  # give up when total becomes negative
                return
            current = -1
            for each in range(index, len(candidates)):
                if candidates[each] != current: # Avoid duplicates
                    current = candidates[each]
                    backtrack(total - current, array + [current], each + 1)
                # Don't make another recursive call here. The for-loop is already skipping candidates
        backtrack(target, [], 0)
        return answers
