class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
class ll:
        def __init__(self):
               self.head=None
        def ins(self,data):
            if self.head==None:
                   self.head=Node(data)
            else:
                    cur=self.head
                    while(cur.next):
                          cur=cur.next
                    cur.next=Node(data)
        def disp(self):
            if self.head==None:
                    print('empty')
            else:
                    cur=self.head
                    while(cur):  
                        print(cur.data)
                        cur=cur.next
                    # self=self.next

ob1=ll()
ob1.ins(10)
ob1.ins(11)
ob1.disp()
ob2=ll()
ob2.ins(44)
ob2.disp()
