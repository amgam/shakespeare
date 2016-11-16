input = open('parse-couplet.txt', 'r')
nP = []
vP = []
pP = []
adjP = []
S = []


def findSentence(s):
	phrase = []
	count = 1
	#s = s[1:]
	i = 0
	while count != 0 and i < len(s):
		j = 0
		if s[i] == '(':
			if i != 0:
				count += 1
			while s[i+j+1] != ' ':
				j += 1
			addition = '[' + s[i+1: i +j + 1]
			phrase.append(addition)
		elif s[i] == ')':
			count -= 1
			j = 1
			if len(phrase) >0:
				addition = phrase[len(phrase) - 1] + ']'
				phrase[len(phrase) - 1] = addition
		elif s[i] == ' ':
			while i + j + 1 < len(s) and s[i+j + 1] != ')' and s[i+j+1] != '(':
				j += 1
		i = j + i + 1
	answer = tuple(phrase)
	S.append(answer)

def findPhrase(s, key):
	phrase = []
	count = 1
	#s = s[1:]
	i = 0
	while count != 0 and i < len(s):
		j = 0
		if s[i] == '(':
			if i != 0:
				count += 1
			while s[i+j+1] != ' ':
				j += 1
			addition = '[' + s[i+1:i+j+1]
			phrase.append(addition)
		elif s[i] == ')':
			count -= 1
			j = 1
			if len(phrase) > 1:
				addition = phrase[len(phrase)-1] + ']'
				phrase[len(phrase)-1] = addition
		elif s[i] == ' ':
			while i + j + 1 < len(s) and s[i+j + 1] != ')' and s[i+j+1] != '(':
				j += 1
		i = i + j + 1
	answer = tuple(phrase)
	if key == 'NP':
		nP.append(answer)
	elif key == 'VP':
		vP.append(answer)
	elif key == 'PP':
		pP.append(answer)
	elif key == 'ADJP':
		adjP.append(answer)
		


for line in input:
	i = 0
	while i < len(line):
		if i + 1 < len(line) and line[i:i+3] == '(S ':
			findSentence(line[i:])
			print line[i:]
		elif i + 3 < len(line) and line[i:i+3] == '(NP':
			findPhrase(line[i:], 'NP')
		elif i + 3 < len(line) and line[i:i+3] == '(VP':
			findPhrase(line[i:], 'VP')
		elif i + 3 < len(line) and line[i:i+3] == '(PP':
			findPhrase(line[i:], 'PP')
		elif i + 5 < len(line) and line[i:i+5] == '(ADJP':
			findPhrase(line[i:], 'ADJP')
		i += 1


input.close()

np = open('NP.txt', 'w')
vp = open('VP.txt', 'w')
adjp = open('ADJP.txt', 'w')
s = open('S.txt', 'w')
for item in nP:
	thing = ' '.join(item)
	np.write(thing + '\n')
for item in vP:
	thing = ' '.join(item)
	vp.write(thing + '\n')
for item in adjP:
	thing = ' '.join(item)
	adjp.write(thing + '\n')
for item in S:
	thing = ' '.join(item)
	s.write(thing + '\n')
np.close()
vp.close()
adjp.close()