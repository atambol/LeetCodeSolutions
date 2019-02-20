class Solution:
    def killProcess(self, pid: 'List[int]', ppid: 'List[int]', kill: 'int') -> 'List[int]':
        # create a parent to child map
        map = {}
        for child, parent in zip(pid, ppid):
            if parent in map:
                map[parent].append(child)
            else:
                map[parent] = [child]
            
        # get all child processes
        killed = []
        queue = [kill]
        while queue:
            newqueue = []
            for pid in queue:
                killed.append(pid)
                if pid in map:
                    newqueue.extend(map[pid])
                
            queue = newqueue
            
        return killed
