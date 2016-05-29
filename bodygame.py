# Version 1.0.0
# https://github.com/chrhyman/bodygame

##################################
# Credits, inspiration, and explanation
#
# This is a Python program to generate an instance (Encounter) of the Body Game.
# The Body Game was devised by Brian Ramirez Kyle, and his story directly inspired
# this program. The story can be read here:
#
# http://www.metabods.com/mb/stories/Body_game.html
#
# Another author, matt1008, wrote another Encounter for the Body Game, also inspired by
# BRK. I've taken inspiration from that work as well. Additionally, as I've created this
# program, BRK has begun a new story in this format, Encounter 813. Both of these can also
# be found on Metabods.
# 
# The idea of the Body Game is an experimental erotic story format. BRK used Excel
# spreadsheets and lots of formulae to generate the skeleton of a story wherein players
# of a mysterious and futuristic game experience randomly chosen changes to their bodies,
# with overrides throwing in more randomness.
#
# Taking inspiration from those stories, without access to BRK's actual Excel sheets,
# I decided to try my hand at making a program that automatically generates
# the same sort of skeleton outline of a story. I wanted to take advantage of the benefits
# you get from using a programming language like Python to do things like track some of
# the changes to age, cock size, weight, height, and so on. But of course, I didn't want
# to limit changes to those easily-tracked attributes, so there is also a 'notes' variable
# that is just a list of all changes undergone by each player, in order.
#
# While I'm not extremely new to coding, I'm entirely self-taught. I've never taken a
# single computer science class (except one in computational linguistics which barely
# taught what a FOR loop was). As a result, if you are familiar with programming
# languages, you'll notice that much of this code is not elegant, readable, or Pythonic.
# I'm a naturally verbose human being, and my code reflects that. I don't mind some levels
# of redundancy, which is probably not a good thing. Sometimes I define a function just to
# create a list that I use in only one other function. It happens.
#
# Feel free to edit any part of this code except the license block. You might want to
# add possible changes or edit the starting ranges for your players. I'm trying to mark
# places you can make changes so it's easy for people with no programming background.
##################################

##################################
# Using this program
#
# If you simply run this program, it will output the text of one standard Body Game with 9
# rounds, which hits about 900 lines with the way I've coded the outputs. I recommend
# making it so the output is sent to a .txt file for easier reading if you have a command
# line setup.
#
# To edit the program, follow the comment block guidelines. If you aren't very Python
# literate, each major function has a comment block like this one that tells you what
# the function does. Follow notes for what you can edit and what you should only edit if
# you're familiar with Python.
#
# If you have feature requests or recommendations, send me an email or post to the github!
##################################

##################################
# Do NOT edit or remove this comment block.
#
# This Python code is released under the MIT License, found below.
#
# This code has been made available under this license by its creator free of charge.
# If you wish to donate to the developer, Chris Hyman, you may send your generous gift to:
#
# Paypal: hymanator93@gmail.com
#
# Please feel no obligation to donate in order to enjoy this program.
#
# MIT License
#
# Copyright (c) 2016 Chris Hyman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
##################################

##################################
# If you have questions, feel free to email me at chrhyman@gmail.com
# or, create an issue on the github repo to let me know about bugs or feedback: 
# https://github.com/chrhyman/bodygame/issues
##################################

# bodygame.py

import random
import math

##################################
# Unit conversions
##################################
def intoft(n):
	ft = str(int(math.floor(n/12)))
	inch = str(n % 12)
	return ft + '\'' + inch + '\"'

def intocm(n):
	cm = str(n*2.54)
	return cm + 'cm'

def intomt(n):
	mt = str(n*2.54/100)
	return mt + 'm'

def lbtokg(n):
	kg = str(n*0.454)
	return kg + 'kg'

##################################
# Global variable for number of players. Edit '5' or '7' to your min/max no. of players
# Don't use quote marks. Any integer is fine (large numbers may take a lot of processing)
##################################
p = random.randint(5,7)

##################################
# Global list of players who are targeted by someone.
# Ensures that all players are targeted.
##################################
pickedtar = []

