class top20:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.num<=20):
            value=self.num
            self.num+=1
            return value
        else:
           raise StopIteration

val=top20()

print(next(val))

for i in val:
    print(i)