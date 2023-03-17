
from typing import Dict, Self


class Trie:

    def __init__(self):
        self.dataset: Dict[str, Self] = {}
        self.isAWord: bool = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.isAWord = True
            return

        char = word[0]
        if not self.dataset.get(char, False):
            self.dataset[char] = Trie()

        self.dataset[char].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0 and self.isAWord:
            return True
        elif len(word) == 0:
            return False

        char = word[0]
        if not self.dataset.get(char, False):
            return False

        return self.dataset[char].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        char = prefix[0]
        if self.dataset.get(char, False):
            return self.dataset[char].startsWith(prefix[1:])
        else:
            return False
