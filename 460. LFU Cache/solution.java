// O(1) time complexity on get and put
// 2 maps and one linkedlist with nodes that internally use LinkedHashSet

class LFUCache {
    private Node tail;
    private Node head;
    private Map<Integer, Integer> keyToVal;
    private Map<Integer, Node> keyToNode;
    private int size;
    private int cap;
    
    public LFUCache(int capacity) {
        tail = new Node(0);
        head = new Node(0);
        keyToVal = new HashMap<>();
        keyToNode = new HashMap<>();
        cap = capacity;
        
        tail.next = head;
        head.prev = tail;
    }
    
    public int get(int key) {
        if (cap == 0) {
            return -1;
        }
        
        // check if key not present
        if (!keyToVal.containsKey(key))
            return -1;
        
        Node node = keyToNode.get(key);
        node.remove(key);
        // create new node if a node with new freq not present
        if (node.next.freq != node.freq+1) {
            createNodeAfter(node);            
        }
        
        // add the key and update keyToNode map
        node = node.next;
        node.add(key);
        keyToNode.put(key, node);
        
        // remove if previous node has become empty
        checkIfEmptyAndRemove(node.prev);
        
        return keyToVal.get(key);
    }
    
    public void put(int key, int value) {
        if (cap == 0) {
            return;
        }
        
        Node node;
        if (keyToVal.containsKey(key)) {
            keyToVal.put(key, value);
            node = keyToNode.get(key);
            
            // create new node if a node with new freq not present
            if (node.next.freq != node.freq+1) {
                createNodeAfter(node);            
            }
            
            // add the key and update keyToNode map
            node = node.next;
            node.add(key);
            keyToNode.put(key, node);

            // remove if previous node has become empty
            node.prev.remove(key);
            checkIfEmptyAndRemove(node.prev);
        } else {
            if (size == cap) {
                node = tail.next;
                Integer removedKey = node.remove();
                if (removedKey != null) {
                    keyToNode.remove(removedKey);
                    keyToVal.remove(removedKey);
                    checkIfEmptyAndRemove(node);
                }
                size--;
            }
            
            if (tail.next.freq != 1) {
                createNodeAfter(tail);  
            }
            node = tail.next;
            node.add(key);
            keyToNode.put(key, node);
            keyToVal.put(key, value);
            size++;
        }
    }

    private void createNodeAfter(Node node) {
        Node newNode = new Node(node.freq+1);
        newNode.next = node.next;
        newNode.prev = node;
        node.next.prev = newNode;
        node.next = newNode;
    }
    
    private void checkIfEmptyAndRemove(Node node) {
        if (node != tail && node != head && node.isEmpty()) {
            node.next.prev = node.prev;
            node.prev.next = node.next;
        }
    }
    
    public class Node {
        public LinkedHashSet<Integer> set;
        public int freq;
        public Node next;
        public Node prev;
        
        public Node(int f) {
            next = null;
            prev = null;
            freq = f;
            set = new LinkedHashSet<>();
        }
        
        public boolean isEmpty() {
            return set.isEmpty();
        }
        
        public void add(int key) {
            set.add(key);
        }
        
        public Integer remove() {
            if (!set.isEmpty()) {
                int key = set.iterator().next();
                set.remove(key);
                return key;
            }
            return null;
        }
        
        public void remove(int key) {
            if (!set.isEmpty())
                set.remove(key);
        }
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
