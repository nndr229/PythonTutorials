list_ = [2,3,1,4]


print(list_)

# Bubble sort

for i in range(len(list_)):
    for j in range(i,len(list_)):
        if list_[i]>list_[j]:
            temp = list_[i]
            list_[i] = list_[j]
            list_[j] = temp

print(list_)


# Stack

# LIFO

print()

# insertion
list_.append(12)
list_.append(14)
list_.append(16)


print(list_)

# deletion

list_.pop()
print(list_)




# Linked List

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



class LL:
    def __init__(self):
        self.head = None

    def insert(self,val):
        node = Node(val)

        if not self.head:
            self.head = node
            return 

        current = self.head

        while current.next:
            current = current.next
        current.next = node




ll = LL()

ll.insert(10)
ll.insert(11)
ll.insert(12)
ll.insert(13)

print(ll.head.val)
print(ll.head.next.val)
print(ll.head.next.next.val)
print(ll.head.next.next.next.val)
# print(ll.head.next.next.next)
