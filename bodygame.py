# Version 1.1.0
#
# Explanation, documentation, and other information available on github:
# https://github.com/chrhyman/bodygame
#
# Note: This program is NSFW, 18+ content.
# 
# Please see vars.py for many easy-to-edit variables if you aren't code-savvy.
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


# bodygame.py

import sys
import random
import math
import vars


if vars.write_to_txt:
    print('Output sent to: ' + vars.tfile)
    sys.stdout = open(vars.tfile, 'a')
    

p = random.randint(vars.minplayers, vars.maxplayers)
rs = vars.rounds

weirdness = 0

pickedtar = []  # list of players who are targeted
players = []    # list of Player objects

# Global dictionaries that hold Player:Attribute pairs
adict = {}
hdict = {}
wdict = {}
sdict = {}
cdict = {}

class Player:
    def __init__(self):
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
        self.notes = []
    def gName(self):
        self.name = random.choice(vars.names)
    def gAgee(self):
        self.agee = random.choice(vars.ages)
    def gEthn(self):
        self.ethn = random.choice(vars.ethns)
    def gHeig(self):
        self.heig = random.choice(vars.heigs)
    def gWeig(self):
        self.weig = random.choice(vars.weigs)
    def gShoe(self):
        self.shoe = random.choice(vars.shoes)
    def gClen(self):
        self.clen = random.uniform(vars.lowclen, vars.highclen)
    def gCwid(self):
        self.cwid = random.choice(vars.cwids)
    def gHair(self):
        self.hair = random.choice(vars.nathair)
        if (random.random() < vars.dyedchance):
            self.hair += ' and dyed ' + random.choice(vars.unnathair)
    def gFeel(self):
        self.feel = random.choice(vars.feels)
    def gTarg(self):
        x = random.randint(0, p - 1)
        if x not in pickedtar:
            self.targ = x
            pickedtar.append(x)
        else:
            self.gTarg()

# Dec and Inc clean up moda() significantly. tar is a list of targets.
class Dec:
    def cock(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].clen *= ((100 - per) / 100.0)
    def age(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].agee *= ((100 - per) / 100.0)
    def heig(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].heig *= ((100 - per) / 100.0)
    def weig(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].weig *= ((100 - per) / 100.0)
    def shoe(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].shoe *= ((100 - per) / 100.0)
    def legs(self, tar, per):   # approx by adding half of height
        for i in range(len(tar)):
            half = 0.5 * players[tar[i]].heig
            players[tar[i]].heig = (half * ((100 - per) / 100.0)) + half

Dec = Dec()

class Inc:
    def cock(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].clen *= ((100 + per) / 100.0)
    def age(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].agee *= ((100 + per) / 100.0)
    def heig(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].heig *= ((100 + per) / 100.0)
    def weig(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].weig *= ((100 + per) / 100.0)
    def shoe(self, tar, per):
        for i in range(len(tar)):
            players[tar[i]].shoe *= ((100 + per) / 100.0)
    def legs(self, tar, per):   # approx by adding half of height
        for i in range(len(tar)):
            half = 0.5 * players[tar[i]].heig
            players[tar[i]].heig = (half * ((100 + per) / 100.0)) + half

Inc = Inc()


def initPlayers():
    global players
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
    for i in range(p):
        if i not in pickedtar:
            print(
                'Error: Player {} is NOT targeted by anyone.'.format(i + 1),
                'All results below, if visible, are in error.')

def makeDicts():
    for i in range(p):
        adict[i] = players[i].agee
        hdict[i] = players[i].heig
        wdict[i] = players[i].weig
        sdict[i] = players[i].shoe
        cdict[i] = players[i].clen

def minmax(d, bool):
    v = list(d.values())
    k = list(d.keys())
    if bool:
        return k[v.index(max(v))]
    else:
        return k[v.index(min(v))]

def findPlayer(cat, bool):
    makeDicts()
    if cat == 3:
        return minmax(adict, bool)
    elif cat == 4:
        return minmax(hdict, bool)
    elif cat == 5:
        return minmax(wdict, bool)
    elif cat == 6:
        return minmax(sdict, bool)
    elif cat == 7:
        return minmax(cdict, bool)

