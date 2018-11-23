# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    perceptron.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/21 11:37:10 by kcosta            #+#    #+#              #
#    Updated: 2018/11/23 16:02:33 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Perceptron(object):
  """Perceptron classifier

  Parameters
  ----------
  eta: float
    Learning rate (between 0.0 and 1.0)
  n_iter: int
    Passes over the training dataset
  precision: float
    Precision threshold for the model

  Attributes
  ----------
  _theta0: float
    θ₀ weight after fitting
  _theta1: float
    θ₁ weight after fitting
  _errors: list
    Number of misclassifications in every epoch
  """

  def __init__(self, eta=0.01, n_iter=10, precision=7.5):
    self.eta = eta
    self.n_iter = n_iter
    self.precision = precision

  def fit(self, X, y):
    self._theta0 = 0.0
    self._theta1 = 0.0
    self._errors = []

    for _ in range(self.n_iter):
      errors = 0
      temp0 = 0
      temp1 = 0

      for xi, target in zip(X, y):
        update = (self.predict(xi) - target)
        temp0 += update
        temp1 += update * xi
        errors += int(((100 * abs(update)) / target) > self.precision)
      self._theta0 -= (self.eta / len(X)) * temp0
      self._theta1 -=(self.eta / len(X)) * temp1
      self._errors.append(errors)
    return self

  def net_input(self, X):
    return self._theta0 + (X * self._theta1)

  def save_model(self, mean, std, filename='./linear_regression/model.csv'):
    f = open(filename, 'w+')
    f.write(f'{self._theta0},{self._theta1},{mean},{std}')
    f.close()
    return self

  def set_weigths(self, theta0=0.0, theta1=0.0):
    self._theta0 = theta0
    self._theta1 = theta1
    return self

  def predict(self, X):
    return self.net_input(X)
