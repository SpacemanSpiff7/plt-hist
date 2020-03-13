import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from collections import defaultdict

cols = defaultdict(list)

for line in sys.stdin:
    sp = line.split('\t')
    for i, token in enumerate(sp):  
        try:
            cols[i].append(float(token))
        except ValueError:
            continue

for array in cols.values():
    sns.distplot(np.array(array))

plt.show()