def intoft(n):
    return str(int(math.floor(n / 12))) + "'" + str(round(n % 12, 1)) + '"'

def intocm(n):
    return str(round(n * 2.54, 1)) + 'cm'

def intomt(n):
    return str(round(n * 0.0254, 2)) + 'm'

def lbtokg(n):
    return str(round(n * 0.454, 1)) + 'kg'

def coinFlip():
    if random.random() >= vars.falsebias:
        return True
    else:
        return False

def gamestate(z):
    az = str(z + 1)
    atar = str(players[z].targ + 1)
    allnotes = ''
    for i in range(len(players[z].notes) - 1):
        allnotes += players[z].notes[i] + ', '
    allnotes += players[z].notes[-1]
    current = """Player {}
Name: {}
Age: {}
Height: {}
Weight: {}lb.
Shoe size: {}
Cock length: {}in.
Cock shape: {}
Notes: {}\n
"""
    print(current.format(
        az, players[z].name, round(players[z].agee, 0),
        intoft(players[z].heig), round(players[z].weig, 1),
        round(players[z].shoe, 1), round(players[z].clen, 1), players[z].cwid,
        allnotes))

# Gives the initial gamestate for all players.
def verbose():
    for i in range(p):
        ai = i + 1
        atar = players[i].targ + 1
        display = """Player {0}'s name is {1}, {2} years old. He is {3}.
He's {4} tall ({5}) and weighs {6}lb ({7}). {1} wears
a size {8} shoe. His {11} cock is {9}in. long ({10}).
His hair is {12}. He's feeling {13}.
His target is player {14}.
"""
        print(display.format(
            ai, players[i].name, players[i].agee, players[i].ethn, 
            intoft(players[i].heig), intomt(players[i].heig), players[i].weig,
            lbtokg(players[i].weig), players[i].shoe, round(
            players[i].clen, 1), intocm(players[i].clen), players[i].cwid,
            players[i].hair, players[i].feel, atar) + '\n')

# Chooses the override type when passed a random integer. Returns a list.
def getOride(pick):
    if pick >= 8:
        return [8, 'other', False, False, False]
    elif pick == 0:
        return [0, 'Sender', coinFlip(), False, False]
    elif pick == 1:
        side = 'left'
        if coinFlip():
            side = 'right'
        a1 = "target's " + side
        return [1, a1, coinFlip(), side, False]
    elif pick == 2:
        side = 'left'
        if coinFlip():
            side = 'right'
        a1 = "sender's " + side
        return [2, a1, coinFlip(), side, False]
    elif pick == 3:
        which = 'min'
        if coinFlip():
            which = 'max'
        return [3, 'age', coinFlip(), False, which]
    elif pick == 4:
        which = 'min'
        if coinFlip():
            which = 'max'
        return [4, 'height', coinFlip(), False, which]
    elif pick == 5:
        which = 'min'
        if coinFlip():
            which = 'max'
        return [5, 'weight', coinFlip(), False, which]
    elif pick == 6:
        which = 'min'
        if coinFlip():
            which = 'max'
        return [6, 'shoe', coinFlip(), False, which]
    elif pick == 7:
        which = 'min'
        if coinFlip():
            which = 'max'
        return [7, 'cock', coinFlip(), False, which]
    else:
        return [400, 'error', False, False, False]

# Uses override chosen to determine target list.
def override(s, t):
    outcome = getOride(random.randint(0, 8 + vars.more_odd_overrides))
    results = outcome
    results.append([])
    if outcome[0] == 0:
        results[5].append(s)    # sender
    elif outcome[0] == 1:   # target's left/right
        nt = t
        if outcome[3] == 'left':
            if nt >= (p - 1):
                nt = 0
            else:
                nt += 1
        if outcome[3] == 'right':
            if (nt == 0):
                nt = p - 1
            else:
                nt -= 1
        results[5].append(nt)
    elif outcome[0] == 2:     # sender's left/right
        nt = s
        if outcome[3] == 'left':
            if nt >= (p - 1):
                nt = 0
            else:
                nt += 1
        if outcome[3] == 'right':
            if nt == 0:
                nt = p - 1
            else:
                nt -= 1
        results[5].append(nt)
    elif 3 <= outcome[0] <= 7:    # attribute-based
        if outcome[4] == 'max':
            results[5].append(findPlayer(outcome[0], True))
        elif outcome[4] == 'min':
            results[5].append(findPlayer(outcome[0], False))
        else:
            results[5].append(700)  # Error ID.
    elif outcome[0] == 8:
        results[5].append(t)    # if NONE/OTHER, original target remains
    else:
        results[5] = 'error 200'
    if outcome[2]:
        results[5].append(t)    # If IN ADDITION, append original target.
    return results

