
import math
def createfs():
	fptr = open("filesystem.txt", "w")
	for i in range(1,700000+1):
		fptr.write(" ")
	currentpos = 700000

	for i in range (1, 1000+1):
		data = str(i)+" 1";
		for j in range(len(data),20):
			data=data+' '

		fptr.write(data)
	fptr.write('-')
	fptr.close()


def isdirexists(currentdir):
	fptr = open("filesystem.txt", "r")
	fptr.seek(720001)
	dirinfo = fptr.read(100000)
	fptr.close()

	for p in dirinfo.split('-'):
		# print(p)
		q=p.split(' ')
		if (q[0] is "0"):
			# print(q[1], len(q[1]), currentdir, len(currentdir))
			if (q[1] == currentdir):
				# print("Verified")
				return 1


def isfileexists(filename, dirname):
	fptr = open("filesystem.txt", "r")
	fptr.seek(720001)
	fileinfo = fptr.read(100000)
	fptr.close()
	for p in fileinfo.split("-"):

		q = p.strip().split(" ")
		# print(p, len(q))
		if (len(q)==4):
			# print(p)
			# print(q[1], filename, q[3], dirname)
			# print(len(q[1]), len(filename), len(q[3]), len(dirname))
			
			if (q[1]==filename and q[2]==dirname):
				# print("Exists")
				return 1

	return 0

def check_file_input():
	while(1):

		fname = input("Enter file name: ")
		if ("-" in fname or " " in fname):
			print ("Can't use dash(-) or space in name")
		else:
			break
	return fname

def check_dir_input():
	while(1):

		fname = input("Enter directory name: ")
		if ("-" in fname or " " in fname):
			print ("Can't use dash(-) or space in name")
		else:
			break
	return fname

def getfreepage():
	fptr = open("filesystem.txt", "r+")
	fptr.seek(700000)
	seekpoint=700000
	while(fptr.tell()<=720000-20):
		# print(fptr.tell())
		p = fptr.read(20).strip().split(" ")
		# print(p)
		if (int(p[1])==1):
			fptr.seek(seekpoint+len(p[0])+1)
			print(fptr.tell())
			fptr.write("0")
			return p[0]
		seekpoint = seekpoint+20
		fptr.seek(seekpoint)

	return -1
def createfile(currentdir):
	if (currentdir==""):
		print("Please first choose a directory")
		return
	filename = "nofilename"
	type = 1
	filename = check_file_input()
	if (len(filename)>50):
		print("Filename is too long!")
		return
	if (isfileexists(filename, currentdir)==1):
		print("File already exists")
		return

	fptr = open("filesystem.txt", "r+")
	fptr.seek(0,2)
	endposition = fptr.tell()+199
	if (fptr==None):
		print("Error")
		fptr.close()
		return
	
	fptr.write(str(type)+" "+filename+" "+currentdir+" 0")
	while (fptr.tell()!=endposition):
		fptr.write(" ")
	
	fptr.write("-")
	fptr.close()
	print("File is created")
	return




def mkdir():
	dirname = "nodirname"
	typ = 0
	dirname = check_dir_input()
	if (len(dirname)>50):
		print("Directory name is too long");
		return
	if (isdirexists(dirname)==1):
		print("This directory already exists");
		return
	fptr = open("filesystem.txt", "r+")
	fptr.seek(0, 2)		#2 indicates SEEK_END
	endposition = fptr.tell()+199

	if (fptr==None):
		print("Error!");
		fptr.close()
		return

	fptr.write(str(typ)+" "+dirname)
	while(fptr.tell()!=endposition):
		fptr.write(" ")

	fptr.write("-")
	fptr.close()
	print("Directory created")
	return



def cddir():
	changedir = "changedir"
	# changedir = str(input("Enter directory name: ")).strip()
	changedir = check_dir_input()
	if (isdirexists(changedir)==1):
		print("You are now in ",changedir)
		return changedir
	else:
		print("Directory doesn't exist. You are now in root")
		return ""




