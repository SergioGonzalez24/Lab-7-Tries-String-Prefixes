# ----------------------------------------------------------
# Lab #7: Tries & String Prefixes
#
# Date: 09-Nov-2022
# Authors:
#           A01745446 Sergio Manuel Gonzalez Vargas
#           A01720627 Rodrigo Alfredo Mendoza España
# ----------------------------------------------------------

from __future__ import annotations
from typing import Generic, Optional, TypeVar
from collections.abc import Iterator

NUM_LETTERS = ord('z') - ord('a') + 1

T = TypeVar('T')  # Generic type for the Tier class
N = TypeVar('N')  # Generic type for the nested Node class


class Trie(Generic[T]):
    
    class Node(Generic[N]):

        __children: list[Optional[Trie.Node[N]]]
        __num_children: int
        value: Optional[N]

        def __init__(self) -> None:
            self.__children = ([None] * NUM_LETTERS)
            self.__num_children = 0
            self.value = None

        def __len__(self) -> int:
            return self.__num_children

        def __bool__(self) -> bool:
            return True

        def __getitem__(self, index: int) -> Optional[Trie.Node[N]]:
            return self.__children[index]

        def __setitem__(
                self,
                index: int,
                value: Optional[Trie.Node[N]]) -> None:
            self.__children[index] = value
            self.__num_children += 1

        def __iter__(self) -> Iterator:
            return iter(self.__children)

    __root: Trie.Node[T]

    def __init__(self) -> None:
        self.__root = Trie.Node()
        self.__length = 0

    def insert(self, key: str, value: T) -> None:
        current: Optional[Trie.Node[T]] = self.__root
        for c in key:
            i: int = Trie.__c2i(c)
            if isinstance(current, Trie.Node):
                if not current[i]:
                    current[i] = Trie.Node()
                current = current[i]
        if isinstance(current, Trie.Node):
            if current.value is None:
                self.__length += 1
            current.value = value

    def search(self, key: str) -> Optional[T]:
        current: Optional[Trie.Node[T]] = self.__root
        for c in key:
            i: int = Trie.__c2i(c)
            if isinstance(current, Trie.Node):
                if not current[i]:
                    return None
                current = current[i]
        if isinstance(current, Trie.Node):
            return current.value
        return None

    def remove(self, key: str) -> bool:
        current: Optional[Trie.Node[T]] = self.__root
        for c in key:
            i: int = Trie.__c2i(c)
            if isinstance(current, Trie.Node):
                if not current[i]:
                    return False
                current = current[i]
        if isinstance(current, Trie.Node):
            if current.value is not None:
                current.value = None
                self.__length -= 1
                return True
        return False

    @staticmethod
    def __c2i(c: str) -> int:
        return ord(c.lower()) - ord('a')

    @staticmethod
    def __i2c(i: int) -> str:
        return chr(i + ord('a'))

    def __len__(self) -> int:
        return self.__length

    @staticmethod
    def __get_items(items: list[tuple[str, T]], 
                    node: Optional[Trie.Node[T]],
                    key: str) -> None:
        
        if isinstance(node, Trie.Node):
            if node.value is not None:
                items.append((key, node.value))
                
            if len(node) != 0:
                for i in range(NUM_LETTERS):
                    if node[i] is not None:
                        Trie.__get_items(items, node[i], key + Trie.__i2c(i))

    def items(self) -> list[tuple[str, T]]:
        
        current: Optional[Trie.Node[T]] = self.__root
        items: list[tuple[str, T]] = []
        Trie.__get_items(items, current, '')
        
        return items

    @staticmethod
    def get_prefixes(node: Optional[Trie.Node[T]],
                       prefixes: dict[str, set[str]] = {}, word: str = ''):
        words: list[str] = []
        hijos: list[str] = []
        
        for num_elemento in range(NUM_LETTERS):
            if node is not None:
                if isinstance(node[num_elemento], Trie.Node):
                    newword = word + Trie.__i2c(num_elemento)
                    hijos = Trie.get_prefixes(
                        node[num_elemento], prefixes, newword)[0]
                    words += hijos
                    if node[num_elemento].value is not None: # type: ignore
                        if (hijos):
                            prefixes[newword] = set(hijos)
                        words.append(newword)
        return [words, prefixes]

    def prefixes(self) -> Optional[dict[str, set[str]]]:
        
        current: Optional[Trie.Node[T]] = self.__root
        prefixes: dict[str, set[str]] = Trie.get_prefixes(current)[1]
        print(prefixes)
        
        return prefixes


if __name__ == '__main__':
    t: Trie[int] = Trie()
    t.insert('help', 1)
    t.insert('he', 2)
    t.insert('hello', 3)
    print(t.search('he'))
    print(t.search('hell'))
    print(t.search('hello'))
    print(t.search('ant'))
    print(t.items())
    print("prefixes")
    print(t.prefixes())