##################################
# The player class that defines how attributes are stored and how they are randomly
# generated. This is where you can edit the ranges for character generation (i.e., how the
# players are before the game begins).
##################################
class Player:

	# Do not edit __init__ unless you know what you're doing!
	def __init__(self):	# initialize attributes
		self.name = ''
		self.agee = 0
		self.ethn = ''
		self.heig = 0
		self.weig = 0
		self.shoe = 0
		self.clen = 0
		self.cwid = ''
		self.hair = ''
		self.feel = ''
		self.targ = 0
		self.notes = []	# A list for all changes undergone by a player, in order.

	# Add names to the list between single quotes with the comma outside the quotes.
	# You can also freely delete names from the list without needing to edit anything else
	def gName(self):
		pNames = ['Sean', 'Dean', 'Sam', 'Tyler', 'Michael', 'Dustin', 'Charles', 'Mark',
			'Jay', 'Tim', 'Ted', 'John', 'Henry', 'Jerry', 'Axel', 'Chris', 'Paul',
			'Ethan', 'Wayne', 'Warren']
		self.name = random.choice(pNames)

	# You can change "18" and "45" below to any positive integer.
	# The result will be inclusive. Do not put the numbers in quotes.
	# Age can be changed by the program.
	def gAgee(self):
		self.agee = random.randint(18, 45)

	# Just some example starting points for writing. You can change this to whatever
	# you want, actually. I chose to go with nationalities/ethnicities/etc because that
	# gives you a lot to work with. This attribute isn't referenced elsewhere in the
	# program or changed. Basically this is a list of strings and the program picks one
	# randomly for each player. Again, use single quotes with commas outside the quotes.
	def gEthn(self):
		pEthns = ['American (White)', 'American (Black)', 'American (Latino)',
			'American (Mixed Heritage)', 'Native American/Indigenous', 'Japanese',
			'Chinese', 'Korean', 'French', 'German', 'Italian', 'British', 'Mexican',
			'Spanish', 'Indian', 'Middle Eastern', 'Russian', 'Brazilian', 'Canadian',
			'Misc: North/Central American', 'Misc: South American', 'Misc: European',
			'Misc: Asian', 'Misc: Oceanic/Islander', 'Misc: African']
		self.ethn = random.choice(pEthns)

	# Starting height in inches. You can change the numbers. 62-78 is 5'2" to 6'6".
	# The program will convert this to x'x" format and meters as well. If the program
	# changes a player's height it will store in inches and be converted when displayed.
	def gHeig(self):
		self.heig = random.randint(62,78) # in inches

	# Starting weight in pounds. You can change the numbers as you wish.
	def gWeig(self):
		self.weig = random.randint(120,250) # in pounds

	# Starting shoe size in US. Only did integers here.
	# Can be edited by the program, so don't add letters without changing other functions.
	# Program edits treat this number as a float, but only use integers in generation.
	def gShoe(self):
		self.shoe = random.randint(7,14) # US

	# Starting cock length in inches. Returns a float rounded to tenths.
	# Change "4.0" or "10.0" to affect range. "1" is just the rounding. No quote marks.
	def gClen(self):
		self.clen = round(random.uniform(4.0,10.0), 1)

	# Starting cock shape. Used to be 'width' in inches. Add shapes (adj) as you please.
	def gCwid(self):
		pCwids = ['wide','thick','narrow','extra-wide','torpedo-shaped','cobra-shaped',
			'flared']
		self.cwid = random.choice(pCwids)

	# Kind of a random one, another writing aide I suppose.
	# natural is a list of possible natural hair colors.
	# unnat is a list of possible dyed hair colors.
	def gHair(self):
		natural = ['brown', 'black', 'blond', 'red', 'gray']
		unnat = ['bleach blond', 'platinum', 'a vibrant primary color', 'a pastel color']
		self.hair = random.choice(natural)
		randno = random.random()
		if (randno > 0.8):		# 80% chance to not have dyed hair, stay in range 0-1.
			self.hair += ' and dyed '
			self.hair += random.choice(unnat)

	# Another writing help: just gives a random feeling the player has at the beginning.
	# Can add or remove entries to list as you please. The game doesn't affect this
	# attribute after picking a random one for the beginning.
	def gFeel(self):
		pFeels = ['nervous', 'anxious', 'cocky', 'proud', 'horny', 'ready', 'sexy',
			'excited', 'aroused', 'pleased', 'eager', 'curious', 'confused']
		self.feel = random.choice(pFeels)

	# Don't edit unless you know what you're doing. Picks targets for each player.
	# When it's Player X's turn, they alter their target. A player's target can
	# be themself.
	def gTarg(self):
		x = random.randint(0,p-1)
		if (x not in pickedtar):
			self.targ = x
			pickedtar.append(x)
		else:
			self.gTarg()

##################################
# Create a global list of players and generate their attributes
##################################
players = [Player() for i in range(p)]
for i in range(p):
	players[i].gName()
	players[i].gAgee()
	players[i].gEthn()
	players[i].gHeig()
	players[i].gWeig()
	players[i].gShoe()
	players[i].gClen()
	players[i].gCwid()
	players[i].gHair()
	players[i].gFeel()
	players[i].gTarg()
##################################
# Error handling.
##################################
for i in range (p):
	if (i not in pickedtar): print 'Error: Player {} is NOT targeted by any other player.\
All results below, if visible, are in error.'.format(i+1)

##################################
# Returns the current state of a particular player in block format.
# Only returns some attributes.
##################################
def gamestate(z):
	az = str(z+1)
	atar = str(players[z].targ + 1)
	allnotes = ''
	for i in range(len(players[z].notes)-1): allnotes += players[z].notes[i] + ', '
	allnotes += players[z].notes[-1]
	current = 'Player {}\nName: {}\nAge: {}\nHeight: {}\nWeight: {}lb.\nShoe size: {} \
		\nCock length: {}in.\nCock shape: {}\nNotes: {}\n'.format(az, players[z].name, \
		players[z].agee, intoft(players[z].heig), players[z].weig, players[z].shoe, \
		players[z].clen, players[z].cwid, allnotes)
	print current

