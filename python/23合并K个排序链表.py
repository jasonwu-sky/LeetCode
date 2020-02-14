# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import queue

class Solution:
    testing = False

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = queue.PriorityQueue(maxsize=10000)
        count = 0
        for l in lists:
            if l:
                q.put((l.val, count, l))
                count = count + 1
        if q.empty():
            return None

        val, temp, head = q.get()
        f = head
        node = head.next
        if node:
            q.put((node.val, count, node))
            count += 1
        while not q.empty():
            val, temp, node = q.get()
            f.next = node
            f = node
            node = node.next

            if node:
                if Solution.testing:  #############################
                    print(node.val)
                q.put((node.val, count, node))
                count += 1
        return head