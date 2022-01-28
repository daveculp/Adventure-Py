from player import player

class gameItem:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.item_type = "normal"
    
    def print_item(self, long_desc = False):
        if long_desc == True:
            print (self.name+": "+self.description)
        else:
            print ("A "+self.name)
    
class consumable(gameItem):
    def __init__(self, name, description, value, heal = 0):
        gameItem.__init__(self,name, description, value)
        self.heal = heal
        self.item_type = "consumable"
        
    def consume(self, player):
        player.hit_points += self.heal
        
class weapon(gameItem):
    def __init__(self, name, description, value, damage):
        gameItem.__init__(self,name, description, value)
        self.damage = damage
        self.item_type = "weapon"
        
class container(gameItem):
    def __init__(self, name, description, value):
        gameItem.__init__(self,name, description, value)
        self.items = []
        self.item_type = "container"
    
    def print_item(self, long_desc = False):
        
        if len(self.items) == 0:
            if long_desc == True:
                print ("An empty "+self.name+": "+self.description)
            else:
                print ("An empty "+self.name)
        else:
            if long_desc == True:
                print(self.name+" which contains:")
                for item in self.items:
                    print ("      ", end = "")
                    item.print_item()
            else:
                print ("A "+self.name)
                
                    
        
        
    
        
        
            