##################################
# Gives the gamestate for all players including initial-only details like feelings.
# Only used at the very beginning of the game.
##################################
def verbose():
	for i in range(p):
		ai = i+1
		atar = players[i].targ + 1
		nheig = intoft(players[i].heig)
		nmheig = intomt(players[i].heig)
		nmweig = lbtokg(players[i].weig)
		nmclen = intocm(players[i].clen)
		display = '''Player {0}\'s name is {1}, {2} years old. He is {3}.
He\'s {4} tall ({5}) and weighs {6}lb ({7}). {1} wears a size {8} shoe.
His {11}{12} cock is {9}in. long ({10}). His hair is {13}.
He\'s feeling {14}. His target is player {15}.'''
		print display.format(ai, players[i].name, players[i].agee, players[i].ethn, 
			nheig, nmheig, players[i].weig, nmweig, players[i].shoe, players[i].clen, 
			nmclen, players[i].cwid, '', players[i].hair, players[i].feel, atar)+'\n'

##################################
# Global dictionaries that hold Player:Attribute pairs
##################################
adict = {}
hdict = {}
wdict = {}
sdict = {}
cdict = {}

##################################
# Re-updates the dictionaries when called.
##################################
def makedicts():
	for i in range(p):
		adict[i] = players[i].agee
		hdict[i] = players[i].heig
		wdict[i] = players[i].weig
		sdict[i] = players[i].shoe
		cdict[i] = players[i].clen

##################################
# Takes dictionary argument and a bool.
# Finds the player with the max (bool=True) or min (bool=False) in that attribute.
##################################
def minmax(d, bool):
	v = list(d.values())
	k = list(d.keys())
	if bool: return k[v.index(max(v))]
	else: return k[v.index(min(v))]

##################################
# Takes a category and finds the minimum or maximum member. True is max, False is min.
# Returns the player number index, or '900' error.
# Also updates the dictionaries to current stats when called.
##################################
def findplayer(cat, bool):
	makedicts()
	if (cat==3): return minmax(adict,bool)
	elif (cat==4): return minmax(hdict,bool)
	elif (cat==5): return minmax(wdict,bool)
	elif (cat==6): return minmax(sdict,bool)
	elif (cat==7): return minmax(cdict,bool)
	else: return 900	# error ID for cat error

##################################
# A coinflip that is slightly biased to True. Change the bias within range 0-1.
# Affects several functions in various ways.
##################################
def coinflip():
	if (random.random() > 0.475): return True
	else: return False

##################################
# Overrides can change who the target is, or add a new target.
# I've simplified the override system GREATLY to make it easy to code.
# Possibilities: "Other" is most frequent, and doesn't change the target in the program.
# Can also target sender, player to sender/target's left or right, or a player with the
# minimum or maximum value in a particular attribute.
# For all overrides, it's possible for the override to be INSTEAD or IN ADDITION
# INSTEAD means the old target is no longer a target.
# IN ADDITION means the old target is also a target.
# For rounds with two overrides, any "instead" gets overridden by any "in addition".
##################################

##################################
# Creates a list that defines an override. [0] is the ID number for override category.
# [1] is a verbose explanation. [2] defines INSTEAD (false) or IN ADDITION (true).
# [3] is left/right for the two OvRs with that possibility, or False.
# [4] is min/max for attribute OvRs, or False
##################################
def createor(pick,a1,a2=False,a3=False,a4=False): return [pick, a1, a2, a3, a4]

##################################
# Defines overrides when given a number. Returns a list defining the override.
# 'other' is more likely than other overrides. It's up to the author whether 'other' is
# actually no override, or a more creative one.
# Examples: All players come. Half. Double. Detachable. Next change too. Skip next turn.
# Same change to X (part). Quantity change. Previous change too. Recurs with each orgasm.
# Affects all targets. And so on.
##################################
def getoride(pick):
	oresults = []
	if (8 <= pick <= 11):	#most likely; 8 is actual ID number.
		oresults = createor(8, 'other')
	elif (pick == 0):
		oresults = createor(0, 'Sender', coinflip())
	elif (pick == 1):
		side = 'left'
		if (coinflip()): side = 'right'
		a1 = 'target\'s ' + side
		oresults = createor(1, a1, coinflip(), side)
	elif (pick == 2):
		side = 'left'
		if (coinflip()): side = 'right'
		a1 = 'sender\'s ' + side
		oresults = createor(2, a1, coinflip(), side)
	elif (pick == 3):
		which = 'min'
		if (coinflip()): which = 'max'
		oresults = createor(3, 'age', coinflip(), False, which)
	elif (pick == 4):
		which = 'min'
		if (coinflip()): which = 'max'
		oresults = createor(4, 'height', coinflip(), False, which)
	elif (pick == 5):
		which = 'min'
		if (coinflip()): which = 'max'
		oresults = createor(5, 'weight', coinflip(), False, which)
	elif (pick == 6):
		which = 'min'
		if (coinflip()): which = 'max'
		oresults = createor(6, 'shoe', coinflip(), False, which)
	elif (pick == 7):
		which = 'min'
		if (coinflip()): which = 'max'
		oresults = createor(7, 'cock', coinflip(), False, which)
	else:
		oresults = [404,'error',False,False,False]
	return oresults

