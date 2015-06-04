import os


listoffiles = open("list.txt","w")
listoffiles.close()



#Enter cd / after testing
os.system("cd ..;cd ..;ls;(du -ah *)> /home/xynazog/L3/DFHDD/list.txt")
lof = open("list.txt","r")
listeverything = []
for line in lof:
	a = []
	a = line.split('\n')
	listeverything.append(a[0])



fullpaths = []
file_size = []
types = []
file_names = []
commontype = {}
file_paths = []
size = []
file_type = []


for files in listeverything:
	#files = files.replace("\\","\\\\")
	a = []
	a = files.split("\t")
	#c = list(a[0])
	size.append(a[0])
	fullpaths.append(a[1])
number_count=0	
#print fullpaths
commonsize = {}

for names in fullpaths:
	c = names.split("/")
	if c[-1].find('.')!=-1 and names.find('/')!=-1:
		d = c[-1].split('.')
		#print d
		a = []
		a = list(names)
		#print a
		x = names.rindex('/')
		a = a[:x]
		b = ''.join(a)
		if d[1].isalpha():
			#types.append(d[1])
			#commontype[d[1]]=[]
			commontype[d[1]] = []
			file_type.append(d[1])	
			file_names.append(d[0])
			file_paths.append(b)
			file_size.append(size[number_count])
	number_count+=1
total_length = len(file_names)
unique_file_types = set(file_type)
#Use Globals if you want to make dynamic lists
# unique_file_sizes = set(file_size)

abc =  zip(*sorted(zip(file_type,file_size,file_names,file_paths)))
print "Types"
file_type = abc[0]
file_size = abc[1]
file_names = abc[2]
file_paths = abc[3]
# for i in xrange(total_length):
# 	print "File Name:"+str(file_names[i])+"\tFile Path:"+str(file_paths[i])+"\tFile Size:"+str(file_size[i])+"\tFile Type:"+str(file_type[i])





commonsize = {}
for i in xrange(total_length):
	if file_type[i] in commontype:
		commontype[file_type[i]].append([file_names[i],file_paths[i],file_size[i]])	
	else:
		commontype[file_type[i]] = [[file_names[i],file_paths[i],file_size[i]]]
final_list = []
for x in commontype:
	a = []
	#print "here"
	#print commontype[x]
	for y in xrange(len(commontype[x])):
		if 'K' in str(commontype[x][y][2]):
			a.append([commontype[x][y][0],commontype[x][y][1],float(commontype[x][y][2].split('K')[0])])
		elif 'M' in str(commontype[x][y][2]):
			a.append([commontype[x][y][0],commontype[x][y][1],float(commontype[x][y][2].split('M')[0])*1024])
		else:
			a.append([commontype[x][y][0],commontype[x][y][1],float(commontype[x][y][2])])
	final_list.append([x,sorted(a,key=lambda qwer: qwer[2])])
	print '\n'	
# for groups in final_list:
# 	print groups
# 	print '\n'

same_files = []


#print final_list[15][1]
pairings = []
for x in xrange(len(final_list)):
	for p1 in xrange(len(final_list[x][1])):
		for p2 in xrange(p1+1,len(final_list[x][1])):
			if final_list[x][1][p1][2]==final_list[x][1][p2][2]:
				pairings.append([final_list[x][0],final_list[x][1][p1],final_list[x][1][p2]])
for pair in pairings:
 	print pair
 	print '\n'
