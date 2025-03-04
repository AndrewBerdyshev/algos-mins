class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_part(head, left, right):
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    for _ in range(left-1):
        prev = prev.next

    current = prev.next
    next_node = None
    for _ in range(right - left + 1):
        temp = current.next
        current.next = next_node
        next_node = current
        current = temp

    prev.next.next = current
    prev.next = next_node

    return dummy.next