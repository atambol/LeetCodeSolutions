class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        // empty k
        if (k == 0) {
            return 0;
        }
        
        // craete a window of capacity k
        Window window = new Window(k);
        Character c;
        int maxLen = 0;
        int i = 0;
        
        // loop over each character
        while (i < s.length()) {
            c = s.charAt(i);
            window.createCapacity(c);
            window.addChar(c);
            maxLen = Math.max(window.getLength(), maxLen);
            i++;
        }
        return maxLen;
    }
    
    // Node to store information on consecutive set of character
    class Node {
        Character character;
        Node next;
        Node prev;
        int count;
        
        public Node(Character c) {
            character = c;
            count = 1;
            next = null;
            prev = null;
        }
    }
    
    // Window to store characters of capacity k
    class Window {
        private Node head;
        private Node tail;
        private Map<Character, Integer> charCountMap;
        private int capacity;
        private int len;
        
        public Window(int k) {
            charCountMap = new HashMap<>();
            tail = new Node(null);
            head = new Node(null);
            tail.next = head;
            head.prev = tail;
            capacity = k;
            len = 0;
        }
        
        // get the length of substring in the current window
        public int getLength() {
            return len;
        }
        
        // create capacity for one more character if the character is not already in window
        public void createCapacity(Character c) {
            if (!charCountMap.containsKey(c)) {
                while (capacity == 0) {
                    removeOldestNode();
                }
            }
        }
        
        // remove the oldest consecutive set of same characters (node)
        private void removeOldestNode() {
            // edge case : no nodes
            if (head.prev == tail) {
                return;
            }
            
            // remove oldest character
            Node node;
            int totalCount;
            node = tail.next;
            extractNode(node);
            totalCount = charCountMap.get(node.character);
            totalCount -= node.count;
            if (totalCount == 0) {
                charCountMap.remove(node.character);
                capacity++;
            } else {
                charCountMap.put(node.character, totalCount);
            }

            len -= node.count;
        }
        
        public void addChar(Character c) {
            // add new character
            Node node;
            if (charCountMap.containsKey(c) && head.prev.character == c) {
                head.prev.count++;
            } else {
                if (!charCountMap.containsKey(c)) {
                    capacity--;
                }
                node = new Node(c);
                insertNodeAtHead(node);
            }
            
            int count = charCountMap.getOrDefault(c, 0);
            charCountMap.put(c, count+1);
            len++;
        }
        
        private void extractNode(Node node) {
            node.prev.next = node.next;
            node.next.prev = node.prev;
            node.next = null;
            node.prev = null;
        }
        
        private void insertNodeAtHead(Node node) {
            head.prev.next = node;
            node.prev = head.prev;
            head.prev = node;
            node.next = head;
        }
    }
}
