class Solution:
    def calculate(self, s: str) -> int:
        numstack = []
        signstack = []
        num = 0
        sign = "+"
        i = 0
        while i < len(s):
            if s[i] == "(":
                numstack.append(num)
                signstack.append(sign)
                num = 0
                sign = "+"
                i += 1
            elif s[i] == " ":
                i += 1
            elif s[i] == ")":
                n1 = numstack.pop()
                sign = signstack.pop()
                if sign == "+":
                    num = n1+num
                else:
                    num = n1-num
                sign = "+"
                i += 1
            elif s[i] in "+-":
                sign = s[i]
                i += 1
            else:
                n1 = ""
                while i < len(s) and s[i] not in "() +-":
                    n1 += s[i]
                    i += 1
                n1 = int(n1)
                if sign == "+":
                    num = n1+num
                else:
                    num = num-n1
                
                sign = "+"
                
        return num
