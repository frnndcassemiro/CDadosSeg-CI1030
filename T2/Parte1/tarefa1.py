import xmltodict
import json
import sys 
import os

d = sys.argv[1]

print('===================\n')
print('Permissões por APK\n')
print('===================')

dic = {}

for filename in os.listdir('manifestos'): #para cada xml existente no diretório
    if filename.endswith(".xml"):

        arq = os.path.join(d,filename) #arquivo com extensão xml
        arqNome = arq.split('.')[0] 

        str_json = arqNome + '.json'  
        arq_json = open(str_json,'w') #abre o arquivo json para escrita

        with open(arq) as fd: #converte o arquivo xml para json
            doc = xmltodict.parse(fd.read())
        arq_json.write(json.dumps(doc))

        saida = []

        with open(str_json) as fd2:
            jsonFile = json.load(fd2)
            
            userPerm =jsonFile['manifest']['uses-permission']
            for row in userPerm:
                for r in row:
                    if 'name' in r :
                        saida.append(row[r].split('.').pop()) #SALVA A LISTA DE PERMISSAO DE CADA APK
        print('\n'+arqNome+':')   
        print(str(saida))   

        dic[arqNome] = set(saida)

print('\n=========================\n')
print('Permissões comuns das APKs\n')
print('=========================\n')

intersec = None 
for k in dic :
    if intersec :
        intersec = intersec.intersection(dic[k])
    else:
        intersec = dic[k]
print (intersec)

print('\n==========================\n')
print('Permissões únicas por APK\n')
print('==========================\n')

for k1 in dic:
    result = dic[k1] 
    for k2 in dic:
        if k1 is not k2:
            result = result.difference(dic[k2])
    if len(result) > 0 :
        print (k1,':',result)
    else :
        print (k1,': não possui nenhuma chave diferentona!')

