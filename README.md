#Bodygame.py
A Python program that creates an instance of the Body Game inspired by Brian Ramirez Kyle.


Credits, inspiration, and explanation

This is a Python program to generate an instance (Encounter) of the Body Game.
The Body Game was devised by Brian Ramirez Kyle, and his story directly inspired
this program. The story can be read here:

http://www.metabods.com/mb/stories/Body_game.html

Another author, matt1008, wrote another Encounter for the Body Game, also inspired by
BRK. I've taken inspiration from that work as well, which can be found here:

http://www.metabods.com/mb/stories/Body_game-_Encounter_56.html

The idea of the Body Game is an experimental erotic story format. BRK used Excel
spreadsheets and lots of formulae to generate the skeleton of a story wherein players
of a mysterious and futuristic game experience randomly chosen changes to their bodies,
with overrides throwing in more randomness.

Taking inspiration from those stories, without access to BRK's actual Excel sheets,
I decided (on a whim -- I was actually on a ten-hour roadtrip with nothing to do when
I started to code this) to try my hand at making a program that automatically generates
the same sort of skeleton outline of a story. I wanted to take advantage of the benefits
you get from using a programming language like Python to do things like track some of
the changes to age, cock size, weight, height, and so on. But of course, I didn't want
to limit changes to those easily-tracked attributes, so there is also a 'notes' variable
that is just a list of all changes undergone by each player, in order.
While I'm not extremely new to coding, I'm entirely self-taught. I've never taken a
single computer science class (except one in computational linguistics which barely
taught what a FOR loop was). As a result, if you are familiar with programming
languages, you'll notice that much of this code is not elegant, readable, or Pythonic.
I'm a naturally verbose human being, and my code reflects that. I don't mind some levels
of redundancy, which is probably not a good thing.

Feel free to edit any part of this code except the license information. You might want to
add possible changes or edit the starting ranges for your players. Some of the randomly
selected attributes or changes have absolutely no effect on the rest of the program, and
can be changed completely as they're entirely text based, simply for the benefit of the
writer. All of those variables and functions will be marked as such, so hopefully people
with even less Python knowledge than myself can edit and modify this program.

This Python code is released under the MIT License, found below.

This code has been made available under this license by its creator free of charge.
If you wish to donate to the developer, Chris Hyman, you may send your generous gift to:
Paypal: hymanator93@gmail.com
Please feel no obligation to donate in order to enjoy this program.

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

If you have questions, feel free to email me at hymanator93@gmail.com
