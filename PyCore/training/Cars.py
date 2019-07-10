
# coding: utf-8

# # Class and Objects
#     * Creating a class 
#     * Creating Objects
#     * Class Magic Methods
#     

# # Class
#   * Collection properties/Attributes and Methods
#   * Should have __init__ method
#       * Should have a property which uniquly identies the Object. In this example 
#            * regNo, owner(Can be options)
#   * Collection of tasks for the method

# In[1]:


class Car:
    wheels = 4
    
    def __init__(self, regNo, owner, make="Default" , model="Default" ):
        print("Called the __INIT__ function")
        self.regNo = regNo
        self.owner = owner
        self.make = make
        self.model = model
        self.seats = 4 ;
        
        self.distance = 0
        self.people = []
        
    def hasVacency(self):
        return len(self.people) < self.seats

    def checkin(self, person):
        # self is prepending to accessing the class attribute
        if person in self.people: 
            print("{0} already available.".format(person))
      
        elif self.hasVacency(): 
            self.people.append(person)
            print("'{0}'' is checkedin".format(person))
        else:
            print("No Vacency for {0}, try later".format(person))

    def checkout(self, person):
        # self is prepending to accessing the class attribute
        if person in self.people: 
            self.people.remove(person)
        else:
            print("No passenger with name: ", person)
            
    def drive(self, miles):
        self.distance += miles

    def picnic(self):
        # self to accessing the class attribute
        self.checkin("Muniswara")
        self.checkin("Rajitha")
        
    def show(self):
        print("regNo    :", self.regNo)
        print("owner    :", self.owner)
        print("make     :", self.make)
        print("model    :", self.model)
        print("seats    :", self.seats)
        print("people   :", self.people)
        print("distance :", self.distance)
        


# In[2]:


mCar = Car('KA03X9999','Muniswara')
mCar.show()


# In Above Example:   
#    * mCar is object of Car class
#    * mCar will have all properties and methods of Car

# In[3]:


mCar.owner, mCar.distance, mCar.people


# In[4]:


mCar.picnic()
mCar.checkin("Ramu")
mCar.checkin("Ravi")


# In[5]:


mCar.drive(20)


# In[6]:


mCar.show()


# In[7]:


mCar.checkin("Kumba")


# In[8]:


mCar.checkout("Ravi")
mCar.checkin("Kumba")
mCar.show()


# In[9]:


class SUV(Car):
    """Class inheritance"""

    def __init__(self, reg , owner, **kwargs ):
       Car.__init__(self, reg , owner, **kwargs)
       self.seats = 6 ; #includes new attribute


# In[10]:


aCar = SUV("KA01BA2111", "SaiReddy", make="Toyota", model="Fortuner")
aCar.show()


# In[14]:


aCar.picnic()
aCar.checkin("Ramu")
aCar.checkin("Ravi")
aCar.checkin("Kumba")


# In[15]:


aCar.show()


# In[12]:


aCar.checkin("SaiReddy")


# In[13]:


aCar.show()

