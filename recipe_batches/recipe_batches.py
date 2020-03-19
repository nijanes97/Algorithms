#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_batches = 999999999999

  if len(recipe) > len(ingredients):
    return 0

  for i in ingredients:
    if min_batches > ingredients[i] / recipe[i]:
      min_batches = int(ingredients[i] / recipe[i])

  return min_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))