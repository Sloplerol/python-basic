Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class C:
    def __init__(self,data):
        self.data = data
    def __contains__(self,word):
        print("hello")
        return word in self.data

    
c = C([1,2,3,4])
3 in c
hello
True
class D:
    def __init__(self,data):
        self.data = data
    def __iter__(self):
        print("Iter",end = " -> ")
        self.i = 0
        return self
    def __next__(self):
        print("next",end = "  -> ")
        if self.i == len(self.data):
            raise StopIteration
        item = self.data[self.i]
        self.i+=1
        return item

    
d = D([1,2,3,4,5])
3 in d
Iter -> next  -> next  -> next  -> True
6 in d
Iter -> next  -> next  -> next  -> next  -> next  -> next  -> False
