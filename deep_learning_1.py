# -*- coding: utf-8 -*-
"""Deep Learning 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WGK4WUAipGvko_YUJDkGM_oEKiwSmwz2
"""

import numpy as np

A = [1,2,3,4]

B = np.array(A)

A, B

"""Lists and Arrays"""

for i in A:
    print(i)

A.append(5)
A + [5]

#Broadcasting
B + np.array(5)

B+ np.array([1,2,3,4])

B * 2

A *2

