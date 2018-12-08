class Solution(object):
    def __init__(self):
        self.unique = set()
        
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        for email in emails:
            if email:
                domainname = email.split("@")[-1]
                localname = "".join(email.split("@")[0].split("+")[0].split("."))
                self.unique.add("{}@{}".format(localname, domainname))
                
        print(self.unique)
        return len(self.unique)