def deleteFile(currentdir):
	if (currentdir==""):
		print("Please first choose directory")
		return -1
	fptr = open("filesystem.txt", "r+")
	fptr.seek(720001)
	filename = " "
	fileinfo = fptr.read(100000)

	filename = check_file_input()
	i=0  
	for p in fileinfo.split("-"):
		q = p.strip().split(" ")
		if (len(q)==4):
			if (q[1]==filename and q[2]==currentdir):
				page_pos = 200
				page_pos = 720001+(page_pos*i)
				fptr.seek(page_pos)
				empty_str=""
				for i in range(199):
					empty_str=empty_str+" "
				fptr.write(empty_str)
				# return i

		i=i+1

	fptr.seek(500001)
	tableinfo = fptr.read(200000)
	count = 0
	for p in tableinfo.split('-'):
		print(p)
		q= p.strip().split(" ")
		if (q[0]==filename and q[1]==currentdir):
			fptr.seek(500001+(count*200))
			for i in range(199):
				fptr.write(" ")

		count = count+1
	# return -1



def move(s_fname, t_fname, currentdir):
	if (currentdir==""):
		print("Please first choose directory")
		return -1
	if(isfileexists(s_fname, currentdir)!=1):
		print("File doesn't exist!")
		return -1
	else:
		fptr = open("filesystem.txt", "r+")
		fptr.seek(720001)
		fileinfo = fptr.read(100000)

		i=0
		for p in fileinfo.split("-"):
			q = p.strip().split(" ")
			if (len(q)==4):
				if (q[1]==s_fname and q[2]==currentdir):
					page_pos = 200
					page_pos = 720001+(page_pos*i)
					fptr.seek(page_pos)
					a=q[0]
					b=t_fname
					c=q[2]
					d=q[3]

					info = q[0]+" "+t_fname+" "+q[2]+" "+q[3]
					print (info)
					fptr.write(info)
					empty_str=""
					for i in range(199-len(info)):
						empty_str=empty_str+" "
					fptr.write(empty_str)
					return i

			i=i+1

		return -1



def write_to_file(fname, text, currentdir):
	if (currentdir==""):
		print("Please first choose directory")
		return -1
	if(isfileexists(fname, currentdir)==0):
		print("File doesn't exist!")
		return -1
	else:
		fptr = open("filesystem.txt", "r+")
		text_length = len(text)
		page_size = 500
		# already_created = 0
		fptr.seek(500000)
		# tableinfo = fptr.read(200000)
		# for p in tableinfo.split('-'):
		# 	q= p.strip().split(" ")
		# 	page_num = q[2]
		# 	free_space = q[3]

		# 	if (free_space>0):
		# 		already_created=1

		# pages_required = int(math.ceil(text_length*1.0/page_size))-already_created
		pages_required = int(math.ceil(text_length*1.0/page_size))
		free_pages=[]
		for i in range(pages_required):
			free_pages.append(getfreepage())

		# if (already_created):
		# 	if (free_space>text_length):
		# 		data_pos = 0
		# 		fptr.seek((data_pos+(page_num-1)*500)+(500-free_space))
		# 		fptr.write(text)
		# 		return
			

		
		page_table = 500000
		fptr.seek(page_table)
		
		used_space = text_length%500
		for page in free_pages:
			
			fptr.seek(page_table+((int(page)-1)*200))
			if (page==free_pages[-1]):
				free_space = 500 - (text_length%500)

			else:
				free_space= 0

			fptr.write("-"+fname+" "+currentdir+" "+str(page)+" "+str(used_space))

		count=0
		for page in free_pages:
			data_pos = 0
			fptr.seek(data_pos+((int(page)-1)*500))
			if (page==free_pages[-1]):
				data_space = 500 - (text_length%500)
				fptr.write(text[count*500:(count*500)+data_space])
			else:
				data_space= 0
				fptr.write(text[count*500:(count+1)*500])

			count=count+1