# Deciphers an override list into a string.
def decipher(list):
    string = ''
    if list[0] == 8:
        string = random.choice(vars.orides)
    else:
        if list[0] == 0:
            string = list[1]
        elif 1 <= list[0] <= 2:
            string = 'Player to ' + list[1]
        elif list[0] == 3:
            if list[4] == 'max':
                string = 'Oldest player'
            else:
                string = 'Youngest player'
        elif list[0] == 4:
            if list[4] == 'max':
                string = 'Tallest player'
            else:
                string = 'Shortest player'
        elif list[0] == 5:
            if list[4] == 'max':
                string = 'Heaviest player'
            else:
                string = 'Lightest player'
        elif list[0] == 6:
            if list[4] == 'max':
                string = 'Player with largest feet'
            else:
                string = 'Player with smallest feet'
        elif list[0] == 7:
            if list[4] == 'max':
                string = 'Player with longest cock'
            else:
                string = 'Player with shortest cock'
        if list[2]:
            string += ' too.'
        else:
            string += ' instead.'
    return string

# Takes a list of tuples where second element is an int.
# Returns random element with int as a weight.
# Example: wchoice([('x', 10), ('y', 400), ('z', 1)])
# Returns 'y' 400 times more often than 'z'
def wchoice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    u = 0
    for c, w in choices:
        if u + w >= r:
            return c
        u += w
    assert False, 'Error: Weighted choice failure.'

# Picks amount of change to make, if applicable.
def howMuch(cat, part):
    if cat in [20, 21, 22, 25, 26, 11, 17]:
        return False
    elif cat == 23:
        if part in [21, 1]:
            return wchoice([(2, 100), (4, 10), (6, 1)]) # arms and legs
        elif part == 7:
            return wchoice([(1, 200), (2, 40), (3, 10), (4, 1)])    # cocks
        else:
            return 1    # body
    elif cat == 24:
        return random.choice([20, 40, 40, 60, 60, 80, 100]) # inflation
    else:   # return a percentage of 100
        return wchoice([(10, 150), (20, 175), (30, 200), (40, 175), (50, 100),
            (60, 50), (70, 25), (80, 10), (90, 5), (100, 1)])

# change = ['targs', 'catID', 'cat words', 'partID', 'part words', 'amount']
def pickChange(tar):
    wei = [w * b for w, b in list(zip(
        vars.wei, vars.getBoringnessList(vars.cat_boringness, weirdness)))]
    wncats = [([i, vars.cats[i]], wei[i]) for i in range(len(vars.cats))]
    q1 = wchoice(wncats)
    if vars.no_bad_cats and q1[0] in vars.bad_cats:
        pickChange(tar)
    q2 = wchoice(vars.pickPart(q1[0], weirdness))
    return [tar, q1[0], q1[1], q2[0], q2[1], howMuch(q1[0], q2[0])]

# Writes the change in ch to notes of all targets.
def wnote(ch):
    hread = ''
    if ch[1] in [6, 13, 24]:
        hread = '{} {} {}%'.format(ch[4], ch[2], ch[5])
    elif ch[1] == 11:
        hread = '{} made {}'.format(ch[4], ch[2])
    elif ch[1] in [17, 20, 25]:
        hread = '{} {}'.format(ch[4], ch[2])
    elif ch[1] == 22:
        hread = '{} transformed {}'.format(ch[4], ch[2])
    elif ch[1] == 23:
        hread = 'quantity of {} increased: +{}'.format(ch[4], ch[5])
    elif ch[1] == 26:
        hread = '{} {}'.format(ch[2], ch[4])
    elif ch[1] == 21:
        if ch[3] == 3:
            hread = 'made most attractive'
        if ch[3] == 7:
            hread = 'given longest cock'
        if ch[3] == 14:
            hread = 'made hairiest'
        if ch[3] == 18:
            hread = 'made tallest'
        if ch[3] == 19:
            hread = 'made horniest'
        if ch[3] == 22:
            hread = 'made most muscular'
    else:
        hread = '{} {}% {}'.format(ch[4], ch[5], ch[2])
    for i in range(len(ch[0])):
        players[ch[0][i]].notes.append(hread)

