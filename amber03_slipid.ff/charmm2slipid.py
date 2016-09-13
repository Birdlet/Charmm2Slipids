# POPC only

ind = []
itp = open('POPC.a.txt', 'r')
gro = open('POPC_only.gro', 'r')
output = open('POPC_only_modified.gro', 'w')

itp_line = list(itp.readlines())
gro_line = list(gro.readlines())


for i in range(20, 154, 1):
	ind.append(itp_line[i][34:38])
#print ind

new_line = list(range(0, len(gro_line)))
#print new_line

for i in range(0,len(gro_line)):
	tmp = gro_line[i]
	try:
		new_line[(int(tmp[0:5].strip()) - 1) * 134 + ind.index(tmp[11:15]) + 2]  = tmp
	except:
		new_line[i] = tmp
		continue

#print new_line
for i in new_line:
	output.write(i)

itp.close()
gro.close()
output.close()



