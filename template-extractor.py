import collections, random


allSentences = open('root_selected.txt', 'r')
npFile = open('NP_selected.txt', 'r')
vpFile = open('VP_selected.txt', 'r')
adjpFile = open('ADJP_selected.txt', 'r')
template = open('syntax-template.txt', 'w')

npCount = sum(1 for line in open('NP_selected.txt'))
vpCount = sum(1 for line in open('VP_selected.txt'))
adjpCount = sum(1 for line in open('ADJP_selected.txt'))

np = []
vp = []
adjp = []

for line in npFile:
	np.append(line)
for line in vpFile:
	vp.append(line)
for line in adjpFile:
	adjp.append(line)


def getRandomPSR(type):
	randPSR = ''
	if type == 'NP':
		index = random.randint(0, len(np))
		randPSR = np[index]
	elif type == 'VP':
		index = random.randint(0, len(vp))
		randPSR = vp[index]
	elif type == 'ADJP':
		index = random.randint(0, len(adjp))
		randPSR = adjp[index]
	result = randPSR.split()
	result = result[2:]
	return result

def helper(lst):
	result = []
	print lst
	print "that was list"
	if len(lst) == 0:
		return result
	if lst[0] == 'NP' or lst[0] == 'VP' or lst[0] == 'ADJP':
		psr = getRandomPSR(lst[0])
		result.extend(helper(psr))
		result.extend(helper(lst[1:]))
	else:
		result.append(lst[0])
		print result
		result.extend(helper(lst[1:]))
	print result
	print "that was result"
	return result

syntax = []
for line in allSentences:
	syntax = line.split()
	output = helper(syntax[2:])
for token in output:
	template.write(token + '\n')

npFile.close()
vpFile.close()
allSentences.close()
adjpFile.close()
template.close()