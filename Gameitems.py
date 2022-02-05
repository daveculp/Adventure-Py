from player import Player

class GameItem:
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
    
class Consumable(GameItem):
    def __init__(self, name, description, value, heal = 0):
        GameItem.__init__(self,name, description, value)
        self.heal = heal
        self.item_type = "consumable"
        
    def consume(self, player):
        player.hit_points += self.heal
        
class Weapon(GameItem):
    def __init__(self, name, description, value, damage):
        GameItem.__init__(self,name, description, value)
        self.damage = damage
        self.item_type = "weapon"
        
class Container(GameItem):
    def __init__(self, name, description, value):
        GameItem.__init__(self,name, description, value)
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
                
                    
        
        
    
        
        
            
