# plt-hist
Bash tool for plotting a histogram

Requires Python 3 and the installation of `matplotlib`, `numpy`, and `seaborn`.

Accepts tab separated columns of numerical entries piped into the program. Any lines that can't be parsed are skipped.

Installation:

```bash
git clone https://github.com/SpacemanSpiff7/plt-hist.git
cd plt-hist
# Append to whatever you use for your environment, here I am using ".bash_profile"
echo "alias histogram='python3 $(realpath plot_hist.py)'" >> ~/.bash_profile
source ~/.bash_profile
```

Example usage:

```bash
head some.file
```
```
0	60.89145984183395	16.194739031135697	62.05422906812093
1	76.11328105561269	25.685796665007597	69.23112776735869
2	49.66338305417318	35.160180757160525	75.9314592566198
3	51.932887323581866	36.997767416412046	71.56795801719112
4	31.766829206833897	50.969366637020954	76.9317009306418
5	42.94247701314698	23.71272235245994	58.78080322304585
6	64.4278408636979	30.730586329709155	57.234406550405474
7	63.812484596524556	9.270041045038921	67.4250310138683
8	66.60444703550056	30.442072759867056	67.18307252745025
9	60.86744810067439	16.254908119688587	70.5111646543144
```

```bash
cat some.file | cut -f 2,3,4 | histogram
```
![Example Histogram](https://github.com/SpacemanSpiff7/images/blob/master/Screen%20Shot%202020-03-13%20at%201.01.54%20PM.png)
