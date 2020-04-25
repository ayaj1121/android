print("a")
a = [1, 2, 3, 4, 5]
for b in a:
    print(b)
print(a)

try:
    raise ass
    z = 5/0
except Exception as e:
    print(type(e).__name__)
except Exception as ass:
    print("own")
print()

class animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def disp(self):
        print(self.name)

a=animal("dog","omni")
a.disp()


for c in range(10):
    print(c)


