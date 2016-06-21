# Version 1.1.0
#
# Explanation, documentation, and other information available on github:
# https://github.com/chrhyman/bodygame
#
# Note: This program is NSFW, 18+ content.
# 
# This module contains easily edited variables.
#
# Do NOT edit or remove this comment block.
#
# This Python code is released under the MIT License, found below.
#
# This code has been made available under this license by its creator free of
# charge. If you wish to donate to the developer, Chris Hyman,
# you may send your generous gift to:
#
# Paypal: hymanator93@gmail.com
# Bitcoin: 1ChrisUZZVzZKnGDbcq5owpuqMHsVBc9TV
# Ether: 0x1ffce080248ac918d14f354bf9021dde54ba34c7
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
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# If you have any questions, bug reports, or feature requests, please create
# an issue on github: https://github.com/chrhyman/bodygame/issues
# Or, feel free to fork!


# vars.py

# Creates a list of all possible names. You can add or remove names from this
# list by editing the "names.txt" file. Each name should be on a separate line.
with open('names.txt', 'r') as f:
    names = f.read().splitlines()

# Minimum and maximum number of players. Can be equal to remove randomness.
minplayers = 5
maxplayers = 7

# Number of rounds to execute each time the program runs.
rounds = 9

# Each round by default has no overrides. This is a list of round numbers.
# On the indicated round number, one override is added.
# Example. Default value is [2, 9]. This means round 1 has zero overrides,
# rounds 2-8 have one override each, and round 9 has two overrides.
# If you want each round to have zero overrides, set this to equal [].
add_oride = [2, 8]

# Sets the lowest and highest randomly generated age.
lowage = 21
highage = 45

# Acts as a hard minimum and hard maximum to age. If a change would make a
# player younger than minage, they are set to minage instead.
minage = 18
maxage = 60

# Sets the shortest and tallest randomly generated heights. In inches.
lowheig = 62
highheig = 78

# Sets the lightest and heaviest randomly generated weight. In US pounds.
lowweig = 120
highweig = 250

# Sets the smallest and largest randomly generated shoe size. In US.
lowshoe = 7
highshoe = 14

# Sets the shortest and longest randomly generated cock length. In inches.
lowclen = 4.0
highclen = 10.0

# Sets a small bias for a coin flip function. More True outcomes tends to mean
# more people change, on average. Decimal between 0 and 1. 0.5 removes bias.
falsebias = 0.45

# Chance a character will have dyed hair. Decimale between 0 and 1.
dyedchance = 0.2

# There are eight types of overrides, and an "Other" category. This variable
# affects how often Other comes up. 0 means equally as often. -1 means
# Other never comes up. 1 or more increases the frequency you get Other.
more_odd_overrides = 1

# Lets you define a list of bad categories. If no_bad_cats = True, then all
# of the categories in bad_cats are excluded from all changes. Refer to
# pickPart() below to see the ID number for each category.
no_bad_cats = False
bad_cats = [0, 1, 2, 3, 6]

# If set to True, running bodygame.py creates or appends to the file in tfile.
# If set to False and run from the command line, it outputs all text there.
write_to_txt = True
tfile = 'output.txt'

# A list of adjectives. Program randomly chooses one for each player.
# This variable has no effect on any other part of the program.
ethns = [
    'American (White)', 'American (Black)', 'American (Latino)',
    'American (Mixed Heritage)', 'Native American/Indigenous', 'Japanese',
    'Chinese', 'Korean', 'French', 'German', 'Italian', 'British', 'Mexican',
    'Spanish', 'Indian', 'Middle Eastern', 'Russian', 'Brazilian', 'Canadian',
    'Misc: North/Central American', 'Misc: South American', 'Misc: European',
    'Misc: Asian', 'Misc: Oceanic/Islander', 'Misc: African'
    ]

ages = [i for i in range(lowage, highage + 1)]

heigs = [i for i in range(lowheig, highheig + 1)]

weigs = [i for i in range(lowweig, highweig + 1)]

shoes = [i for i in range(lowshoe, highshoe + 1)]

# Adjectives to describe cocks.
cwids = [
    'wide', 'thick', 'narrow', 'extra-wide', 'torpedo-shaped', 'cobra-shaped',
    'flared', 'normal', 'fat', 'thin'
    ]

# A list of possible natural hair colors.
nathair = [
    'brown', 'black', 'blond', 'red', 'gray', 'dark brown', 'strawberry blond',
    'auburn', 'ginger', 'golden', 'light brown', 'copper', 'dark blond',
    'white', 'light blond'
    ]