# Applies attribute modifications if applicable for change ch.
def moda(ch):
    if ch[1] == 2:  # smaller
        if ch[3] == 7:
            Dec.cock(ch[0], ch[5])
        if ch[3] == 12:
            Dec.shoe(ch[0], ch[5])
        if ch[3] == 6:  # body
            Dec.shoe(ch[0], ch[5])
            Dec.heig(ch[0], ch[5])
            Dec.weig(ch[0], ch[5])
            Dec.cock(ch[0], ch[5])
    elif ch[1] == 3:    # shorter
        if ch[3] == 7:
            Dec.cock(ch[0], ch[5])
        if ch[3] == 21:
            Dec.legs(ch[0], ch[5])
    elif ch[1] == 6:    # decrease
        if ch[3] == 0:
            Dec.age(ch[0], ch[5])
            for i in range(len(ch[0])):
                if players[ch[0][i]].agee < vars.minage:
                    print('Exception: Age cannot go below {}.\n'.format(
                        str(vars.minage)), "Setting {}'s age to {}.\n".format(
                        players[ch[0][i]].name, str(vars.minage)))
                    players[ch[0][i]].agee = vars.minage
        if ch[3] == 18:
            Dec.heig(ch[0], ch[5])
        if ch[3] == 30:
            Dec.weig(ch[0], ch[5])
    elif ch[1] == 9:    # larger
        if ch[3] == 6:  # body
            Inc.shoe(ch[0], ch[5])
            Inc.heig(ch[0], ch[5])
            Inc.weig(ch[0], ch[5])
            Inc.cock(ch[0], ch[5])
        if ch[3] == 7:
            Inc.cock(ch[0], ch[5])
        if ch[3] == 12:
            Inc.shoe(ch[0], ch[5])
        if ch[3] == 21:
            Inc.legs(ch[0], ch[5])
    elif ch[1] == 10:   # longer
        if ch[3] == 7:
            Inc.cock(ch[0], ch[5])
        if ch[3] in [21, 29]:
            Inc.legs(ch[0], ch[5])
    elif ch[1] == 13:   # increase
        if ch[3] == 0:
            Inc.age(ch[0], ch[5])
            for i in range(len(ch[0])):
                if players[ch[0][i]].agee > vars.maxage:
                    print('Exception: Age cannot go above {}.\n'.format(
                        str(vars.maxage)), "Setting {}'s age to {}\n".format(
                        players[ch[0][i]].name, str(vars.maxage)))
                    players[ch[0][i]].agee = vars.maxage
        if ch[3] == 18:
            Inc.heig(ch[0], ch[5])
        if ch[3] == 30:
            Inc.weig(ch[0], ch[5])
    elif ch[1] == 18:   # more massive
        if ch[3] == 7:
            Inc.cock(ch[0], ch[5])
    elif ch[1] == 20:   # double
        if ch[3] == 18:
            for i in range(len(ch[0])):
                players[ch[0][i]].heig *= 2
        if ch[3] == 30:
            for i in range(len(ch[0])):
                players[ch[0][i]].weig *= 2
    elif ch[1] == 21:   # surpass others
        if ch[3] == 7:  # cock length
            new_clen = players[findPlayer(7, True)].clen + 1
            for i in range(len(ch[0])):
                players[ch[0][i]].clen = new_clen
        if ch[3] == 18: # height
            new_heig = players[findPlayer(4, True)].heig + 1
            for i in range(len(ch[0])):
                players[ch[0][i]].heig = new_heig
    elif ch[1] == 24:   # inflated
        if ch[3] == 7:
            Inc.cock(ch[0], ch[5])
    else: print('Error: Category ID not found.',
        'Attribute calculations may be inaccurate.')

