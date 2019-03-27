class Nums:
    def __init__(self, val, op=None):
        self.val = val
        self.op = op
        self.next = None
        
class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        head = Nums(0, 0)
        curr = head
        
        # create objects for each number and following operator
        while i < len(s):
            if s[i] in "+-*/":
                curr.op = s[i]
                i += 1
            elif s[i] == " ":
                i += 1
            else:
                val = []
                while i < len(s) and s[i] not in "+-*/ ":
                    val.append(s[i])
                    i += 1

                node = Nums(int("".join(val)))
                curr.next = node
                curr = node

        # first pass - resolve * and /
        curr = head.next
        while curr.op:
            if curr.op in "*/":
                nxt = curr.next
                if not nxt:
                    break

                if curr.op == "*":
                    curr.val *= nxt.val
                elif curr.op == "/":
                    curr.val //= nxt.val
                curr.op = nxt.op
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        # seconds pass - resolve + and -
        curr = head.next
        while curr.op:
            if curr.op == "+":
                curr.val += curr.next.val
            else:
                curr.val -= curr.next.val
            curr.op = curr.next.op
            curr.next = curr.next.next
            
        return head.next.val
