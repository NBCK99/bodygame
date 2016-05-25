# Version 0.7.16w21c
# https://github.com/chrhyman/bodygame

##################################
# Credits, inspiration, and explanation
#
# This is a Python program to generate an instance (Encounter) of the Body Game.
# The Body Game was devised by Brian Ramirez Kyle, and his story directly inspired
# this program. The story can be read here:
# http://www.metabods.com/mb/stories/Body_game.html
# Another author, matt1008, wrote another Encounter for the Body Game, also inspired by
# BRK. I've taken inspiration from that work as well, which can be found here:
# http://www.metabods.com/mb/stories/Body_game-_Encounter_56.html
# The idea of the Body Game is an experimental erotic story format. BRK used Excel
# spreadsheets and lots of formulae to generate the skeleton of a story wherein players
# of a mysterious and futuristic game experience randomly chosen changes to their bodies,
# with overrides throwing in more randomness.
#
# Taking inspiration from those stories, without access to BRK's actual Excel sheets,
# I decided (on a whim -- I was actually on a ten-hour roadtrip with nothing to do when
# I started to code this) to try my hand at making a program that automatically generates
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
# of redundancy, which is probably not a good thing.
#
# Feel free to edit any part of this code except the next comment block. You might want to
# add possible changes or edit the starting ranges for your players. Some of the randomly
# selected attributes or changes have absolutely no effect on the rest of the program, and
# can be changed completely as they're entirely text based, simply for the benefit of the
# writer. All of those variables and functions will be marked as such, so hopefully people
# with even less Python knowledge than myself can edit and modify this program.
##################################

##################################
# Do NOT edit or remove this comment block.
#
# This Python code is released under the MIT License, found below.
#
# This code has been made available under this license by its creator free of charge.
# If you wish to donate to the developer, Chris Hyman, you may send your generous gift to:
# Paypal: hymanator93@gmail.com
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
# or to create an issue on the github repo: 
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
# Global variable for the number of players
##################################

p = random.randint(5,7)

##################################
# Global list of players who are targeted by someone.
# Ensures that all players are targeted.
##################################

pickedtar = []

##################################
# The player class that defines how attributes are stored
# and how they are randomly generated. If you wish to add
# or change the possibilities in the program, this is where
# you should make edits. Each section will describe how you
# can edit them.
# Remember that the numbers below are the default player generation,
# not the changes that they can undergo or limits on changes!
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
	def gShoe(self):
		self.shoe = random.randint(7,14) # US

	# Starting cock length in inches. Returns a float rounded to tenths.
	# Change "4.0" or "10.0" to affect range. "1" is just the rounding.
	def gClen(self):
		self.clen = round(random.uniform(4.0,10.0), 1)

	# Starting cock shape. Used to be 'width' in inches. Add shapes (adj) as you please.
	def gCwid(self):
		pCwids = ['wide','thick','narrow','extra-wide','torpedo-shaped','cobra-shaped',
			'flared']
		self.cwid = random.choice(pCwids)

	# Kind of a random one, another writing aide I suppose.
	# natural is a list of possible natural hair colors.
	# unnat is a list of possible dyed hair colors. (don't remove 'diff' though)
	# sometimes gives nonsense, feel free to ignore in writing
	def gHair(self):
		natural = ['brown', 'black', 'blond', 'red', 'gray']
		unnat = ['bleach blond', 'platinum', 'a vibrant primary color',
			'a pastel color', 'diff']
		self.hair = random.choice(natural)
		randno = random.random()
		if (randno > 0.8):		# 80% chance to not have dyed hair, change in range 0-1.
			self.hair += ' and dyed '
			pick = random.choice(unnat)
			if (pick == 'diff'):	# picks dyed color to be another natural hair color
				self.hair += random.choice(natural)
			else:
				self.hair += random.choice(unnat)

	# Another writing help: just gives a random feeling the player has at the beginning.
	# Can add or remove entries to list as you please. The game doesn't affect this
	# attribute after picking a random one for the beginning.
	def gFeel(self):
		pFeels = ['nervous', 'anxious', 'cocky', 'proud', 'horny', 'ready', 'sexy',
			'excited', 'aroused', 'pleased', 'eager', 'curious', 'confused']
		self.feel = random.choice(pFeels)

	# Don't edit unless you know what you're doing. Picks targets for each player.
	# When it's Player X's turn, they change their target. A player's target can
	# be themself.
	def gTarg(self):
		x = random.randint(0,p-1)
		if (x not in pickedtar):
			self.targ = x
			pickedtar.append(x)
		else:
			self.gTarg()

