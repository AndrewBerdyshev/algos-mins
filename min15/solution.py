class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_part(head, left, right):
    saved = Node(0)
    saved.next = head
    prev = saved

    for i in range(left-1):
        prev = prev.next

    current = prev.next
    next = None
    for i in range(right - left + 1):
        temp = current.next
        current.next = next
        next = current
        current = temp

    prev.next.next = current
    prev.next = next

    return saved.next