def read_from_file(fname, currentdir):
	page_numbers = []

	if (currentdir==""):
		print("Please first choose directory")
		return -1
	if(isfileexists(fname, currentdir)==0):
		print("File doesn't exist!")
		return -1
	else:
		fptr = open("filesystem.txt", "r+")
		fptr.seek(500001)
		tableinfo = fptr.read(200000)
		for p in tableinfo.split('-'):
			# print(p)
			q= p.strip().split(" ")

			# print(q)
			if (q==['']):
				continue
			page_num = q[2]
			used_space = q[3]
			if (q[0]==fname and q[1]==currentdir):
				page_numbers.append(page_num)
		if (len(page_numbers)==0):
			print("File is empty")
			return
		
		data_pos = 0
		str_data = ""
		for page in page_numbers:
			data_pos = 0
			fptr.seek(data_pos+((int(page)-1)*500))
			str_data = str_data+fptr.read(500).strip()
		return str_data



			
def read_some_from_file(fname, currentdir, start, size):
	data = read_from_file(fname, currentdir)
	return data[start: start+size]




def write_at_pos_file(fname, currentdir, text, pos):
	page_numbers = []
	used_spaces = []
	page_positions = []

	used_space = 0
	file_length = len(read_from_file(fname, currentdir))
	if (file_length<pos):
		print("Can't write here. Use the append function ")

	if (currentdir==""):
		print("Please first choose directory")
		return -1
	if(isfileexists(fname, currentdir)==0):
		print("File doesn't exist!")
		return -1
	else:
		fptr = open("filesystem.txt", "r+")
		text_length = len(text)
		page_size = 500
		# already_created = 0
		fptr.seek(500001)
		table_data = fptr.read(200000)
		for p in table_data.split('-'):
			# print(p)
			q= p.strip().split(" ")
			if (q[0]==fname and q[1]==currentdir):
				page_num = int(q[2])
				used_space = used_space + int(q[3])

				page_numbers.append(page_num)
				used_spaces.append(used_space)

		i = 0
		print (page_numbers)
		print (used_spaces)
		print (pos)
		for page, spaces in zip (page_numbers, used_spaces):
			if (pos>spaces):
				i=i+1
				print(i)
				continue
			elif (pos>=0 and pos<spaces):
				fptr.seek(((int(page_numbers[i])-1)*500)+pos)
				fptr.write(text[0:spaces-pos])

				if (len(page_numbers)>1):
					fptr.seek(((int(page_numbers[i+1])-1)*500)+0)
					fptr.write(text[spaces-pos:text_length])
				break
				

			i=i+1



def truncate(fname, currentdir, target):
	page_numbers = []
	used_spaces = []
	page_positions = []

	used_space = 0
	file_length = len(read_from_file(fname, currentdir))
	if (file_length<target):
		print("Error. Target size is bigger than file size")
		return

	if (currentdir==""):
		print("Please first choose directory")
		return -1
	if(isfileexists(fname, currentdir)==0):
		print("File doesn't exist!")
		return -1
	else:
		fptr = open("filesystem.txt", "r+")
		page_size = 500
		# already_created = 0
		fptr.seek(500001)
		table_data = fptr.read(200000)
		for p in table_data.split('-'):
			if (len(p)>200):
				continue
			if (any(c.isalnum() for c in p)==False):
				continue
			print(p)
			
			q= p.strip().split(" ")

			if (q[0]==fname and q[1]==currentdir):
				page_num = int(q[2])
				used_space = used_space + int(q[3])

				page_numbers.append(page_num)
				used_spaces.append(used_space)

		j = 0
		# big = 0
		print (page_numbers)
		print (used_spaces)

		for page, spaces in zip (page_numbers, used_spaces):
			if (spaces>target):
				print (spaces, target)
				fptr.seek((int(page_numbers[j])-1)*500+target)
				for i in range(500):
					fptr.write(" ")

				print (j)

				fptr.seek((int(page_numbers[j+1])-1)*500)
				for i in range(500):
					fptr.write(" ")

				break
				

			j=j+1	
		# for page, spaces in zip (page_numbers, used_spaces):
		# 	if (spaces>target):
				
		# 		fptr.seek((int(page_numbers[i])-1)*500)
		# 		for i in range(500):
		# 			fptr.write(" ")
		# 		# i=i+1
		# 		print(i)
		# 		# continue
		# 	else:
		# 		# i=i+1
		# 		print(i)
		# 		fptr.seek((int(page_numbers[i])-1)*500)
				
		# 		for i in range(500):
		# 			fptr.write(" ")

		# 		fptr.seek(((int(page_numbers[i-1])-1)*500)+(target-used_spaces[i-1]))
		# 		for i in range(500-(target-used_spaces[i-1])):
		# 			fptr.write(" ")

		# 	i=i+1
		# 		break
		



			




