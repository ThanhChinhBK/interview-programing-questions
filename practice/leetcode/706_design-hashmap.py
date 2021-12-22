from typing import Optional

class Node:
    def __init__(self, key, value, next_):
        self.key = key
        self.val = value
        self.next = next_
            
class MyHashMap:
    

    def __init__(self):
        self.num_node = 1000
        self.hashmap = [None] * 1000

    def put(self, key: int, value: int) -> None:
        ind = key % self.num_node
        if self.hashmap[ind] is None:
            self.hashmap[ind] = Node(key, value, None)
        else:
            last_node = self.hashmap[ind]
            while last_node.next is not None:
                if last_node.key == key:
                    last_node.val = value
                    return
                last_node = last_node.next
            if last_node.key == key:
                last_node.val = value
                return
            last_node.next = Node(key, value, None)

    def get(self, key: int) -> int:
        ind = key % self.num_node
        if self.hashmap[ind] is None:
            return -1
        else:
            curr_node = self.hashmap[ind]
            while curr_node is not None:
                if curr_node.key == key:
                    return curr_node.val
                curr_node = curr_node.next
            return -1

    def remove(self, key: int) -> None:
        ind = key % self.num_node
        if self.hashmap[ind] is None:
            return
        curr_node = self.hashmap[ind]
        if curr_node.key == key:
            self.hashmap[ind] = curr_node.next
        prev_node = curr_node
        curr_node = curr_node.next
        while curr_node is not None:
            if curr_node.key == key:
                prev_node.next = curr_node.next
                return
            curr_node = curr_node.next
            prev_node = prev_node.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
