sol = []

        queue = []
        current_index = 0
        next_index = 1
        queue.append(root)

        while (next_index - current_index != 0):
            intermediate_sol = []
            tmp = next_index
            for i in range(current_index, next_index):
                if not queue[i]:
                    continue
                intermediate_sol.append(queue[i].val)
                if queue[i].left != None:
                    queue.append(queue[i].left)
                    tmp += 1

                if queue[i].right != None:
                    queue.append(queue[i].right)
                    tmp += 1
            current_index = next_index
            next_index = tmp
            print(intermediate_sol)
            sol.append(intermediate_sol)
        return sol
