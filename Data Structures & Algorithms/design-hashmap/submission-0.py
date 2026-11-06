class ListNode:
    def __init__(self, key: int = -1, val: int = -1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        # A prime number size around 1000 provides a good hash distribution
        self.size = 1009
        # Initialize each bucket with a dummy head node to simplify insertions/deletions
        self.map = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        cur = self.map[self._hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self._hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self._hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)