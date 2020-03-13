# plt-hist
Bash tool for plotting a histogram

Example usage:

```bash
# change file name to path on your machine
echo "alias histogram='python3 plot_hist.py'" >> ~/.bash_profile
source ~/.bash_profile

head some.file
0	87.3620786227997
1	43.18670088814325
2	55.770814367184045
3	40.29361956923501
4	47.895042029062246
5	41.049393108902436
6	33.58014402360192
7	39.50618335101543
8	23.375927367608785
9	41.30484760005847

cat some.file | cut -f 2 | histogram

```
