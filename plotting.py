import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

health_data = pd.read_csv('health_data.csv', header=0, sep=',')

health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line')

plt.xlim(xmin=0)
plt.ylim(ymin=0)

plt.show()
