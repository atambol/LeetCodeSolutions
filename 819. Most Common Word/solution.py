class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # edge case
        if not paragraph:
            return ""
        
        # calculate freq
        freq = {}
        banned = set(banned)
        j = 0
        i = 0
        while i < len(paragraph):
            if not (0 <= ord(paragraph[i]) - ord('a') < 26 or \
                0 <= ord(paragraph[i]) - ord('A') < 26):
                if i != j:
                    w = paragraph[j:i].lower()
                    if w not in banned:
                        if w not in freq:
                            freq[w] = 0
                        freq[w] += 1
                j = i + 1
            i += 1
        
        # insert last word
        if paragraph[i-1] != " ":
            w = paragraph[j:i].lower()
            if w not in banned:
                if w not in freq:
                    freq[w] = 0
                freq[w] += 1
        
        # get most frequent word
        maxf = 0
        word = ""
        for w, f in freq.items():
            if f > maxf:
                maxf = f
                word = w
                
        return word
            