# Inelegantly serializes a list with commas and AND
def listpl(t):
    if len(t) == 1:
        return players[t[0]].name
    elif len(t) > 1:
        x = ''
        for i in range(len(t) - 1):
            x += players[t[i]].name + ', '
        return x[:-2] + ' and ' + players[t[-1]].name
    else:
        return 'No one'

def makeChange(tar):
    if tar == []:
        print('No changes.')
    else:
        ch = pickChange(tar)
        hread = ''
        hrt = listpl(ch[0])
        if ch[1] in [6, 13, 24]:
            hread = "{}'s {} {} {}%.".format(hrt, ch[4], ch[2], ch[5])
        elif ch[1] in [17, 20, 25]:
            hread = "{}'s {} {}.".format(hrt, ch[4], ch[2])
        elif ch[1] == 21:
            if ch[3] == 3:
                hread = hrt + ' made most attractive.'
            if ch[3] == 7:
                hread = hrt + ' given longest cock.'
            if ch[3] == 14:
                hread = hrt + ' made hairiest.'
            if ch[3] == 18:
                hread = hrt + ' made tallest.'
            if ch[3] == 19:
                hread = hrt + ' made horniest.'
            if ch[3] == 22:
                hread = hrt + ' made most muscular.'
        elif ch[1] == 22:
            hread = "{}'s {} transformed {}.".format(hrt, ch[4], ch[2])
        elif ch[1] == 11:
            hread = "{}'s {} made {}.".format(hrt, ch[4], ch[2])
        elif ch[1] == 23:
            hread = "Quantity of {}'s {} increased: +{}.".format(
                hrt, ch[4], ch[5])
        elif ch[1] == 25:
            hread = "{}'s nipples can come.".format(hrt)
        elif ch[1] == 26:
            pl = 'is'
            if len(ch[0]) > 1:
                pl = 'are'
            hread = '{} {} {} {}.'.format(hrt, pl, ch[2], ch[4])
        else:
            hread = "{}'s {} {}% {}.".format(hrt, ch[4], ch[5], ch[2])
        print('Transform: ' + hread + '\n')
        wnote(ch)
        if ch[1] in [2, 3, 6, 9, 10, 13, 18, 20, 21, 24]:
            moda(ch)

# A single turn by sender a with target b, c overrides.
def turn(a, b, c):
    orides = [] # A list of override lists
    mtars = []
    for i in range(c):
        orides.append(override(a, b))
    if orides == []:
        print('Override: None.')
        mtars = [b]
    else:
        for i in range(len(orides) - 1):
            print('Override: ' + decipher(orides[i]))
        temp_str = 'Override: ' + decipher(orides[-1])
        if len(orides) > 1:
            temp_str = 'and ' + temp_str
        print(temp_str)
    for i in range(len(orides)):
        mtars.extend(orides[i][5])
    mtars = sorted(set(mtars))  # remove duplicates, order numerically
    makeChange(mtars)

# Executes round number r (index from 1, not 0)
def round_(r):
    print('\n\nThis is round {}.\n'.format(str(r)))
    global weirdness
    weirdness = float(r / rs) * 1.5
    if weirdness >= 1.0:
        weirdness = 1
    noov = 0
    pl = 'are'
    s = 's'
    for i in range(len(vars.add_oride)):
        if r >= vars.add_oride[i]:
            noov += 1
    if noov == 1:
        pl = 'is'
        s = ''
    print('There {} {} override{} for each turn this round.\n\n'.format(
    pl, str(noov), s))
    for i in range(p):
        print("It is player {}'s turn to change player {}.".format(
            str(i + 1), str(players[i].targ + 1)))
        turn(i, players[i].targ, noov)
    print("That's the end of round {}. Current player stats:\n".format(str(r)))
    for i in range(p):
        gamestate(i)

def game():
    print('Welcome to the Body Game!\n\n')
    print('There are {} players.\n\n'.format(str(p)))
    verbose()
    for i in range(rs):
        round_(i + 1)
    print('\nAnd that concludes the Body Game! Thank you for playing.\n\n')

def main():
    initPlayers()
    game()

if __name__ == '__main__':
    main()