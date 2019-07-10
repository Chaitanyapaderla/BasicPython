



class SuperMarket(object):
    
    def __init__(self, name, location, product="sarukulu"):
        self.name = name
        self.location = location
        
        self.inSlip = []
        self.inBasket = []
        
    # slip preparation
        
    def add2Slip(self, item):

            if item in self.inSlip: 
                print("Oops: '{0}' already available. Check in list".format(item))

            else:
                self.inSlip.append(item)
                print("'{0}' add item to list".format(item))     
            
    def delFromSlip(self, item):

            if item in self.inSlip: 
                print("'{0}' removed from slip".format(item))
                self.inSlip.remove(item)
                  
    def add2Basket(self, item):

            if item in self.inBasket: 
                print("Oops: '{0}' already available. Check in list".format(item))

            elif item not in self.inSlip:
                print("Oops: '{0}' is not in slip.".format(item))

            else:
                self.inBasket.append(item)
                print("'{0}' add item to list".format(item))     
            
    def delFromBasket(self, item):

            if item in self.inBasket: 
                print("'{0}' removed from slip".format(item))
                self.inBasket.remove(item)
                     
    def audit(self):
        
        pending = set(self.inSlip) - set(self.inBasket)
        if len(pending) > 0:
            print("Yet to buy - {0}".format(pending))
        else:
            print("Done with shoping")
            
            
    def show(self):
        print("inSlip   :", self.inSlip)
        print("inBasket :", self.inBasket)
