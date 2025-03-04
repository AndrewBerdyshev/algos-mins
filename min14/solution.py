class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def find_cycle_start(head):
    first = head
    last = head
    
    while last is not None and last.next is not None:
        first = first.next
        last = last.next.next
        
        if first == last:
            break
    
    if last is None or last.next is None:
        return None
    
    first = head
    while first != last:
        first = first.next
        last = last.next
    
    return first
