class Calculator(object):
  def evaluate(self, string):
    return eval(string)
print Calculator().evaluate('1.1*2.2*3.3')