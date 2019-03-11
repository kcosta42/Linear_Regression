import argparse
import linear_regression.core as core

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Gradient Descent Function.')

  parser.add_argument("dataset", type=str, help="Dataset to learn from")
  parser.add_argument('-v', '--visual', action="store_true", help="Show model")

  args = parser.parse_args()
  core.gradient_descent(args.dataset, args.visual)