##################################
# EDITABLE: Make "Other" override more or less likely on the first line of this func.
# Returns an override list with original target t and sender s.
# Appends an entry to the results list with the final target(s) as a list.
##################################
def override(s, t):
	pick = random.randint(0,11)	# Change between 8-11 to make "Other" less frequent.
								# Change to 7 to remove "Other" possibility.
	outcome = getoride(pick)
	results = outcome
	results.append([])
	if (outcome[0] == 0): results[5].append(s)	# sender
	elif (outcome[0] == 1):			# target's left/right
		nt = t
		if (outcome[3]=='left'):
			if (nt >= (p-1)): nt = 0
			else: nt += 1
		if (outcome[3]=='right'):
			if (nt == 0): nt = p-1
			else: nt -= 1
		results[5].append(nt)
	elif (outcome[0] == 2):			# sender's left/right
		nt = s
		if (outcome[3]=='left'):
			if (nt >= (p-1)): nt = 0
			else: nt += 1
		if (outcome[3]=='right'):
			if (nt == 0): nt = p-1
			else: nt -= 1
		results[5].append(nt)
	elif (3 <= outcome[0] <= 7):	# attribute-based
		if (outcome[4]=='max'): results[5].append(findplayer(outcome[0], True))
		elif (outcome[4]=='min'): results[5].append(findplayer(outcome[0], False))
		else: results[5].append(700)	# Error ID.
	elif (outcome[0] == 8): results[5].append(t) # if NONE/OTHER, original target remains
	else: results[5] = 'error 200'
	if outcome[2]: results[5].append(t)	# If IN ADDITION, append original target.
	return results

##################################
# Deciphers an override list into text.
##################################
def decipher(list):
	string = ''
	if list[0] == 8: string = 'Other.'
	else:
		if (list[0] == 0): string = list[1]
		elif (1 <= list[0] <= 2): string = 'Player to ' + list[1]
		elif (list[0] == 3):
			if (list[4] == 'max'): string = 'Oldest player'
			else: string = 'Youngest player'
		elif (list[0] == 4):
			if (list[4] == 'max'): string = 'Tallest player'
			else: string = 'Shortest player'
		elif (list[0] == 5):
			if (list[4] == 'max'): string = 'Heaviest player'
			else: string = 'Lightest player'
		elif (list[0] == 6):
			if (list[4] == 'max'): string = 'Player with largest feet'
			else: string = 'Player with smallest feet'
		elif (list[0] == 7):
			if (list[4] == 'max'): string = 'Player with longest cock'
			else: string = 'Player with shortest cock'
		if list[2]: string += ' too.'
		else: string += ' instead.'
	return string

##################################
# Takes an iterable of of two-item iterables. Returns a random first element chosen
# using the weight of the second element. Example: wchoice([('x',10),('y',400),('z',1)])
##################################
def wchoice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   u = 0
   for c, w in choices:
      if u + w >= r: return c
      u += w
   assert False, "Error 100: Weighted choice failure"

##################################
# Takes a list of parts in part and assigns the respective weights in wei
##################################
def addwei(part, wei): return [(part[i], wei[i]) for i in range(len(part))]

##################################
# A global of all categories for changes and their respective weights. Weight can be any
# positive integer (their relative distances determine weight). To make 'less hairy' more/
# less frequent, find its index (index 5, the 6th entry in list) and change that number in
# wei (the number at index 5, i.e. the 6th position, is 20).
# Adding a transformation type may involve some necessary Python knowledge.
##################################
cats = ['less defined', 'narrower', 'smaller', 'shorter', 'higher', 'less hairy',
	'decreased', 'more defined', 'wider', 'larger', 'longer', 'deeper', 'hairier',
	'increased','stronger', 'thicker', 'more cocklike', 'more contagious', 'more massive',
	'more attractive', 'doubled', 'halved', 'into cock', 'quantity increase', 'inflated',
	'nipple come', 'constantly']

wei = [10, 10, 20, 7, 3, 20, 25, 40, 60, 165, 95, 5, 75, 150, 40, 50, 70, 20, 85,
	45, 45, 15, 30, 40, 25, 15, 25]

##################################
# Pairs categories with weights and ID numbers
##################################
wncats = [([i, cats[i]], wei[i]) for i in range(len(cats))]

##################################
# A global list of body parts to change, made into a list paired with ID number
##################################
parts = ['age', 'arms', 'ass', 'attractiveness', 'balls', 'belly', 'body',
	'cock', 'coming', 'come production', 'cuteness', 'face', 'feet', 'hair',
	'hairiness', 'hands', 'hard', 'head', 'height', 'horniness', 'horny', 'legs',
	'muscles', 'in need of something in their ass', 'nipples', 'pecs', 'thighs', 'toes',
	'tongue', 'torso', 'weight', 'voice', 'player', False]
nparts = [[i, parts[i]] for i in range(len(parts))]

##################################
# Picks something to affect based on the category chosen.
# Each part is weighted by the number list. These weights can be changed to any positive
# integer; relative distances determine weight. In order to know what numbers refer to
# which categories and parts, refer to the WEIGHT guide at the end of this program.
##################################

