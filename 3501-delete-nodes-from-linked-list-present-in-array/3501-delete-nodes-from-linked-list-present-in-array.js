/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var modifiedList = function(nums, head) {
    var i = 0, prev = null, hd = null, checker= new ListNode(0,head) 
    var now = checker
    nums=new Set(nums)

    // if (head===null)
    //     return head
    // for(const it of nums)
    // {
    //     hd=head
    //     prev=null
    //     while(hd !== null)
    //     {
    //         if(prev===null && hd.val===it)
    //         {
    //             prev = hd
    //             hd = hd.next
    //             prev.next = null
    //             head = hd
    //             prev = null
    //         }
    //         else if(hd.val===it && hd.next===null)
    //         {    prev.next = null
    //             hd = hd.next
    //         }
    //         else if(hd.val===it)
    //         {
    //             prev.next = hd.next
    //             hd.next=null
    //             hd=prev.next
    //         }
    //         else
    //         {
    //             prev = hd
    //             hd = hd.next
    //         }
    //     }
    // }
    // return head

    while(now.next!==null)
    {
        if(nums.has(now.next.val))
            now.next= now.next.next
        else
            now = now.next
    }

    return checker.next
};