class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Pyramid:
    def __init__(self, list):
        self.pyramid = []
        node = list.next
        while node:
            self.pyramid.push(node)
            node = node.next
    def __recover(self, index):
        pass
    def insert(self, el):
        branchl = None
        branchr = None
        i = 0
        while i < len(self.pyramid):
            branchl = 2*i+1
            branchr = 2*i+2
            if self.pyramid[branchl] < el:
                

def mergeKLinkedLists(lists):
    res = lists.pop()
    if len(lists) == 0:
        return res
    pyramid = Pyramid(res)
    for list in lists:
        for el in list:
            pyramid.insert(el)
