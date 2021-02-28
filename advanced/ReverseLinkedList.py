def reverseLinkedList(node):
    prev = None
    curr = node

    while curr is not None:
        next = node._next
        curr._next = prev
        prev = curr
        curr = next
    node = prev