def pickpart(cat):
	if cat == 0: poss = addwei([nparts[2], nparts[25]], [60, 40])
	elif cat == 1: poss = addwei([nparts[7], nparts[28]], [40, 60])
	elif cat == 2: poss = addwei([nparts[7], nparts[12], nparts[6]], [40, 75, 65])
	elif cat == 3: poss = addwei([nparts[7], nparts[13], nparts[21], nparts[28]],
		[30, 20, 45, 40])
	elif (cat == 4 or cat == 11): poss = [(nparts[31], 100)]
	elif (cat == 5 or cat == 12): poss = addwei([nparts[1],nparts[2],nparts[6],nparts[11], 
		nparts[21], nparts[25], nparts[29]], [100, 100, 125, 150, 100, 100, 110])
	elif cat == 6: poss = addwei([nparts[0], nparts[10], nparts[14], nparts[18],
		nparts[30]], [50, 75, 125, 150, 150])
	elif cat == 7: poss = addwei([nparts[1], nparts[2], nparts[6], nparts[21], nparts[22],
		nparts[25], nparts[26], nparts[29]], [100, 75, 150, 100, 175, 100, 100, 125])
	elif cat == 8: poss = addwei([nparts[2], nparts[7], nparts[12], nparts[28]],
		[100, 100, 75, 75])
	elif cat == 9: poss = addwei([nparts[1], nparts[2], nparts[4], nparts[5], nparts[6],
		nparts[7], nparts[12], nparts[15], nparts[21], nparts[22], nparts[24], nparts[25],
		nparts[26], nparts[28]], [50, 90, 125, 50, 100, 190, 70, 25, 50, 70, 75,90,25,30])
	elif cat == 10: poss = addwei([nparts[1], nparts[7], nparts[13],nparts[21],nparts[28],
		nparts[29]], [25, 100, 30, 35, 70, 10])
	elif cat == 13: poss = addwei([nparts[0], nparts[9], nparts[10], nparts[3],nparts[19],
		nparts[18], nparts[30], nparts[22], nparts[14]], [5, 50, 10, 10, 10,75,75,70,50])
	elif cat == 14: poss = addwei([nparts[1], nparts[21],nparts[26],nparts[25],nparts[29],
		nparts[6]], [100, 100, 75, 50, 100, 125])
	elif cat == 15: poss = addwei([nparts[1], nparts[21], nparts[26],nparts[25],nparts[2],
		nparts[6], nparts[28]], [50, 50, 25, 75, 100, 25, 75])
	elif cat == 16: poss = addwei([nparts[27], nparts[28], nparts[24]], [25, 75, 75])
	elif cat == 17: poss = [(nparts[19], 100)]
	elif cat == 18: poss = addwei([nparts[28], nparts[7], nparts[4],nparts[25],nparts[22],
		nparts[2]], [50, 100, 120, 80, 50, 100])
	elif cat == 19: poss = addwei([nparts[25], nparts[7],nparts[31],nparts[29],nparts[12],
		nparts[11], nparts[6], nparts[24], nparts[14], nparts[2]], [100, 150, 25, 50, 30,
		100, 100, 100, 30, 70])
	elif cat == 20: poss = addwei([nparts[1], nparts[3], nparts[6], nparts[7],
		nparts[9], nparts[10], nparts[14], nparts[18], nparts[19], nparts[21], nparts[30],
		nparts[32]], [50, 40, 10, 70, 75, 10, 20, 15, 10, 50, 15, 1])
	elif cat == 21: poss = addwei([nparts[18], nparts[30], nparts[14]], [50, 50, 100])
	elif cat == 22: poss = addwei([nparts[21], nparts[27], nparts[28], nparts[24]], [25,
		25, 100, 75])
	elif cat == 23: poss = addwei([nparts[21], nparts[1], nparts[7], nparts[6]], [50, 50,
		100, 10])
	elif cat == 24: poss = addwei([nparts[5], nparts[4], nparts[7], nparts[25],
		nparts[17]], [25, 100, 100, 50, 10])
	elif cat == 25: poss = [(nparts[33], 100)]
	elif cat == 26: poss = addwei([nparts[16], nparts[8], nparts[20], nparts[23]], [100,
		70, 80, 75])
	else: poss = [([250,'error'], 100)]
	return wchoice(poss)

##################################
# Picks the amount of change to make, if applicable
##################################
def howmuch(cat, part):
	if (cat in [20, 21, 22, 25, 26]):
		return False
	elif (cat == 23):
		if part in [21, 1]: return wchoice([(2,100),(4,10),(6,1)])	# arms and legs
		elif part == 7: return wchoice([(1,100),(2,30),(3,10),(4,1)])	# cocks
		else: return 1	# body only can increase +1 at a time
	elif cat == 24: return random.choice([20,40,40,60,60,80,100]) # inflation
	else:	# return a percentage - first number is percentage of 100, second is weight
		return wchoice([(10, 150), (20, 175), (30, 200), (40, 175), (50, 100), (60, 50),
			(70, 25), (80, 10), (90, 5), (100, 1)])

##################################
# A global list for a change that pickchange() redefines. Also acts as var template.
##################################
change = ['targets', 'category ID', 'category in words', 'affected ID',
	'affected in words', 'degree of change']

##################################
# Defines changes and picks one at random when called.
# Returns a change list including the targets in tar.
##################################
def pickchange(tar):
	change[0] = tar
	q1 = wchoice(wncats)
	change[1] = q1[0]
	change[2] = q1[1]
	q2 = pickpart(change[1])
	change[3] = q2[0]
	change[4] = q2[1]
	q3 = howmuch(change[1], change[3])
	change[5] = q3
	return change

