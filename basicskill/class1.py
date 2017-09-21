_metaclass_=type
class person:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def greet(self):
        print "hello %s"%self.name
foo=person()
foo.setname('matthewang')
foo.greet()