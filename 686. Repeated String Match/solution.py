class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lb = len(B)
        if len(A) > lb:
            if A.find(B) >= 0:
                return 1
            else:
                A += A
                if A.find(B) >= 0:
                    return 2
                else:
                    return -1
        else:
            a = A
            count = 1
            while len(A) < lb:
                A += a
                count += 1

            if A.find(B) >= 0:
                return count
            else:
                A += a
                if A.find(B) >= 0:
                    return count + 1
                else:
                    return -1
