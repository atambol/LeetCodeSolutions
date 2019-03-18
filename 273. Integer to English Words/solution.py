class Solution:
    def __init__(self):
        self.trans = {
            "0": "Zero",
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen",
            "20": "Twenty",
            "30": "Thirty",
            "40": "Forty",
            "50": "Fifty",
            "60": "Sixty",
            "70": "Seventy",
            "80": "Eighty",
            "90": "Ninety"
        }
        self.places = {
            1: "Thousand",
            2: "Million",
            3: "Billion",
            4: "Trillion"
        }
        
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        return self.translateNum(num, 1)
        
    def translateNum(self, num, n):
        sol = []
        triplets = []
        while num:
            t = num%1000
            num = num//1000
            triplet = str(t)
            while len(triplet) != 3:
                triplet = "0"+triplet
                
            triplets.append(triplet)
        triplets.reverse()
        
        for i, t in enumerate(triplets):
            s = self.translateTriplet(t, len(triplets) - i - 1)
            if s:
                sol.append(s)
        
        return " ".join(sol)
    
    def translateTriplet(self, t, i):
        if t == "000":
            return ""
        
        sol = []
        if t[0] != "0":
            sol.append(self.trans[t[0]])
            sol.append("Hundred")
        
        if t[1] != "0":
            if t[1] == "1":
                sol.append(self.trans[t[1:3]])
            else:
                sol.append(self.trans[t[1] + "0"])
                if t[2] != "0":
                    sol.append(self.trans[t[2]])
        else:
            if t[2] != "0":
                sol.append(self.trans[t[2]])
            
        if i != 0:
            sol.append(self.places[i])
            
        return " ".join(sol)
            
        
