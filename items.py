class item:
    
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self. value = value
    
    def print_item(self, long_desc = False):
        if long_desc == False:
            print (self.name+": "+self.description)
        else:
            print (self.description)
            
