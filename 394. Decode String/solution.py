class Solution:
    def decodeString(self, s: str) -> str:
        # create num and string stacks
        nums = [["1"]]
        strings = [[]]
        
        # handle 4 cases
        for i in range(len(s)):
            if 0 <= ord(s[i]) - ord("0") < 10:
                if not i or (i and not 0 <= ord(s[i-1]) - ord("0") < 10):
                    nums.append([])
                nums[-1].append(s[i])
            elif s[i] == "[":
                strings.append([""])
            elif s[i] == "]":
                num = int("".join(nums.pop()))
                string = "".join(strings.pop())
                strings[-1].append(num*string)
            else:
                strings[-1].append(s[i])
        
        # join final results
        num = int("".join(nums.pop()))
        string = "".join(strings.pop())
        return num*string
        
                
