
from typing import List, Optional


class WordDictionary:

    def __init__(self):
        self.chars: List[Optional[WordDictionary]] = [None] * 26
        self.isWord: bool = False

    def addWord(self, word: str) -> None:
        curr = self
        a: int = ord('a')
        for c in word:
            ch: int = ord(c) - a
            if not curr.chars[ch]:
                curr.chars[ch] = WordDictionary()

            curr = curr.chars[ch]

        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.chars:
                    if ch and ch.search(word[i+1:]):
                        return True
                return False

            if not curr.chars[ord(c) - ord('a')]:
                return False

            curr = curr.chars[ord(c) - ord('a')]

        return curr and curr.isWord
