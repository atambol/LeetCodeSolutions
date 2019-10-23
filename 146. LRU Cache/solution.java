class LRUCache {
    private int cap;
    private HashMap<Integer, Record> map;
    private Record tail;
    private Record head;
    
    public LRUCache(int capacity) {
        cap = capacity;
        tail = new Record(-1, -1);
        head = new Record(-1, -1);
        head.prev = tail;
        tail.next = head;
        map = new HashMap<Integer, Record>();
    }
    
    public int get(int key) {
        if (map.containsKey(key)) {
            Record record = map.get(key);
            Record prev, next;
            prev = record.prev;
            next = record.next;
            prev.next = next;
            next.prev = prev;
            
            prev = head.prev;
            next = head;
            record.prev = prev;
            record.next = next;
            next.prev = record;
            prev.next = record;
            
            return record.value;
        } else {
            return -1;
        }
    }
    
    public void put(int key, int value) {
        Record record;
        Record prev, next;
        if (map.containsKey(key)) {
            record = map.get(key);
            prev = record.prev;
            next = record.next;
            prev.next = next;
            next.prev = prev;
            record.value = value;
        } else if (cap == 0) {
            record = tail.next;
            map.remove(record.key);
            prev = record.prev;
            next = record.next;
            prev.next = next;
            next.prev = prev;

            record.key = key;
            record.value = value;
            map.put(key, record);
        } else {
            cap--;
            record = new Record(key, value);
            map.put(key, record);
        }
        
        prev = head.prev;
        next = head;
        record.prev = prev;
        record.next = next;
        next.prev = record;
        prev.next = record;
    }
    
    class Record {
        public int key;
        public int value;
        public Record next;
        public Record prev;
        
        public Record(int k, int v) {
            key = k;
            value = v;
            next = null;
            prev = null;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