##################################
# Create a global list of players.
##################################
players = [Player() for i in range(0,p)]

##################################
# Randomly generate attributes for each player.
##################################
for i in range(0, p):
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
for i in range (0, p):
	if (i not in pickedtar):
		print 'Error: Player {} is NOT targeted by any other player. \
			All results below, if visible, are in error.\n\n'.format(i+1)

##################################
# Returns the current state of a particular player in block format.
# Only returns some attributes.
##################################
def gamestate(z):
	az = str(z+1)
	atar = str(players[z].targ + 1)
	current = 'Player ' + az + '\nName: ' + players[z].name + '\nAge: ' + \
		str(players[z].agee) + '\nHeight: ' + intoft(players[z].heig) + '\nWeight: ' + \
		str(players[z].weig) + 'lb.\nShoe size: ' + str(players[z].shoe) + \
		'\nCock length: ' + str(players[z].clen) + 'in.\nCock shape: ' + players[z].cwid \
		+ '\nNotes: ' + str(players[z].notes) + '\n'
	print current

##################################
# Gives the gamestate for all players including initial-only details like feelings.
# Only used at the very beginning of the game.
##################################
def verbose():
	for i in range(0, p):
		ai = i+1
		atar = players[i].targ + 1
		nheig = intoft(players[i].heig)
		nmheig = intomt(players[i].heig)
		nmweig = lbtokg(players[i].weig)
		nmclen = intocm(players[i].clen)
		display = '''Player {0}\'s name is {1}, {2} years old. He is {3}.
He\'s {4} tall ({5}) and weighs {6}lb ({7}). {1} wears a size {8} shoe.
His {11}{12} cock is {9}in. long ({10}). His hair is {13}. He\'s feeling
{14}. His target is player {15}.'''
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
	for i in range(0,p):
		adict[i] = players[i].agee
		hdict[i] = players[i].heig
		wdict[i] = players[i].weig
		sdict[i] = players[i].shoe
		cdict[i] = players[i].clen

##################################
# Takes dictionary argument and finds the player with the max/min in that attribute.
##################################
def minmax(d, bool):
	v = list(d.values())
	k = list(d.keys())
	if bool: return k[v.index(max(v))]
	else: return k[v.index(min(v))]

##################################
# Takes a category and finds the minimum or maximum member. True is max, False is min.
# Returns the player number index, or '900' error.
# Also updates the dictionaries when called.
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
# A coinflip that is slightly biased to True
##################################
def coinflip():
	if (random.random() > 0.475): return True
	else: return False

##################################
# Overrides can change who the target is, or add a new target.
# I've simplified the override system GREATLY to make it easy to code.
# The only possibilities (other than no override) are:
# Sender, sender's left or right, target's left or right.
# And by attributes of age, heigh, weight, shoe size, and cock length.
# For attributes, the override will be player with max or player with min.
# The program will probably not handle ties properly.
# For all overrides, it's possible for the override to be INSTEAD or IN ADDITION
# INSTEAD means the old target is no longer a target.
# IN ADDITION means the old target is also a target.
##################################
# Creates a list that defines an override. [0] is the ID number for override category.
# [1] is a verbose explanation. [2] defines INSTEAD or IN ADDITION.
# [3] is left/right for the two ORs with that possibility, or False.
# [4] is min/max for attribute ORs, or False
##################################
def createor(pick,a1,a2=False,a3=False,a4=False):
	theres = []
	theres.append(pick)	# pick number for IDing it
	theres.append(a1)	# explanation in words
	theres.append(a2)	# if True, add new target. if False, replace as new target
	theres.append(a3)	# False if n/a, or str left, right if there's a side
	theres.append(a4)	# False if n/a, or str min, max if it's an attribute
	return theres

