/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    let seen = [];
    let node = head;
    let prev = null;
    while (node){
        if (seen.includes(node.val)){
            prev.next = node.next
        } else {
            seen.push(node.val)
            prev = node;
        }
        node = node.next;
    }
    return head
};