input = open('couplet.txt.xml', 'r')
output = open('parse-couplet.txt', 'w')
for line in input:
	if line.find('<parse>') != -1:
		output.write(line)
input.close()
output.close()

