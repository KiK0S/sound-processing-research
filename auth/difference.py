#!/home/kikos/anaconda3/bin/python3
import sys
values = []
names = []
sys.stdin = open('names.txt')
n = int(input())
for i in range(n):
	NAME = input()
	inp = open(NAME + '_data')
	print(NAME, end = ' ')
	s = inp.read()
	data = s.split()
	for i in range(0, len(data)):
		data[i] = float(data[i])
	values.append(data)
print()
LEN = len(values[0])
g = []
for i in range(n):
	g.append([0 for j in range(0, n)])
for i in range(0, n):
	for j in range(0, n):
		for k in range(0, LEN):
			g[i][j] += (values[i][k] - values[j][k]) * (values[i][k] - values[j][k])
		# g[i][j] -= LEN
		print("%.4f"%g[i][j], end = ' ')
	print()