# A list of possible dyed hair colors.
unnathair = [
    'bleach blond', 'platinum', 'cobalt blue', 'green', 'deep red', 'orange',
    'violet', 'jet black', 'pink', 'lavender', 'aqua', 'light blue',
    'a pastel color', 'a vibrant color', 'with highlights'
    ]

# A list of emotions players might feel at the beginning of the game.
# This variable has no effect on any other part of the program.
feels = [
    'nervous', 'anxious', 'cocky', 'proud', 'horny', 'ready', 'sexy',
    'excited', 'aroused', 'pleased', 'kinky', 'eager', 'curious', 'confused',
    'confident', 'flirtatious', 'bored', 'amused', 'playful'
    ]

# A list of "Other" overrides. None of these are accounted for in the program.
# e.g., the program doesn't do anything different for "Also next change".
orides = [
    'All targets come.', 'Other.', 'Change recurs next turn.',
    'Plus last change.', 'Also next change.', 'Change recurs with each orgasm',
    'None.', 'Also affects another player of sender\'s choice'
    ]

# Used in many places. Editing might break something.
cats = [
    'less defined', 'narrower', 'smaller', 'shorter', 'stretchier',
    'less hairy', 'decreased', 'more defined', 'wider', 'larger', 'longer',
    'detachable', 'hairier', 'increased', 'stronger', 'thicker',
    'more cocklike', 'produce(s) lube', 'more massive', 'more attractive',
    'doubled', 'surpass others', 'into cock', 'quantity increase', 'inflated',
    'produce(s) come', 'constantly'
    ]

# Used in other places. Don't add or remove numbers. However, you can change
# them. These are weights that bias for or against certain categories. They
# line up with the categories above. First weight in row three default is 7.
# 'detachable' comes up 7x for every 20x that you get 'constantly' (last cat)
wei = [
    10, 10, 20, 7, 10,
    20, 25, 40, 60, 165, 95,
    7, 75, 150, 40, 50,
    50, 10, 85, 45,
    45, 20, 25, 30, 25,
    15, 20
    ]

# Same warnings as for 'wei'. This is a list of Boringness constants for each
# category. If a cat is 'boring' it comes up less and less often as the game
# progresses. 1 is absolutely boring (it will never come up in the last round).
# 0 is absolutely weird (it will never come up in the first round).
# e.g., 'less defined' is absolutely boring. 'wider' is middle of the road.
# 'produce(s) come' is almost absolutely weird.
cat_boringness = [
    1, 1, 1, 1, 0.01,
    0.9, 0.9, 1, 0.5, 0.3, 0.3,
    0.01, 0.3, 0.2, 0.7, 1,
    0.01, 0.01, 0.3, 1,
    0.7, 0.2, 0.01, 0.01, 0.01,
    0.01, 0.2
    ]

# Used all over so don't add or remove. Don't edit the index numbers.
parts = [
    [0, 'age'],
    [1, 'arms'],
    [2, 'ass'],
    [3, 'attractiveness'],
    [4, 'balls'],
    [5, 'belly'],
    [6, 'body'],
    [7, 'cock'],
    [8, 'coming'],
    [9, 'come production'],
    [10, 'cuteness'],
    [11, 'face'],
    [12, 'feet'],
    [13, 'hair'],
    [14, 'hairiness'],
    [15, 'hands'],
    [16, 'hard'],
    [17, 'head'],
    [18, 'height'],
    [19, 'horniness'],
    [20, 'horny'],
    [21, 'legs'],
    [22, 'muscles'],
    [23, 'in need of something in their ass'],
    [24, 'nipples'],
    [25, 'pecs'],
    [26, 'thighs'],
    [27, 'toes'],
    [28, 'tongue'],
    [29, 'torso'],
    [30, 'weight'],
    [31, 'voice'],
    [32, 'asshole'],
    [33, 'sweat glands'],
    [34, 'fingers']
    ]

# My way of combining "weirdness" and "boringness" to get a scalar for weights.
def getBoringness(bx, w):
    return max(abs(bx - w), min(bx, abs(bx - 1.0)))

def getBoringnessList(bx, w):
    result = []
    for i in range(len(bx)):
        result.append(getBoringness(bx[i], w))
    return result

