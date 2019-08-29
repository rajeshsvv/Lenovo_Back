class Operator:
    def __init__(self,type,size):
        self.size=size
        self.type=type

    def __gt__(self,other):
        if self.size>other.size:
            return self.size
        return "Statement False"

t=Operator("Ornage",70)
p=Operator("Anar",10)
print(t<p)




