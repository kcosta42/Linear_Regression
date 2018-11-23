# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainer.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/20 18:54:24 by kcosta            #+#    #+#              #
#    Updated: 2018/11/23 16:05:52 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from linear_regression.perceptron import Perceptron
import matplotlib.pyplot as plt
import pandas as pd

def read_dataset(dataset, visual=False):

  df = pd.read_csv(dataset)
  X = df.iloc[0:, 0].values
  y = df.iloc[0:, 1].values

  if visual:
    plt.scatter(X, y, marker='x')
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.show()

  mean = X[0:].mean()
  std = X[0:].std()

  X_std = (X[0:] - mean) / std
  ppn = Perceptron(eta=0.15, n_iter=19).fit(X_std, y)
  print("Model Trained.")

  if visual:

    plt.plot(range(1, len(ppn._errors) + 1), ppn._errors, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of misclassifications')
    plt.show()

    plt.scatter(X, y, marker='x')
    plt.plot(X, ppn._theta1 * X_std + ppn._theta0)
    plt.title('Linear Regression')
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.show()

  ppn.save_model(mean, std)
  return
