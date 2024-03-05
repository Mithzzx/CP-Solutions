# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:

        l = list(head)
        l.pop(-n)
        return l


S = Solution()
print(S.removeNthFromEnd(head=[1, 2, 3, 4, 5], n=2))
