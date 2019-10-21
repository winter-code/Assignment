import csv

csvfile = open('greybdata.csv', 'r').read()
companynames = csvfile.split('\n')

wordcnt = {}
def train(words):
	for word in words:
		word = word.lower()
		elem = ''
		for ch in word:
			if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
				elem += ch
			else:
				break
		if elem in wordcnt.keys():
			wordcnt[elem] += 1
		else:
			wordcnt[elem] = 1
	cnt = 1
	wordcntkeys = wordcnt.keys()
	wordcntkeys = sorted(wordcntkeys)
	for key in wordcntkeys:
		if wordcnt[key] > 1:
			wordcnt[key] = [cnt, wordcnt[key]]
			cnt += 1
		else:
			wordcnt[key] = [0, wordcnt[key]]

def predict(word):
	originalword = word
	word = word.lower()
	elem = ''
	for ch in word:
		if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
			elem += ch
		else:
			break
	try:
		if(wordcnt[elem][0] > 0):
			print(word, "Group " + str(wordcnt[elem][0]))
		else:
			print(originalword, "Ungrouped")
	except KeyError:
		print(originalword, "Ungrouped")

train(companynames)

# Enter the company name in the predict function to get the group number

predict("Samsung corp")
predict("Apple corp")
predict("Microsoft group")