##################################
# write change in ch to notes of all targets
##################################
def wnote(ch):
	hread = ''
	if ch[1] in [6, 13, 24]: hread = '{} {} {}%'.format(ch[4],ch[2],ch[5])
	elif ch[1] in [20, 21]: hread = '{} {}'.format(ch[4],ch[2])
	elif ch[1] == 22: hread = '{} transformed {}'.format(ch[4],ch[2])
	elif ch[1] == 23:
		hread = 'quantity of {} increased: +{}'.format(ch[4],ch[5])
	elif ch[1] == 25: hread = 'nipples can come'
	elif ch[1] == 26:
		hread = '{} {}'.format(ch[2],ch[4])
	else:
		hread = '{} {}% {}'.format(ch[4],ch[5],ch[2])
	for i in range(len(ch[0])):
		players[ch[0][i]].notes.append(hread)

##################################
# I don't feel like coming up with anything more elegant
# All this shit just to do Player X VS Players X and Y VS Players X, Y, and Z
##################################
def listpl(t):
	hrt = 'No one'
	if len(t) == 1:
		hrt = 'Player ' + str(t[0]+1)
	elif len(t) == 2:
		hrt = 'Players ' + str(t[0]+1) + ' and ' + str(t[1]+1)
	elif len(t) > 2:
		x = len(t)
		y = 0
		hrt = 'Players '
		while x > 2:
			hrt += str(t[y]+1) + ', '
			y += 1
			x -= 1
		hrt += str(t[y]+1) + ', and ' + str(t[y+1]+1)
	return hrt

##################################
# Classes to clean up moda() significantly
##################################
class Dec:
	def cock(self, tar, per):
		for i in range(len(tar)): players[tar[i]].clen *= ((100-per) / 100.0)
	def age(self, tar, per):
		for i in range(len(tar)): players[tar[i]].agee *= ((100-per) / 100.0)
	def heig(self, tar, per):
		for i in range(len(tar)): players[tar[i]].heig *= ((100-per) / 100.0)
	def weig(self, tar, per):
		for i in range(len(tar)): players[tar[i]].weig *= ((100-per) / 100.0)
	def shoe(self, tar, per):
		for i in range(len(tar)): players[tar[i]].shoe *= ((100-per) / 100.0)
	def legs(self, tar, per):	# approx by taking half of height, applying change, adding
		for i in range(len(tar)):
			half = 0.5*players[tar[i]].heig
			x = (half*((100-per)/100.0))+half
			players[tar[i]].heig = x

Dec = Dec()

class Inc:
	def cock(self, tar, per):
		for i in range(len(tar)): players[tar[i]].clen *= ((100+per) / 100.0)
	def age(self, tar, per):
		for i in range(len(tar)): players[tar[i]].agee *= ((100+per) / 100.0)
	def heig(self, tar, per):
		for i in range(len(tar)): players[tar[i]].heig *= ((100+per) / 100.0)
	def weig(self, tar, per):
		for i in range(len(tar)): players[tar[i]].weig *= ((100+per) / 100.0)
	def shoe(self, tar, per):
		for i in range(len(tar)): players[tar[i]].shoe *= ((100+per) / 100.0)
	def legs(self, tar, per):	# approx by taking half of height, applying change, adding
		for i in range(len(tar)):
			half = 0.5*players[tar[i]].heig
			x = (half*((100+per)/100.0))+half
			players[tar[i]].heig = x

Inc = Inc()

##################################
# if change modifies another attribute, apply that modification using the change in ch
# and the target(s) in that list
##################################
def moda(ch):
	if ch[1] == 2:	# smaller
		if ch[3] == 7: Dec.cock(ch[0],ch[5])
		if ch[3] == 12:	Dec.shoe(ch[0],ch[5])
		if ch[3] == 6:	# body
			Dec.shoe(ch[0],ch[5])
			Dec.heig(ch[0],ch[5])
			Dec.weig(ch[0],ch[5])
			Dec.cock(ch[0],ch[5])
	elif ch[1] == 3:	# shorter
		if ch[3] == 7: Dec.cock(ch[0],ch[5])
		if ch[3] == 21: Dec.legs(ch[0],ch[5])
	elif ch[1] == 6:	# decrease
		if ch[3] == 0: Dec.age(ch[0],ch[5])
		if ch[3] == 18: Dec.heig(ch[0],ch[5])
		if ch[3] == 30: Dec.weig(ch[0],ch[5])
	elif ch[1] == 9:	# larger
		if ch[3] == 6:	# body
			Inc.shoe(ch[0],ch[5])
			Inc.heig(ch[0],ch[5])
			Inc.weig(ch[0],ch[5])
			Inc.cock(ch[0],ch[5])
		if ch[3] == 7: Inc.cock(ch[0],ch[5])
		if ch[3] == 12: Inc.shoe(ch[0],ch[5])
		if ch[3] == 21: Inc.legs(ch[0],ch[5])
	elif ch[1] == 10:	# longer
		if ch[3] == 7: Inc.cock(ch[0],ch[5])
		if ch[3] in [21, 29]: Inc.legs(ch[0],ch[5])
	elif ch[1] == 13:	# increase
		if ch[3] == 0: Inc.age(ch[0],ch[5])
		if ch[3] == 18: Inc.heig(ch[0],ch[5])
		if ch[3] == 30: Inc.weig(ch[0],ch[5])
	elif ch[1] == 18:	# more massive
		if ch[3] == 7: Inc.cock(ch[0],ch[5])
	elif ch[1] == 20:	# double
		if ch[3] == 18:
			for i in range(len(ch[0])): players[ch[0][i]].heig *= 2
		if ch[3] == 30:
			for i in range(len(ch[0])): players[ch[0][i]].weig *= 2
	elif ch[1] == 21:	# halve
		if ch[3] == 18:
			for i in range(len(ch[0])): players[ch[0][i]].heig *= 0.5
		if ch[3] == 30:
			for i in range(len(ch[0])): players[ch[0][i]].weig *= 0.5
	elif ch[1] == 24:	# inflated
		if ch[3] == 7: Inc.cock(ch[0],ch[5])
	else: print 'Error: Category ID not found.'
	
