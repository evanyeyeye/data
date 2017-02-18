from lxml import html
import dryscrape
import time
import sys

banks = {
	'Wells Fargo': {
		'url': 'https://www.wellsfargo.com/mortgage/rates/',
		'title_xpath': '//table[@id="PurchaseRatesTable"]/tbody/tr/th[@id="productName"]/a/text()',
		'rate_xpath': '//table[@id="PurchaseRatesTable"]/tbody/tr/td[contains(@headers, "intRate")]/text()',
		'title_replace': (('-Rate',''), (' Rate', ''), ('-', ' '), ('/1', ' Year'))
	},
	'Chase': {
		'url': 'https://www.chase.com/mortgage/mortgage-rates',
		'title_xpath': '//table[@id="rates-assumptions-table"]/tbody/tr/td[@class="left-align"]/text()',
		'rate_xpath': '//table[@id="rates-assumptions-table"]/tbody/tr/td[@class="left-align"]/following-sibling::td[1]/text()',
		'title_replace': ((' Rate', ''), ('/1 LIBOR', ' Year'))
	},
	'Citi': {
		'url': 'https://online.citi.com/US/JRS/portal/template.do?ID=mortgage_home_mortgage',
		'title_xpath': '',
		'rate_xpath': '',
		'title_replace': ''
	},
	'Bank of America': {
		'url': 'https://www.bankofamerica.com/mortgage/mortgage-rates/',
		'title_xpath': '//div[@class="table"]//header/p[@data-font="cnx-regular"]/text()',
		'rate_xpath': '//div[@class="table"]//p[@class="partial-rate"]/span[@class="update-partial"]/text()',
		'title_replace': (('-year', ' Year Fixed'), ('fixed', 'Fixed'), ('/1 ', ' Year ARM'), (' variable', ''))
	},
	'Capital One': {
		'url': 'https://www.capitalone.com/home-loans/mortgage/rates',
		'title_xpath': '//h3[@class="ng-binding"]/text()',
		'rate_xpath': '//div[text()="MONTHLY"]/following-sibling::div[1]/text()',
		'title_replace': (('/1 Adjustable', ' Year ARM'), ('-', ' '))
	}
}

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

def wrangle(b):
	session = dryscrape.Session()
	session.visit(banks[b]['url'])
	tree = html.fromstring(session.body())
	#print (html.tostring(tree))
	titles, rates = parse(tree, banks[b]['title_xpath'], banks[b]['rate_xpath'], banks[b]['title_replace'])
	return formatCSV(b, titles, rates)

def parse(tree, t_xpath, r_xpath, t_replace):
	temp = tree.xpath(t_xpath)
	for i in range(len(temp)):
		for re in t_replace:
			temp[i] = temp[i].replace(re[0], re[1])
		temp[i] = temp[i].strip()
	t = []
	for tt in temp:
		if tt == '':
			continue
		t.append(tt)
	#print(t)
	r = tree.xpath(r_xpath)
	#print (r)
	return t, r

def formatCSV(b, t, r):
	final = [b, time.strftime("%m/%d/%Y")]
	for c in col_order:
		found = False
		for i in range(len(t)):
			if t[i] == c:
				final.append(r[i].replace('%',''))
				found = True
				break
		if not found:
			final.append('-')
	final.append(banks[b]['url'])
	return ','.join(final) + '\n'

scraped_data = ""
with open('banks_enabled') as file:
	for line in file:
		line = line.replace('\n', '')
		if not line in banks:
			print ('The bank: ' + line + ' is unavailable.')
			continue
		print (scraped_data)
		scraped_data += wrangle(line)

open('output_data.txt', 'w+').write(scraped_data)