def show_memory_map(currentdir):
	if (currentdir!=""):
		currentdir=""
		print("Your directory is changed. Now in root")

	fptr = open("filesystem.txt", "r")
	fptr.seek(720001)
	dirinfo = fptr.read(100000)
	fptr.close()
	dict={}
	for p in dirinfo.split('-'):
		q=p.strip().split(' ')
		if (len(q)==2):
			dirname = q[1]
			dict[dirname]=[]

	for p in dirinfo.split('-'):
		q=p.strip().split(' ')
		if (len(q)==4):
			dirname = q[2]
			dict[dirname].append(q[1])

	return dict
	




import os
fptr = None
for file in os.listdir():
    if (file=='filesystem.txt'):
        fptr = open("filesystem.txt", "r")
        print("Opened File System")
        break;
if (fptr==None):
	createfs()
	print("File System created")
	# fptr.close()
	exit()


currentdir="";

while (1):

	print("\n\t\t***********************************************\n");
	print("\t\t**************Welcome File System!**************\n");
	print("\t\t***********************************************\n");

	print("\t\t1-Create File\n");
	print("\t\t2-Delete File\n");
	print("\t\t3-Make Directory\n");
	print("\t\t4-Change Directory\n");
	print("\t\t5-Move File\n");
	print("\t\t6-Write to File (Append)\n");
	print("\t\t7-Write to File (At position) \n");
	print("\t\t8-Read From File (Whole file)\n");
	print("\t\t9-Read From File (Some part)\n");
	print("\t\t10-Truncate File\n");
	print("\t\t11-Show Memory Map\n");
	print("\t\t0-EXIT\n\n");

	choice = int(input("Enter operation no.:"));
	# print(choice)
	if(choice==1):
		print("The current dir is ",currentdir);
		createfile(currentdir);
		
	if(choice==2):
	    a = deleteFile(currentdir);
	    if (a==-1):
	        print("File deletion error!");
	    else:
	        print("File deleted successfully");
		    

	if(choice==3):
		mkdir();

	if(choice==4):
		currentdir=cddir();

	if(choice==5):
		print("Source File: ")
		s_fname = check_file_input()
		print("Target File: ")
		t_fname = check_file_input()

		move(s_fname, t_fname, currentdir)
		
	if(choice==6):
		fname = check_file_input()
		text = input("Enter text: ")
		write_to_file(fname, text, currentdir); #append
		

		# a = getfreepage()
		# print(a)

	if (choice==7):
		fname = check_file_input()
		text = input("Enter text: ")
		pos = int(input("Enter position: "))
		write_at_pos_file(fname, currentdir,text,pos)
	if (choice==8):
		fname = check_file_input()
		print(read_from_file(fname, currentdir))
	if (choice==9):
		fname = check_file_input()

		start = int(input("Enter startng byte: "))
		size = int(input("Enter size to be displayed: "))

		print(read_some_from_file(fname, currentdir, start, size))
	

	if (choice==10):
		fname= check_file_input()
		target = int(input("Enter target size"))
		truncate(fname, currentdir, target)
	if (choice==11):
		dict = show_memory_map(currentdir)
		for key in dict:
			print (key, "--->", dict[key])

	if(choice==0):
		printf("Thanks for using Our File System!\n\n");
		break