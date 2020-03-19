#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  
  if len(items) == 0 or capacity == 0:
    return 0
  values = []
  inventory = {
    'Value': 0,
    'Chosen': []
  }
  best_value = 0

  for i in range(len(items)):
    values.append(items[i].value / items[i].size)
  
  for j in range(len(values)):
    if capacity - items[j].size > 0 and values[j] > best_value:
        best_value = j

  if capacity - items[best_value].size > 0:
    inventory['Chosen'].append(items[best_value].index)
    inventory['Value'] += items[best_value].value
    del items[best_value]
    for i in knapsack_solver(items, capacity - items[best_value].size):
      if int(i['Value']) > 0:
        inventory['Chosen'].append(i['Chosen'])
        inventory['Value'] += int(i['Value'])
      
  print(inventory)
  return inventory


  

# 1 42 81
# 2 42 42
# 3 68 56
# 4 68 25
# 5 77 14
# 6 57 63
# 7 17 75
# 8 19 41
# 9 94 19
# 10 34 12

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')