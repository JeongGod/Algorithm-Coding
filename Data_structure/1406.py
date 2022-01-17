from re import L
import sys

input = sys.stdin.readline
"""
현재 있는 곳이 커서의 위치라고 생각하자.
"""
class LinkedList:
    def __init__(self, node):
        self.head = node
    

class Node:
    def __init__(self, val):
        self.val = val
        self.head = None
        self.tail = None

    def delete(self):
        self.tail.head = self.head
        self.head.tail = self.tail
    
    def insert(self, node):
        node.head = self.head
        node.tail = self
        if self.head is not None:
            self.head.tail = node
        if self.head is None:
            linked.start = node
        self.head = node

def main(cur):
    for _ in range(T):
        command = list(input().rstrip().split())
        if command[0] == "L":
            if cur.head.val is None:
                continue
            cur = cur.head
        elif command[0] == "D":
            if cur.tail is None:
                continue
            cur = cur.tail
        elif command[0] == "B":
            if cur.head.val is None:
                continue
            cur.head.delete()
        elif command[0] == "P":
            cur.insert(Node(command[1]))
        
def show():
    cur = start.tail
    while cur.val is not None:
        print(cur.val, end="")
        cur = cur.tail
    print("")  

if __name__ == "__main__":
    global start
    early = input().rstrip()
    cur = Node(early[0])
    linked = LinkedList(cur)
    start = Node(None)
    cur.head = start
    cur.head.tail = cur
    cur.tail = Node(None)
    cur.tail.head = cur
    cur = cur.tail
    for i in range(1, len(early)):
        cur.insert(Node(early[i]))

    T = int(input())
    main(cur)
    show()