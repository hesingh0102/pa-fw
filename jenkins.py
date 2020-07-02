
file = open('curl_output.txt', 'r')
for line in file:
    if ('\\r\\n\\t' in line):
        line = line.replace('\\r\\n\\t','\n')
    elif ('\\r\\n' in line):               
        line = line.replace('\\r\\n','\n')
    print(line)

file.close()




