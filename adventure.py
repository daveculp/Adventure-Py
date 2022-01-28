from rooms import room
from random import randint
from player import player
from gameitems import item
from time import sleep
import sys

bad_parse_msgs = [
    "I have no idea what you are saying!",
    "What???",
    "Speak up, I can't hear you!",
    "I dont understand.",
    "???????"
    ]
    
class adventure:
    
    def __init__(self, filename):
        self.rooms = []
        self.load_adv(filename)
        player_name = input ("What is your name adventurer? ")
        self.player = player(player_name)
        
    def load_adv(self, filename):
        print("Loading datafile....")
        f = open(filename, "r")
        
        while True:
            north = south = east = west = None
            room_type = room.TYPE_NORMAL
            while True:
                #this loops reads in a whole room and fills in the data structures
                line = f.readline().rstrip()
                if line == "****": break # end of the room, break out and write the room
                
                #seperatea the tag and the data
                tag = line[1: line.find(">")]
                data = line[line.find(">")+1:]
                
                if tag == "ENDROOMS": break # end of file
                
                if tag == "ROOMNUM":
                    room_num = int(data)
                if tag == "NAME": 
                    name = data
                elif tag == "DESC":
                    desc = data
                elif tag == "NORTH":
                    north = int(data)
                elif tag == "SOUTH":
                    south = int(data)
                elif tag == "EAST":
                    east = int(data)
                elif tag == "WEST":
                    west = int(data)
                elif tag == "TYPE":
                    if data == "SHOP":
                        room_type = room.TYPE_SHOP
            
            if tag == "ENDROOMS": break #nothing to write, exit
            new_room = room(name, desc, room_type)
            new_room.set_exits(north,south,east,west)  
            
            self.rooms.append(new_room)
        f.close()

    def get_command(self):
        return input(">>>").rstrip()

    def execute_command(self, command):
        if command.lower() =="n":
            self.move_player("north")
        elif command.lower() == "s":
            self.move_player("south")
        elif command.lower() == "e":
            self.move_player("east")
        elif command.lower() == "w":
            self.move_player("west")
        elif command.lower() == "q":
            sys.exit()
        elif command.lower() == "i":
            self.player.print_inventory()
        else:
            print( bad_parse_msgs[randint(0, len(bad_parse_msgs)-1)])
            
    def move_player(self, direction):
        global player
        if self.rooms[self.player.location].exits[direction] != None:
            self.player.location = self.rooms[self.player.location ].exits[direction]
        else:
            c = randint(0,4)
            if c == 0:
                print("Really, trying to walk through walls are we?")
            elif c == 1:
                print("Have you been drinking?  You cant go that way!")
            elif c == 2:
                print("Luckily nobody is around to watch you stumble around.  You cant go that way!")
            elif c == 3:
                print ("You cant go that way......idiot.")
            elif c == 4:
                print ("You will never get anywhere trying to walk through walls!")
            





game = adventure("rooms.txt")
sword = item("Sword", "A jewel encrusted sword", 400)
water_bottle = item("Water bottle", "A clear water bottle", 10)
game.rooms[0].items.append(water_bottle)

game.player.add_item(sword)

while True:
    game.rooms[game.player.location].print_room()
    command = game.get_command()
    game.execute_command(command)

        #print("I have no idea what you are saying!")
        
        
    



            

