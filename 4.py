import os
def main():
	filename = raw_input("Enter the filename: \n>")
	#filename = filename+str
	new_file = open("no_of_files.txt","a")
	new_file.close()
	os.system("ls > no_of_files.txt")
	new_file = open("no_of_files.txt","r")
	a = []
	for line in new_file:
		a.append(line)
	count = 0
	length = len(filename)
	for element in a:
		print element[0:length]
		print element[length]
		if element[0:length]==filename and element[length].isdigit():
			count+=1	
	print count		
	new_file.close()
	count_f = count
	#if os.stat(filename+".txt")==0:
	#Create a file if it doesnt exist.
	f_temp = open(filename+".txt","a")
	f_temp.close()
	#Latest_commit will have all the latest file contents
	f4 = open("latest_commit.txt","w")
	f3 = open(filename+".txt","r")
	#Put all the data of the temp file into latest_commit
	for line in f3:
		f4.write(line)
	f4.close()	
	while True:
		option = input("What do you want to do? \n1. Edit the original file\n2. Check the latest commit file \n3. Check the temporary file number: \n4. List out the files \n5. Commit into the original file and exit. \n>")
		if option==1:
			newoption = input("What do you want to do? \n1. Append a new line.\n2. Delete any existing line \n>")
			if newoption==1:
				append_line = raw_input("Enter the line you want to append: \n>")
				#open(filename+str(count_f)+".txt",'a')
				f1 = open("latest_commit.txt",'r')
				f2 = open("temporary.txt",'w')
				#Copying file contents to another temporary file
				for line in f1:
					print "LINE IS HERE"
					print line
					f2.write(line)

				print "Temporary file to be changed"
				f2 = open("temporary.txt")
				for line in f2:
					print line
				f2.close()		
				
				fd_write = open("temporary.txt","a")
				if count_f==0:
					fd_write.write(append_line)	
				else:
					fd_write.write("\n"+append_line)
				fd_write.close()
				print "Changed file"
				with open("temporary.txt") as f2:
					for line in f2:
						#print "Mein"
						print line
				f2.close()		
				print "Here"
				commit = raw_input("Do you want to commit the file? \n1.Yes \n2.No")
				if commit=="1":
					f5 = open("latest_commit.txt","w")
					f6 = open(filename+str(count_f)+".txt","w")
					fd_copy = open("temporary.txt","r+")
					print "Start Commiting"
					for line in fd_copy:
						print "This is the content"
						print line
						f5.write(line)
						f6.write(line)
					f5.close()
					f6.close()
					fd_copy.close()
					count_f+=1			
				# else:
				# 	commit_no = input("Changes will be lost. Do you still want to continue? \n1.Yes \n2.No and Commit please!")
				# 	if commit_no==2:
				# 		f5
				fd_read = open("latest_commit.txt","r")
				print "Original File"
				for line in fd_read:
					print line
				fd_read.close()
				
			elif newoption==2:
				del_line = input("Enter the line number to be deleted: \n>")
				del_line-=1
				fd_del = open("latest_commit.txt","r")
				lines = []
				for line in fd_del:
					lines.append(line)
				fd_del.close()
				print lines
				print "LINES"
				try:
					del lines[del_line]
				except:
					print "Input out of range"
					pass	
				fd = open("latest_commit","w")
				#lines.remove(int(del_line):int(del_line)+1)
				# for line in lines:
				# 	if count<del_line:
				# 		count+=1
				# 		fd.write(line)
				# 	elif count>del_line:
				# 		count+=1
				# 		fd.write(line)
				# 	fd.close()		
				print lines
				fd_temp = open("temporary.txt","w")
				for line in lines:
					fd_temp.write(line)
				fd_temp.close()	

				#for line in lines:
				#	fd.write(line)
				commit = raw_input("Do you want to commit the file? \n1.Yes \n2.No")
				if commit=="1":
					f5 = open("latest_commit.txt","w")
					f6 = open(filename+str(count_f)+".txt","w")
					fd_copy = open("temporary.txt","r+")
					print "Start Commiting"
					for line in fd_copy:
						print "This is the content"
						print line
						f5.write(line)
						f6.write(line)
					f5.close()
					f6.close()
					fd_copy.close()
					count_f+=1
				
				fd_read = open("latest_commit","r")
				for line in fd_read:
					print line
				fd_read.close()
		elif option==2:
			rd = open("latest_commit.txt","r")
			for line in rd:
				print line
			rd.close()	 
		elif option==3:
			number = input("Enter the number of commit:\n>")
			rd = open("temp"+str(number)+".txt","r")
			for line in rd:
				print line	
			rd.close()		
		elif option==4:
			os.system("ls")
		elif option==5:
			fd_1 = open(filename+".txt","w")
			fd_2 = open("latest_commit.txt","r")
			for line in fd_2:
				print line
				fd_1.write(line)
			fd_1.close()
			fd_2.close()
			break	
		else:
			break		
main()			
