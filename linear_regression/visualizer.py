# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    visualizer.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/23 14:47:09 by kcosta            #+#    #+#              #
#    Updated: 2018/11/26 11:10:47 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt

def show_data(X, y):
  plt.scatter(X, y, marker='x')
  plt.xlabel('mileage')
  plt.ylabel('price')
  plt.show()

def show_errors(ppn):
  plt.plot(range(1, len(ppn._errors) + 1), ppn._errors, marker='o')
  plt.xlabel('Epochs')
  plt.ylabel('Number of misclassifications')
  plt.show()

def show_model(ppn, X_std, X, y):
  plt.scatter(X, y, marker='x')
  plt.plot(X, ppn._theta1 * X_std + ppn._theta0)
  plt.title('Linear Regression')
  plt.xlabel('mileage')
  plt.ylabel('price')
  plt.show()