##################################
# Defines overrides when given a number. Returns a list defining the override.
# IN ADDITION is slightly more likely than INSTEAD due to coinflip()
# 'other' is more likely than other overrides. It's up to the author
# whether 'other' is actually no override, or a more creative one.
# Examples: All players come. Half. Double. Detachable. Next change too. Skip next turn.
# Same change to X. Quantity change. Previous change too. Recurs with each orgasm.
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
# Returns an override list with original target t and sender s.
# Appends an entry to the results list with the final target(s) as a list.
##################################
def override(s, t):
	pick = random.randint(0,11)
	outcome = getoride(pick)
	results = outcome
	results.append([])
	if (outcome[0] == 0):			# sender
		results[5].append(s)
	elif (outcome[0] == 1):			# target's left/right
		nt = t
		if (outcome[3]=='left'):
			if (nt >= p): nt = 0
			else: nt += 1
		if (outcome[3]=='right'):
			if (nt == 0): nt = p-1
			else: nt -= 1
		results[5].append(nt)
	elif (outcome[0] == 2):			# sender's left/right
		nt = s
		if (outcome[3]=='left'):
			if (nt >= p): nt = 0
			else: nt += 1
		if (outcome[3]=='right'):
			if (nt == 0): nt = p-1
			else: nt -= 1
		results[5].append(nt)
	elif (3 <= outcome[0] <= 7):	# attribute
		if (outcome[4]=='max'):
			results[5].append(findplayer(outcome[0], True))
		elif (outcome[4]=='min'):
			results[5].append(findplayer(outcome[0], False))
		else:
			results[5].append(700)	# Error ID.
	elif (outcome[0] == 8):			# if NONE/OTHER, original target remains
		results[5].append(t)
	else:
		results[5] = 'error 200'
	if outcome[2]:					# If IN ADDITION, append original target.
		results[5].append(t)
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
   upto = 0
   for c, w in choices:
      if upto + w >= r:
         return c
      upto += w
   assert False, "Error 100: Weighted choice failure"

##################################
# A global of all categories for changes and their respective weights. Weight can be any
# positive integer (their relative distances determine weight).
##################################
cats = ['less defined', 'narrower', 'smaller', 'shorter', 'higher', 'less hairy',
	'decrease', 'more defined', 'wider', 'larger', 'longer', 'deeper', 'hairier',
	'increase', 'stronger', 'thicker', 'more cocklike', 'more contagious', 'more massive',
	'more attractive', 'doubled', 'halved', 'into cock', 'quantity increase', 'inflation',
	'nipple cum', 'constantly']

wei = [20, 15, 35, 20, 3, 20, 35, 100, 75, 175, 100, 15, 100, 175, 100, 100, 75, 25, 100,
	150, 125, 50, 40, 50, 25, 10, 20]

##################################
# A list of tuples. The second element in each tuple is the weight. The first element is
# a list itself. The first element of the list is an ID number, second is the category.
# Can be passed directly to wchoice() to select a category according to the weights.
##################################
wncats = [([i, cats[i]], wei[i]) for i in range(len(cats))]

##################################
# A global list of body parts to change, made into a list paired with ID number
##################################
parts = ['age', 'arms', 'ass', 'attractiveness', 'balls', 'belly', 'body', # 0-6
	'cock', 'coming', 'come production', 'cuteness', 'face', 'feet', 'hair', # 7-13
	'hairiness', 'hands', 'hard', 'head', 'height', 'horniness', 'horny', 'legs', # 14-21
	'muscles', 'needs something in ass', 'nipples', 'pecs', 'thighs', 'toes', # 22-27
	'tongue', 'torso', 'weight', 'voice', 'player', False] # 28-33
nparts = [[i, parts[i]] for i in range(len(parts))]

