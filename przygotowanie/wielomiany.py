class Polynomial:
    def __init__(self,list):
        self.list=list
    def __str__(self):
        s = str(self.list[0])
        for i in range(1,len(self.list)):
            if self.list[i]>0:
                s+='+'
                s+=(str(self.list[i])+'x^'+str(i))
            elif self.list[i] <0:
                s += (str(self.list[i])+'x^'+str(i))
        return s
    def __add__(self,other):
        l1=len(self.list)
        l2=len(other.list)
        l0=[]
        for k in range(0,min(l1,l2)):
            l0.append(self.list[k]+other.list[k])
        if l1<l2:
            l0+=other.list[l2-l1+1:]
        else:
            l0+=self.list[l1-l2+1:]
        return Polynomial(l0)


print(Polynomial([2,4,5]))
a = Polynomial([5,4,2])
b = Polynomial([2,3,2])
print(a+b)
print(a)
print(b)