#errorcodes
#1 directory already exsists
#
#
#
#
#
#
#
#
#
#




import shutil
import os

#remove files
def rm(f):
	try:
		os.remove(f)
	except:
		shutil.rmtree(f)
#copy files
def copy(sor,des):
	try:
		shutil.copy2(sor,des)
	except:
		shutil.copytree(sor,des)
#move files
def move(sor,des):
	shutil.move(sor,des)
	#used like move("file.txt","file/")
	# or move("file.txt","file/file.txt")

#make directorys
def mkdir(dirk):
	try:
		os.mkdir(dirk)
	except:
		return "filemanager module internal errorcode: 1"

#rename things
def rename(dirk):
	try:
		os.rename(dirk)
	except:
		print("error renaming file")


#list files in current directory
def ls():
	dir = os.listdir()
	return dir


#list folders
def lsdir():
	dir = os.listdir()
	stuff_in_dir = list()
	for non in dir:
		#print(non)
		stuff_in_dir.append(non)
	#print(stuff_in_dir)
	return stuff_in_dir

#change dir
def cdir(dir):
	os.chdir(dir)