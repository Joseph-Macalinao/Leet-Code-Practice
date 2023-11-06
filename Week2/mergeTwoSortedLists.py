# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    fin_link = []
    curr1 = list1
    curr2 = list2
    while curr1.next.val != None and curr2.next.val != None:
        if curr1.val < curr2.val:
            fin_link.append(curr1)
            curr1 = curr1.next
        elif curr1.val > curr2.val:
            fin_link.append(curr2)
            curr2 = curr2.next
    
    if curr1.next == None:
        while curr2.next.val != None:
            fin_link.append(curr2)
        curr2 = curr2.next

    if curr2.next == None:
        while curr1.next.val != None:
            fin_link.append(curr1)
        curr1 = curr1.next
    
    head = fin_link[0]
    tmp = head
    for i in range(len(1, fin_link)):
        tmp.next = fin_link[i]
        tmp = tmp.next
    return head
    

print(mergeTwoLists([1,2,4], [1,3,4]))