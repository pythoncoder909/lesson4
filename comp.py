
class Computer: 
     
 def _init_(self):
    self._maxprice=900
 def sell(self):
    print("selling price: {}".format(self._maxprice)) 
 def setMaxPrice(self,price):
        self.maxprice=price
c= Computer()
c.sell()
c._maxprice=1000
c.sell()
c.setMaxPrice(1000)
c.sell()
