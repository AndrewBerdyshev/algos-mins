class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
        
    def print(self):
        current = self
        while current:
            print(current.val, end="->" if current.next else "\n")
            current = current.next

class Pyramid:
    def __init__(self, list):
        self.pyramid = []
        node = list
        while node:
            self.pyramid.append(node)
            node = node.next

    def __swap(self, a, b):
        self.pyramid[a], self.pyramid[b] = self.pyramid[b], self.pyramid[a]

    def append(self, el):
        self.pyramid.append(el)
        current = len(self.pyramid) - 1
        
        while current > 0:
            parent = (current - 1) // 2
            if self.pyramid[current].val < self.pyramid[parent].val:
                self.__swap(current, parent)
                current = parent
            else:
                break
    
    def isEmpty(self):
        return len(self.pyramid) == 0
    
    def getMin(self):
        min = self.pyramid[0]

        self.pyramid[0] = self.pyramid[-1]
        self.pyramid.pop()

        if self.pyramid:
            self.__sift_down(0)
        return min
    
    def __sift_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self.pyramid) and self.pyramid[left].val < self.pyramid[smallest].val:
            smallest = left
        if right < len(self.pyramid) and self.pyramid[right].val < self.pyramid[smallest].val:
            smallest = right
            
        if smallest != index:
            self.__swap(index, smallest)
            self.__sift_down(smallest)

def mergeKLinkedLists(linkedlists):
    if len(linkedlists) == 0:
        return None
    res = linkedlists.pop()
    if len(linkedlists) == 0:
        return res
    pyramid = Pyramid(res)
    for list in linkedlists:
        current = list
        while current:
            pyramid.append(current)
            current = current.next

    current = None
    res = current
    while not pyramid.isEmpty():
        if not current:
            current = pyramid.getMin()
            current.next = None
            res = current
        else:
            current.next = pyramid.getMin()
            current = current.next
            current.next = None
    return res
