class Vehicle:
    
    def __init__(self,name,max_speed,capacity):
        self.name=name
        self.max_speed=max_speed
        self.capacity=capacity
        
        
    def fare(self):
        return 50 * self.capacity
    
    
class Bus(Vehicle):
    
    def fare(self):
        amount=super().fare()
        amount=amount + (amount * (10/100))
        return amount
    
    
schoolBus1=Vehicle("Anabil",100,42)
schoolBus2=Bus("Projapoti",133,38)

print(f"Vehicle name: {schoolBus1.name}\nTop speed: {schoolBus1.max_speed}")
print(f"Capacity: {schoolBus1.capacity}\nTotal fare: {schoolBus1.fare()}\n\n")    

print(f"Vehicle name: {schoolBus2.name}\nTop speed: {schoolBus2.max_speed}")
print(f"Capacity: {schoolBus2.capacity}\nTotal fare: {schoolBus2.fare()}\n\n")    
    
        