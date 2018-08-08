import random

class Codec:
    size = 7
    base_url = "http://tinyurl.com/"
    key_map = dict()
    char_map = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "0",
        11: "a",
        12: "b",
        13: "c",
        14: "d",
        15: "e",
        16: "f",
        17: "g",
        18: "h",
        19: "i",
        20: "j",
        21: "k",
        22: "l",
        23: "m",
        24: "n",
        25: "o",
        26: "p",
        27: "q",
        28: "r",
        29: "s",
        30: "t",
        31: "u",
        32: "v",
        33: "w",
        34: "x",
        35: "y",
        36: "z"
    }
        
    def generate_random_key(self):
        key = []
        for i in range(random.randint(3, Codec.size)):
            key.append(Codec.char_map[random.randint(1, len(Codec.char_map)+1)])
        return "".join(key)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        random_key = ""
        try:
            while True:
                random_key = self.generate_random_key()
                x=Codec.key_map[random_key]
        except KeyError:
            Codec.key_map[random_key] = longUrl
            return Codec.base_url + random_key
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl.split(Codec.base_url)[-1]
        return Codec.key_map[key]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
