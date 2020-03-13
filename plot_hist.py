import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

nums = []

for line in sys.stdin:
    try:
        nums.append(int(line))
    except ValueError:
        continue

nums = np.array(nums)

sns.distplot(nums)
plt.show()
