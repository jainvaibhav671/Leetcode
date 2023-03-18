
from typing import List


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history: List[str] = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        _next = self.curr + 1
        self.history = self.history[:_next]
        self.history.append(url)
        self.curr = _next

    def back(self, steps: int) -> str:

        if steps > self.curr:
            self.curr = 0
        else:
            self.curr -= steps

        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        _forward = len(self.history) - self.curr - 1
        if steps > _forward:
            self.curr += _forward
        else:
            self.curr += steps

        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
