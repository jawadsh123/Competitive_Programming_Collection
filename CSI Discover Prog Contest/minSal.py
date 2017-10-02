
from collections import deque

with open('input.txt') as f:
	content = f.readlines()
	content = [x.strip('\n') for x in content]
	line = [[] for i in range(len(content))]

	d = dict()

	emp_set = deque()

	for i in range(len(content)):
		x = content[i]
		line[i] = x.split(', ')

	CEO = []
	for x in line:
		if x[2] == "NOBODY":
			CEO.append(x[0])


	for i in range(len(CEO)):

		emp_set.append(CEO[i])
		last_emp = ''

		while len(emp_set) != 0:
			sup = emp_set.popleft()
			for x in line:
				if x[2] == sup:
					emp_set.append(x[0])
					last_emp = x[0]

		d[CEO[i]] = last_emp		


	fp = open("output.txt", 'w')


	for key in d:
		fp.write(key + ": " + d[key] + '\n')
