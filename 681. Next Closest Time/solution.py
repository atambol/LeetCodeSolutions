class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time_str = time[0] + time[1] + time[3] + time[4]
        time_int = [int(x) for x in time_str]
        time = self.get_next_time(time_int)
        for t in time:
            valid, f_t = self.validate_time(t)
            if valid:
                return f_t
        
    def get_next_time(self, time):
        """
        :returns an int time
        """
        next_number = self.get_next_number(time)
        min_number = min(time)
        l = len(time)
        while True:
            for i in range(l-1, -1, -1):
                time[i] = next_number[time[i]]
                if time[i] != min_number:
                    break
            
            rval = 0
            for i in range(l):
                rval = rval*10 + time[i]
            yield rval
        
        
    def get_next_number(self, numbers_int):
        nums = sorted(numbers_int)
        next_number = {}
        for i in range(len(nums)-1):
            next_number[nums[i]] = nums[i+1]
            
        next_number[nums[len(nums)-1]] = nums[0]
        return next_number
    
    def validate_time(self, time):
        hours = int(time/100)
        minutes = time%100
        if hours < 24 and minutes < 60:
            # return True, str(hours) + ":" + str(minutes)
            if hours == 0:
                h = "00"
            elif hours < 10:
                h = "0" + str(hours)
            else:
                h = str(hours)
                
            if minutes == 0:
                m = "00"
            elif minutes < 10:
                m = "0" + str(minutes)
            else:
                m = str(minutes)
            return True, h + ":" + m
        else:
            return False, ""
        
        
