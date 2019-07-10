


from numpy.random import randint

class RTO:
    
    Codes = {
         "krpuram"   : "KA 27 Z",
         "indranagar" : "KA 03 X",  
    } 
    

    def __init__(self, name ):
        self.name = name
        self.code = self.Codes[name]
        
    def register(self, model, make, name):
        
        regno = "{0} {1:04d}".format( self.code, randint(2000) )
        # self.name = name
        
        return regno
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "RTO - {0}".format(self.name)
    

class Car:

    prizes = [ 
       ["Benz", "c-class", 50],
       ["Benz", "e-class", 65],
       ["Benz", "a-class", 35],
       ["Benz", "b-class", 30],
    ]
        
    def __init__(self, model, make ):
        self.model = model
        self.make = make
        
        self.prize = self.getPrize()
        self.regno = None
        
    
    def getPrize(self):
        # print( self.prizes )
        for make, model, prize in self.prizes:
            if model == self.model and make == self.make:
                return prize
#             else:
#                 print("{make}!={c_make}  - {model}!={c_model}".format(
#                     make=self.make, model=self.model,
#                     c_model=model, c_make=make
#                 ))
            
        print("No price list for {make}-{model}".format(make=self.make, model=self.model))
        return 
        
        
    def show(self):
        print( self.model, self.make, self.regno, self.prize)
        
        
    def __str__(self):
        return self.regno
    
    def __repr__(self):
        return "{name} - {0}".format(self.regno, name = self.__class__.__name__)
    
                
        
class BenzCar(Car):

    def __init__(self, model):
        Car.__init__(self, model, "Benz")
        

class SalesMan(object):
    
    def __init__(self, name, rto ):
        self.name = name
        self.rto = rto

        self.soldCars = [] 
        self.busy = False
        
    def buy(self, model, client):
        car = BenzCar(model)
        car.regno = self.rto.register(model, car.make, client)
        
        self.soldCars.append( car )
            
        return car
            
        
    def total(self):
        
        total = 0
        for car in self.soldCars:
            try:
                total += car.prize
            except Exception as err:
                import pdb; pdb.set_trace()
            
        return total
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "SalesMan - {0}".format(self.name)
    
    def show(self):
        
        for car in self.soldCars:
            print("   ", car)

class ShowRoom(object):
    """Show Room 
      showroom = ShowRoom( name )
    """
    
    def __init__(self, name ):
        self.name = name
        self.salesMen = []
        self.noSalesMan = 0

        self.rtos = {
            "krpuram"    : RTO("krpuram"),
            "indarnagar" : RTO("indranagar")
        }
        
    def addSalesMan(self, name, rto):
        """ """
        rto  = self.rtos[rto]
        salesMan = SalesMan(name, rto)
        
        self.salesMen.append( salesMan )
        self.noSalesMan += 1
        
        
    def total(self):
        
        total = 0
        for salesman in self.salesMen:
            total += salesman.total()
            
        return total
    
    def getSaleMan(self):
        
        for saleMan in self.salesMen:
            if not saleMan.busy:
                saleMan.busy = True
                return saleMan
            
        print( "All sales man are busy. Please wait in Lounge.")
        
        return None
    
    def show(self):
        
        for salesman in self.salesMen:
            print(salesman, "\n\t", salesman.show() )

