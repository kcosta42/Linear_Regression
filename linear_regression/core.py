# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    core.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/20 17:44:34 by kcosta            #+#    #+#              #
#    Updated: 2018/11/23 15:52:58 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import linear_regression.predictor as predictor
import linear_regression.trainer as trainer

def linear_function(x):

  try:
    predictor.predict(x)
  except:
    print('Unexpected Error')
  return

def gradient_descent(dataset, visual=False):

  try:
    trainer.read_dataset(dataset, visual)
  except:
    print('Unexpected Error')
  return
