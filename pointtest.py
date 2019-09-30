class point:
    def __init__(self, dim, data,mult):
        self.dim=dim
        self.data=[]
        self.mult=mult
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
    def add (self,p2):
        add=0
        for i in range(self.dim):
            add=self.data[i]+p2.data[i]
            return sum
    def sqmag(self,p1):
        mag=0
        for i in range(self.dim):
            mag=(self.data[i])**2+(p1.data[i])**2
        return mag

from point import*
p1=point(3,[1.,2.,3.])
p2=point(3,[6.,7.,8.])
print(p1.dot(p2))
print(p2.scale)
print(p1.add(p2))
print(p1.sqmag(p2))
       
