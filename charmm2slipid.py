# For modify POPC and SOL(TIP3)
# Cholestrol is in same order
# 2016-08-31
#

import sys
import getopt
import pandas as pd

def usage():
	print '''
	python charmm2slipid.py [option] [value] ...
	-h or --help
	-i or --input="Origninal file like Charmm-gui.gro"
	-o or --output="Modified file like Slipid.gro"
	'''
	return 0

if ( len(sys.argv ) == 1 ):
	print('-h or --help for detail')
	sys.exit(1)
	
shortargs = 'hi:o:'
longargs = ['help', 'input=', 'output=']

opts,args = getopt.getopt( sys.argv[1:], shortargs, longargs)
# print(opts,args)

if args:
	print('-h or --help for detail')
	print(args)
	sys.exit(1)

paramdict = {}	
	
for opt,val in opts:
	if opt in ( '-h', '--help' ):
		usage()
		sys.exit(1)
	if opt in ( '-i', '--input' ):
		paramdict['input'] = val
		continue
	if opt in ( '-o', '--output' ):
		paramdict['output'] = val
		continue

def convert(fin, fout):
	# ind = []
	# ind_old = []
	# itp = open('slipid_top/POPC.itp', 'r')
	# itp_charmm = open('charmm-gui_top/POPC.itp', 'r')
	gro = open(fin, 'r')
	output = open(fout, 'w')

	
	gro_line = list(gro.readlines())

	# # Get the Atom index of POPC in Slipid
	# itp_line = list(itp.readlines())
	# for i in range(20, 154, 1):
		# ind.append(itp_line[i][34:38])
		
	# # Get the Atom index of POPC in Charmm-gui
	# itp_charmm_line = list(itp_charmm.readlines())
	# for i in range(18, 154, 1):
		# ind_old.append(itp_charmm_line[i][36:40])
	

	df_ind = pd.read_table('./a-index/charmm-slipid-popc.txt')
	ind_old = list(df_ind[0:]['CharA'])
	ind = list(df_ind[0:]['SlipA'])

	# print ind
	# print ind_old

	
	new_line = list(range(0, len(gro_line)))
	#print new_line

	for i in range(0, len(gro_line)):
		tmp = gro_line[i]

		if tmp[5:9].strip() == 'POPC':
				index_Slipid = ind.index(tmp[11:15])
				index_Charmm = ind_old.index(tmp[11:15])
				# Exchange the Position
				new_line[i + index_Slipid - index_Charmm ]  = tmp
			
				
		elif tmp[5:9].strip() == 'CHL1':
			if tmp[11:15] == "  H3": 
				_tmp = tmp
				continue
			if tmp[11:15] == "  O3":
				new_line[i-1] =  tmp[0:5] + 'CHOL' + tmp[9:]
				new_line[i-1] = _tmp[0:5] + 'CHOL' + tmp[9:]
			new_line[i] = tmp[0:5] + 'CHOL' + tmp[9:]
			
		elif tmp[5:9].strip() == 'TIP3':
			if tmp[12:15].strip() == 'OH2':
				new_line[i] = tmp[0:5] + 'SOL     OW' + tmp[15:]
			elif tmp[12:15].strip() == 'H1':
				new_line[i] = tmp[0:5] + 'SOL    HW1' + tmp[15:]
			else:
				new_line[i] = tmp[0:5] + 'SOL    HW2' + tmp[15:]
		
		elif tmp[5:9].strip() == 'CLA':
			new_line[i] = tmp[0:5] + 'CL      CL' + tmp[15:]
		
		elif tmp[5:9].strip() == 'SOD':
			new_line[i] = tmp[0:5] + 'NA      NA' + tmp[15:]
			
		else:
			new_line[i] = tmp

				
	#print new_line
	for i in new_line:
		#print i 
		try:
			output.write(i)
		except:
			continue

	
	gro.close()
	output.close()
	return(0)

print('Running...')
convert(opts[0][1], opts[1][1])	
print('Done.')




