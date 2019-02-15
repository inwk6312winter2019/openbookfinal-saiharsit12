import string

def character_word_count(filename):
	fin=open(filename)
	count = 0
	for line in fin:
		line=line.replace("-"," ")
		word=line.split()
		for item in word:
			item=item.strip(string.punctuation + string.whitespace)
			item=item.lower()
			count += 1
	return count


def file_read(filename):
	fin=open(filename)
	d=dict()
	for line in fin:
		line=line.replace("-"," ")
		word=line.split()
		for item in word:
			item=item.strip(string.punctuation + string.whitespace)
			item=item.lower()
			d[item]=d.get(item,0)+1
	return d

def print_dict(d):
	list1=list()
	for key,value in d.items():
		list1.append((value,key))
		list1.sort(reverse=True)
	for key,value in list1[:20]:
		print(key, value, sep='\t')

def count_the_article():
	pass

def starts_with_vow():
	pass

def sorted_words():
	pass

def unique_words(h):
	d = dict()
	for item in h:
		if item not in d:
			d[item] = 1
		else:
			d[item] += 1
	return d

words1=character_word_count("Book1.txt")
words2=character_word_count("Book2.txt")
words3=character_word_count("Book3.txt")
d1=file_read("Book1.txt")
d2=file_read("Book2.txt")
d3=file_read("Book3.txt")
print("Total no. of words in Book 1 is ",words1)
print("Total no. of words in Book 2 is ",words2)
print("Total no. of words in Book 3 is ",words3)
#print("Total no. of words in book2 is ",count2)
#print("Total no. of words in book3 is ",count3)
print_dict(d1)
print_dict(d2)
print_dict(d3)
unique_words(d1)
#print(unique_words(file_read("Book1.txt")))
