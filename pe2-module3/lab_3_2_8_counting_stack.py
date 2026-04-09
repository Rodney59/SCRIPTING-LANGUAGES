class Stack:
    def __init__(self):
        self.__stk = []

    def get_stk(self):
        return self.__stk

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def push(self, val):
        self.__counter += 1
        return Stack.push(self, val)

    def pop(self):
        self.__counter -= 1
        return Stack.pop(self)


stk = CountingStack()
for i in range(4):
    stk.push(i)

for i in range(2):
    stk.pop()

print(stk.get_counter())
print(stk.get_stk())