import sys
import pefile

def permissao(key, d):
        p = d[key]
        saida = None
        if p == '2':
                saida = ' é executável: --x'   
        if p == '4':
                saida = ' [não] é executável: r--'
        if p == '8':
                saida = ' [não] é executável: -w-'
        if p == '6':
                saida = ' é executável: r-x'
        if p == 'a':
                saida = ' é executável: -wx'
        if p == 'c':
                saida = ' [não] é executável: rw-'
        if p == 'e':
                saida = ' é executável: rwx'
        return saida   

d1 = {}
pe1 = pefile.PE(sys.argv[1]) #recebe um arquivo binario
for section in pe1.sections: #para cada secao do exe
        d1[section.Name.decode('utf-8')] = str(hex(section.Characteristics).split())[4] #key recebe o nome da secao
s1 = set(d1.keys())

print ("-----------------------------")

d2 = {}
pe2 = pefile.PE(sys.argv[2]) #recebe um arquivo binario
for section in pe2.sections: #para cada secao do exe
        d2[section.Name.decode('utf-8')] = str(hex(section.Characteristics).split())[4] #key recebe o nome da secao
s2 = set(d2.keys())

print ("-----------------------------")
for k in s1.intersection(s2):
        print (sys.argv[1],'e',sys.argv[2],'contêm a seção',k,':',permissao(k,d1))
print ("-----------------------------")
for k in s1.difference(s2):
        print ('Somente',sys.argv[1],'possui a seção',k,':',permissao(k,d1))
print ("-----------------------------")
for k in s2.difference(s1):
        print ('Somente',sys.argv[2],'possui a seção',k,':',permissao(k,d2))