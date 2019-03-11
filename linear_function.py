import argparse
import linear_regression.core as core

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Linear Function.')

  parser.add_argument("mileage", type=int, help="Mileage")

  args = parser.parse_args()
  core.linear_function(args.mileage)
