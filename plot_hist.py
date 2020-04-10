import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from collections import defaultdict

cols = defaultdict(list)
nbins = None

if len(sys.argv) > 1:
    if sys.argv[1] == '-n':
        try:
            nbins = int(sys.argv[2])
        except (IndexError, ValueError):
            print('ERROR: \'-n\' must be a positive integer. Example use:\n\t\t$ cat numbers.txt | histogram  -n 25')
            exit(1)

for line in sys.stdin:
    sp = line.split('\t')
    for i, token in enumerate(sp):  
        try:
            cols[i].append(float(token))
        except ValueError:
            continue

for array in cols.values():
    arr = np.array(array)
    sns.distplot(arr, bins=nbins, label='Mean:    {:.4E}\nMedian: {:.4E}\nRange:  [{:.4E}, {:.4E}]'.format(np.mean(arr), np.median(arr), np.min(arr), np.max(arr)))

plt.legend()
plt.show()
