class Orange:
    def __init__(self):
        self.color="Purple"
        self.type="citrus"

    def set_size(self,size):
        self.size=size

    def show(self):
        print(f"color:{self.color},type:{self.type}")


t1=Orange()
t1.show()

t1.size=100
print(t1.size)
