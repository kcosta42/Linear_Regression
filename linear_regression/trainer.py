# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainer.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/20 18:54:24 by kcosta            #+#    #+#              #
#    Updated: 2018/11/26 11:14:55 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from linear_regression.perceptron import Perceptron
from linear_regression.visualizer import show_data, show_errors, show_model
import pandas as pd

def read_dataset(dataset, visual=False):

  df = pd.read_csv(dataset)
  X = df.iloc[0:, 0].values
  y = df.iloc[0:, 1].values

  if visual:
    show_data(X, y)

  mean = X[0:].mean()
  std = X[0:].std()

  X_std = (X[0:] - mean) / std
  ppn = Perceptron(eta=0.15, n_iter=19).fit(X_std, y)
  ppn.save_model(mean, std)
  print("Model Trained.")

  if visual:
    show_errors(ppn)
    show_model(ppn, X_std, X, y)

  return
