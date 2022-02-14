from room import Room
from random import randint
from player import Player
from Gameitems import *
from time import sleep
import sys
import clear_screen

#verbs = ['get', 'take', 'open','go', 'run', 'move', 'look', 'attack','kill', 'examine', 'eat', 'drink', 'shout']


	
class Adventure:
	bad_parse_msgs = [
		"I have no idea what you are saying!",
		"What???",
		"Speak up, I can't hear you!",
		"I dont understand.",
		"???????",
		"Um.......yeah.....no."
		]
	def __init__(self, filename):
		self.rooms = []
		self.title = ""
		player_name = input ("What is your name adventurer? ")
		self.player = Player(player_name)
		self.load_adv(filename)
		self.do_title()
		self.current_room = self.rooms[self.player.location]

	def do_title(self):
		clear_screen.clear()
		print ("Welcome "+self.player.name+" to")
		print ("="*len(self.title)+"====")
		print ("= "+self.title+" =")
		print ("="*len(self.title)+"====")
		
	def load_adv(self, filename):
		print("Loading datafile....")
		sleep(1)
		f = open(filename, "r")
		self.title = f.readline().strip()
		#print (self.title)
		while True:
			
			line = f.readline().strip()
			tag = line[1: line.find(">")]
			data = line[line.find(">")+1:]
			if tag == "ROOM":
				room_num = int(data)
				self.load_room(room_num, f)
			elif tag == "ITEM":
				self.load_item(f)
			elif tag == "CONTAINER":
				self.load_container(f)
			elif tag == "ENDADV": break # end of file
				
		f.close()
	
	def load_room(self, room_num,f):
		north = south = east = west = None
		room_type = Room.TYPE_NORMAL
		desc = ""
		while True:
			line = f.readline().strip()
			tag = line[1: line.find(">")]
			data = line[line.find(">")+1:]
			if tag == "ENDROOM": break # end of file
				
			if tag == "ROOM":
				room_num = int(data)
			if tag == "NAME": 
				name = data
			elif tag == "DESC":
				if desc == "":
					desc = data
				else:
					desc = desc+" "+data
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
					room_type = Room.TYPE_SHOP
		new_room = Room(name, desc, room_type)
		new_room.set_exits(north,south,east,west)  
		self.rooms.append(new_room)
	
	def load_item(self,f):
		item_type = "NORMAL"
		inside = None
		while True:
			line = f.readline().strip()
			tag = line[1: line.find(">")]
			data = line[line.find(">")+1:]
			if tag == "ENDITEM": break
			
			if tag == "DESC":
				desc = data
			elif tag == "NAME":
				name = data
			elif tag == "HEAL":
				heal = int(data)
			elif tag == "DAMAGE":
				damage = int(data)
			elif tag == "ROOM":
				if data == "player":
					room_num = data
				else:
					room_num = int(data)
			elif tag == "VALUE":
				value = int(data)
			elif tag == "INSIDE":
				#print ("inside"+data)
				inside = data
			elif tag == "CONSUMABLE" or tag == "WEAPON" or tag == "CONTAINER":
				item_type = tag
		
		if item_type == "NORMAL":
			new_item = GameItem(name, desc, value)
		elif item_type == "WEAPON":
			new_item = Weapon(name, desc, value, damage)
		elif item_type == "CONSUMABLE":
			new_item = Consumable(name, desc, value, heal)
		elif item_type == "CONTAINER":
			new_item = Container(name, desc, value)
		#new_item.print_item()
		if inside != None:
			#print ("placing item inside another item!")
			for item in self.rooms[room_num].item_list:
				if item.name == inside:
					item.items.append(new_item)
					#print (item)
		elif room_num == "player":
			self.player.add_item(new_item)
		else:
			self.rooms[room_num].item_list.append(new_item)
			
	def get_command(self):
		command_str = str(self.player.hit_points) +" hit points:>>>"
		command = input(command_str).rstrip().lower()
		return command.split()

	def execute_command(self, commands):
		#single letter commands
		if len(commands) == 1:
			command = commands[0].lower()
			if command.lower() =="n" or command.lower() == "north":
				self.move_player("north")
			elif command.lower() == "s" or command.lower() == "south":
				self.move_player("south")
			elif command.lower() == "e" or command.lower() == "east":
				self.move_player("east")
			elif command.lower() == "w" or command.lower() == "west":
				self.move_player("west")
			elif command.lower() == "q" or command.lower() == "quit":
				sys.exit()
			elif command.lower() == "i" or command.lower() == "inventory":
				self.player.print_inventory()
			elif command.lower() == "l" or command.lower() == "?" or command.lower() == "look":
				game.rooms[game.player.location].print_room()
			elif command.lower() == "c" or command.lower == "char":
				self.player.print_player()
			else:
				print( Adventure.bad_parse_msgs[randint(0, len(Adventure.bad_parse_msgs)-1)])
			return
		
		#movement commands
		if commands[0] in ['go', 'run', 'move', 'walk']:
			direction = commands[1][0].lower()
			if direction =="n":
				self.move_player("north")
			elif direction == "s":
				self.move_player("south")
			elif direction == "e":
				self.move_player("east")
			elif direction == "w":
				self.move_player("west")
			return
		
		#get and take item commands
		if commands[0] in ['get','take']:
			found = False
			for item in self.rooms[self.player.location].item_list:
				if commands[1] == item.name:
					self.player.add_item(item)
					self.rooms[self.player.location].item_list.remove(item)
					found = True
					print (commands[1]+" taken")
			if not found:
				print("I dont see a "+commands[1]+" here.")
			return
			
		if commands[0] == "drop":
			drop_item = commands[1]
			for item in self.player.inventory:
				if item.name == drop_item:
					self.player.inventory.remove(item)
					print(item.name+" droped")
					self.rooms[self.player.location].item_list.append(item)
					return
			print("You are not carrying that item!")
			return
		
		#open items
		if commands[0] in ['open']:
			#print ("Open routine")
			for item in self.player.inventory:
				#item.print_item()
				#print (item.item_type)
				if item.name == commands[1] and item.item_type == "container":
					#print ("Found it")
					if len(item.items) == 0:
						print ("There is nothing inside.")
					else:
						print ("inside the "+str(commands[1])+" you see:")
						for inside_item in item.items:
							inside_item.print_item()
			return
		print( Adventure.bad_parse_msgs[randint(0, len(Adventure.bad_parse_msgs)-1)])
			
		
			
	def move_player(self, direction):
		global player
		if self.current_room.exits[direction] != None:
			self.player.location = self.rooms[self.player.location ].exits[direction]
			self.current_room = self.rooms[self.player.location ]
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
				
	def main(self):
		while True:
			
			if self.current_room.entered == False:
				game.player.print_player()
				self.current_room.print_room()
			commands = self.get_command()
			self.execute_command(commands)
			
	verbs = {
		'go': move_player,
		'run': move_player,
		'move': move_player,
		'north': move_player,
		'south': move_player,
		'east': move_player,
		'west': move_player
	}
			

			
			
game = Adventure("rooms.txt")
game.main()



		
		
	



			