##################################
# Picks something to affect based on the category chosen.
##################################
def pickpart(cat):
	if cat == 0: poss = [nparts[2], nparts[25]]
	elif cat == 1: poss = [nparts[7], nparts[28]]
	elif cat == 2: poss = [nparts[7], nparts[12], nparts[6]]
	elif cat == 3: poss = [nparts[7], nparts[13], nparts[21], nparts[28]]
	elif (cat == 4 or cat == 11): poss = [nparts[31]]
	elif (cat == 5 or cat == 12): poss = [nparts[1], nparts[2], nparts[6], nparts[11], 
		nparts[21], nparts[25], nparts[29]]
	elif cat == 6: poss = [nparts[0], nparts[10], nparts[14], nparts[18], nparts[30]]
	elif cat == 7: poss = [nparts[1], nparts[2], nparts[6], nparts[21], nparts[22],
		nparts[25], nparts[26], nparts[29]]
	elif cat == 8: poss = [nparts[2], nparts[7], nparts[12], nparts[28]]
	elif cat == 9: poss = [nparts[1], nparts[2], nparts[4], nparts[5], nparts[6],
		nparts[7], nparts[12], nparts[15], nparts[21], nparts[22], nparts[24], nparts[25],
		nparts[26], nparts[28]]
	elif cat == 10: poss = [nparts[1], nparts[7], nparts[13], nparts[21], nparts[28],
		nparts[29]]
	elif cat == 13: poss = [nparts[0], nparts[9], nparts[10], nparts[3], nparts[19],
		nparts[18], nparts[30], nparts[22], nparts[14]]
	elif cat == 14: poss = [nparts[1], nparts[21], nparts[26], nparts[25], nparts[29],
		nparts[6]]
	elif cat == 15: poss = [nparts[1], nparts[21], nparts[26], nparts[25], nparts[2],
		nparts[6], nparts[28]]
	elif cat == 16: poss = [nparts[27], nparts[28], nparts[24]]
	elif cat == 17: poss = [nparts[19]]
	elif cat == 18: poss = [nparts[28], nparts[7], nparts[4], nparts[25], nparts[22],
		nparts[2]]
	elif cat == 19: poss = [nparts[25], nparts[7], nparts[31], nparts[29], nparts[12],
		nparts[11], nparts[6], nparts[24], nparts[14], nparts[2]]
	elif cat == 20: poss = [nparts[1], nparts[3], nparts[6], nparts[7],
		nparts[9], nparts[10], nparts[14], nparts[18], nparts[19], nparts[21], nparts[30],
		nparts[32]]
	elif cat == 21: poss = [nparts[18], nparts[30], nparts[14]]
	elif cat == 22: poss = [nparts[21], nparts[27], nparts[28], nparts[24]]
	elif cat == 23: poss = [nparts[21], nparts[1], nparts[7], nparts[6]]
	elif cat == 24: poss = [nparts[5], nparts[4], nparts[7], nparts[25], nparts[17]]
	elif cat == 25: poss = [nparts[33]]
	elif cat == 26: poss = [nparts[16], nparts[8], nparts[20], nparts[23]]
	else: poss = [[250,'error']]
	return random.choice(poss)

##################################
# Picks the amount of change to make, if applicable
##################################
def howmuch(cat, part):
	if (cat in [20, 21, 22, 24, 25, 26]):
		return False
	elif (cat == 23):
		if part in [21, 1]: return wchoice([(2,100),(4,10),(6,1)])	# arms and legs
		elif part == 7: return wchoice([(1,100),(2,30),(3,10),(4,1)])	# cocks
		else: return 1	# body only can increase +1 at a time
	else:	# return a percentage
		return wchoice([(10, 30), (20, 125), (30, 175), (40, 200), (50, 150), (60, 100),
			(70, 50), (80, 25), (90, 10), (100, 1)])

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
	pass

##################################
# if change modifies another attribute, apply that modification using the change in ch
# and the target(s) in tar
##################################
def moda(ch, tar):
	pass

##################################
# Makes a change
##################################
def makechange(tar):
	if tar == []: print 'No changes.'
	else:
		# pick a random change
		# send the verbose to each player's notes
		# if modifiable, modify attributes
		# print changes or errors
		ch = pickchange(tar)
		wnote(ch)
		if ch == '':
			moda(ch)
		print 'Transform: ' + str(ch)+'\n'

##################################
# Defines a single turn by one player.
# Sender a, target b, and with c overrides.
##################################
def turn(a, b, c):
	orides = override(a, b)
	orides2 = override(a, b)
	mtars = []	# A list of targets to affect.
	ps = ''
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
	mtars = sorted(set(mtars))	# remove duplicates
	ps += '(Target: Player'
	if len(mtars) > 1: ps += 's'
	ps += ' '
	for i in mtars:
		ps += str(i+1) + ', '
	ps = ps[:-2]
	ps += ')'
	if len(mtars) > 0: print ps
	makechange(mtars)

##################################
# Defines a single round. Executes round number r.
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
	for i in range(0,p):
		print 'It is player ' + str(i+1) + '\'s turn to change player ' \
			+ str(players[i].targ+1) + '.'
		turn(i, players[i].targ, noov)

	# Iterates over the players and gives each gamestate. Put a # at the beginning
	# of each of the next three lines if this is too much text and you want to cut down.
	print '\nThat is the end of round {}. Current player stats:\n'.format(r)
	for i in range(0,p): gamestate(i)

##################################
# Creates and initiates the game.
##################################
def game():
	print 'Welcome to the Body Game!\n\n'
	print 'There are ' + str(p) + ' players.\n\n'
	verbose()
	for i in range(1,10):	# there are 9 rounds
		round(i)
	print '\n\n\nAnd that concludes the Body Game! Thank you for playing.'

game()