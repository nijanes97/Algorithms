#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profits = []

  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      profits.append({"first": prices[i], "second": prices[j], "value": prices[j] - prices[i]})
  
  maximum = profits[0]["value"]

  for i in range(len(profits)):
    if profits[i]['value'] > maximum:
      maximum = profits[i]['value']

  return maximum


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))