# LinkedList

- node를 사용하여 구현
- node는 데이터 필드, 링크 필드로 구성되어 있음

## Singly Linked List

* 리스트를 구성하는 노드를 한 방향으로 연결하는 자료구조

```python
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
        if self.tail:
            cur = self.tail
            cur.next = new_node
            self.tail = cur.next
        else:
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = new_node
            self.tail = new_node

    def insert(self, index, data):
        new_node = Node(data)
        cur = self.head
        for _ in range(index):
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

    def display(self):
        lst = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            lst.append(cur.data)
        return lst


a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.insert(2, 4)
a.insert(0, 5)
print(a.display())
```

