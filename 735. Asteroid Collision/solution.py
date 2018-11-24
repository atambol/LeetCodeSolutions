class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        sol = []
        for asteroid in asteroids:
            # if the asteroid goes right, append it
            if asteroid > 0:
                sol.append(asteroid)
            else:
                # if it goes left, check the previous asteroid if it was positive
                while sol and sol[-1] > 0:
                    
                    # if the prev asteroid had more weight, dont append this one
                    if abs(sol[-1]) > abs(asteroid):
                        break
                        
                    # if the prev asteroid had equal weight, both cancel out
                    elif abs(sol[-1]) == abs(asteroid):
                        sol.pop()
                        break
                        
                    # if prev asteroid was lighter, pop it and continue
                    else:
                        sol.pop()
                        
                # else clause executed only if no break encountered
                else:            
                    sol.append(asteroid)

        return sol
                        
