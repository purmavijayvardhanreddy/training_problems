class p1:
    def p1_prop(self):
        print('p1_prop')
class c1(p1):
    def p1_prop(self):
        print('c1_prop')
        super().p1_prop()
        # ob=p1()
        # ob.p1_prop()
class b(c1):
    def p_prop(self):
        print('vv')
    # pass

ob=b()
ob.p1_prop()