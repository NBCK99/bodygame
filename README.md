Note: This repo is NSFW, 18+ content.

# Version
The current version of this program is 1.0.0, stable. View change summaries between versions under the relevant closed pull request.

So this is finally a stable release! I have a lot more plans to tweak this program and make it better (see more details under pull request 3 for planned updates), but I wanted to put something up and maybe write a story of my own to advertise this.

As it stands, this program will give you a full skeleton for an encounter of the Body Game. There are editable parts to it, but I want to make a lot of changes to make it much more friendly. I also want this to be a bit more diverse in possibilities.

I've always really loved stories centered around transformation games like this, and I want to make a good program so more of those stories exist!

# How to Use
Simply download and run bodygame.py. The program will randomly select number of players, and then output the entire game with randomly selected changes and overrides. The program currently takes no inputs.

#More Info
Bodygame. py is a Python program that creates an instance of the Body Game inspired by Brian Ramirez Kyle.

This is a Python program to generate an instance (Encounter) of the Body Game.
The Body Game was devised by Brian Ramirez Kyle, and his story directly inspired
this program. The story can be read here:

http://www.metabods.com/mb/stories/Body_game.html

Another author, matt1008, wrote another Encounter for the Body Game, also inspired by BRK. I've taken inspiration from that work as well. Additionally, as I've created this program, BRK has begun a new story in this format, Encounter 813. Both of these can also be found on Metabods.

The idea of the Body Game is an experimental erotic story format. BRK used Excel
spreadsheets and lots of formulae to generate the skeleton of a story wherein players
of a mysterious and futuristic game experience randomly chosen changes to their bodies,
with overrides throwing in more randomness.

Without access to BRK's actual Excel sheets, I have tried my hand at making a program in Python that automatically generates
the same sort of skeleton outline of a story. 

While I'm not extremely new to coding, I'm entirely self-taught. As a result, if you are familiar with programming
languages, you'll notice that much of this code is not elegant, readable, or Pythonic.

Feel free to edit any part of this code except the license information. You might want to
add possible changes or edit the starting ranges for your players, and the simplest of these are marked in comments (lines with a # at the start)

If you are familiar with coding things, have fun tweaking the program! I've left a ridiculous number of comments to help you find your way around my mess.

This Python code is released under the MIT License, found below.

This code has been made available under this license by its creator free of charge.
If you wish to donate to the developer, Chris Hyman, you may send your generous gift to:

Paypal: hymanator93@gmail.com

Please feel no obligation to donate in order to enjoy this program.

#License
MIT License

Copyright (c) 2016 Chris Hyman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

#Notes
- Generates a game of 5, 6, or 7 players.
- For each new player you get:
  - A random name
  - An age between 18 and 45
  - An ethnicity/nationality/etc.
  - A height from 5'2" to 6'6"
  - A weight from 120 to 250 pounds
  - A shoe size from 7 to 14, US
  - A cock length of 4 to 10 inches
  - A cock shape
  - A hair color
  - A random emotion or feeling
  - And a target for that player (which may or may not be themself)
- A game consists of 9 rounds. Round 1 has no overrides, Rounds 2-8 have one, and Round 9 has two overrides. 
- Overrides currently in use are "none" (target remains the same), "other" (target remains the same), or a target specification + IN ADDITION or INSTEAD (that is, the original target + new target OR new target only). "Other" is meant to give the writer creative freedom (Override: All targets come, or Override: Double change), without actually keeping track of those changes.
- A turn consists of the program choosing a random transformation type (larger, increase quantity, etc), a random (logically relevant though sometimes odd) thing to transform (legs, cock, pecs, entire body), and a degree to which it changes (if applicable).
- The transformation is presented in a human-readable format
- The transformation is recorded to the "notes" attribute for the players targeted by the change
- Modifications are made to the relevant attributes if possible (50% height increase of a 6'0" player results in their height attribute changing to say 9'0")
- At the end of a round, a summary of most player attributes is listed for each player (including the notes that list all changes undergone), updating with any changes they've undergone that round.

If you have questions, feel free to email me at hymanator93@gmail.com, or open an issue on this github repo.
