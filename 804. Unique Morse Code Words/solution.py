class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sol = set()
        
        mcodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            code = []
            for letter in word:
                code.append(mcodes[ord(letter) - 97])
            sol.add("".join(code))
            
        return len(sol)
