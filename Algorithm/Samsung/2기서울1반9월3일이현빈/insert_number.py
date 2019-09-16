import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        # 리스트의 마지막 원소에 접근
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def insert(self, data, index):
        new_node = Node(data)
        cur = self.head
        for i in range(index):
            cur = cur.next
        tmp = cur.next
        new_node.next = tmp
        cur.next = new_node

    def display(self):
        lst = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            lst.append(cur.data)

        return lst


for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    lst = list(map(int, input().split()))
    new = LinkedList()
    for ele in lst:
        new.append(ele)
    info = [list(map(int, input().split())) for _ in range(M)]
    for ele in info:
        new.insert(ele[1], ele[0])
    numbers = new.display()
    print('#{} {}'.format(tc, numbers[L]))