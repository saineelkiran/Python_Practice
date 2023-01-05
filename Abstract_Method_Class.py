from abc import ABC ,abstractmethod
#ABC Abstract Base Classes

class landline(ABC):
    @abstractmethod
    def called(self):
        pass
class mobile(landline):
    def called(self):
        print("phone reachable")

class serviceprovider:
    def sp(self,p1):
        print("Hi, thanks for joining Airtel")
        p1.called()
p1=mobile()
#p1.called()
p2=serviceprovider()
p2.sp(p1)