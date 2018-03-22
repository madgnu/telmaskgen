#! /usr/bin/env python3

import sys

def intersect(a, b):
	c = []
	for i in range(len(a)):
		c.insert(i, a[i] | b[i])
	return c

def calc_cardinality(a, b):
	diffs = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			diffs = diffs + 1
	return diffs


def make_one(m):
	for i in range(len(m)):
		for j in range(len(m)):
			if (i != j) and (calc_cardinality(m[i], m[j]) < 2):
				m[i] = intersect(m[i], m[j])
				m.pop(j)
				return 1, m
	return 0, m

def print_mask(m):
	s = '^'
	l = list(map(lambda n: sorted(list(n)), m))
	for i in range(len(l)):
		if len(l[i]) == 1:
			s = s + ''.join(l[i])
		elif len(l[i]) == 10:
			s = s + '.'
		else:
			s = s + '[' + ''.join(l[i]) + ']'
	s = s + '$'
	return s

def main(fname):
	f = open(fname)
	tels = sorted(f.read().splitlines())
	fm = list(map(lambda tel: list(map(lambda n: set(n), tel)), tels))
	fl = 1
	while fl > 0: fl, fm = make_one(fm)
	r = list(map(lambda m: print_mask(m), fm))
	print('|'.join(r))
	sys.exit(0)

if (__name__ == '__main__'):
	main(sys.argv[1])

