# Mars Rover

This started out as interview practice and a way to improve my Python knowledge. The spec was to create a rover that
could take one of 3 instructions and process it within a given set of boundaries, whilst avoiding obstacles.

After enjoying building the original one, I decided to expand it and provide different versions of each part of the
code.

## Types of rover

There are multiple types of rover which each act in a slightly different way. The first rover `Rover` is also the base
of the rovers extend.
class that the rest.

### Rover

The `Rover` can move in four directions:

- North
- East
- South
- West

It processes the instructions as follows:

- Forward - attempts to move one block in the direction it is facing, unless blocked by an obstacle or another rover
- Right - change direction in a clockwise direction
- Left - change direction in an anti-clockwise direction

### Octopus

The `Octopus` can move in eight directions:

- North
- East
- South
- West
- North East
- North West
- South East
- South West

It processes instructions in the same way as the `Rover`.

### Madman

The `Madman` works in the same four directions as the `Rover`.

It processes instructions in the same way as the `Rover`, except it doesn't follow the instruction it receives, it
instead picks a random instruction to follow.

### Jumper

The `Madman` works in the same four directions as the `Rover`.

It processes instructions in the same way as the `Rover`, except forward. The forward command attempts to move 2 spaces
instead of 1, as if it is "jumping" over the space directly in front of it.

### Insomniac

The `Madman` works in the same four directions as the `Rover`.

It processes instructions in the same way as the `Rover`, except sometimes it falls asleep. It takes two rates: wake
rate and sleep rate. When it is asleep, it ignores the instruction. When it is awake, it acts as a regular rover.

## Types of runner

There are two ways to run a set of rovers:

- one-by-one
- step-by-step

### Runner

The `Runner` takes one rover at a time and have it process all of its instructions. Then repeats this for each rover.

### Stepper

The `Stepper` takes all rovers and has them each run their next instruction. This repeats for every instruction.

## Board

The `Board` stores the rovers and the obstacles. It also provides ways to display the current state of the known grid.
It also tells the rovers if they're lost, or if their next move is blocked by either an obstacle or another rover.

## Renderers

The renderers provide ways to visualise the board.

### Console

Displays the board state as a block of text onto the console.

### MatPlotLib

Uses MatPlotLib to display and update the same figure of the current state using different colours.

### PyGame

Uses PyGame to display current state using different colours in a grid.

## Generators

Some simple helper functions that make it easy to generate a random simulation.

### Rover generator

Generates a given number of rovers from the provided options of classes.

### Obstacle generator

Generates a given number of obstacles within a min and max coord.

### Instructions generator

Generates a given number of instruction lists, where each list is the same length of instructions. All instructions are
randomly selected.