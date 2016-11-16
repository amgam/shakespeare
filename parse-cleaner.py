input = open('parse-couplet.txt', 'r')
output = open('parse-couplet-cleaned.txt', 'w')

for line in input:
	i = line.index('<parse>')
	j = line.index('</parse>')
	output.write(line[i+7:j] + '\n')
	
input.close()
output.close()