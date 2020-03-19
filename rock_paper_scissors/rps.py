#!/usr/bin/python

import sys

moves = ['scissors', 'paper', 'rock']

def rock_paper_scissors(n):
  turns = []

  stack = [[]]
  
  while len(stack) > 0:
    turn = stack.pop()

    if n == 0 or len(turn) == n:
      turns.append(turn)
    else:
      for i in moves:
        stack.append(turn + [i])

  return turns


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')