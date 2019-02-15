import string

def file_read(filename):
	fin=open(filename)
	count=0
	d=dict()
	for line in fin:
		line=line.replace("-"," ")
		word=line.split()
		for item in word:
			item=item.strip(string.punctuation + string.whitespace)
			item=item.lower()
			d[item]=d.get(item,0)+1
			count=count+1
	return count,d

def print_dict(d):
	print(len(d))
	for key,value in d.items():
		print(key,value)

def diff_words(d):
	dict_words=dict()
	for key in d.keys():
		if key not in dict_words:
			dict_words[key]="none"
	return dict_words

def compare_books(d1,d2):
	res = dict()
	for key in d1:
		if key not in d2:
			res[key] = None
	return res

def vocab(d1,d2):
	if len(d1)>len(d2):
		return "Book 1"
	elif len(d2)>len(d1):
		return "Book 2"
	else:
		return None

count1,d1=file_read("Book1.txt")
print("Total no of words in book1 is ",count1)
print_dict(d1)
dict_words=diff_words(d1)
print_dict(dict_words)
count2,d2=file_read("Book2.txt")
print("Total no of words in book2 is",count2)
d1minusd2=compare_books(d1,d2)
d2minusd1=compare_books(d2,d1)
print("Most prominent vocabulary usage among two books is:",vocab(d1,d2))
