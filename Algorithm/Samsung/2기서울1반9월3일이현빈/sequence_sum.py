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
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.tail:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            self.tail = new_node
            cur.next = new_node
        else:
            cur = self.tail
            self.tail = new_node
            cur.next = new_node

    def insert(self, index, data):
        new_node = data.head.next
        cur = self.head
        new_cur = data.tail
        for _ in range(index):
            cur = cur.next
        new_cur.next = cur.next
        cur.next = new_node

    def display(self):
        lst = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            lst.append(cur.data)

        return lst


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(M)]
    new_lst = [LinkedList() for _ in range(M)]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            new_lst[i].append(lst[i][j])

    for i in range(1, M):
        index = 0
        flag = False
        node = new_lst[0].head
        while node.next != None:
            if node.next.data > lst[i][0]:
                flag = True
                break
            node = node.next
            index += 1
        if flag:
            new_lst[0].insert(index, new_lst[i])
        else:
            for j in range(len(lst[i])):
                new_lst[0].append(lst[i][j])

    print('#{} {}'.format(tc, ' '.join(list(map(str, new_lst[0].display()[:-11:-1])))))
