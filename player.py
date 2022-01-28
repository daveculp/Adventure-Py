#from gameitems import item

class player:
    
    def __init__(self, name):
        self.name = name
        self.location = 0
        self.inventory = []
        self.hit_points = 20
    
    def print_inventory(self):
        print ("You are carrying the following items:")
        for item in self.inventory:
            item.print_item()

    def print_player(self):
        print ("\nName: "+self.name)
        print ("Hit points: "+str(self.hit_points)+"\n")
        self.print_inventory()
    
    def add_item(self, item):
        if item != None:
            self.inventory.append(item)
            
            
    
        
