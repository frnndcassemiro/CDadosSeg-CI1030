import sys
import pefile

dic = {}

saida = None

pe = pefile.PE(sys.argv[1]) #recebe um arquivo binario

for section in pe.sections: #para cada secao do exe
        key = section.Name.decode('utf-8') #key recebe o nome da secao
        if key not in dic:
                permis = str(hex(section.Characteristics).split())[4] #valida as permissoes
                if permis == '2':
                        saida = 'Seção: '+ key + ' é executável: --x'   
                if permis == '4':
                        saida = 'Seção: '+ key + ' [não] é executável: r--'
                if permis == '8':
                        saida = 'Seção: '+ key + ' [não] é executável: -w-'
                if permis == '6':
                        saida = 'Seção: '+ key + ' é executável: r-x'
                if permis == 'a':
                        saida = 'Seção: '+ key + ' é executável: -wx'
                if permis == 'c':
                        saida = 'Seção: '+ key + ' [não] é executável: rw-'
                if permis == 'e':
                        saida = 'Seção: '+ key + ' é executável: rwx'
                dic[key] = saida   

for k in dic: #printa o dicionario na saida padrao
        print (dic[k])    