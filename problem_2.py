import os
class Paths:
	def __init__(self):
		self.paths=[]
		
	def find_files(self,suffix, path):
		if(not(os.path.exists(path))):
			print("Invalid path")
			return True
		files = os.listdir(path)
		for i in files:
			if(os.path.isdir(path+"/"+i)):
				self.find_files(suffix,path+"/"+i)
			else:
				if((i.endswith(suffix))):
					self.paths.append(path+"/"+i)

	def print_paths(self):
		if(len(self.paths)==0):
			print("File not found")
			return
		for i in self.paths:
			print(i)



path1=Paths()

if(not(path1.find_files(".c","/nanodegree/testdir"))):
	path1.print_paths()
	
'''
prints the following since the files were found

/nanodegree/testdir/subdir3/subsubdir1/b.c
/nanodegree/testdir/subdir1/a.c
/nanodegree/testdir/subdir5/a.c
/nanodegree/testdir/t1.c
'''

path2= Paths()
if(not(path2.find_files(".py","/nanodegree/testdir"))):
	path2.print_paths()

#prints 'File not found' since a .py file does not exist


path3=Paths()
if(not(path3.find_files(".c","/invalid/path"))):
	path3.print_paths()
	
#prints 'Invalid path' since the path is not a valid one
