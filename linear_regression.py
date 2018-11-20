#!/usr/bin/python3

import argparse
import linear_regression.core as core

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Linear Regression Function.')

  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-p', '--predict', type=int, metavar='value', help='Predict based on input value')
  group.add_argument('-t', '--train', type=str, metavar='file', help='Train model based on input file')

  parser.add_argument('-v', '--visual', action="store_true", help="Show model")

  args = parser.parse_args()
  core.linear_regression(args.predict, args.train, args.visual)