##################################
# Makes a change
##################################
def makechange(tar):
	if tar == []: print 'No changes.'
	else:
		ch = pickchange(tar)	# Initialize the change.
		hread = ''		# Initialize human-readable output
		hrt = listpl(ch[0])	# Format the list of players affected.
	# Format the human-readable output of the change.
		if ch[1] in [6, 13, 24]: hread = '{}\'s {} {} {}%.'.format(hrt,ch[4],ch[2],ch[5])
		elif ch[1] in [20, 21]: hread = '{}\'s {} {}.'.format(hrt,ch[4],ch[2])
		elif ch[1] == 22: hread = '{}\'s {} transformed {}.'.format(hrt,ch[4],ch[2])
		elif ch[1] == 23:
			hread = 'Quantity of {}\'s {} increased: +{}.'.format(hrt,ch[4],ch[5])
		elif ch[1] == 25: hread = '{}\'s nipples can come.'.format(hrt)
		elif ch[1] == 26:
			pl = 'is'
			if len(ch[0]) > 1: pl = 'are'
			hread = '{} {} {} {}.'.format(hrt,pl,ch[2],ch[4])
		else:
			hread = '{}\'s {} {}% {}.'.format(hrt,ch[4],ch[5],ch[2])
		wnote(ch)	# write changes to notes list for each target
		if ch[1] in [2, 3, 6, 9, 10, 13, 18, 20, 21, 24]: moda(ch)	# if poss, mod stats
		print 'Transform: ' + hread +'\n'	# Output the transformation

##################################
# Defines a single turn by one player.
# Sender a, target b, and with c overrides.
##################################
def turn(a, b, c):
	orides = override(a, b)
	orides2 = override(a, b)
	mtars = []	# A list of targets to affect.
	if (c==0):
		print 'Override: None.'
		orides = [999,'none',False,False,False,[b]]
		orides2 = False
	elif (c==1):
		orides2 = False
		print 'Override: ' + decipher(orides)
	elif (c==2):
		print 'Override: ' + decipher(orides) + '\nand Override: ' + decipher(orides2)
	else:
		orides = [400,'error',False,False,False,None] # error ID
		print 'Error 400'
	if orides:
		if orides[5]: mtars.extend(orides[5])
	if orides2:
		if orides2[5]: mtars.extend(orides2[5])
	mtars = sorted(set(mtars))	# remove duplicates, put in numerical order
	makechange(mtars)	# Send targets to make change.

##################################
# Defines a single round. Executes round number r when called.
##################################
def round(r):
	print '\n\nThis is round ' + str(r) + '.\n'
	
	# This setup has no overrides the first round,
	# then one override for rounds 2-8,
	# then two overrides for each additional round.
	noov = 0
	if (r>1):
		noov += 1
	if (r>8):
		noov += 1
	print 'There is/are ' + str(noov) + ' override(s) for each turn this round.\n\n'
	
	# Iterates over the number of players and gives each player their turn.
	for i in range(p):
		print 'It is player ' + str(i+1) + '\'s turn to change player ' \
			+ str(players[i].targ+1) + '.'
		turn(i, players[i].targ, noov)

	# Iterates over the players and gives each gamestate. Put a # at the beginning
	# of each of the next two lines if this is too much text and you want to cut down.
	print '\nThat is the end of round {}. Current player stats:\n'.format(r)
	for i in range(p): gamestate(i)

##################################
# Creates and initiates the game.
#
# You can edit the number of rounds here.
##################################
def game():
	print 'Welcome to the Body Game!\n\n'
	print 'There are ' + str(p) + ' players.\n\n'
	verbose()
	rs = 9	# Defines the number of rounds. Default is 9.
	for i in range(rs):
		round(i+1)
	print '\n\n\nAnd that concludes the Body Game! Thank you for playing.'

game()

##################################
# Appendix
##################################

