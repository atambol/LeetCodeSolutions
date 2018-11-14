class Codec:
    def __init__(self):
        self.map = {}
        self.id = 1
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        urlId = str(self.id)
        self.id += 1
        self.map[urlId] = longUrl
        return "http://tinyurl.com/" + urlId

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        urlId = shortUrl.lstrip("http://tinyurl.com/")
        if urlId in self.map:
            return self.map[urlId]
        else:  
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
