import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

fig, [(ax1,ax2),(ax3,ax4)] = plt.subplots(nrows=2,ncols=2)
ax2.axis('off')
ax3.axis('off')
ax1.pie([60,40],labels=['1kolor','2kolor'])
ax4.pie([60,40])
plt.show()