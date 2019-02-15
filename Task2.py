import string

def file_read(filename):
	fin=open(filename)
	count=0
	for line in fin:
		line=line.replace("-"," ")
#		print(line)
		if "get" in line:
			fout=open("get.log","a")
			fout.write(line)
			fout.close()
		if "post" in line:
			fout=open("post.log","a")
			fout.write(line)
			fout.close()
		if "put" in line:
			fout=open("put.log","a")
			fout.write(line)
			fout.close()
		if "delete" in line:
			fout=open("delete.log","a")
			fout.write(line)
			fout.close()
#		for item in word:
#			item=item.strip(string.punctuation + string.whitespace)
#			item=item.lower()
#			print(item)

file_read("access.log")
