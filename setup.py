# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/20 12:21:13 by kcosta            #+#    #+#              #
#    Updated: 2018/11/20 12:54:57 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from setuptools import setup, find_packages

with open('README.md') as f:
  readme = f.read()

setup(
  name='linear_regression',
  version='0.1',
  description=readme,
  author='kcosta',
  author_email='kcosta@student.42.fr',
  url='https://github.com/kcosta42/Linear_Regression',
  license='MIT',
  packages=find_packages(exclude=('tests', 'docs'))
)
