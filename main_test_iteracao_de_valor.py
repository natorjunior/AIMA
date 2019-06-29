# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:48:13 2019

@author: Trisa
"""
from MoneyModel import MoneyModel
import matplotlib.pyplot as plt


model = MoneyModel(1, 4, 3)
for i in range(1):
    model.step()
import numpy as np

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    print(cell)

#plt.imshow(agent_counts, interpolation='nearest')
#plt.colorbar()