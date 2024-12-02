from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def absMethod():
        pass

class childClass(AbstractClass):
    def absMethod():
        print("Some thing")
cc = childClass
cc.absMethod()