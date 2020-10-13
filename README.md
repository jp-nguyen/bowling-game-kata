# [The Bowling Game Kata](http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata)

## Description

The game consists of 10 frames. In each frame, the player has two opportunities
to knock down 10 pins. The score for the frame is the total number of pins 
knocked down + bonuses for strikes and spares.

A **spare** is when the player knocks down all 10 pins in two tries. The bonus
for the frame is the number of pins knocked down by the next roll.

A **strike** is when the player knocks down all 10 pins on their first try. The
bonux for that frame is the value of the next two balls rolled.

In the tenth frame, a player who rolls a spare or strike is allowed to roll the
extra balls to complete the frame. However, no more than three balls can be
rolled in the tenth frame.

## Requirements 

To fulfill this kata, the following needs to be implemented:

* a class named `Game` which has two methods:
  + `roll(pins: int)` : called when the player rolls a ball. The argument is the number of pins knocked down 
  + `score()` : called at the end of the game, returning the total score for the game

## Goal

The goal of doing this kata is to practice doing *Test Driven Development* and
adapting that mindset when thinking about problems. The idea is that you should
be creating the unit tests before writing the code and logic to fulfill the
test, continuously improving the readability and modularity of the code as you
go. At the end, your code should be easy to read and understand!

A good roadmap to do this kata would be doing the following tests:
* A Gutter Game: rolling all zeroes
* Rolling all ones
* Rolling a spare
* Rolling a strike
* A Perfect Game: rolling all strikes

## Milestones

* **2020-10-13**: Completed the kata via walkthrough in `Python`