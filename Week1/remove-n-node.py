class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # oops this works for
    # a list but it asked
    #for a linked list
    #return head[:-n] + head[len(head) - n + 1:]
    counter = 0
    current = head
    while current.next != None:
        counter += 1
        current = current.next
    counter += 1
    remove_num = counter - n
    current = head
    new_counter = 1
    for i in range(counter):
        if i == remove_num:
            current.next = current.next.next
        



n5 = Node(5, None)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
removeNthFromEnd(n1, 2)
