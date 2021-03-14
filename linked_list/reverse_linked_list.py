def reverseList(head):
    if not head or head.next is None:
        return head
    prev = head
    curr = head.next
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head.next = None
    return prev
