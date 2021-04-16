class Node:
    def __init__(self, data=0, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        if self.tail is None:
            self.tail = new_node
            self.tail.next=None
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def getIndex(self,data):
        cur = self.head
        idx=0
        while cur:
            if cur.data == data:
                return idx
            cur = cur.next
            idx +=1
        return None #-1

    def insert(self,idx,data):
        new_node = Node(data)
        # 삽입에는 3가지 방법이 있음
        # 맨앞에 추가
        # 주어진 인덱스에 추가
        # 마지막에 추가
        if idx == 0:
            if self.head :
                next_node= self.head
                self.head = new_node
                self.head.next = next_node
            else:
                self.head = new_node
            self.size +=1
        else:
            cur_node=self.head
            cur_i =0
            pre=None
            while cur_i < idx:
                if cur_node:
                    pre = cur_node
                    cur_node=cur_node.next
                else:
                    break
                cur_i +=1
            if cur_i == idx:
                new_node.next = cur_node
                pre.next = new_node
                self.size +=1
            else:
                return -1

    # # add new node before the given data
    # def insertNodeatData(self, data, node):
    #     index = self.getdataIndex(data)
    #     if 0 <= index:
    #         self.insertNodeatindex(index,node)
    #     else:
    #         return -1
    #

    def clear(self):
        self.head = None

    def delete(self,idx):
        cur_i =0
        cur = self.head
        pre = None
        next_node = self.head.next
        if idx==0:
            self.head = next_node
            self.size -=1
        else:
            while cur_i < idx:
                if cur.next:
                    pre = cur
                    cur = next_node
                    next_node = next_node.next
                else:
                    break
                cur_i +=1
            if cur_i == idx:
                pre.next = next_node
                self.size -=1
            else:
                return -1

    def size(self):
        return self.size

    def tolist(self):
        cur =self.head
        li=[]
        while cur:
            li.append(cur.data)
            cur =cur.next
        return li

    def tostring(self):
        cur = self.head
        string = ""
        while cur:
            string += str(cur.data)
            if cur.next:
                string +=' '
            cur = cur.next
        return string

    def getDataByIndex(self,index):
        cur = self.head
        idx=0
        while cur:
            if index == idx:
                return cur.data
            cur = cur.next
            idx +=1
        return None #-1

T=int(input())
for t in range(1,T+1):
    n,m,idx,= map(int,input().split())
    ll = LinkedList()
    for data in map(int,input().split()):
        ll.append(data)

    # print(ll.tostring())

    for i in range(m):
        insert_i , value = map(int,input().split())
        ll.insert(insert_i,value)

    # print(ll.tostring())

    # print(ll.getDataByIndex(idx))
    print('#{} {}'.format(t,ll.getDataByIndex(idx)))