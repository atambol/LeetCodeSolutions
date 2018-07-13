/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if (head == NULL) {
        return false;
    }
    
    struct ListNode *slowRunner = head->next;
    if (slowRunner == NULL) {
        return false;
    }
    struct ListNode *fastRunner = slowRunner->next;
    if (fastRunner == NULL) {
        return false;
    }    
    
    do {
        if (slowRunner == fastRunner) {
            return true;
        }
        
        slowRunner = slowRunner->next;
        fastRunner = fastRunner->next;
        if (fastRunner == NULL) {
            return false;
        }
        fastRunner = fastRunner->next;
    } while(fastRunner != NULL);
    return false;
}
