import fileinput

input = open('parse-couplet-cleaned.txt', 'r')

root = []
threshold = 3


def recurse(s, depth, count):
	if s == '':
		return []
	result = []
	if s[0] == '(':
		count += 1
		result.extend(recurse(s[1:], count, count))
	elif s[0] == ')':
		count -= 1
		result.extend(recurse(s[1:], count, count))
	elif s[0] == ' ':
		i = 0
		print s[i]
		while i < len(s) and s[i] != ')' and s[i] != '(':
			i += 1
		result.extend(recurse(s[i:], count, count))
	else:
		if depth == threshold:
			i = 1
			while s[i] != ' ':
				i += 1
			addition = '[' + s[0:i] + ']'
			result.append(addition)
			result.extend(recurse(s[i:], count, count))
		elif depth == threshold - 1:
			i = 1
			while s[i] != ' ':
				i += 1
			addition = '[' + s[0:i]
			result.append(addition)
			result.extend(recurse(s[i:], count, count))
			addition = result[len(result)-1] + ']'
			result[ len(result) - 1] = addition
		else:
			result.extend(recurse(s[1:], count, count))
	return result

'''
def findSentence(s):
	phrase = []
	count = 1
	i = 0
	while count > 0 and i < len(s):
		if s[i] == '(':
			count += 1
		elif s[i] == ')':
			count -= 1
		elif s[i] != ' ':
			j = 0
			k = 0
			while s[i+j + 1] != ')':
				if s[i+j+1] == '(':
					count += 1
				if s[i+j+1] == ' ':
					k = j+1
				j += 1
			phrase.append(s[i:i+k])
		i += j
	answer = tuple(phrase)
	root.append(answer)


def traceFromRoot(s):
	
	phrase = []
	count = 1
	i = 0
	j=0
	while count > 0 and i < len(s):
		j = 1
		if s[i] == '(':
			count += 1
		elif s[i] == ')':
			count -= 1
		elif s[i] != ' ':
			rel = 1
			relIndex = 0
			k = 0
			while s[i+j] != ')':
				if s[i+j] == '(':
					count += 1
					rel -= 1
				if s[i+j] == ' ':
					k = j
				j += 1
				if rel > 0:
					relIndex = k
			phrase.append(s[i:i+k])
		i += j
	answer = tuple(phrase)
	root.append(answer)		

'''
for line in input:
	i = 0
	rel = 0
	if line[1] == 'R':
		if 4 < len(line) and line[1:5] == 'ROOT':
			result = recurse(line[5:], 0, 0)
			add = tuple(result)
			root.append(add)

'''
				while count > 0 and i < len(s) and rel > 0:
					j = 1
					if s[i] == '(':
						count += 1
					elif s[i] == ')':
						count -= 1
					elif s[i] != ' ':
						relIndex = 0
						k = 0
						while s[i+j] != ')':
							if s[i+j] == '(':
								count += 1
								rel += 1
							if s[i+j] == ' ':
								k = j
							j += 1
							if rel > 0:
								relIndex = k
							if rel > 0 and count == 0:
								max = 0
						phrase.append(s[i:rel])
					i += j
				answer = tuple(phrase)
				root.append(answer)		
'''
print root
input.close()
output = open('root.txt', 'w')
for item in root:
	i = 0
	thing = ' '.join(item)
	output.write(thing + '\n')
output.close()

