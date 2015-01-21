def clique(n):
	c = 0
	print "in a clique..."
	c = c +1
	for j in range(n):
		c = c +2
		for i in range(j):
			print i, "cippa lippa", j
			c = c +1
	c = c + 1
	print c

clique(4)