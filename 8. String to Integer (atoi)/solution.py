class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        char_map = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0
        }

        sign_map = {
            '-': -1,
            '+': 1
        }
        
        if str == '':
            return 0
        
        else:
            str = str.strip()
            sign = 1
            if str[0] in ['+', '-']:
                    sign = sign_map[str[0]]
                    str = str[1:]
            integer = 0
            
            while str:
                char = str[0]
                try:
                    mapped = char_map[char]
                except KeyError as a:
                    break
                integer = integer * 10 + mapped
                str = str[1:]
            return self.my_return(sign, integer)

        
    def my_return(self, sign, integer):
        if integer.bit_length() > 31:
            if sign < 0:
                return -2147483648
            else:
                return 2147483647
        else:
            return sign*integer
