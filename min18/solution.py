class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()
        
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]

