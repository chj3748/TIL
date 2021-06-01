# 문자열 트라이 | bj 14725 개미굴
# 트라이 기초문제
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    # def search(self, string):
    #     current_node = self.head
    #
    #     for char in string:
    #         if char in current_node.children:
    #             current_node = current_node.children[char]
    #         else:
    #             return False
    #
    #     if current_node.data:
    #         return True
    #     else:
    #         return False

    # def starts_with(self, prefix):
    #     current_node = self.head
    #     words = []
    #
    #     for p in prefix:
    #         if p in current_node.children:
    #             current_node = current_node.children[p]
    #         else:
    #             return None
    #
    #     current_node = [current_node]
    #     next_node = []
    #     while True:
    #         for node in current_node:
    #             if node.data:
    #                 words.append(node.data)
    #             next_node.extend(list(node.children.values()))
    #         if len(next_node):
    #             current_node = next_node
    #             next_node = []
    #         else:
    #             break
    #     return words
    def trie_print(self, depth, string=None):
        if string is None:
            current_node = self.head
        else:
            current_node = string
        for next_node in sorted(current_node.children):
            print('--' * depth + next_node)
            self.trie_print(depth + 1, current_node.children[next_node])


trie = Trie()
for _ in range(N):
    input_data = input().split()
    trie.insert(input_data[1:])

trie.trie_print(0)
