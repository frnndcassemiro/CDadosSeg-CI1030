from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count
import gensim.downloader as api 
import pandas as pd


''' função para pegar somente mm/dd das datas, visto que todos anos sao iguais = 2013.
algumas datas faltam o primeiro digito 0, que é inserido manualmente na clausula if()'''
def ParseDate(list_date):
	ans = []
	st = ''
	for date in list_date:
		st = date.split('/')

		st = st[0] + st[1]

		if(len(st) < 4):
			st = '0' + st

		ans.append(st)
		st = ''
	return ans

''' função para pegar somente hh:mm dos horários de ataques. alguns horarios faltam o primeiro digito 0 (ex: 2:34), que é adicionado manualmente'''
def ParseTime(list_time):
	ans = []
	st = ''
	for time in list_time:
		ind = time.index(':')

		st = time[ind-2:ind] + time[ind+1:ind+3]

		if(st[0] == ' '):
			st = '0' + st[1:]

		ans.append(st)
		st = ''
	return ans

#numeros vieram como floats por default no excel, transformamos em string e retiramos a parte decimal
def ParsePort(list_port):
	ans = []
	st = ''

	for port in list_port:
		st = (str(port).split('.')[0])
		ans.append(st)
		st = ''
	return ans

#remover '.' dos ips e tratal-los como inteiros para entrada no modelo
def ParseIP(list_ip):
	ans = []
	lst = []
	st = ''

	for ip in list_ip:
		lst = ip.split('.')

		for elem in lst:
			st += elem

		ans.append(st)
		# print(st)

		lst, st = [], ''

	return ans

def ParseProtocol(list_prot):
	ans = []

	for prot in list_prot:
		if prot == 'UDP':
			ans.append('0')
		elif prot == 'TCP':
			ans.append('1')
		else:
			pass
	return ans

#discretizar o que serao nossos labels 'y' nos modelos
def ParseHost(list_host):
	ans = []

	for host in list_host:
		if host == 'groucho-oregon':
			ans.append('0')
		elif host == 'groucho-us-east':
			ans.append('1')
		elif host == 'groucho-singapore':
			ans.append('2')
		elif host == 'groucho-tokyo':
			ans.append('3')
		elif host == 'groucho-sa':
			ans.append('4')
		elif host == 'zeppo-norcal':
			ans.append('5')
		elif host == 'groucho-eu':
			ans.append('6')
		elif host == 'groucho-norcal':
			ans.append('7')
		elif host == 'groucho-sydney':
			ans.append('8')
		else:
			pass
	return ans

#criar modelos em word2vec para country, locale
def ParseWord2Vec(list_w2v):
	data_part1 = list_w2v[:156380]
	model = Word2Vec([list_w2v], min_count = 0)
	
	return model

#substituir caracteres textuais por sua representação em word2vec
def Sub(lst, model):
	ans = []

	for elem in lst:
		representation = model.wv[elem].tolist()
		ans.append(representation)

	return ans

def main():
	dataset = pd.read_csv('AWS_Honeypot.csv')

	dataset = dataset.dropna()	
	
	date = list(dataset['datetime'])
	time = list(dataset['Time'])
	host = list(dataset['host'])
	proto = list(dataset['proto'])
	src_port = list(dataset['spt'])
	dst_port = list(dataset['dpt'])
	ips = list(dataset['srcstr'])
	country = list(dataset['country'])
	locale = list(dataset['locale'])
	
	date = ParseDate(date)
	time = ParseTime(time)
	src_port = ParsePort(src_port)
	dst_port = ParsePort(dst_port)
	ips = ParseIP(ips)
	proto = ParseProtocol(proto)
	host = ParseHost(host)
	country_model = ParseWord2Vec(country)
	locale_model = ParseWord2Vec(locale)

	country = Sub(country,country_model)
	locale = Sub(locale,locale_model)
	

	temp, temp2 = [], []
	for x in range(0, len(host)):
		temp.append(date[x]) 
		temp.append(time[x])
		temp.append(src_port[x])
		temp.append(dst_port[x])
		temp.append(ips[x])
		temp.append(proto[x])
		for y in country[x]:
			temp.append(y)
		for y in locale[x]:
			temp.append(y)
		temp2.append(temp)
		temp = []


	
	return temp2, host #temp = x, host =y