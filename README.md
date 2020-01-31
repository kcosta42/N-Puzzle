# N-Puzzle

About
-----
>We had to create a program capable of solving 15-puzzles of various sizes, as optimally as possible.

This is one of the first projects of the Advanced Algorithm branch at School 42 Paris

Implemented Algorithms
----------------------
- [A* search](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)

Installation
------------
Run `make install`

Usage
-----
`python3 npuzzle.py [-h] [--size SIZE] [-s] [-u] [-i] [-n ITERATIONS] [-f FILENAME] [-t {snail,row}] [-a {A*,BFS}] [--heuristic {euclidean,manhattan,tiles-out,uniform-cost}] [-d]`
  * -h: show this help message and exit
  * --size SIZE: Size of the puzzle's side. Must be >3.
  * -s: Forces generation of a solvable puzzle. Overrides -u.
  * -u: Forces generation of an unsolvable puzzle.
  * -i: Enable interactive mode. Overrides --size -f.
  * -n ITERATIONS: Number of passes.
  * -f FILENAME: Generate puzzle from file. Overrides --size.
  * -t {snail,row}: NPuzzle type.
  * -a {A*,BFS}: Algorithm used for search.
  * --heuristic {euclidean, manhattan, tiles-out, uniform-cost}: Heuristic function
  * -d: Print every step to the solution.

### Example
```
>python3 npuzzle.py --size 3 -s
Initial State:
2 8 4
5 0 6
1 3 7
Starting Search...

Total number of states ever selected in the openSet (Complexity in time): 2302
Maximum number of states ever represented in memory at the same time during the search (Complexity in size): 933


Number of moves required: 22

State 0:
2 8 4
5 0 6
1 3 7

[...]

State 22:
1 2 3
8 0 4
7 6 5
```

##### Project done in 2020
