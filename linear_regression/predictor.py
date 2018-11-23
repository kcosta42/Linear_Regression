# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predictor.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/23 14:47:07 by kcosta            #+#    #+#              #
#    Updated: 2018/11/23 16:03:28 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from linear_regression.perceptron import Perceptron
import pandas as pd

def predict(value):

  theta0 = 0.0
  theta1 = 0.0
  mean = 0.0
  std = 1.0
  try:
    df = pd.read_csv('./linear_regression/model.csv', header=None)
    theta0 = df.iloc[0, 0]
    theta1 = df.iloc[0, 1]
    mean = df.iloc[0, 2]
    std = df.iloc[0, 3]
  except:
    pass

  ppn = Perceptron().set_weigths(theta0, theta1)
  value_std = (value - mean) / std
  print(f'Estimated Price: {ppn.predict(value_std)}')