#os.system('su') 	
for pair in pairings:
	#print pair
	#print pair[2][0]+"."+pair[0]
	file1 =  pair[1][0]+"."+pair[0]
	#print pair[2][0]
	#f1 = open("/home/xynazog/"+pair[1][1]+"/"+str(file1),'r')
	address1 = "/home/xynazog/"+pair[1][1]+"/"+str(file1)
	#linesoffirst = []
	#for line in f1:
	#	linesoffirst.append(line)
	#for line in f1:
	#	print line
	#f1.close()
	file2 = pair[2][0]+"."+pair[0]	
	#f2 = open("/home/xynazog/"+pair[2][1]+"/"+str(file2),'rw+')
	address2 = "/home/xynazog/"+pair[2][1]+"/"+str(file2)
	#linesofsecond = []
	#for line in f2:
	#	linesofsecond.append(line)
	#f2.close()
	print address1
	print address2
	try:
		address1 = address1.replace(" ","\ ")
	except:
		pass
	try:
		address2 = address2.replace(" ","\ ")
	except:
		pass		
	x = os.system("cmp --silent "+address1+" "+address2)
	print x
	if x==0:
		same_files.append(pair)
print "Same Files"
print "\n"
#print same_files	
for files in same_files:
	print "File Type: "+str(files[0])
	fl1 = str(files[1][1])+"/"+str(files[1][0])+"."+str(files[0])
	fl2 = str(files[2][1])+"/"+str(files[2][0])+"."+str(files[0])
	print "First File Location: "+ fl1
	print "Second File Location: "+ fl2
	print "\n"
	option_rem = input("Do you want to remove a file? \n1.First Location \n2.Second Location:\n>")
	if option_rem==1:
		print "Removing file at the first Location if permissions available!"
		os.system("sudo rm /home/xynazog/"+str(fl1))
	else:
		pass	
	if option_rem==1:
		print "Removing file at the second Location if permissions available!"
		os.system("sudo rm /home/xynazog/"+str(fl2))
	else:
		pass
# for lists in final_list:
# 	#for files in lists:
# 	print lists
# 		#print len(files)
# 	print '\n'	

# for filety in unique_file_types:
# 	a = []
# 	for each in commontype[filety]:
		#print each[2]
		# if str(each[2].split('.')[1])=="0M":
		# 	a.append([each[0],each[1],int(str(each[2].split('.')[0]))*1024])
		# else:	
		# 	a.append([each[0],each[1],each[2]])
	#print filety
	#print sorted(a)
	#,key= lambda x : str(a[2])
#print commontype
#print commonsize
# print "Bro"
# new_file_type = file_type
# print new_file_type
# for i in xrange(total_length):
# 	current_file_type = file_type[i]
# 	#print type(current_file_type)
# 	count_file_remaining = new_file_type.count(current_file_type)
# 	print count_file_remaining
# 	print current_file_type
# 	if count_file_remaining==0:
# 		print "yes"
# 	else:
# 		new_file_type = new_file_type[1:]
		









#for i in xrange(total_length):
	#print file_type[i],file_size[i]
	#if file_type[i] in commontype:
		#print commontype
	#print commonsize
	#if file_size[i] in commonsize:
 		#print commontype
 		#print "Third"
 		#print commonsize[file_size[i]]
 		#.append([file_names[i],file_paths[i]])
 		
 		#commontype[file_type[i]].append([commonsize[file_size[i]].append([file_names[i],file_paths[i]])])
	#else:
 		#commonsize[file_size[i]] = [file_names[i],file_paths[i]]
 		#print "First"
 		#print commonsize
 		#print "Second"
 		#print commontype
 		#print "\n"	
 		#commontype[file_type[i]] = commonsize
 		#print commontype
 		#break
 	#else:
 	#	commonsize[file_size[i]] = [[file_names[i],file_paths[i]]]
 	#	commontype[file_type[i]].append([commonsize[file_size[i]]])




#for key in commontype:
	#print key
#for sizesq in commonsize:
#	print commontype[key]
#print commonsize
#print "\n"		
# for path in fullpaths:
# 	a = []
# 	print path
# 	a = list(path)
# 	print a
# 	print path.rindex('/')
# 	x = path.rindex('/')
# 	a = a[:x]
# 	b = ''.join(a)
# 	paths.append(b)	
#for i in xrange(len(fullpaths)):
	# print fullpaths[i]
	# print types[i]
	# print namefiles[i]
#types
#namefiles
#commontype
#commontype['']