# WEIGHT guide:
alloftheweights = ''' 
([ID#, 'change type'], weight of change): [([ID#, 'body part'], weight of part), (etc)]

The part weights can be edited in pickpart() (around line 550) and the category weights
can be edited in the 'wei' list around line 520.

You can make a weight 0 to prevent it from being rolled.

This text block between triple quotes is simply explanatory and holds no other role.

([0, 'less defined'], 10): [([2, 'ass'], 60), ([25, 'pecs'], 40)]
([1, 'narrower'], 10): [([7, 'cock'], 40), ([28, 'tongue'], 60)]
([2, 'smaller'], 20): [([7, 'cock'], 40), ([12, 'feet'], 75), ([6, 'body'], 65)]
([3, 'shorter'], 7): [([7, 'cock'], 30), ([13, 'hair'], 20), ([21, 'legs'], 45),
	([28, 'tongue'], 40)]
([4, 'higher'], 3): [([31, 'voice'], 100)]
([5, 'less hairy'], 20): [([1, 'arms'], 100), ([2, 'ass'], 100), ([6, 'body'], 125),
	([11, 'face'], 150), ([21, 'legs'], 100), ([25, 'pecs'], 100), ([29, 'torso'], 110)]
([6, 'decreased'], 25): [([0, 'age'], 50), ([10, 'cuteness'], 75),
	([14, 'hairiness'], 125), ([18, 'height'], 150), ([30, 'weight'], 150)]
([7, 'more defined'], 40): [([1, 'arms'], 100), ([2, 'ass'], 75), ([6, 'body'], 150),
	([21, 'legs'], 100), ([22, 'muscles'], 175), ([25, 'pecs'], 100),
	([26, 'thighs'], 100), ([29, 'torso'], 125)]
([8, 'wider'], 60): [([2, 'ass'], 100), ([7, 'cock'], 100), ([12, 'feet'], 75),
	([28, 'tongue'], 75)]
([9, 'larger'], 165): [([1, 'arms'], 50), ([2, 'ass'], 90), ([4, 'balls'], 125),
	([5, 'belly'], 50), ([6, 'body'], 100), ([7, 'cock'], 190), ([12, 'feet'], 70),
	([15, 'hands'], 25), ([21, 'legs'], 50), ([22, 'muscles'], 70), ([24, 'nipples'], 75),
	([25, 'pecs'], 90), ([26, 'thighs'], 25), ([28, 'tongue'], 30)]
([10, 'longer'], 95): [([1, 'arms'], 25), ([7, 'cock'], 100), ([13, 'hair'], 30),
	([21, 'legs'], 35), ([28, 'tongue'], 70), ([29, 'torso'], 10)]
([11, 'deeper'], 5): [([31, 'voice'], 100)]
([12, 'hairier'], 75): [([1, 'arms'], 100), ([2, 'ass'], 100), ([6, 'body'], 125),
	([11, 'face'], 150), ([21, 'legs'], 100), ([25, 'pecs'], 100), ([29, 'torso'], 110)]
([13, 'increased'], 150): [([0, 'age'], 5), ([9, 'come production'], 50),
	([10, 'cuteness'], 10), ([3, 'attractiveness'], 10), ([19, 'horniness'], 10),
	([18, 'height'], 75), ([30, 'weight'], 75), ([22, 'muscles'], 70),
	([14, 'hairiness'], 50)]
([14, 'stronger'], 40): [([1, 'arms'], 100), ([21, 'legs'], 100), ([26, 'thighs'], 75),
	([25, 'pecs'], 50), ([29, 'torso'], 100), ([6, 'body'], 125)]
([15, 'thicker'], 50): [([1, 'arms'], 50), ([21, 'legs'], 50), ([26, 'thighs'], 25),
	([25, 'pecs'], 75), ([2, 'ass'], 100), ([6, 'body'], 25), ([28, 'tongue'], 75)]
([16, 'more cocklike'], 70): [([27, 'toes'], 25), ([28, 'tongue'], 75),
	([24, 'nipples'], 75)]
([17, 'more contagious'], 20): [([19, 'horniness'], 100)]
([18, 'more massive'], 85): [([28, 'tongue'], 50), ([7, 'cock'], 100),
	([4, 'balls'], 120), ([25, 'pecs'], 80), ([22, 'muscles'], 50), ([2, 'ass'], 100)]
([19, 'more attractive'], 45): [([25, 'pecs'], 100), ([7, 'cock'], 150),
	([31, 'voice'], 25), ([29, 'torso'], 50), ([12, 'feet'], 30), ([11, 'face'], 100),
	([6, 'body'], 100), ([24, 'nipples'], 100), ([14, 'hairiness'], 30), ([2, 'ass'], 70)]
([20, 'doubled'], 45): [([1, 'arms'], 50), ([3, 'attractiveness'], 40), ([6, 'body'], 10),
	([7, 'cock'], 70), ([9, 'come production'], 75), ([10, 'cuteness'], 10),
	([14, 'hairiness'], 20), ([18, 'height'], 15), ([19, 'horniness'], 10),
	([21, 'legs'], 50), ([30, 'weight'], 15), ([32, 'player'], 1)]
([21, 'halved'], 15): [([18, 'height'], 50), ([30, 'weight'], 50),
	([14, 'hairiness'], 100)]
([22, 'into cock'], 30): [([21, 'legs'], 25), ([27, 'toes'], 25), ([28, 'tongue'], 100),
	([24, 'nipples'], 75)]
([23, 'quantity increase'], 40): [([21, 'legs'], 50), ([1, 'arms'], 50),
	([7, 'cock'], 100), ([6, 'body'], 10)]
([24, 'inflated'], 25): [([5, 'belly'], 25), ([4, 'balls'], 100), ([7, 'cock'], 100),
	([25, 'pecs'], 50), ([17, 'head'], 10)]
([25, 'nipple come'], 15): [([33, False], 100)]
([26, 'constantly'], 25): [([16, 'hard'], 100), ([8, 'coming'], 70), ([20, 'horny'], 80),
	([23, 'in need of something in their ass'], 75)]

'''