# The big mess of shit that does a lot of the work. This function takes the
# category (let's say "increased") and weirdness (calculated per round) and
# returns a list of possible parts to apply that category of change to. For
# instance you can "increase" a player's attractiveness or come production.
# The function can be easy to read. Each category starts with an IF statement.
# the == NUMBER checks which category the function received. Once the function
# finds the category, it says that possibilities (POSS) are equal to a list
# (between the square [] brackets). Each entry on the list looks something
# like this:
#
#       ([21, 'legs'], 100 * getBoringness(1, w)),
#
# 21 -- the identification number for the body part
# 'legs' -- the body part in words
# 100 -- the base weight for this body part
# * getBoringness() -- multiplies the weight by the boringness scalar
# 1 -- the boringness. For this example, 'legs' is a boring outcome because
#      it comes from 'larger' where something like 'larger nipples' is weirder.
#
# You can freely change the weights to any integer and the boringness to
# any decimal 0 < boringness <= 1.
def pickPart(cat, w):
    if cat == 0:    # less defined (1)
        poss = [
            ([2, 'ass'], 50 * getBoringness(1, w)),
            ([25, 'pecs'], 50 * getBoringness(1, w))
            ]
    elif cat == 1:  # narrower (1)
        poss = [
            ([7, 'cock'], 40 * getBoringness(1, w)),
            ([28, 'tongue'], 60 * getBoringness(1, w))
            ]
    elif cat == 2:  # smaller (1)
        poss = [
            ([7, 'cock'], 40 * getBoringness(1, w)),
            ([12, 'feet'], 75 * getBoringness(1, w)),
            ([6, 'body'], 65 * getBoringness(1, w))
            ]
    elif cat == 3:  # shorter (1)
        poss = [
            ([13, 'hair'], 20 * getBoringness(1, w)),
            ([21, 'legs'], 45 * getBoringness(1, w)),
            ([28, 'tongue'], 40 * getBoringness(1, w))
            ]
    elif cat == 4:  # stretchier (0.01)
        poss = [
            ([6, 'body'], 50 * getBoringness(0.01, w)),
            ([7, 'cock'], 50 * getBoringness(0.1, w)),
            ([24, 'nipples'], 35 * getBoringness(0.2, w)),
            ([28, 'tongue'], 20 * getBoringness(0.3, w))
            ]
    elif cat == 5:  # less hairy (0.9)
        poss = [
            ([1, 'arms'], 100 * getBoringness(1, w)),
            ([2, 'ass'], 100 * getBoringness(1, w)),
            ([6, 'body'], 125 * getBoringness(0.9, w)),
            ([11, 'face'], 150 * getBoringness(1, w)),
            ([21, 'legs'], 100 * getBoringness(1, w)),
            ([25, 'pecs'], 100 * getBoringness(1, w)),
            ([29, 'torso'], 110 * getBoringness(1, w))
            ]
    elif cat == 6:  # decreased (0.9)
        poss = [
            ([0, 'age'], 50 * getBoringness(0.8, w)),
            ([10, 'cuteness'], 75 * getBoringness(1, w)),
            ([14, 'hairiness'], 125 * getBoringness(1, w)),
            ([18, 'height'], 150 * getBoringness(0.7, w)),
            ([30, 'weight'], 150 * getBoringness(0.7, w))
            ]
    elif cat == 7:  # more defined (1)
        poss = [
            ([1, 'arms'], 100 * getBoringness(1, w)),
            ([2, 'ass'], 75 * getBoringness(1, w)),
            ([6, 'body'], 150 * getBoringness(0.9, w)),
            ([21, 'legs'], 100 * getBoringness(1, w)),
            ([22, 'muscles'], 175 * getBoringness(1, w)),
            ([25, 'pecs'], 100 * getBoringness(0.9, w)),
            ([26, 'thighs'], 100 * getBoringness(1, w)),
            ([29, 'torso'], 125 * getBoringness(1, w))
            ]
    elif cat == 8:  # wider (0.5)
        poss = [
            ([2, 'ass'], 100 * getBoringness(0.9, w)),
            ([7, 'cock'], 100 * getBoringness(0.8, w)),
            ([12, 'feet'], 75 * getBoringness(0.9, w)),
            ([28, 'tongue'], 75 * getBoringness(0.9, w))
            ]
    elif cat == 9:  # larger (0.3)
        poss = [
            ([1, 'arms'], 50 * getBoringness(1, w)),
            ([2, 'ass'], 90 * getBoringness(0.5, w)),
            ([4, 'balls'], 125 * getBoringness(0.4, w)),
            ([5, 'belly'], 50 * getBoringness(1, w)),
            ([6, 'body'], 100 * getBoringness(0.7, w)),
            ([7, 'cock'], 200 * getBoringness(0.3, w)),
            ([12, 'feet'], 70 * getBoringness(0.9, w)),
            ([15, 'hands'], 25 * getBoringness(1, w)),
            ([21, 'legs'], 50 * getBoringness(1, w)),
            ([22, 'muscles'], 70 * getBoringness(0.8, w)),
            ([24, 'nipples'], 75 * getBoringness(0.6, w)),
            ([25, 'pecs'], 90 * getBoringness(0.5, w)),
            ([26, 'thighs'], 25 * getBoringness(1, w)),
            ([28, 'tongue'], 30 * getBoringness(0.9, w))
            ]
    elif cat == 10: # longer (0.3)
        poss = [
            ([1, 'arms'], 25 * getBoringness(1, w)),
            ([7, 'cock'], 100 * getBoringness(0.2, w)),
            ([13, 'hair'], 30 * getBoringness(1, w)),
            ([21, 'legs'], 35 * getBoringness(0.9, w)),
            ([28, 'tongue'], 70 * getBoringness(0.7, w)),
            ([29, 'torso'], 10 * getBoringness(0.9, w))
            ]
    elif cat == 11: # detachable (0.01)
        poss = [
            ([7, 'cock'], 60 * getBoringness(0.01, w)),
            ([12, 'feet'], 25 * getBoringness(0.01, w))
            ]
    elif cat == 12: # hairier (0.3)
        poss = [
            ([1, 'arms'], 100 * getBoringness(1, w)),
            ([2, 'ass'], 100 * getBoringness(0.9, w)),
            ([6, 'body'], 125 * getBoringness(0.5, w)),
            ([11, 'face'], 150 * getBoringness(1, w)),
            ([21, 'legs'], 100 * getBoringness(0.9, w)),
            ([25, 'pecs'], 100 * getBoringness(0.8, w)),
            ([29, 'torso'], 110 * getBoringness(0.9, w))
            ]
    elif cat == 13: # increased (0.2)
        poss = [
            ([0, 'age'], 10 * getBoringness(0.4, w)),
            ([9, 'come production'], 50 * getBoringness(0.6, w)),
            ([10, 'cuteness'], 10 * getBoringness(1, w)),
            ([3, 'attractiveness'], 10 * getBoringness(1, w)),
            ([19, 'horniness'], 10 * getBoringness(1, w)),
            ([18, 'height'], 45 * getBoringness(0.6, w)),
            ([30, 'weight'], 45 * getBoringness(0.6, w)),
            ([22, 'muscles'], 70 * getBoringness(0.5, w)),
            ([14, 'hairiness'], 50 * getBoringness(0.7, w))
            ]
    elif cat == 14: # stronger (0.7)
        poss = [
            ([1, 'arms'], 100 * getBoringness(1, w)),
            ([21, 'legs'], 100 * getBoringness(1, w)),
            ([26, 'thighs'], 75 * getBoringness(1, w)),
            ([25, 'pecs'], 50 * getBoringness(0.9, w)),
            ([29, 'torso'], 100 * getBoringness(1, w)),
            ([6, 'body'], 125 * getBoringness(0.8, w))
            ]
    elif cat == 15: # thicker (1)
        poss = [
            ([1, 'arms'], 50 * getBoringness(1, w)),
            ([21, 'legs'], 50 * getBoringness(1, w)),
            ([26, 'thighs'], 25 * getBoringness(0.9, w)),
            ([25, 'pecs'], 75 * getBoringness(0.8, w)),
            ([2, 'ass'], 100 * getBoringness(0.6, w)),
            ([6, 'body'], 25 * getBoringness(0.9, w)),
            ([28, 'tongue'], 75 * getBoringness(1, w))
            ]
    elif cat == 16: # more cocklike (0.01)
        poss = [
            ([27, 'toes'], 25 * getBoringness(0.01, w)),
            ([28, 'tongue'], 75 * getBoringness(0.01, w)),
            ([24, 'nipples'], 75 * getBoringness(0.01, w)),
            ([34, 'fingers'], 25 * getBoringness(0.01, w))
            ]
    elif cat == 17: # produce(s) lube (0.01)
        poss = [
            ([24, 'nipples'], 50 * getBoringness(0.01, w)),
            ([33, 'sweat glands'], 10 * getBoringness(0.3, w)),
            ([32, 'asshole'], 20 * getBoringness(0.1, w))
            ]
    elif cat == 18: # more massive (0.3)
        poss = [
            ([28, 'tongue'], 50 * getBoringness(1, w)),
            ([7, 'cock'], 100 * getBoringness(0.2, w)),
            ([4, 'balls'], 120 * getBoringness(0.1, w)),
            ([25, 'pecs'], 80 * getBoringness(0.5, w)),
            ([22, 'muscles'], 50 * getBoringness(0.8, w)),
            ([2, 'ass'], 100 * getBoringness(0.5, w))
            ]
    elif cat == 19: # more attractive (1)
        poss = [
            ([25, 'pecs'], 100 * getBoringness(0.7, w)),
            ([7, 'cock'], 150 * getBoringness(0.4, w)),
            ([31, 'voice'], 25 * getBoringness(1, w)),
            ([29, 'torso'], 50 * getBoringness(0.9, w)),
            ([12, 'feet'], 30 * getBoringness(0.5, w)),
            ([11, 'face'], 100 * getBoringness(1, w)),
            ([6, 'body'], 100 * getBoringness(0.1, w)),
            ([24, 'nipples'], 100 * getBoringness(0.01, w)),
            ([14, 'hairiness'], 30 * getBoringness(0.7, w)),
            ([2, 'ass'], 70 * getBoringness(0.4, w))
            ]
    elif cat == 20: # doubled (0.7)
        poss = [
            ([7, 'cock'], 70 * getBoringness(0.1, w)),
            ([9, 'come production'], 75 * getBoringness(0.2, w)),
            ([10, 'cuteness'], 10 * getBoringness(1, w)),
            ([14, 'hairiness'], 20 * getBoringness(0.7, w)),
            ([19, 'horniness'], 10 * getBoringness(1, w))
            ]
    elif cat == 21: # surpass others (0.2)
        poss = [
            ([3, 'attractiveness'], 10 * getBoringness(1, w)),
            ([7, 'cock'], 90 * getBoringness(0.01, w)),
            ([14, 'hairiness'], 40 * getBoringness(0.7, w)),
            ([18, 'height'], 30 * getBoringness(0.7, w)),
            ([19, 'horniness'], 20 * getBoringness(1, w)),
            ([22, 'muscles'], 50 * getBoringness(0.3, w))
            ]
    elif cat == 22: # into cock (0.01)
        poss = [
            ([21, 'legs'], 25 * getBoringness(0.01, w)),
            ([27, 'toes'], 25 * getBoringness(0.2, w)),
            ([28, 'tongue'], 100 * getBoringness(0.1, w)),
            ([24, 'nipples'], 75 * getBoringness(0.01, w)),
            ([34, 'fingers'], 25 * getBoringness(0.01, w))
            ]
    elif cat == 23: # quantity increase (0.01)
        poss = [
            ([21, 'legs'], 50 * getBoringness(0.7, w)),
            ([1, 'arms'], 50 * getBoringness(0.7, w)),
            ([7, 'cock'], 100 * getBoringness(0.2, w)),
            ([6, 'body'], 10 * getBoringness(0.4, w))
            ]
    elif cat == 24: # inflated (0.01)
        poss = [
            ([5, 'belly'], 10 * getBoringness(0.9, w)),
            ([4, 'balls'], 100 * getBoringness(0.5, w)),
            ([7, 'cock'], 100 * getBoringness(0.5, w)),
            ([25, 'pecs'], 50 * getBoringness(0.3, w)),
            ([17, 'head'], 5 * getBoringness(1, w))
            ]
    elif cat == 25: # produce(s) come (0.01)
        poss = [
            ([24, 'nipples'], 50 * getBoringness(0.01, w)),
            ([33, 'sweat glands'], 10 * getBoringness(0.7, w)),
            ([32, 'asshole'], 20 * getBoringness(0.2, w))
            ]
    elif cat == 26: # constantly (0.2)
        poss = [
            ([16, 'hard'], 100 * getBoringness(0.7, w)),
            ([8, 'coming'], 70 * getBoringness(0.5, w)),
            ([20, 'horny'], 50 * getBoringness(0.9, w)),
            ([23, 'in need of something in their ass'],
                75 * getBoringness(0.5, w))
            ]
    else:
        poss = [([250, 'error'], 100)]  # Error ID
    return poss
