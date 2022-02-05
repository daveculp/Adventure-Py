#from gameitems import item
import clear_screen

class Room:
    TYPE_NORMAL = 0
    TYPE_SHOP = 1
    
    def __init__(self, name, desc, room_type = TYPE_NORMAL):
        
        self.name = name
        self.desc = desc
        self.room_type = room_type
        self.entered = False
        self.itemList = []
        self.exits = {'north':None, 'south':None, 'east':None, 'west':None}

    def set_exit(self,door, location):
        self.exits[door] = location
        
    def set_exits(self,n,s,e,w):
        self.set_exit("north", n)
        self.set_exit("south", s)
        self.set_exit("east", e)
        self.set_exit("west", w)
    
    def print_room_header(self):
        print("\n")
        print ("="*len(self.name)+"====")
        print ("= "+self.name+" =")
        print ("="*len(self.name)+"====")
        
    def print_room(self):
        
        self.print_room_header()
        
        self.entered = True

        print (self.desc)
        if self.room_type == self.TYPE_SHOP:
            print ("This is a shop")
           
        if len(self.itemList) > 0:
            print ("You see the following in the room:")
            for item in self.itemList:
                item.print_item()
        for key, value in self.exits.items():
            if value != None:
                print ("You see an exit to the "+key )
