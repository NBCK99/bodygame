Note: This repo is NSFW, 18+ content.

# Version
The current version of this program is 1.1.0, stable.

# How to Use
For macOS and other UNIX systems, you will already have Python installed. For users who do not have it installed, simply visit python.org and follow their instructions.

Download (clone) this repository to your local machine. Edit names.txt and vars.py as you wish. From the command line, navigate to the directory of this repo. For example:

    cd ~/Desktop/bodygame

would work for Mac users with this directory on their desktop. Then call:

    python bodygame.py

(Or 'py bodygame.py' or 'python3 bodygame.py'.) By default, the program will create "output.txt" where you will find your story skeleton! (If you want to display output in the console, change write_to_txt in vars.py to False.

#More Info
**bodygame.py** is a Python program that creates an instance of the Body Game, which was devised by Brian Ramirez Kyle. His story (which can be found here: http://www.metabods.com/mb/stories/Body_game.html) directly inspired this program.

Another author, matt1008, wrote another Encounter for the Body Game, also inspired by BRK. Additionally, as I've created this program, BRK has begun a new story in this format, Encounter 813. Both of these can also be found on Metabods.

The idea of the Body Game is an experimental erotic story format. BRK used Excel spreadsheets and lots of formulae to generate the skeleton of a story wherein players of a mysterious and futuristic game experience randomly chosen changes to their bodies, with overrides throwing in more randomness.

In this program, I have tried my hand at making a program in Python that automatically generates the same sort of skeleton outline of a story. After talking a bit to Brian I got his spreadsheets to help inspire me a bit, and so I could include some things that haven't made it into stories yet. Not everything from his work is in this program, and not everything in this program directly correlates to another person's creations. I cherish collaboration.

On that note, I'm an entirely self-taught coder. I'd seriously appreciate any feedback on my style or implementation. I know I'm sometimes doing something the hard way, but it's often the solution that makes most intuitive sense to me. The problem is I don't learn by relying on my intuition!

Feel free to edit any part of this code except the license information. You might want to add possible changes or edit the starting ranges for your players. A list of simple, easy-to-edit variables can be found in vars.py. I've left lots of comments to help you find your way around customizing things even if you're pretty code illiterate.

If you have anything you want to discuss (feedback, suggestions, feature requests, bug reports), please open an issue in the Issues tab or email me privately at chrhyman@gmail.com

This Python code is released under the MIT License, found below.

This code has been made available under this license by its creator free of charge.
If you wish to donate to the developer, Chris Hyman, you may send your generous gift to:

Paypal: hymanator93@gmail.com
Bitcoin: 1ChrisUZZVzZKnGDbcq5owpuqMHsVBc9TV
Ether: 0x1ffce080248ac918d14f354bf9021dde54ba34c7

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
