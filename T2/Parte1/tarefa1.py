import xmltodict
import json
import sys 
import os

d = sys.argv[1]

print('===================\n')
print('Permissões por APK\n')
print('===================')


for filename in os.listdir('manifestos'):
    if filename.endswith(".xml"):
        arq = os.path.join(d,filename)
        arqNome = arq.split('.')[0]

        arq_saida1 = arqNome + '.json'  
        saida1 = open(arq_saida1,'w')

        with open(arq) as fd:
            doc = xmltodict.parse(fd.read())
        saida1.write(json.dumps(doc))

        saida = []

        with open(arq_saida1) as fd2:
            jsonFile = json.load(fd2)
            
            userPerm =jsonFile['manifest']['uses-permission']
            for row in userPerm:
                for r in row:
                    if 'name' in r :
                        saida.append(row[r].split('.').pop())
        print('\n'+arqNome+':')   
        print(str(saida))   
