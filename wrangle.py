from lxml import html
import requests
import time

urls = {}

col_order = [
	'30 Year Fixed',
	'20 Year Fixed',
	'15 Year Fixed',
	'10 Year ARM',
	'7 Year ARM',
	'5 Year ARM',
	'30 Year Fixed FHA',
	'30 Year Fixed VA',
	'15 Year Fixed VA',
	'5 Year ARM VA',
	'30 Year Fixed Jumbo',
	'15 Year Fixed Jumbo',
	'7 Year ARM Jumbo',
]

def wrangle(s):
	page = requests.get(urls[s])
	tree = html.fromstring(page.content)
	#print (html.tostring(tree))
	if s == 'Wells Fargo':
		titles = tree.xpath('//table[@id="PurchaseRatesTable"]/tbody/tr/th[@id="productName"]/a/text()')
		for i in range(len(titles )):
			titles[i] = titles[i].replace('-Rate','').replace(' Rate', '').replace('-', ' ').replace('/1', ' Year')
		rates = tree.xpath('//table[@id="PurchaseRatesTable"]/tbody/tr/td[contains(@headers, "intRate")]/text()')
		return formatCSV(s, titles, rates)

def formatCSV(s, t, r):
	final = [s, time.strftime("%m/%d/%Y")]
	for c in col_order:
		found = False
		for i in range(len(t)):
			if t[i] == c:
				final.append(r[i].replace('%',''))
				found = True
				break
		if not found:
			final.append('-')
	final.append(urls[s])
	#print(t)
	#print (col_order)
	return ','.join(final) + '\n'

infile = open('banks.txt', 'r').read().split('\n')
banks = []
for line in infile:
	bank, url = line.split(',')
	urls[bank] = url
	banks.append(bank)

print (urls)

for b in banks:
	scrape = wrangle(b)
	print (scrape)
	open('data/' + b + '.txt', 'w+').write(scrape)
	break



