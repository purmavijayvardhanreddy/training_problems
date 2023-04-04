class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def ins(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.ins(data)
            else:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.ins(data)   

    def levelorder(self):
        # print(self.data)
        que=[self]
        while(len(que)):
            e=que.pop(0)
            print(e.data,end=" ")
            if e.left:
                que.append(e.left)
            if e.right:
                que.append(e.right)
    def height(self,root):
        if root==None:
            return 0
        if root.left or root.right:
            if root.right and root.right:
                return 1+max(self.height(root.left),self.height(root.right))
            elif self.right:
                return 1+self.height(root.right)
            else:
                return 1+self.height(root.left)
        else:
            return 0
    def preorder(self,root):
        if root == None:
            return
        self.preorder(root.left)
        print(root.data,end=" ")
        self.preorder(root.right)
    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.right)
        print(root.data,end=" ")
        self.postorder(root.left)
    def inorder(self,root):
        if root == None:
            return
        print(root.data,end=" ")
        self.inorder(root.left)
        
        self.inorder(root.right)
      
    
        

l=[5,3,8,1,4,7,9,2]
if len(l):
    rt=Node(l[0])
    p=rt
    for i in range(1,len(l)):
        rt.ins(l[i])
    # print(rt.data)
    # print(rt.left.data)
    rt.levelorder()
    print()
    rt.preorder(p)
    print()
    rt.postorder(p)
    print()
    rt.inorder(p)
    print()
    print("height" , rt.height(p))


