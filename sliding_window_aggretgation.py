from collections import deque


class SlidingWindowAggregation:
    """ https://scrapbox.io/data-structures/Sliding_Window_Aggregation """

    def __init__(self, f=sum):
        self.f = f
        self.front_stack = deque()
        self.back_stack = deque()

    def empty(self):
        return self.front_stack or self.back_stack

    def __len__(self):
        return len(self.front_stack) + len(self.back_stack)

    def fold_all(self):
        try:
            assert self.empty(), "Both stack is empty"
            if not self.front_stack:
                return self.back_stack[-1][1]
            elif not self.back_stack:
                return self.front_stack[-1][1]
            else:
                return self.f(self.front_stack[-1][1], self.back_stack[-1][1])
        except AssertionError as err:
            print("AssertionError :", err)

    def push(self, x):
        if not self.back_stack:
            self.back_stack.append((x, x))
        else:
            tmp = self.f(self.back_stack[-1][1], x)
            self.back_stack.append((x, tmp))

    def popleft(self):
        try:
            assert self.empty(), "Both stack is empty"
            if not self.front_stack:
                x, fx = self.back_stack.pop()
                self.front_stack.append((x, x))
                while self.back_stack:
                    x, fx = self.back_stack.pop()
                    fx = self.f(x, self.front_stack[-1][1])
                    self.front_stack.append((x, fx))
            self.front_stack.pop()

        except AssertionError as err:
            print("AssertionError :", err)
