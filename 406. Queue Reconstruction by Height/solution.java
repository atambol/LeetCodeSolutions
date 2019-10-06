class Solution {
    public int[][] reconstructQueue(int[][] people) {
        // sort by the number of people on front
        Arrays.sort(people, (a, b) -> Integer.compare(a[1], b[1]));
        
        // insert the person in the solution
        List<int[]> sol = new ArrayList<int[]>();
        for (int i = 0; i < people.length; i++) {
            insert(sol, people[i]);
        }
        
        // reconstruct the array
        for (int i = 0; i < people.length; i++) {
            people[i] = sol.get(i);
        }
        
        return people;
    }
    
    public void insert(List<int[]> sol, int[] person) {
        // edge case - empty sol
        if (sol.isEmpty()) {
            sol.add(person);
            return;
        }
        
        // maintain a count
        int count = person[1];
        boolean inserted = false;
        int i = 0;
        
        // find the position until which count is 0
        while (i < sol.size() && count > 0) {
            if (sol.get(i)[0] >= person[0]) {
                count--;
            }
            i++;
        }
        
        // insert to the farthest right such that no smaller elements get pushed to right
        while (i < sol.size() && sol.get(i)[0] < person[0]) {
            i++;
        }
        sol.add(i, person);
    }
}
