class Calculator(object):
  def evaluate(self, string):
    return eval(string)
print Calculator.evaluate('2/2+3-4*7')